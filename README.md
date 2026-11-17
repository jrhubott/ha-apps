# jrhubott's Home Assistant apps

A Home Assistant app repository. Each app installs a ready-made multi-arch image from ghcr.io, so
nothing is built on the Home Assistant host.

## Install

In Home Assistant, open **Settings → Apps → App store**, choose **⋮ → Repositories** and add:

```
https://github.com/jrhubott/ha-apps
```

Apps from this repository get the ID prefix `d4cd87db_` on every install (the Supervisor derives
it from the repository URL), for example `d4cd87db_music_assistant_lights_edge`.

## Apps

| App | Folder | What it is |
|---|---|---|
| Music Assistant (light follow) | `music_assistant_lights` | Music Assistant with Hue lights that follow a speaker, newest stable release |
| Music Assistant (light follow) Beta | `music_assistant_lights_beta` | The same on the newest beta |
| Music Assistant (light follow) Edge | `music_assistant_lights_edge` | The same on the feature branches (upstream `dev`/`main`) |

An app shows up in the store once its first image is built and its folder is committed.

## Music Assistant (light follow)

An unofficial build of the [Music Assistant](https://music-assistant.io) server with the
light-follow feature from the
[server fork](https://github.com/jrhubott/music-assistant-server) and
[frontend fork](https://github.com/jrhubott/music-assistant-frontend). Run only one Music Assistant
app at a time: they all use the host network on ports 8095 and 8094.

| Channel | Built from | Version |
|---|---|---|
| Stable | fork `release/<tag>` of upstream's newest stable release | `2.11.0`, then `2.11.0.1` after a feature update |
| Beta | fork `release/<tag>` of upstream's newest beta | `2.11.0b10`, then `2.11.0b10.1` |
| Edge | the `edge` branches in [`channels.json`](channels.json) | `2.11.0.dev202611170630` |

Service credentials go in `/share/music_assistant_dev/app_vars.json`, shared by all three
channels. Source builds do not contain the official bundled credentials. See an app's
documentation tab, or [template/DOCS.md](template/DOCS.md).

How it is built:

- The forks' nightly `fork-sync` run rebases the feature branches and builds the `release/<tag>`
  branches, testing both.
- [`build.yml`](.github/workflows/build.yml) runs daily at 06:30 UTC.
  [`scripts/resolve.py`](scripts/resolve.py) picks the channels whose sources changed since the
  last build ([`state.json`](state.json)). Each is built from source with the server's own
  `Dockerfile`, then [`image/`](image) swaps in the light-follow frontend wheel and sets
  `MASS_APP_VARS_FILE`. The build fails if `app_secrets.json` shows up.
- [`scripts/publish.py`](scripts/publish.py) renders [`template/`](template) into the channel's app
  folder with the new version and a changelog entry, and commits it. Edit the template, not the
  generated folders.
- [`channels.json`](channels.json) holds the forks, the edge branches, the image name and each
  channel's slug.
- To build by hand, run **Build** from the Actions tab: pick a channel, and tick **force** to
  rebuild unchanged sources.

## Adding an app

Add a top-level folder with a `config.yaml` (unique `slug`), `DOCS.md`, `CHANGELOG.md`, `icon.png`
and `logo.png`. Point `image:` at a published multi-arch image and set `version:` to one of its
tags. To build that image here, give the app its own workflow; `build.yml` only builds Music
Assistant. [`lint.yml`](.github/workflows/lint.yml) lints every folder that has a `config.yaml`.
