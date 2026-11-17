"""Write the Home Assistant app folder of each channel whose image was just pushed.

Reads one result JSON per built channel (the build matrix entry) from the directory given, renders
template/ into <slug>/, adds a CHANGELOG entry and records the build in state.json.
"""

from __future__ import annotations

import json
import shutil
import sys
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "template"


def render_app(cfg: dict, build: dict, repo: str) -> Path:
    meta = cfg["channels"][build["channel"]]
    app = ROOT / meta["slug"]
    app.mkdir(exist_ok=True)
    for item in TEMPLATE.iterdir():
        if item.name == "config.yaml.tmpl":
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
        stage=meta["stage"],
        image=build["image"],
        server_fork=build["server_repo"],
        server_ref=build["server_branch"],
        repo=repo,
    )
    (app / "config.yaml").write_text(config)

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
    if build["channel"] != "edge":
        entry += (
            f"\nUpstream release notes: https://github.com/music-assistant/server/releases/tag/"
            f"{build['tag']}\n"
        )
    changelog.write_text(header + "\n" + entry + rest)
    return app


def main(results_dir: str, repo: str) -> int:
    cfg = json.loads((ROOT / "channels.json").read_text())
    state_file = ROOT / "state.json"
    state = json.loads(state_file.read_text()) if state_file.exists() else {}
    builds = [json.loads(p.read_text()) for p in sorted(Path(results_dir).glob("**/*.json"))]
    if not builds:
        print("No successful builds to publish")
        return 0
    for build in builds:
        app = render_app(cfg, build, repo)
        state[build["channel"]] = {
            "version": build["version"],
            "tag": build["tag"],
            "server_sha": build["server_sha"],
            "frontend_sha": build["frontend_sha"],
        }
        print(f"{build['channel']}: {app.name} is now {build['version']}")
    state_file.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
