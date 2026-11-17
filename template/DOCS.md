# Music Assistant (light follow)

An unofficial build of the [Music Assistant](https://music-assistant.io) server with Hue lights
that follow a speaker. It is built from source from the
[server](https://github.com/jrhubott/music-assistant-server) and
[frontend](https://github.com/jrhubott/music-assistant-frontend) forks. Report problems with it
there, not to the Music Assistant project.

Only run one Music Assistant app at a time: they all use the host network on ports 8095 and 8094.

## Service credentials

Official Music Assistant builds ship API keys for services such as Spotify, Qobuz, Tidal and
Last.fm. Those keys are licensed only for the official builds, so this app does not include them.
Put your own in this file, which every channel of this app reads:

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
invalid JSON is ignored without an error.

## Moving from the official app

This app keeps its data apart from the official one. To bring your library and settings along,
stop both apps, then on the host copy
`/mnt/data/supervisor/addons/data/<hash>_music_assistant/` into this app's data folder before its
first start.

The Edge channel runs upstream's development branch and can migrate the database to a schema that
stable releases cannot read. Copy data into Edge, never out of it.
