# Changelog

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
