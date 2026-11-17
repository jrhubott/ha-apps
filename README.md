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

### Copy data from another Music Assistant app

Each app keeps its settings and library in its own `/data` folder, which lives on the host under
a folder named after the app's slug. To move from the official app to one of these (or between
channels), copy that folder from the
[Advanced SSH & Web Terminal](https://github.com/hassio-addons/app-ssh) app with **protection
mode** turned off, so it can run `docker`.

Find the slugs with `ha apps list | grep -i music` (`ha addons list` on older versions). The
app containers are named `app_<slug>` (`addon_<slug>` on older versions); check with
`docker ps -a --format '{{.Names}}' | grep -i music`.

**1. Find the data folder.** Ask Docker where the target app's `/data` is on the host:

```bash
SRC=d5369777_music_assistant_dev
DST=d4cd87db_music_assistant_lights_edge
DATA=$(dirname "$(docker inspect app_$DST --format '{{range .Mounts}}{{if eq .Destination "/data"}}{{.Source}}{{end}}{{end}}')")
echo $DATA
docker run --rm -v $DATA:/d alpine ls -la /d/$SRC /d/$DST
```

Go on only if both folders are listed, with `settings.json` in each. If not, fix the slugs or
container name first.

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
  `settings.json`, so beta data can't go back to stable.
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
