# ha-apps

Home Assistant apps for an unofficial Music Assistant server with Hue lights that follow a speaker.

## Install

In Home Assistant, open **Settings → Apps → App store**, choose **⋮ → Repositories** and add:

```
https://github.com/jrhubott/ha-apps
```

| App | Built from | Version |
|---|---|---|
| Music Assistant (light follow) | upstream's newest stable release + the feature | `2.11.0`, then `2.11.0.1` after a feature update |
| Music Assistant (light follow) Beta | upstream's newest beta + the feature | `2.11.0b10`, then `2.11.0b10.1` |
| Music Assistant (light follow) Edge | the feature branches, on upstream `dev`/`main` | `2.11.0.dev202611170630` |

An app shows up in the store once its first image is built. Home Assistant pulls a ready
multi-arch image (`ghcr.io/jrhubott/music-assistant-lights`); nothing is built on the host.

Service credentials go in `/share/music_assistant_dev/app_vars.json`. See an app's
documentation tab, or [template/DOCS.md](template/DOCS.md).

## How it works

- Sources: the [server fork](https://github.com/jrhubott/music-assistant-server) and
  [frontend fork](https://github.com/jrhubott/music-assistant-frontend). Their nightly
  `fork-sync` run rebases the feature branches and builds `release/<tag>` branches, testing both.
- [`build.yml`](.github/workflows/build.yml) runs daily at 06:30 UTC.
  [`scripts/resolve.py`](scripts/resolve.py) picks the channels whose sources changed since the
  last build ([`state.json`](state.json)). Each one is built from source with the server's own
  `Dockerfile`; [`image/`](image) then swaps in the light-follow frontend wheel. A source build
  never contains the official `app_secrets.json`, and the build fails if one shows up.
- [`scripts/publish.py`](scripts/publish.py) renders [`template/`](template) into the channel's
  app folder with the new version and a changelog entry, and commits it.
- Start a build by hand from the Actions tab: pick a channel, and tick **force** to rebuild
  unchanged sources.
- [`channels.json`](channels.json) holds the forks, the edge branches, the image name and each
  app's slug.
