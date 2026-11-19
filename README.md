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

| App | Folder and slug | Home Assistant slug | Container | What it is |
|---|---|---|---|---|
| Music Assistant Edge (jrhubott) | `music_assistant_lights_edge` | `d4cd87db_music_assistant_lights_edge` | `app_d4cd87db_music_assistant_lights_edge` | Upstream Music Assistant `dev`/`main` plus the feature branches merged into the forks' `edge` branches (fixes and features in progress) |
| Music Assistant Stable (jrhubott) | `music_assistant_jrhubott_stable` | `d4cd87db_music_assistant_jrhubott_stable` | `app_d4cd87db_music_assistant_jrhubott_stable` | Upstream Music Assistant `stable` (the latest release plus backports about to be released) plus the stable-based fixes merged into the forks' `stable` branches |

The Home Assistant slug is the one `ha apps` commands, the data folder and the container name use.
The Edge slug still says `lights` from the app's first name; it was kept so existing installs keep
their data. An app shows up in the store once its first image is built and its folder is committed.

## Music Assistant Edge (jrhubott)

An unofficial build of the [Music Assistant](https://music-assistant.io) server built from the
`edge` branches of the
[server fork](https://github.com/jrhubott/music-assistant-server) and
[frontend fork](https://github.com/jrhubott/music-assistant-frontend). Each `edge` branch is
upstream `dev` (server) or `main` (frontend) plus the feature branches merged into it by hand;
the forks' nightly `fork-sync` run merges upstream in and tests it. Run only one Music Assistant
app at a time: they all use the host network on ports 8095 and 8094. Versions look like
`2.11.0.dev202611170630` (upstream nightly base plus build time).

## Music Assistant Stable (jrhubott)

The same, built from the forks' `stable` branches: upstream `stable` plus stable-based ports of
features, merged in by hand. The same nightly `fork-sync` run merges upstream `stable` in. Versions
look like `2.10.12.post202611181417` (the latest upstream release plus build time). They are not
`.dev` versions, because a stable server with a `.dev` version points its dashboards at the
nightly web frontend.

## Both apps

The full setup, including how to add a feature to `edge` or `stable`, is documented on the BookStack page
"Music Assistant forks: edge branch and ha-apps", which is the record of truth.

Service credentials go in `/share/music_assistant_dev/app_vars.json`. Source builds do not contain the official bundled credentials. See an app's
documentation tab, or [template/DOCS.md](template/DOCS.md).

How it is built:

- The forks' nightly `fork-sync` run merges upstream into `edge` and `stable` and tests them.
- [`build.yml`](.github/workflows/build.yml) runs hourly at :17 and builds a channel only when one of its branches has a new commit. If a build fails, it is not retried for the same commits; a new commit on either branch of that channel, or a run with `force`, builds again.
  [`scripts/resolve.py`](scripts/resolve.py) builds a channel when its server or frontend commit
  changed since the last build ([`state.json`](state.json)). Each channel's base image is the one
  upstream's `release.yml` names for it (`NIGHTLY` for edge, `STABLE` for stable). It is built from source with the server's own
  `Dockerfile`, then [`image/`](image) swaps in the fork's frontend wheel and sets
  `MASS_APP_VARS_FILE`. The build fails if `app_secrets.json` shows up.
- [`scripts/publish.py`](scripts/publish.py) renders [`template/`](template) into the channel's app
  folder with the new version and a changelog entry, and commits it. Edit the template, not the
  generated folders.
- [`channels.json`](channels.json) holds the forks, the image name, and per channel the branches,
  the app's slug, name and texts. `template/DOCS.md.tmpl` uses `@KEY@` placeholders filled from it.
- To build by hand, run **Build** from the Actions tab (tick **force** to rebuild unchanged
  sources), or `gh workflow run build.yml -R jrhubott/ha-apps -f channel=edge` (or `channel=stable`).

### Copy data from another Music Assistant app

Each app keeps its settings and library in its own `/data` folder, which is
`/mnt/data/supervisor/apps/data/<slug>/` on the host (`addons/data` instead of `apps/data` on
older versions). To move from the official app to this one, copy that
folder from the [Advanced SSH & Web Terminal](https://github.com/hassio-addons/app-ssh) app with
**protection mode** turned off, so it can run `docker`.

Find the slugs with `ha apps list | grep -i music` (`ha addons list` on older versions).

**1. Check the folders.** Run this on its own first:

```bash
SRC=d5369777_music_assistant_dev
DST=d4cd87db_music_assistant_lights_edge
DATA=/mnt/data/supervisor/apps/data
docker run --rm -v $DATA:/d alpine ls -la /d/$SRC /d/$DST
```

Go on only if both folders are listed, with `settings.json` in each. If not, ask Docker where a
running app keeps its data; the parent of that folder is `DATA`:

```bash
docker inspect app_$DST --format '{{range .Mounts}}{{if eq .Destination "/data"}}{{.Source}}{{end}}{{end}}'
```

The container is named `app_<slug>` (`addon_<slug>` on older versions). A stopped app has no
container, so inspect one that is running.

**2. Copy.** Each command checks the folders again and does nothing if one is missing:

```bash
ha apps stop $SRC; ha apps stop $DST

# copy the source next to the target, leaving out caches the server rebuilds
docker run --rm -v $DATA:/d alpine sh -c "test -f /d/$SRC/settings.json && test -d /d/$DST && \
  cp -a /d/$SRC /d/$DST.new && rm -rf /d/$DST.new/cache.db /d/$DST.new/.cache /d/$DST.new/collage_images"

# swap it in, keeping the target's old data as $DST.before-copy
docker run --rm -v $DATA:/d alpine sh -c "test -f /d/$DST.new/settings.json && \
  mv /d/$DST /d/$DST.before-copy && mv /d/$DST.new /d/$DST"

ha apps start $DST
```

Nothing in the target is touched until the copy has finished, so a failed copy leaves only a
`$DST.new` folder to delete.

- Copy only to the same or a newer version. An older server can't read a newer `library.db` or
  `settings.json`, so edge data can't go back to a stable release, and can't be copied into the
  Stable app.
- The copy carries the source's server ID, provider logins and player settings. Keep the source
  app stopped. If you run both, remove and re-add the second one in Home Assistant's Music
  Assistant integration.
- To undo, stop the target and put its old data back:

  ```bash
  docker run --rm -v $DATA:/d alpine sh -c "rm -rf /d/$DST && mv /d/$DST.before-copy /d/$DST"
  ```

  Once the target works, remove the copy with
  `docker run --rm -v $DATA:/d alpine rm -rf /d/$DST.before-copy`.

## Adding an app

Add a top-level folder with a `config.yaml` (unique `slug`), `DOCS.md`, `CHANGELOG.md`, `icon.png`
and `logo.png`. Point `image:` at a published multi-arch image and set `version:` to one of its
tags. To build that image here, give the app its own workflow; `build.yml` only builds Music
Assistant. [`lint.yml`](.github/workflows/lint.yml) lints every folder that has a `config.yaml`.
