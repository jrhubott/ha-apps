# Music Assistant Stable (jrhubott)

An unofficial build of the [Music Assistant](https://music-assistant.io) server: the latest upstream stable release plus jrhubott's stable-based fixes.
It is built from source from the `stable` branches of the
[server](https://github.com/jrhubott/music-assistant-server) and
[frontend](https://github.com/jrhubott/music-assistant-frontend) forks, which follow
upstream's `stable` branch (the latest release plus backports about to be released). Report problems with it
there, not to the Music Assistant project.

Only run one Music Assistant app at a time: they all use the host network on ports 8095 and 8094.

## Service credentials

Official Music Assistant builds ship API keys for services such as Spotify, Qobuz, Tidal and
Last.fm. Those keys are licensed only for the official builds, so this app does not include them.
Put your own in this file:

```
/share/music_assistant_dev/app_vars.json
```

It is a flat JSON object with only the keys you have, for example:

```json
{
  "spotify_client_id": "…",
  "lastfm_api_key": "…",
  "lastfm_api_secret": "…",
  "fanarttv_api_key": "…"
}
```

The names are the ones in `APP_VAR_NAMES` in the server's
`music_assistant/helpers/app_vars.py`. Restart the app after you change the file. A file with
invalid JSON is ignored without an error, and so is a file in the official bundle's format (with
`salt` and `secrets` keys): the bundle only works in official builds.

## Moving from the official app

This app keeps its data apart from the official one. To bring your library and settings along,
copy the official app's data folder (`/mnt/data/supervisor/apps/data/<hash>_music_assistant/`)
into this app's data folder. The repository README has the commands.

This app runs upstream's stable branch. You can copy data into it from the official app or another app on the same stable version, but not from Edge: edge data can have a newer schema.
