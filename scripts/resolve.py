"""Decide which channels need a new image and print the build matrix.

stable/beta: the fork's release/<tag> branch for upstream's newest stable and beta release,
with the frontend fork's release/<frontend version> branch that server tag pins.
edge: the tips of the two feature branches.

A channel is built when its server or frontend commit differs from the last published build
(state.json), or when --force is given. Channels whose branches do not exist yet are skipped.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def api(path: str, raw: bool = False):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", "application/vnd.github.raw" if raw else "application/vnd.github+json")
    token = os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode()
    return body if raw else json.loads(body)


def branch_sha(repo: str, branch: str) -> str | None:
    try:
        return api(f"/repos/{repo}/branches/{urllib.parse.quote(branch, safe='')}")["commit"]["sha"]
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def file_at(repo: str, ref: str, path: str) -> str:
    return api(f"/repos/{repo}/contents/{path}?ref={ref}", raw=True)


def upstream_releases(repo: str) -> tuple[dict | None, dict | None, str | None]:
    """Return upstream's newest stable, newest current beta, and newest nightly tag."""
    rels = [r for r in api(f"/repos/{repo}/releases?per_page=60") if not r["draft"]]
    rels.sort(key=lambda r: r["published_at"], reverse=True)
    nightly = next((r["tag_name"] for r in rels if ".dev" in r["tag_name"]), None)
    rels = [r for r in rels if ".dev" not in r["tag_name"]]
    stable = next((r for r in rels if not r["prerelease"]), None)
    beta = next((r for r in rels if r["prerelease"]), None)
    if stable and beta and beta["published_at"] < stable["published_at"]:
        beta = None  # that beta line already shipped as stable
    return stable, beta, nightly


def base_image_version(repo: str, sha: str, key: str) -> str:
    workflow = file_at(repo, sha, ".github/workflows/release.yml")
    for name in (key, "STABLE"):
        match = re.search(rf'BASE_IMAGE_VERSION_{name}:\s*"([^"]+)"', workflow)
        if match:
            return match.group(1)
    raise SystemExit(f"No BASE_IMAGE_VERSION_{key} in {repo}@{sha} release.yml")


def frontend_pin(repo: str, sha: str) -> str:
    pyproject = file_at(repo, sha, "pyproject.toml")
    match = re.search(r"music-assistant/frontend/releases/download/([^/\s]+)/", pyproject)
    if not match:
        raise SystemExit(f"No frontend pin in {repo}@{sha} pyproject.toml")
    return match.group(1)


def next_release_version(tag: str, previous: dict | None) -> str:
    """
    Return the app version of a release channel build.

    The first build of a tag uses the tag itself; rebuilds of the same tag (new feature commits)
    append .1, .2, ... Home Assistant's update check (AwesomeVersion) ranks those above the tag,
    which it does not do for PEP 440 .postN versions.
    """
    if not previous or previous.get("tag") != tag:
        return tag
    match = re.fullmatch(re.escape(tag) + r"(?:\.(\d+))?", previous["version"])
    return f"{tag}.{int(match.group(1) or 0) + 1 if match else 1}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", default="all", choices=["all", "stable", "beta", "edge"])
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    cfg = json.loads((ROOT / "channels.json").read_text())
    state_file = ROOT / "state.json"
    state = json.loads(state_file.read_text()) if state_file.exists() else {}
    server_fork, frontend_fork = cfg["server_fork"], cfg["frontend_fork"]
    stable, beta, nightly = upstream_releases(cfg["upstream_server"])

    candidates: list[dict] = []
    for channel, rel in (("stable", stable), ("beta", beta)):
        if not rel:
            print(f"{channel}: upstream has no current {channel} release")
            continue
        tag = rel["tag_name"]
        server_branch = f"release/{tag}"
        server_sha = branch_sha(server_fork, server_branch)
        if not server_sha:
            print(f"{channel}: {server_fork} has no {server_branch} yet")
            continue
        frontend_version = frontend_pin(server_fork, server_sha)
        frontend_branch = f"release/{frontend_version}"
        frontend_sha = branch_sha(frontend_fork, frontend_branch)
        if not frontend_sha:
            print(f"{channel}: {frontend_fork} has no {frontend_branch} yet")
            continue
        candidates.append(
            {
                "channel": channel,
                "tag": tag,
                "server_branch": server_branch,
                "server_sha": server_sha,
                "frontend_branch": frontend_branch,
                "frontend_sha": frontend_sha,
                "frontend_version": frontend_version,
            }
        )

    edge = cfg["edge"]
    server_sha = branch_sha(server_fork, edge["server_branch"])
    frontend_sha = branch_sha(frontend_fork, edge["frontend_branch"])
    if server_sha and frontend_sha and nightly:
        base = nightly.split(".dev")[0]
        version = f"{base}.dev{datetime.now(UTC):%Y%m%d%H%M}"
        candidates.append(
            {
                "channel": "edge",
                "tag": version,
                "server_branch": edge["server_branch"],
                "server_sha": server_sha,
                "frontend_branch": edge["frontend_branch"],
                "frontend_sha": frontend_sha,
                "frontend_version": version,
            }
        )
    else:
        print("edge: a feature branch or the upstream nightly is missing")

    matrix: list[dict] = []
    for item in candidates:
        channel = item["channel"]
        if args.channel not in ("all", channel):
            continue
        previous = state.get(channel)
        unchanged = (
            previous
            and previous.get("server_sha") == item["server_sha"]
            and previous.get("frontend_sha") == item["frontend_sha"]
            and (channel == "edge" or previous.get("tag") == item["tag"])
        )
        if unchanged and not args.force:
            print(f"{channel}: {previous['version']} is current")
            continue
        meta = cfg["channels"][channel]
        version = item["tag"] if channel == "edge" else next_release_version(item["tag"], previous)
        matrix.append(
            {
                **item,
                "version": version,
                "mass_version": item["tag"],
                "slug": meta["slug"],
                "base_image_version": base_image_version(
                    server_fork, item["server_sha"], meta["base_image_key"]
                ),
                "server_repo": server_fork,
                "frontend_repo": frontend_fork,
                "image": cfg["image"],
            }
        )
        print(f"{channel}: build {version} from {item['server_branch']}@{item['server_sha'][:9]}"
              f" + {item['frontend_branch']}@{item['frontend_sha'][:9]}")

    out = os.environ.get("GITHUB_OUTPUT")
    text = f"matrix={json.dumps(matrix)}\ncount={len(matrix)}\n"
    if out:
        with open(out, "a") as fh:
            fh.write(text)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
