# Changelog

## 2.10.14.post202611281856

Built 2026-11-28 19:23 UTC from:

- server [`stable`](https://github.com/jrhubott/music-assistant-server/tree/8880fa73d713a5592e348c0f76ff34c7a7f13d63) (8880fa73d)
- frontend [`stable`](https://github.com/jrhubott/music-assistant-frontend/tree/440b64bc0a1d8d0e512d270747d25187840499f2) (440b64bc0)

Upstream release notes: https://github.com/music-assistant/server/releases/tag/2.10.14

### Server: 32 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/418b827b3f72...8880fa73d713))

- Keep WiiM and Bose SoundTouch speakers at their own volume when AirPlay starts (#8176) ([a7af18f](https://github.com/jrhubott/music-assistant-server/commit/a7af18f396439d2557a64c4d192b06c8ea56e6d7))
- Deezer: fix audiobooks stopping after the first chapter (#8054) ([abf2e29](https://github.com/jrhubott/music-assistant-server/commit/abf2e294109762d2ef954db7815b5ac5e1c57e85))
- Check a radio station again after its address could not be reached (#8100) ([af3e64c](https://github.com/jrhubott/music-assistant-server/commit/af3e64cd3275f173f32c05402d026e060a72e209))
- Stop a WiiM on squeezelite from pausing what plays right after a stop (#7968) ([d423c08](https://github.com/jrhubott/music-assistant-server/commit/d423c08c7ec4e91423ea4ac9fabb3313ba0ed8cd))
- Keep the control connection to HomePods and Apple TVs open (#8145) ([4863556](https://github.com/jrhubott/music-assistant-server/commit/4863556623a511548adf88603fa950472ec1c6e8))
- Don't create dashboard displays for Chromecast Audio and Home Mini speakers (#7997) ([c10303e](https://github.com/jrhubott/music-assistant-server/commit/c10303e4bb846f9c1a9c3074922cfe64f4e5714d))
- Fix Spotify Connect staying silent when playback starts outside the Spotify app (#8129) ([136ad5b](https://github.com/jrhubott/music-assistant-server/commit/136ad5b68181ff9717120343bb58bc316e883f97))
- Fix Spotify Connect hanging after a stop with go-librespot (#8127) ([034b653](https://github.com/jrhubott/music-assistant-server/commit/034b6531c75c749c78c926e0dd8db38e41406088))
- Keep syncing YouTube Music tracks when an upload can't be resolved (#8130) ([80def9d](https://github.com/jrhubott/music-assistant-server/commit/80def9d66bbcfba8224809b9ad7b32d01e43a681))
- Update airplay-cli to v0.5.19 (#8200) ([bc2a792](https://github.com/jrhubott/music-assistant-server/commit/bc2a792b8096881dc1656d2facc93488a993e384))
- Bump `aiosendspin` to 11.0.0 to fix silent line-in from idle Sendspin devices (#8184) ([9acd461](https://github.com/jrhubott/music-assistant-server/commit/9acd4618b1c24ee6e97e07cd1f82fda9af0ce5fe))
- Play podcast episodes from Spotify playlists instead of failing on them as tracks (#8188) ([5e82cba](https://github.com/jrhubott/music-assistant-server/commit/5e82cbad7e86dc4441691a71565405c62fe33ea7))
- Sync Audible audiobooks that have no cover image (#7993) ([cb19678](https://github.com/jrhubott/music-assistant-server/commit/cb196781507b1ed1ac98828d2d2aadca8f6cc8a7))
- Stop the queue when another device takes over Spotify playback (#8007) ([d5a765d](https://github.com/jrhubott/music-assistant-server/commit/d5a765dbc4c040d9a12b940251b665b0f907dcca))
- Keep yt-dlp up to date for YouTube Music (#8137) ([cb55d5e](https://github.com/jrhubott/music-assistant-server/commit/cb55d5ee396d77f2ed97bdc2ffcd64cc82ec0440))
- Stop an AirPlay play echo during group setup from resuming the old queue (#8103) ([55d4ae5](https://github.com/jrhubott/music-assistant-server/commit/55d4ae5b10ab69be7a439aa54d05758f4e3a6aec))
- Sync uploaded YouTube Music music into the library (#8114) ([b340c52](https://github.com/jrhubott/music-assistant-server/commit/b340c5224bc89f75a07a923b20eb8399e6cda8a9))
- ytmusicapi fails on uploaded album playlist (#7330) ([3be29f6](https://github.com/jrhubott/music-assistant-server/commit/3be29f6408ec31874d68ea2cd3907998d13fe856))
- Fix playback stopping when the next track changes right after a track starts (#8101) ([d2a0e4a](https://github.com/jrhubott/music-assistant-server/commit/d2a0e4aeda0494c294f2462289e744547f149db4))
- Fix Apple Music start delay that grows with track length (#8099) ([6949d78](https://github.com/jrhubott/music-assistant-server/commit/6949d7840bfe33bf4b37fba4b49ea7c83c0a9676))
- Add a Bluesound player that doesn't answer at startup as unavailable (#7995) ([de4af03](https://github.com/jrhubott/music-assistant-server/commit/de4af03004d417a8a690efa3c4f85215984a7827))
- Keep adding Bluesound players when a stereo pair speaker has no presets (#7996) ([8d5f87d](https://github.com/jrhubott/music-assistant-server/commit/8d5f87d0d196d3cb3b39475d024be22924a9b1de))
- Decode HTML entities in radio stream titles (#7868) ([02e88bc](https://github.com/jrhubott/music-assistant-server/commit/02e88bc1f8ab1ea557eb09fe5568e5e9df9872c2))
- MusicCast: don't show the previous track's info while on an input like TV (#8067) ([1a0b8d8](https://github.com/jrhubott/music-assistant-server/commit/1a0b8d893ae1389da44dd348c9114dc0c2702394))
- Stop an announcement to an AirPlay group from resuming the old queue (#7959) ([6a3e9ea](https://github.com/jrhubott/music-assistant-server/commit/6a3e9eaab300b7feeabf1c5d51ba7cf94c542f76))
- Pass Sonos volume changes through quickly during AirPlay playback (#7732) ([24e485b](https://github.com/jrhubott/music-assistant-server/commit/24e485b657525bc1cf663c5f795052b6216f5e80))
- Remove CodSpeed benchmarks (#8146) ([bc94226](https://github.com/jrhubott/music-assistant-server/commit/bc94226141e4039ed5ed5cdb946499accfe96f0c))
- Fix short audio gaps in live inputs when the server briefly stalls (#8138) ([7820190](https://github.com/jrhubott/music-assistant-server/commit/78201905246ea7b9ef9027e451ce5904b7b618dd))
- Keep Spotify Connect paused when a speaker reopens its stream (#8049) ([150356f](https://github.com/jrhubott/music-assistant-server/commit/150356f48bf391b20f131ecb3f6bf1e884c555d2))
- Let Cast speakers in a Sendspin group play short sounds from the start (#8119) ([3b33ba5](https://github.com/jrhubott/music-assistant-server/commit/3b33ba536794a93593a9e9602e13bae5cef3b4a7))
- Fix missing last track when a CUE sheet lists one file per track (#8057) ([277fb34](https://github.com/jrhubott/music-assistant-server/commit/277fb34cd96dcb4b09352095e442cf73f9a74238))
- Keep HEOS groups in sync after the controller reconnects (#7994) ([6f61ebc](https://github.com/jrhubott/music-assistant-server/commit/6f61ebcace66b366595995da6d2774633bc70c37))

### Frontend: no new commits

## 2.10.13.post202611252232

Built 2026-11-25 22:57 UTC from:

- server [`stable`](https://github.com/jrhubott/music-assistant-server/tree/418b827b3f72ba13606fb252678ee784dbd1ad3e) (418b827b3)
- frontend [`stable`](https://github.com/jrhubott/music-assistant-frontend/tree/440b64bc0a1d8d0e512d270747d25187840499f2) (440b64bc0)

Upstream release notes: https://github.com/music-assistant/server/releases/tag/2.10.13

### Server: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-server/compare/dfdf61ddee1c...418b827b3f72))

- Fix the AirPlay Receiver sometimes not starting or stopping playback (#8065) ([00846a4](https://github.com/jrhubott/music-assistant-server/commit/00846a4a89535e441670a616b1d730f3b45f6e47))

### Frontend: no new commits

## 2.10.13.post202611232121

Built 2026-11-23 21:39 UTC from:

- server [`stable`](https://github.com/jrhubott/music-assistant-server/tree/dfdf61ddee1c406c4918d1489c6608674e426691) (dfdf61dde)
- frontend [`stable`](https://github.com/jrhubott/music-assistant-frontend/tree/440b64bc0a1d8d0e512d270747d25187840499f2) (440b64bc0)

Upstream release notes: https://github.com/music-assistant/server/releases/tag/2.10.13

### Server: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-server/compare/3a3b854adf22...dfdf61ddee1c))

- Fix Sendspin player takeover for legacy clients with a lowercase MAC id (#8073) ([2c0219d](https://github.com/jrhubott/music-assistant-server/commit/2c0219d3c1def8f23699e39494e211fd77ef034b))

### Frontend: no new commits

## 2.10.13.post202611211629

Built 2026-11-21 16:53 UTC from:

- server [`stable`](https://github.com/jrhubott/music-assistant-server/tree/3a3b854adf228af6554fc465ff159760bb096795) (3a3b854ad)
- frontend [`stable`](https://github.com/jrhubott/music-assistant-frontend/tree/440b64bc0a1d8d0e512d270747d25187840499f2) (440b64bc0)

Upstream release notes: https://github.com/music-assistant/server/releases/tag/2.10.13

### Server: 41 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/bef82530e2bf...3a3b854adf22))

- Party: add a TV link that shows the dashboard without signing in ([8f93183](https://github.com/jrhubott/music-assistant-server/commit/8f93183b61bf33b33f0b26e61484346e65db57f8))
- Keep a group playing when a play request on one of its speakers cannot start (#8019) ([717c241](https://github.com/jrhubott/music-assistant-server/commit/717c241dedbc78680313f85e3ff68c5edf0bad98))
- Show at most 100 releases of an artist on a music service (#8018) ([61cbb98](https://github.com/jrhubott/music-assistant-server/commit/61cbb98981aa53685fc026905f5caa762462680c))
- Don't quit Cast sessions that Music Assistant didn't start (#7811) ([8f2fdf4](https://github.com/jrhubott/music-assistant-server/commit/8f2fdf4cb0770f11b503a48601b96f5b540bb0f0))
- Use MP3 by default for most Google Cast speakers to prevent dropouts (#8014) ([64575d8](https://github.com/jrhubott/music-assistant-server/commit/64575d8b172c0e7710e26a26d094896f98f23481))
- Bump fastmcp from 3.4.7 to 3.4.10 ([a7482d0](https://github.com/jrhubott/music-assistant-server/commit/a7482d0116193e08c5391d1ad347ef29a8a47ac7))
- Bump pillow from 12.3.0 to 13.0.0 (#7128) ([183eb9d](https://github.com/jrhubott/music-assistant-server/commit/183eb9d7727ef26eeb4c359f437b5fcda6744839))
- Bump certifi from 2025.11.12 to 2026.10.19 (#7127) ([6a0b401](https://github.com/jrhubott/music-assistant-server/commit/6a0b4017936a5c4b92ac1021a20ae88f5afd389c))
- Bump aiohttp from 3.14.3 to 3.14.4 (#7110) ([6433168](https://github.com/jrhubott/music-assistant-server/commit/6433168ce8a79c8de20251849535aef01dd918e0))
- Close the first-time setup 15 minutes after the server starts (#7410) ([c2b588e](https://github.com/jrhubott/music-assistant-server/commit/c2b588ed465824192f633f22d946bc53825e53d2))
- Keep the queue on the new track after Next while the player still reports the old stream (#7955) ([8c89828](https://github.com/jrhubott/music-assistant-server/commit/8c89828308ff0221b25bde060df9de090e79a3a1))
- Keep the duplicate album check from freezing a library with many same-title albums (#7956) ([e5bd074](https://github.com/jrhubott/music-assistant-server/commit/e5bd074c47dbacf8e201797ea6454feaba06afe2))
- Show a connection error instead of "no libraries" when Plex setup cannot reach the server (#7957) ([13a568d](https://github.com/jrhubott/music-assistant-server/commit/13a568d41567c919924f93b5b867a5ecfc96c58c))
- Hide provider tokens in the failed image fetch warning (#7855) ([a57fa61](https://github.com/jrhubott/music-assistant-server/commit/a57fa61f847415f83d805e7a7889c5bd4de526cc))
- Keep a muted WiiM speaker muted when its volume changes (#7834) ([9c1db71](https://github.com/jrhubott/music-assistant-server/commit/9c1db71eb707612446de4ff896d158b4fa64bccb))
- Ask to save the SSL certificate and key before Verify (#7832) ([04b797c](https://github.com/jrhubott/music-assistant-server/commit/04b797ce97c57328e645e4e099b4984a266a31cb))
- Start fully played podcast episodes and audiobooks from the beginning (#7772) ([e4bcbf4](https://github.com/jrhubott/music-assistant-server/commit/e4bcbf4fd92b412ca49747e2a34f44ce357efc4d))
- Accept ReplayGain gain tags without a space before dB (#7767) ([d3db121](https://github.com/jrhubott/music-assistant-server/commit/d3db1216279cbd5904441ba292555c6bc170abe4))
- Delete only playlist art inside the provider's images folder (#7781) ([14456eb](https://github.com/jrhubott/music-assistant-server/commit/14456ebc94994defe7c714aae3cd6b9c2e2ced67))
- Fix tracks greyed out in a saved playlist when users share a provider type (#7774) ([6a0e87d](https://github.com/jrhubott/music-assistant-server/commit/6a0e87d11b722c593c8986b43993cddcaff02ace))
- Fix Snapcast restoring a missing 'default' stream after an announcement (#7784) ([1d13d6a](https://github.com/jrhubott/music-assistant-server/commit/1d13d6a951b78f16211b5e0f3115b0b643f9bb59))
- Fix hi-res playback failing on gen 1 HEOS speakers (#7776) ([6bc44ad](https://github.com/jrhubott/music-assistant-server/commit/6bc44adda24447e92a92299e89e62e1c1c135952))
- Explain in the log why the Sendspin Cast bridge is skipped for unsupported devices (#7775) ([a92088b](https://github.com/jrhubott/music-assistant-server/commit/a92088bcedd297755ebc0905b69827c50bb494e3))
- Play gPodder and iTunes Podcasts episodes whose guid and stream url contain a space (#7768) ([1026bb1](https://github.com/jrhubott/music-assistant-server/commit/1026bb125adaf0fa061a7e36e570361441aa72c4))
- Fix ARD Sounds account login and sync subscriptions and progress (#7645) ([708b25c](https://github.com/jrhubott/music-assistant-server/commit/708b25c698d64595fe5def876d5f57cbda54f4c3))
- ⬆️ Update music-assistant-frontend to 2.17.297.post4 (#7960) ([b6a9078](https://github.com/jrhubott/music-assistant-server/commit/b6a9078da4bf9bf6ab9b006b062f25d81a6e068f))
- Harden return URL validation and handle IdP errors at the auth callback (#7759) ([73f56bf](https://github.com/jrhubott/music-assistant-server/commit/73f56bf5fcc13a22341b298e3d8d6dbb271c7340))
- Restart playback where it was when a speaker loses its stream connection (#7878) ([17abccd](https://github.com/jrhubott/music-assistant-server/commit/17abccd351ef3697520d11c17e778a3d7f5f94a4))
- Hand the AirPlay metadata task to create_task as a coroutine ([0e1fb61](https://github.com/jrhubott/music-assistant-server/commit/0e1fb61aebc0e893683968d2fb92e56970b7a30c))
- Fix the album cover on an Apple TV, Shairport Sync pause and seek, and HomePod group drift (airplay-cli v0.5.15) (#7850) ([4f4492c](https://github.com/jrhubott/music-assistant-server/commit/4f4492cf08a9257e129680b3f28d1d62797b52bc))
- Keep album artwork on AirPlay when the next track shares the cover (#6912) ([d438d98](https://github.com/jrhubott/music-assistant-server/commit/d438d98e96d806ad1122c3c8368863ac4bdfefc5))
- Keep the album cover on an Apple TV across tracks of the same album (airplay-cli v0.5.14) (#7699) ([b1640f2](https://github.com/jrhubott/music-assistant-server/commit/b1640f2a1820e10a7eb067d4a00245716e81210b))
- Release AirPlay speakers on stop and notice when another app takes them over (airplay-cli v0.5.13) (#7673) ([6862fcd](https://github.com/jrhubott/music-assistant-server/commit/6862fcd4c8285cff0663a85f7ba8f526c731fb2a))
- Release AirPlay speakers on stop and let another app take them over (#7671) ([0d4ecb2](https://github.com/jrhubott/music-assistant-server/commit/0d4ecb27e1d55f56da1e0d376f917ad9b52c7764))
- Stop repeated AirPlay Docker address warnings in the log (#7829) ([0ce6709](https://github.com/jrhubott/music-assistant-server/commit/0ce6709041d190a40b441f29222c06cf7382e3b5))
- Keep DLNA players available after a failed event subscription renewal (#7846) ([ae8dd43](https://github.com/jrhubott/music-assistant-server/commit/ae8dd433948e696a4f8b94b0640bcfc33c90e9bc))
- Fix Smart Fades not recovering when its model download fails (#7823) ([a1dbe65](https://github.com/jrhubott/music-assistant-server/commit/a1dbe65f76a3967395b99de8da7838e51a3e86c8))
- Fix sign-in being blocked by Cloudflare for Tailscale and CGNAT addresses (#7791) ([fbc707a](https://github.com/jrhubott/music-assistant-server/commit/fbc707a746aecb27f9ce031d1a6c3661e0ac5dea))
- Reset repeat mode when entering dynamic mode (#7754) ([08c0ff4](https://github.com/jrhubott/music-assistant-server/commit/08c0ff43abc6c931b5ca7431fe293f63c108e4d4))
- Fix AirPlay 1 speakers staying silent after a live input restarts (#6819) ([7de3bdb](https://github.com/jrhubott/music-assistant-server/commit/7de3bdb61af89905eed6cd741f34dd1dd8bd236e))
- …and more, see the compare link

### Frontend: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/a622edcb6d31...440b64bc0a1d))

- Party: remember a TV link so the dashboard signs itself back in ([147d2d7](https://github.com/jrhubott/music-assistant-frontend/commit/147d2d712a5bd63dbb8aa16691dec9cedf4048e9))

## 2.10.12.post202611191605

Built 2026-11-19 16:23 UTC from:

- server [`stable`](https://github.com/jrhubott/music-assistant-server/tree/bef82530e2bff150f5ecf70d217ae065adc619ee) (bef82530e)
- frontend [`stable`](https://github.com/jrhubott/music-assistant-frontend/tree/a622edcb6d31af88642f9a8bbbe64a1678b38ba4) (a622edcb6)

Upstream release notes: https://github.com/music-assistant/server/releases/tag/2.10.12

### Server: no new commits

### Frontend: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/4318416bb24a...a622edcb6d31))

- [Backport to stable] 2.17.297.post4 (#3249) ([8710763](https://github.com/jrhubott/music-assistant-frontend/commit/871076355b19c6c96f5dd38fef7147cff40bba8c))

## 2.10.12.post202611191302

Built 2026-11-19 13:21 UTC from:

- server [`stable`](https://github.com/jrhubott/music-assistant-server/tree/bef82530e2bff150f5ecf70d217ae065adc619ee) (bef82530e)
- frontend [`stable`](https://github.com/jrhubott/music-assistant-frontend/tree/4318416bb24ade685a77ea9eaf7124c455bd310a) (4318416bb)

Upstream release notes: https://github.com/music-assistant/server/releases/tag/2.10.12

### Server: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-server/compare/392ba560d1a7...bef82530e2bf))

- Keep a waiting headphone zone renderer off the speaker on stable ([b5c14e5](https://github.com/jrhubott/music-assistant-server/commit/b5c14e5074e0ffef0726fa92bd94e13790d4a544))

### Frontend: no new commits

## 2.10.12.post202611181428

Built 2026-11-18 14:53 UTC from:

- server [`stable`](https://github.com/jrhubott/music-assistant-server/tree/392ba560d1a7e5faeab6a13cdf3ac504980bd0c6) (392ba560d)
- frontend [`stable`](https://github.com/jrhubott/music-assistant-frontend/tree/4318416bb24ade685a77ea9eaf7124c455bd310a) (4318416bb)

Upstream release notes: https://github.com/music-assistant/server/releases/tag/2.10.12
