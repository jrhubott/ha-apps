"""Write the Home Assistant app folder of each channel whose image was just pushed.

Reads one result JSON per built channel (the build matrix entry) from the directory given, renders
template/ into <slug>/, adds a CHANGELOG entry and records the build in state.json.

The optional third argument is the build matrix as JSON. A channel in it without a result failed;
its commits are recorded under state.json "failed" so the hourly build doesn't retry them.
"""

from __future__ import annotations

import json
import shutil
import sys
import urllib.error
from datetime import UTC, datetime
from pathlib import Path

from resolve import api

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "template"
# a nightly upstream merge can bring in dozens of commits; the rest are behind the compare link
MAX_LISTED_COMMITS = 40


def commit_section(label: str, repo: str, base: str, head: str) -> str:
    """Return a CHANGELOG section listing the commits from base to head, or "" when unknown."""
    if not base:
        return ""  # the channel's first build has nothing to compare with
    if base == head:
        return f"\n### {label}: no new commits\n"
    try:
        data = api(f"/repos/{repo}/compare/{base}...{head}")
    except (urllib.error.URLError, TimeoutError, ValueError) as err:
        print(f"{repo}: could not list the commits {base[:9]}...{head[:9]}: {err}")
        return ""
    # merges (upstream syncs, "Merge branch ... into edge") only repeat the commits they bring in
    commits = [c for c in data.get("commits", []) if len(c.get("parents", [])) < 2]
    url = f"https://github.com/{repo}/compare/{base[:12]}...{head[:12]}"
    noun = "commit" if len(commits) == 1 else "commits"
    # the API returns at most 250 commits; total_commits counts the whole range, merges included
    partial = data.get("total_commits", 0) > len(data.get("commits", []))
    count = f"at least {len(commits)}" if partial else str(len(commits))
    lines = [f"\n### {label}: {count} new {noun} ([compare]({url}))\n"]
    # the compare API lists oldest first; newest first reads like the rest of the changelog
    for commit in list(reversed(commits))[:MAX_LISTED_COMMITS]:
        subject = commit["commit"]["message"].splitlines()[0].strip()
        lines.append(f"- {subject} ([{commit['sha'][:7]}]({commit['html_url']}))")
    if len(commits) > MAX_LISTED_COMMITS or partial:
        lines.append("- …and more, see the compare link")
    return "\n".join(lines) + "\n"


def render_app(cfg: dict, build: dict, repo: str) -> Path:
    meta = cfg["channels"][build["channel"]]
    app = ROOT / meta["slug"]
    app.mkdir(exist_ok=True)
    for item in TEMPLATE.iterdir():
        if item.suffix == ".tmpl":
            continue
        target = app / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)
    config = (TEMPLATE / "config.yaml.tmpl").read_text().format(
        name=meta["name"],
        version=build["version"],
        slug=meta["slug"],
        # "stable" is the default stage, and the app linter rejects a repeated default
        stage_line="" if meta["stage"] == "stable" else f"stage: {meta['stage']}\n",
        image=build["image"],
        server_fork=build["server_repo"],
        server_ref=build["server_branch"],
        summary=meta["summary"],
        repo=repo,
    )
    (app / "config.yaml").write_text(config)
    # DOCS.md has JSON braces in it, so it uses @KEY@ placeholders instead of str.format
    docs = (TEMPLATE / "DOCS.md.tmpl").read_text()
    for key, value in {
        "NAME": meta["name"],
        "SUMMARY": meta["summary"],
        "BRANCH": meta["server_branch"],
        "SOURCE": meta["source"],
        "DATA_NOTE": meta["data_note"],
    }.items():
        docs = docs.replace(f"@{key}@", value)
    (app / "DOCS.md").write_text(docs)

    changelog = app / "CHANGELOG.md"
    old = changelog.read_text() if changelog.exists() else "# Changelog\n"
    header, _, rest = old.partition("\n")
    entry = (
        f"\n## {build['version']}\n\n"
        f"Built {datetime.now(UTC):%Y-%m-%d %H:%M} UTC from:\n\n"
        f"- server [`{build['server_branch']}`](https://github.com/{build['server_repo']}/tree/"
        f"{build['server_sha']}) ({build['server_sha'][:9]})\n"
        f"- frontend [`{build['frontend_branch']}`](https://github.com/{build['frontend_repo']}/tree/"
        f"{build['frontend_sha']}) ({build['frontend_sha'][:9]})\n"
    )
    if build.get("upstream_release"):
        entry += (
            f"\nUpstream release notes: https://github.com/music-assistant/server/releases/tag/"
            f"{build['upstream_release']}\n"
        )
    entry += commit_section(
        "Server",
        build["server_repo"],
        build.get("previous_server_sha", ""),
        build["server_sha"],
    )
    entry += commit_section(
        "Frontend",
        build["frontend_repo"],
        build.get("previous_frontend_sha", ""),
        build["frontend_sha"],
    )
    changelog.write_text(header + "\n" + entry + rest)
    return app


def main(results_dir: str, repo: str, attempted_json: str = "[]") -> int:
    cfg = json.loads((ROOT / "channels.json").read_text())
    state_file = ROOT / "state.json"
    state = json.loads(state_file.read_text()) if state_file.exists() else {}
    builds = [json.loads(p.read_text()) for p in sorted(Path(results_dir).glob("**/*.json"))]
    built = {build["channel"] for build in builds}
    failed = state.setdefault("failed", {})
    for item in json.loads(attempted_json or "[]"):
        if item["channel"] not in built:
            failed[item["channel"]] = {
                "server_sha": item["server_sha"],
                "frontend_sha": item["frontend_sha"],
                "at": f"{datetime.now(UTC):%Y-%m-%d %H:%M} UTC",
            }
            print(f"{item['channel']}: build failed; not retrying these commits")
    for build in builds:
        failed.pop(build["channel"], None)
        app = render_app(cfg, build, repo)
        state[build["channel"]] = {
            "version": build["version"],
            "tag": build["tag"],
            "server_sha": build["server_sha"],
            "frontend_sha": build["frontend_sha"],
        }
        print(f"{build['channel']}: {app.name} is now {build['version']}")
    if not failed:
        del state["failed"]
    state_file.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:4]))
