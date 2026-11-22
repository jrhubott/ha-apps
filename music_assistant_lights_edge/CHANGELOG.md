# Changelog

## 2.11.0.dev202611221936

Built 2026-11-22 20:02 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/987b9ad962c34145b992862f74fb8937a4940c57) (987b9ad96)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/49af3f6db092ad57912daff94548b3c858e636ca) (49af3f6db)

### Server: 5 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/a6e6df46d5c7...987b9ad962c3))

- Standardise the naming across the BBC Sounds provider code (#8006) ([2297db5](https://github.com/jrhubott/music-assistant-server/commit/2297db51b86bcd532a376eaa7049961abe1d7764))
- Use library method for removing cookie jar when unloading BBC Sounds (#8044) ([49b124b](https://github.com/jrhubott/music-assistant-server/commit/49b124b944c8133e673996af628fbf6913f267dc))
- Deezer: fix audiobooks stopping after the first chapter (#8054) ([cb056ca](https://github.com/jrhubott/music-assistant-server/commit/cb056ca32ec8f49867d657a760381eb61823d84d))
- Show how far the server's clock runs off in the diagnostics report (#8051) ([bfd87a5](https://github.com/jrhubott/music-assistant-server/commit/bfd87a5a1ce97df101e806febfa61f916e55b40f))
- Show a WiiM stereo pair as one player (#7988) ([057a0f1](https://github.com/jrhubott/music-assistant-server/commit/057a0f172580f4dddea16ae8905b2eef0a659914))

### Frontend: 4 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/9ca880e45b5c...49af3f6db092))

- Find live sources by name in search (#3297) ([b4854be](https://github.com/jrhubott/music-assistant-frontend/commit/b4854be473ffb2b92da80ecda3dbb6bb7626db2c))
- Add a Live sources page (#3295) ([c39b369](https://github.com/jrhubott/music-assistant-frontend/commit/c39b3695c185995408c5efc38f3984411ce5a251))
- Show the Live sources folder by name in Browse (#3294) ([ba9426e](https://github.com/jrhubott/music-assistant-frontend/commit/ba9426e0f6cb9c091aa6be3e95f1a0d8eb226b7b))
- Add a subwoofer to Sendspin multi-channel players (#3286) ([10bb300](https://github.com/jrhubott/music-assistant-frontend/commit/10bb30073fe3096a5af343ae8d0ae640e9eb7273))

## 2.11.0.dev202611220511

Built 2026-11-22 05:31 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/a6e6df46d5c79a32a3b06b81b23650557c89eab3) (a6e6df46d)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/9ca880e45b5cb1c52f6443c903823daf9465f71e) (9ca880e45)

### Server: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-server/compare/a575610980d1...a6e6df46d5c7))

- Tie Hue Party Auto brightness to the song's energy ([7a2a9f9](https://github.com/jrhubott/music-assistant-server/commit/7a2a9f9678aeb06c54baea6434609f0b287c96d5))

### Frontend: no new commits

## 2.11.0.dev202611220424

Built 2026-11-22 04:43 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/a575610980d17ca9e512ba4e7d83b281f573507e) (a57561098)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/9ca880e45b5cb1c52f6443c903823daf9465f71e) (9ca880e45)

### Server: 20 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/fa6ecc8e429a...a575610980d1))

- Catch drops after a rising build in Hue Party Auto ([7906304](https://github.com/jrhubott/music-assistant-server/commit/7906304e0c00dfe6db63753b8ab82a58f6b8a36f))
- Add dance floor and party modes to Hue Lights Sync ([a237a6a](https://github.com/jrhubott/music-assistant-server/commit/a237a6a269934d589508c3bd93d1e3bb9529fddd))
- ⬆️ Update music-assistant-frontend to 2.17.378 (#8052) ([3cc661d](https://github.com/jrhubott/music-assistant-server/commit/3cc661d46429ca62a1f505507ddfb7a89e62bae1))
- Stop showing Spotify Connect playback on a speaker that is off (#8047) ([b1f9602](https://github.com/jrhubott/music-assistant-server/commit/b1f9602c1e74283888c0ec38bc35cf2e029ca972))
- Keep AirPlay and Sendspin groups in sync when the server's clock runs fast or slow (#8040) ([5da3671](https://github.com/jrhubott/music-assistant-server/commit/5da36710ce66b500d6c7c187ec092b1d89066eda))
- Show an error when no speaker of a universal group can play (#8048) ([fd20a75](https://github.com/jrhubott/music-assistant-server/commit/fd20a7596d227e78ce9cad8ef4298353f773ada2))
- Stop Sonos speakers going silent when a track repeats (#8038) ([f539f97](https://github.com/jrhubott/music-assistant-server/commit/f539f97c39a8c51f869e38e2c4a55b5fabcbf285))
- Add Spotify Recently Played browse folder and recommendation row (#8024) ([38e70db](https://github.com/jrhubott/music-assistant-server/commit/38e70dbd06d143d4ea7beb97390734e7d7602a4e))
- Send fewer Spotify search requests (#8030) ([95975c7](https://github.com/jrhubott/music-assistant-server/commit/95975c7080c12c9cd62535834d143b131b0af631))
- Stop an announcement to an AirPlay group from resuming the old queue (#7959) ([a3acc37](https://github.com/jrhubott/music-assistant-server/commit/a3acc375bc706323ac8fc4dafe14650373ed0914))
- Share the 'can this speaker play now' check between plugins (#8045) ([23bf06a](https://github.com/jrhubott/music-assistant-server/commit/23bf06ace147b230f68468b00db0a226d8787f16))
- Let speakers switch back to the AirPlay Receiver and play it once they are on (#8028) ([ee58111](https://github.com/jrhubott/music-assistant-server/commit/ee5811120671909432cea2af69c176c81c43348b))
- Show how long to wait when a provider is rate limited (#8025) ([91aa9dc](https://github.com/jrhubott/music-assistant-server/commit/91aa9dcb038222d9043eec8c54c46024249a54f9))
- Control each zone of a Sonos Amp Multi separately (#8032) ([4bb0e13](https://github.com/jrhubott/music-assistant-server/commit/4bb0e13ba3e59320674cfec1023ce7091feafb0b))
- Add or remove a subwoofer on combined Sendspin speakers (#8000) ([81ad03c](https://github.com/jrhubott/music-assistant-server/commit/81ad03c39fd2d0d95c28b845b75b9775f02a25aa))
- Add a subwoofer to combined Sendspin speakers (#7999) ([cdcc454](https://github.com/jrhubott/music-assistant-server/commit/cdcc454bead33dec851063957e21eccdeff99cbd))
- Fix Apple HomeView speakers staying silent on AirPlay 2 (airplay-cli v0.5.16) (#8042) ([f967754](https://github.com/jrhubott/music-assistant-server/commit/f967754284cbb38b85d74b517052df04ae5bd385))
- Speed up two slow AirPlay tests (#8041) ([4422531](https://github.com/jrhubott/music-assistant-server/commit/44225317b411a2495b07710f3888c61bd6d930b6))
- Bring an AirPlay speaker in a Sendspin group back within seconds after it drops out (#8034) ([6310991](https://github.com/jrhubott/music-assistant-server/commit/6310991be0040579e2768940bc6e41031d54db08))
- Gather live sources in one Browse folder, and list them for the app (#8037) ([e8363ab](https://github.com/jrhubott/music-assistant-server/commit/e8363ab853559b810aae966a32994456171769dc))

### Frontend: no new commits

## 2.11.0.dev202611220012

Built 2026-11-22 00:38 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/fa6ecc8e429a6001ced0d463c3f73611a9c5921f) (fa6ecc8e4)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/9ca880e45b5cb1c52f6443c903823daf9465f71e) (9ca880e45)

### Server: no new commits

### Frontend: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/1730114b9b62...9ca880e45b5c))

- Move party tips to a full-width bar and hide fullscreen buttons with anti burn-in ([8b33ee1](https://github.com/jrhubott/music-assistant-frontend/commit/8b33ee1850e2047d6525766e75e7fff1f20780fe))

## 2.11.0.dev202611212031

Built 2026-11-21 20:50 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/fa6ecc8e429a6001ced0d463c3f73611a9c5921f) (fa6ecc8e4)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/1730114b9b62ac20c1b3caaf791a292ba11147c9) (1730114b9)

### Server: 4 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/682965c58d1a...fa6ecc8e429a))

- Party: add fair queue, PIN host controls and a lyrics-only setting ([6cd4a1a](https://github.com/jrhubott/music-assistant-server/commit/6cd4a1a89cd99c1d2469bf0be5126a4ff43d03a4))
- Party: describe the burn-in swap between songs ([e95d623](https://github.com/jrhubott/music-assistant-server/commit/e95d623bce759ccbe3251205c74ee8abe9f7a02d))
- Party: add a setting to hide the copy link button ([bd6182a](https://github.com/jrhubott/music-assistant-server/commit/bd6182a77e5dddd4b1b2c159c1021210727d18c9))
- Party: add a setting for word-by-word lyrics ([5e7afba](https://github.com/jrhubott/music-assistant-server/commit/5e7afbabac66fceebd97f4c73e26079a8291dbe6))

### Frontend: 6 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/df7bb55f801e...1730114b9b62))

- Party: add host mode and lyrics-only messages to the guest page ([4014359](https://github.com/jrhubott/music-assistant-frontend/commit/4014359d234a48a02422f0ce6ba1444c26fe1411))
- Party screen: only swap sides for burn-in between songs ([08f3792](https://github.com/jrhubott/music-assistant-frontend/commit/08f37924262b3862506288b811efdb3d09059ad3))
- Party screen: remove the Powered by Music Assistant footer ([5747353](https://github.com/jrhubott/music-assistant-frontend/commit/57473534450f55d054e1befdb9ceaf28eb07b056))
- Party tips: match the song badges and add four tips ([fa621c1](https://github.com/jrhubott/music-assistant-frontend/commit/fa621c119bb7840e438655739a538c44a477ee24))
- Party: add a setting to hide the copy link button ([c02b5cd](https://github.com/jrhubott/music-assistant-frontend/commit/c02b5cd80f1fba6619d0231c53a243399e49cd4b))
- Party dashboard: add a setting for word-by-word lyrics ([0ec773a](https://github.com/jrhubott/music-assistant-frontend/commit/0ec773af0e3172bfae63f8d5f80c6dcc255af405))

## 2.11.0.dev202611211653

Built 2026-11-21 17:18 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/682965c58d1a5d45a6c1e2eaa7ef193d53867b7f) (682965c58)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/df7bb55f801e4ee235109aa0a3d872e6377aee02) (df7bb55f8)

### Server: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-server/compare/6e02d3c152f8...682965c58d1a))

- Add a Wake AirPlay button for Sonos speakers that stopped announcing it ([d1f4f30](https://github.com/jrhubott/music-assistant-server/commit/d1f4f3050222b6632435f58deeb6af485a97c00a))

### Frontend: 3 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/97112d821b57...df7bb55f801e))

- Replace dynamic sample and dashboard icons with Lucide (#3292) ([565b515](https://github.com/jrhubott/music-assistant-frontend/commit/565b515dcbe69c56f6b8b4644c63602dd5b890b2))
- Replace settings icons with Lucide (#3293) ([22b9ba8](https://github.com/jrhubott/music-assistant-frontend/commit/22b9ba885e64c45a6b4ff80ec048a71e62e46bdd))
- Show a live source once in now playing (#3291) ([40478bd](https://github.com/jrhubott/music-assistant-frontend/commit/40478bd054c121fe1af8093c347b4c254a59e3bb))

## 2.11.0.dev202611211629

Built 2026-11-21 16:53 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/6e02d3c152f84102a4ef6dd89a599b564f1ebc88) (6e02d3c15)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/97112d821b57b3ca93ea37e5c587e49fc781470e) (97112d821)

### Server: 9 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/82a0912b5c23...6e02d3c152f8))

- Give the follow handler tests' stub provider the sources a config update reads ([fa28b85](https://github.com/jrhubott/music-assistant-server/commit/fa28b85a5806962215d0ac74dbc04d7a27ecc47f))
- Respect a rate limit from Zvuk Music and KION Music (#8036) ([ab5531a](https://github.com/jrhubott/music-assistant-server/commit/ab5531a84f10718e641daa0b00580c025fbbd369))
- Keep the sleep timer when pausing a player that can't pause (#8033) ([5013cf4](https://github.com/jrhubott/music-assistant-server/commit/5013cf4b8bc13d8f69a41c6a88a415a7cd19e0e0))
- Deezer: give audiobook authors their own pages (#7927) ([8d13a78](https://github.com/jrhubott/music-assistant-server/commit/8d13a7862a4ecccb5add617cbad1a2ca230e5999))
- Speakers say which of their sources are inputs (#8029) ([9ad9972](https://github.com/jrhubott/music-assistant-server/commit/9ad9972ca6f34015a8f38377d2fc6d58fcf38371))
- Fail playlist-migration matching per track instead of per provider (#7881) ([b628d60](https://github.com/jrhubott/music-assistant-server/commit/b628d60e581a472f9021a7d63c6eaf3312aff153))
- Share one method for storing the main artists of albums and tracks (#7998) ([ff104e2](https://github.com/jrhubott/music-assistant-server/commit/ff104e29cef196137a156cb139d0343c48273290))
- Speed up library pages and the MusicBrainz link run on a new install (#7984) ([192df99](https://github.com/jrhubott/music-assistant-server/commit/192df99bb80091287d67204ba87a8020f84b8d43))
- Show a live source by its own name on its own player (#8031) ([b6a755a](https://github.com/jrhubott/music-assistant-server/commit/b6a755a909825fb8083c99951e8966e161fa4f86))

### Frontend: 0 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/e5acd4f37223...97112d821b57))


## 2.11.0.dev202611211502

Built 2026-11-21 15:28 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/82a0912b5c23d212a4567c2c5a6acd98fa239395) (82a0912b5)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/e5acd4f37223f0a23989f21fb447cc9ff37a803d) (e5acd4f37)

### Server: 8 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/419af4e0e13a...82a0912b5c23))

- Remove an old upgrade step that switched disabled players back on (#7981) ([1c6ad96](https://github.com/jrhubott/music-assistant-server/commit/1c6ad964b7a472f050ae3eab649025414310ab12))
- Check broad error catches in playback and the player providers (#7979) ([15d6bf1](https://github.com/jrhubott/music-assistant-server/commit/15d6bf17503464e06ae4ba711c1bf467a326d5d3))
- Remove duplicate albums found during the MusicBrainz lookup (#7821) ([4fb2cae](https://github.com/jrhubott/music-assistant-server/commit/4fb2cae894f6abebfbc8ff0f6c7120ff9d6a6ac9))
- Line-in sources follow the player access of the user (#8015) ([9b5ff42](https://github.com/jrhubott/music-assistant-server/commit/9b5ff42f4ab0ffa5b8e8fc1dd4f32d93443fc1db))
- Don't abort a playlist migration or import when a music service rate limits (#8026) ([bfb1fc3](https://github.com/jrhubott/music-assistant-server/commit/bfb1fc328e93bffdf27ccd62e87aa4e76940d3b6))
- Use public provider properties and helpers in the Apple Music provider (#8022) ([5fe7a96](https://github.com/jrhubott/music-assistant-server/commit/5fe7a96f238fda0172b4f9d06488669ca292973a))
- Update to latest py-opensonic (#8020) ([e96268a](https://github.com/jrhubott/music-assistant-server/commit/e96268a8fea79be44e7f1fc3f278772d824e0d6e))
- ⬆️ Update music-assistant-models to 1.1.249 (#8027) ([201f645](https://github.com/jrhubott/music-assistant-server/commit/201f64537d93c412d12825e0a227f432cbbf67c8))

### Frontend: 4 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/b2cf99a6368c...e5acd4f37223))

- Show only lights that really follow a speaker as followers ([9487d66](https://github.com/jrhubott/music-assistant-frontend/commit/9487d66d847120d5a3bf3d20f844737cf100c94e))
- Show each analysis module's progress on its own card (#3289) ([26a9180](https://github.com/jrhubott/music-assistant-frontend/commit/26a9180c5eb5e4cec18e39d03082833f65e2efab))
- Open settings in place on Metadata, Audio analysis and Background tasks (#3288) ([a001d7b](https://github.com/jrhubott/music-assistant-frontend/commit/a001d7be24942d8778835d600d1b86f75a7626c2))
- Show a missing AI engine under its picker (#3287) ([88b7bcc](https://github.com/jrhubott/music-assistant-frontend/commit/88b7bcc5c0b9fb1f8eb966b4c09d2ca63b0b28ef))

## 2.11.0.dev202611210750

Built 2026-11-21 08:12 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/419af4e0e13aa79b22e0afc967892298f4a26619) (419af4e0e)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/b2cf99a6368cf45d4e95d186014eaf9a6493b4b0) (b2cf99a63)

### Server: 42 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/ae59f69dd7c9...419af4e0e13a))

- Let lights follow a multi-channel speaker on its own protocol ([86280b5](https://github.com/jrhubott/music-assistant-server/commit/86280b5df5fc996b63da9fca8823886dd3fdfd5c))
- Move the light follow scenario to the top of Grouping as GROUP-900 ([a717e98](https://github.com/jrhubott/music-assistant-server/commit/a717e98e9d7b56c4d7244d3b2353c6f8649d3e2c))
- Restart playback when a speaker drops its stream and goes silent (#8017) ([772e48c](https://github.com/jrhubott/music-assistant-server/commit/772e48cc70c6ac501f767ce85d89b1cb6960f352))
- Stop an AirPlay device from taking the model of another device with the same name (#7978) ([7bed10f](https://github.com/jrhubott/music-assistant-server/commit/7bed10fab99ddd741478a151832baf667ac4f727))
- Tidy up after the queue took over releasing audio (#8013) ([26682cc](https://github.com/jrhubott/music-assistant-server/commit/26682cc181edb4844990fb0c5a7434efbb761632))
- Don't quit Cast sessions that Music Assistant didn't start (#7811) ([048d03f](https://github.com/jrhubott/music-assistant-server/commit/048d03f978b37d99b4ab315bb1be7cc272197d68))
- Bring a squeezelite player back to the power state it had (#8005) ([9ad09ae](https://github.com/jrhubott/music-assistant-server/commit/9ad09aee8b35b93fccd0eaab9ce22a22c5afe618))
- ⬆️ Update music-assistant-frontend to 2.17.377 (#8016) ([9996e94](https://github.com/jrhubott/music-assistant-server/commit/9996e9414b76ae9db59c76adda266d411108b15e))
- Name the audio input of a Sendspin player (#8010) ([0a06967](https://github.com/jrhubott/music-assistant-server/commit/0a069672482b67a13eb878903dbe61adeee0f8da))
- Keep a track playing when a radio queue refreshes its upcoming tracks (#7894) ([86d6e50](https://github.com/jrhubott/music-assistant-server/commit/86d6e50d34dd90cb4fd951e54c9a1e15ed0aa268))
- Use MP3 by default for most Google Cast speakers to prevent dropouts (#8011) ([0d4edc8](https://github.com/jrhubott/music-assistant-server/commit/0d4edc840dfafc7305844bef305020709130ccf3))
- Let the queue alone decide when the audio of a track is released (#7884) ([55a42e7](https://github.com/jrhubott/music-assistant-server/commit/55a42e7dc1d85913a8e16a2fff3c98fde0efdeea))
- Show only the pre-announce toggle in basic announcement settings (#8009) ([3b5699a](https://github.com/jrhubott/music-assistant-server/commit/3b5699a23073ca692d42893a9002b063c633eff3))
- Keep Sonos playing after the upcoming tracks are replaced (#8004) ([dcd891f](https://github.com/jrhubott/music-assistant-server/commit/dcd891feb4f573f5d13d919025189d9b7e98e84e))
- Show the background task limit without the advanced switch (#8008) ([e1e79c4](https://github.com/jrhubott/music-assistant-server/commit/e1e79c48c408d5a97d2d20990724e0414b0b99d8))
- Emby provider: support audiobook libraries (#7962) ([85136fc](https://github.com/jrhubott/music-assistant-server/commit/85136fcbd630036f1e2231507236e52516a707b0))
- Bump transformers to 5.23.0 and huggingface-hub to 2.4.0 (#8002) ([7cda51b](https://github.com/jrhubott/music-assistant-server/commit/7cda51b69921501593e02f1c3496bcaa599d21e9))
- Support native decoding Jellyfin wma formats, including wmapro & wmalossless (#7989) ([fa41378](https://github.com/jrhubott/music-assistant-server/commit/fa41378e1e14ddf817fb11ab4a26ca99c9ac55e1))
- Narrow broad exception handlers in Plex and Plex Connect (BLE001) (#7992) ([8d7a77f](https://github.com/jrhubott/music-assistant-server/commit/8d7a77faaafd9d87de205bcc20627b963d642c4e))
- Make the Audio Analysis settings page read less from disk on large libraries (#7991) ([166bcd5](https://github.com/jrhubott/music-assistant-server/commit/166bcd56422d763e807637226a746fff05672ee0))
- Call the player queue defaults Playback in setting texts (#7990) ([8a5dae9](https://github.com/jrhubott/music-assistant-server/commit/8a5dae9c495690d5e451f027cbe0efb6d81f03bd))
- Close the first-time setup 15 minutes after the server starts (#7410) ([86eab1f](https://github.com/jrhubott/music-assistant-server/commit/86eab1ff5eb53310d17bc2ecba9771ca10f435d0))
- Describe how a player provider delivers a set of speakers (#7983) ([d09d26e](https://github.com/jrhubott/music-assistant-server/commit/d09d26ef3a3492695d39bae50b31101eb12d0a14))
- Follow Home app volume changes on an idle HomePod (#7982) ([0c85ff8](https://github.com/jrhubott/music-assistant-server/commit/0c85ff8849b56d1fe05500d55fad6c1ac3e21a73))
- Keep an Apple TV room audible after switching its audio output (#7977) ([38ca99c](https://github.com/jrhubott/music-assistant-server/commit/38ca99c76e1c105fc38317bcad01ae9ab872368c))
- Play a stereo pair of HomePods as one player (#7937) ([515d036](https://github.com/jrhubott/music-assistant-server/commit/515d036053a19adb0acd29009c4666dedfdbe4ca))
- ⬆️ Update music-assistant-frontend to 2.17.376 (#7985) ([9b0ab9b](https://github.com/jrhubott/music-assistant-server/commit/9b0ab9b6264daebd71525161fc7bd96971575271))
- Play an Apple TV and its HomePods in a Sendspin group (#7950) ([74fbc26](https://github.com/jrhubott/music-assistant-server/commit/74fbc2605b483772d9458b6e5f1d25e8811d3ca7))
- Match album tracks to MusicBrainz by release length and ISRC (#7845) ([05a69a6](https://github.com/jrhubott/music-assistant-server/commit/05a69a60c4d4049a6ac52b71efdb4fcb2ba4e238))
- Apply Home Assistant player control changes right away (#7975) ([8ae3a4f](https://github.com/jrhubott/music-assistant-server/commit/8ae3a4fe52a1db8d8121ace472d301002aaf7c0e))
- Map OpenSubsonic release_types field onto MusicAssistant AlbumType. (#7951) ([a886664](https://github.com/jrhubott/music-assistant-server/commit/a8866645f038f84ee1aef6749001c080c2deb00a))
- List Home Assistant as an AI and text-to-speech service (#7974) ([4110870](https://github.com/jrhubott/music-assistant-server/commit/4110870d45e3bb8f6a3ba2a6135336f4176b8d7c))
- Keep Sonos playing when crossfading into a track added after playback started (#7964) ([8d1d6c2](https://github.com/jrhubott/music-assistant-server/commit/8d1d6c27710438158257b866b41f84d27ff7e7ca))
- Shorter Spotify Soloist setup texts (#7973) ([e7673f1](https://github.com/jrhubott/music-assistant-server/commit/e7673f1507af52f9b62ea77a4df442af737f0c47))
- Reuse your Soloist API key between Spotify and Spotify Connect (#7972) ([28fce35](https://github.com/jrhubott/music-assistant-server/commit/28fce359e96213164b4323b8aa2ec983d06aec83))
- Keep open sessions up to date after a profile or preference change (#7971) ([501408b](https://github.com/jrhubott/music-assistant-server/commit/501408b1daa896d93554b782a76d22ab3d5e6d2c))
- Log ISRCs that MusicBrainz lacks for an album (#7831) ([c6c67dd](https://github.com/jrhubott/music-assistant-server/commit/c6c67dda21dd49946640c808aa994e78a3bd8c10))
- Fix an occasionally failing mDNS lookup test (#7969) ([f6dbcd7](https://github.com/jrhubott/music-assistant-server/commit/f6dbcd7ec5095533ea3708b39a0a32e5cd70f11e))
- Fix Sendspin failing to start when port 8927 is taken (#7792) ([091b6b2](https://github.com/jrhubott/music-assistant-server/commit/091b6b2c1a3a5625f93c2072bc2c5792ca2c0900))
- Play an Apple TV and its HomePods as one player (#7936) ([667d645](https://github.com/jrhubott/music-assistant-server/commit/667d645ddbd8f6580cfd277ae954e78942a94b11))
- …and more, see the compare link

### Frontend: no new commits

## 2.11.0.dev202611202015

Built 2026-11-20 20:36 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/ae59f69dd7c981456270ee099e2d19780657ec78) (ae59f69dd)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/b2cf99a6368cf45d4e95d186014eaf9a6493b4b0) (b2cf99a63)

### Server: no new commits

### Frontend: 36 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/2f8877c55569...b2cf99a6368c))

- Add share links for tracks, albums and artists (#3040) ([fa83313](https://github.com/jrhubott/music-assistant-frontend/commit/fa83313c6f7454b094c7652ebfe70e3ef5f4493a))
- Open the docs at the new Playback heading from a player's Playback page (#3285) ([0ca85ee](https://github.com/jrhubott/music-assistant-frontend/commit/0ca85eec89fe71cabd65333823330f45ce60f2c3))
- Return to the previous page after saving settings (#3284) ([879e683](https://github.com/jrhubott/music-assistant-frontend/commit/879e6837ba6428e563c3c7019cd0daf300da1ae8))
- Add a back arrow to Settings pages (#3282) ([6b69177](https://github.com/jrhubott/music-assistant-frontend/commit/6b69177afa62fc6f5bf4488ec00b6a8db4b73ad0))
- Keep Escape going back after picking from a dropdown (#3283) ([6b14f59](https://github.com/jrhubott/music-assistant-frontend/commit/6b14f5920ae3339786471e703336ffb791e42d92))
- Call each player's queue settings Playback (#3281) ([5555b9b](https://github.com/jrhubott/music-assistant-frontend/commit/5555b9b53bcdf42ca3feb4a73f8044a6b1fb24f5))
- Redesign the setup wizard layout (#3280) ([b00f1e5](https://github.com/jrhubott/music-assistant-frontend/commit/b00f1e5751935cf214125dfa961d1905c0c31a2f))
- Show the AI step's services without a settings link (#3279) ([b99e0c7](https://github.com/jrhubott/music-assistant-frontend/commit/b99e0c770feb4c594cd17cce8af9c36f5b639887))
- Show Audio analysis and Metadata on one page each (#3274) ([290bbf5](https://github.com/jrhubott/music-assistant-frontend/commit/290bbf5de8c1d7de068beb27cc8db5c6d04138f6))
- Do the Home Assistant settings right on its page (#3275) ([a628180](https://github.com/jrhubott/music-assistant-frontend/commit/a628180de5f3df8988e05c1cd055439f5ea58f85))
- Save settings that apply right away without a Save button (#3276) ([ad8d6c8](https://github.com/jrhubott/music-assistant-frontend/commit/ad8d6c8e6e43c4424db4be00829a140f34ebad02))
- Pick the engine of each AI feature right on the AI page (#3273) ([e37e18b](https://github.com/jrhubott/music-assistant-frontend/commit/e37e18b5d0794a93fef79444d73d7713a525e9f0))
- Make the remaining setup wizard steps more inviting (#3270) ([6c7c1d1](https://github.com/jrhubott/music-assistant-frontend/commit/6c7c1d1bdeb3d49acc45d4d84a70943ef9257972))
- Keep Settings in a centred column on wide screens (#3272) ([a98df33](https://github.com/jrhubott/music-assistant-frontend/commit/a98df3330b7dbcd1adba512344dbedbeebb81352))
- Add AI services right on the AI page (#3271) ([f8db007](https://github.com/jrhubott/music-assistant-frontend/commit/f8db007b1c75a4462c568f6a211f0696cf7405e5))
- Polish the setup wizard's choice and music app steps (#3265) ([055cb47](https://github.com/jrhubott/music-assistant-frontend/commit/055cb479e836cf240d7e17953cac83faebd711f5))
- Make choosing a folder for Local files simpler (#3269) ([d454012](https://github.com/jrhubott/music-assistant-frontend/commit/d4540121d91549145fc06f90685442d92d4d7c17))
- Add a folder or network share right from the folder picker (#3267) ([51e4910](https://github.com/jrhubott/music-assistant-frontend/commit/51e491012e44b12cc35372e62c06219f90e359aa))
- Line up the category labels on provider cards (#3268) ([05e2ac4](https://github.com/jrhubott/music-assistant-frontend/commit/05e2ac4870fd3bd207f3be44938cf69b0e1eea13))
- Make the optional steps of the setup wizard more inviting (#3266) ([37f7c5f](https://github.com/jrhubott/music-assistant-frontend/commit/37f7c5f56ca39baece61300a3ceb5039021fac15))
- Reorder and hide the rows of a podcast episode page (#3246) ([46cf150](https://github.com/jrhubott/music-assistant-frontend/commit/46cf150c21ec7bc42dbaee6e8a6c8d6330d2f4d9))
- Start the first setup with a welcome and keep account creation in the wizard (#3264) ([628a922](https://github.com/jrhubott/music-assistant-frontend/commit/628a9225ef8aaf42fac5cad8643b282e99f14524))
- Explain how to set up a fresh server when using the dev frontend (#3263) ([bee28f2](https://github.com/jrhubott/music-assistant-frontend/commit/bee28f22119a4ef50f6bbdf2c6a2371c164e2e21))
- Clarify library-based statistics (#3132) ([12a202b](https://github.com/jrhubott/music-assistant-frontend/commit/12a202b6b01281eccdf7402dcc900d87f833ee90))
- Offer enabled guests in selected music-source sharing (#3219) ([ff4c9c4](https://github.com/jrhubott/music-assistant-frontend/commit/ff4c9c46f06cf45563d0b4331ed662dc61c4874d))
- Open a Discover section in full by clicking its title (#3114) ([2a01093](https://github.com/jrhubott/music-assistant-frontend/commit/2a010937c7a5e12f4a1e8c9a34e9a4c1ab494dcf))
- Ask about AI in the setup wizard (#3262) ([b95dee8](https://github.com/jrhubott/music-assistant-frontend/commit/b95dee8972197a554e939bb1794e678e9b7e1611))
- Open the Marketplace on AI services from the AI page (#3261) ([d15a5cf](https://github.com/jrhubott/music-assistant-frontend/commit/d15a5cfe2d6e98e2c48ff9c11aa7b7481d131543))
- Combine Sendspin speakers into a stereo pair (#3253) ([7bd92a9](https://github.com/jrhubott/music-assistant-frontend/commit/7bd92a942bb3e15d16fd0c50b6f6ca7c0d60cfc5))
- Hold the timeline while an announcement interrupts the queue (#3258) ([b4f8556](https://github.com/jrhubott/music-assistant-frontend/commit/b4f85569c05e21618ca0ced03702248e48b3d6af))
- Filter plugins by what they do (#3254) ([5279799](https://github.com/jrhubott/music-assistant-frontend/commit/5279799977dbb44df5b0fa133c6b3d87a7d6df87))
- Use the new names Home Assistant Link and Home Assistant app (#3260) ([0e2c656](https://github.com/jrhubott/music-assistant-frontend/commit/0e2c6563cbafb1a99c726b6c8b37d323310f5b6a))
- Connect Home Assistant before setting up remote access in the setup wizard (#3259) ([0752a39](https://github.com/jrhubott/music-assistant-frontend/commit/0752a39a04790b5e7c1f98347fe8bf5aca3dacfa))
- Make the setup wizard's network step only about remote access (#3255) ([9f55283](https://github.com/jrhubott/music-assistant-frontend/commit/9f55283c29cda1da6635f0fe08d4f9f4f31e5be7))
- Show the AI from Home Assistant on its settings page (#3257) ([b6569f6](https://github.com/jrhubott/music-assistant-frontend/commit/b6569f6588d93910abc522355832d85d98447c56))
- Add an AI page to the settings (#3256) ([8f767d0](https://github.com/jrhubott/music-assistant-frontend/commit/8f767d092748b973edaeb600ef5b95aa8cf6a463))

## 2.11.0.dev202611191735

Built 2026-11-19 17:50 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/ae59f69dd7c981456270ee099e2d19780657ec78) (ae59f69dd)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/2f8877c5556938eb0d2ddac6289160ec0b602c9b) (2f8877c55)

### Server: 6 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/18e180904469...ae59f69dd7c9))

- Name the headphone zone of a Sonos speaker apart from the speaker ([1e02ccf](https://github.com/jrhubott/music-assistant-server/commit/1e02ccf2c1dccb5e7ac9ca75b1395f70cb70b7cd))
- Hold the queue's position while an announcement plays (#7847) ([0af34ba](https://github.com/jrhubott/music-assistant-server/commit/0af34bac92f7c552cc37207078e6815e5128a6fd))
- Show remotes and volume knobs on Sendspin as controllers (#7966) ([f220f63](https://github.com/jrhubott/music-assistant-server/commit/f220f63bdf35f68c2cce2a69f87ad0728bd43bdc))
- Stop a WiiM on squeezelite from pausing what plays right after a stop (#7968) ([54d1972](https://github.com/jrhubott/music-assistant-server/commit/54d1972b82da3a0cf815f46f25f7a683387df8ad))
- Let every provider declare what it offers in its manifest (#7965) ([f7f46ff](https://github.com/jrhubott/music-assistant-server/commit/f7f46ff0055a4f4545f6bfa5cc70308ed5094873))
- Bump aioslimproto to 3.6.8 (#7967) ([2506795](https://github.com/jrhubott/music-assistant-server/commit/2506795527e19da7c373528e5ebd70184ebc2899))

### Frontend: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/458548af4979...2f8877c55569))

- Show party tips under the QR code and give the leaderboard its own card ([a44d446](https://github.com/jrhubott/music-assistant-frontend/commit/a44d44601899e722e6acc91f28e7792a33e89fab))

## 2.11.0.dev202611191715

Built 2026-11-19 17:35 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/18e180904469d49093ac913857501a2965c4bcac) (18e180904)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/2f8877c5556938eb0d2ddac6289160ec0b602c9b) (2f8877c55)

### Server: no new commits

### Frontend: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/458548af4979...2f8877c55569))

- Show party tips under the QR code and give the leaderboard its own card ([a44d446](https://github.com/jrhubott/music-assistant-frontend/commit/a44d44601899e722e6acc91f28e7792a33e89fab))

## 2.11.0.dev202611191605

Built 2026-11-19 16:23 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/18e180904469d49093ac913857501a2965c4bcac) (18e180904)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/458548af4979d032bc8bfe5716c7605e9f4a3d41) (458548af4)

### Server: 52 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/debde5ce9679...18e180904469))

- Party: add a TV link that shows the dashboard without signing in ([8818815](https://github.com/jrhubott/music-assistant-server/commit/88188151c2b248d83d76781f6182eb07926291a8))
- Give the follow handler tests' stub provider the sources a config update reads ([df61055](https://github.com/jrhubott/music-assistant-server/commit/df61055b318d5af64220b435cff35e36ea66586e))
- Add guest nicknames, shout-outs, reactions and a DJ leaderboard to the party plugin ([7d865c1](https://github.com/jrhubott/music-assistant-server/commit/7d865c16a9fdd238d73cc83e261ae312ca1107ff))
- Pick the models while adding OpenAI Compatible (#7958) ([26b876e](https://github.com/jrhubott/music-assistant-server/commit/26b876e196405854e26a259b2cf417fe5bd0d274))
- Forget a Sendspin device's pairing when its player is removed (#7773) ([3182337](https://github.com/jrhubott/music-assistant-server/commit/3182337bd96e585c39b0213bb75f01dda89fe85b))
- Keep the queue on the new track after Next while the player still reports the old stream (#7955) ([b0553f8](https://github.com/jrhubott/music-assistant-server/commit/b0553f8969459cdf72c79c8ffe6616c5ec7e3347))
- Keep the duplicate album check from freezing a library with many same-title albums (#7956) ([d62d4d5](https://github.com/jrhubott/music-assistant-server/commit/d62d4d5235dfb8ed0c28c2db97179e85e8d1748b))
- Show a connection error instead of "no libraries" when Plex setup cannot reach the server (#7957) ([7500276](https://github.com/jrhubott/music-assistant-server/commit/75002764e5865942053d2c4fc4e3d887e41080b4))
- Stop playback when a music service gives no audio for three tracks in a row (#7945) ([92442c0](https://github.com/jrhubott/music-assistant-server/commit/92442c094382aa1ff5d3b898022575195afd6bc9))
- Add Jellyfin playlist track editing (#7896) ([31a9e32](https://github.com/jrhubott/music-assistant-server/commit/31a9e32aa6230a4b8ee24f9ac6bf8f41f6dec9fb))
- Narrow broad exception handlers in AriaCast Receiver (BLE001) (#7953) ([fad7b80](https://github.com/jrhubott/music-assistant-server/commit/fad7b80504144030bbc2426181bcad829b91d2bb))
- Pair Sendspin players on the Home Assistant host with their local token (#7371) ([ce4f033](https://github.com/jrhubott/music-assistant-server/commit/ce4f0334a0a638d33fb6571e504157393a2fcbbb))
- Keep AirPlay speakers with another sender after it takes them over from a Sendspin group (#7952) ([951e22e](https://github.com/jrhubott/music-assistant-server/commit/951e22e60cc44a05c8cde58b003cb09dd3809343))
- Add lyrics support for Jellyfin provider (#7933) ([8fb733a](https://github.com/jrhubott/music-assistant-server/commit/8fb733a1f0953a7d306b59a91402428a4a8b5d21))
- Add Title Reveal game to Music Quiz (#7852) ([d44cd8d](https://github.com/jrhubott/music-assistant-server/commit/d44cd8d752e02efb7108c6254451467b99a88b09))
- Narrow exception handling in Playlist Metadata (#7929) ([68a68ac](https://github.com/jrhubott/music-assistant-server/commit/68a68acee62cf5b0ba982c0e81692973c59daa79))
- Narrow exception handling in Smart Playlist (#7924) ([4d0ded3](https://github.com/jrhubott/music-assistant-server/commit/4d0ded379417fb9a7b6267ea9eca9e641eeb801a))
- Use lazy log arguments in the remaining providers and turn on the G004 lint rule (#7914) ([c226587](https://github.com/jrhubott/music-assistant-server/commit/c226587de2070caeb2aaa28691c42241221fa7f4))
- Allow source-sharing clients to request guest recipients (#7849) ([6721e27](https://github.com/jrhubott/music-assistant-server/commit/6721e27f7abdcc8d79e667ac97cf9b7cde13da3e))
- Let Discover rows hide fully played episodes and audiobooks (#7898) ([63130f9](https://github.com/jrhubott/music-assistant-server/commit/63130f9912a49ab614831d2853cb7ef7bb75d59d))
- Start checking broad error catches, first batch of providers (#7921) ([10e16dc](https://github.com/jrhubott/music-assistant-server/commit/10e16dcaa9fbf64f2971b1db8e699419322d4f29))
- ⬆️ Update music-assistant-models to 1.1.247 (#7949) ([222258c](https://github.com/jrhubott/music-assistant-server/commit/222258c92f0291139be159d2c33be83a23e72ed2))
- Subsonic: use sonicSimilarity for similar tracks (#7931) ([3a6a60b](https://github.com/jrhubott/music-assistant-server/commit/3a6a60b94da9124f92698de5e943d54013b070da))
- ⬆️ Update music-assistant-frontend to 2.17.375 (#7948) ([498d7a4](https://github.com/jrhubott/music-assistant-server/commit/498d7a4dda1dda5f2029668e8936da942eb5ff47))
- Fetch missing 'now playing' metadata images from Spotify oEmbed API for BBC Sounds (#7883) ([c50632b](https://github.com/jrhubott/music-assistant-server/commit/c50632bd235d8d21f28a80fb6e6e87c765494d3b))
- Narrow BookOrbit broad exception handlers for BLE001 (#7928) ([0d8b2dd](https://github.com/jrhubott/music-assistant-server/commit/0d8b2dd0ce8a78ce952e49566699fb7e410e5777))
- Clearer texts around community providers (#7944) ([847926d](https://github.com/jrhubott/music-assistant-server/commit/847926d6293f667dec340772005e7b0ccafcbeb8))
- Run a provider from its provider or providers folder in dev mode (#7946) ([126c6d6](https://github.com/jrhubott/music-assistant-server/commit/126c6d646ec14ee680e7051258e82dab0a09bac2))
- Explain both routes to someone adding a provider (#7943) ([f3566b2](https://github.com/jrhubott/music-assistant-server/commit/f3566b271fdb2ec0ce1c9b3761f6322363ba166b))
- Let music providers say in their manifest what they offer (#7930) ([451ff48](https://github.com/jrhubott/music-assistant-server/commit/451ff4883141af652101160ae62672ed5d3a8028))
- Show the position in the track on a squeezelite speaker in a Sendspin group (#7942) ([f088901](https://github.com/jrhubott/music-assistant-server/commit/f088901a2fc47cb5161f3bb755d18945b26f7188))
- Read the AirPlay session and stream settings through the player (#7932) ([37d3d8e](https://github.com/jrhubott/music-assistant-server/commit/37d3d8eeabcd264bfc1bc59e90376b2bf1487674))
- Fix a DLNA error at startup for Sonos stereo pairs (#7935) ([dd67435](https://github.com/jrhubott/music-assistant-server/commit/dd67435d1d38048a7e506790f874ad360dda9d88))
- Make the Raumfeld player tests pass in any order (#7940) ([32de8c7](https://github.com/jrhubott/music-assistant-server/commit/32de8c743d19e691ee6baf8ee94aeb38e005370e))
- Play a Sendspin device's line-in without a separate plugin (#7909) ([05f89e6](https://github.com/jrhubott/music-assistant-server/commit/05f89e6823b97e2c5dc26a643b84f334d986cd77))
- Don't treat Sendspin remotes, artwork screens and lights as speakers (#7882) ([6e87e46](https://github.com/jrhubott/music-assistant-server/commit/6e87e463b9e4239ac6627d5a91f088382f446401))
- Show the repeat and shuffle of the queue on Squeezebox and squeezelite players (#7934) ([a2abfe6](https://github.com/jrhubott/music-assistant-server/commit/a2abfe682078c8fb51b3273a6d3f8741a6b2aeab))
- Group the crossfade, volume normalization and self-registration settings by what they do (#7889) ([3cc9d30](https://github.com/jrhubott/music-assistant-server/commit/3cc9d3085572cbbdcbe8dbdd19e9396afce1af07))
- Let a provider serve a page of its own, listed in the app's menu (#7910) ([629ce2e](https://github.com/jrhubott/music-assistant-server/commit/629ce2eb997784584d0288dbcf295f1a7a3d30b6))
- Let a speaker keep its music service stream when it moves to the next track (#7870) ([c6dfc87](https://github.com/jrhubott/music-assistant-server/commit/c6dfc87a0e86a5fa10d49ee3e389dff8b0e72ad6))
- …and more, see the compare link

### Frontend: 12 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/967425ccb219...458548af4979))

- Add guest nicknames, shout-outs, reactions and a DJ leaderboard to the party screen ([19eed8e](https://github.com/jrhubott/music-assistant-frontend/commit/19eed8ed737617b79088793e29519b49c5452985))
- Hide fully played episodes on the Latest podcast episodes row (#3233) ([144001b](https://github.com/jrhubott/music-assistant-frontend/commit/144001bde874993c8dd44daf24cb4d2a4916f261))
- Show controllers in their own section on the Players page (#3252) ([b582530](https://github.com/jrhubott/music-assistant-frontend/commit/b582530da5b739e14d4173c78e603fcb77f62042))
- Use the shared settings card for the links on a player's page (#3251) ([4b91746](https://github.com/jrhubott/music-assistant-frontend/commit/4b91746b6ad10f301aebd11822ca8f871075fcaa))
- Simplify the provider lists to one list per settings page (#3250) ([fc72a49](https://github.com/jrhubott/music-assistant-frontend/commit/fc72a491231c96c4cbc4b6b0786d221e8f53dafd))
- Game interface for Title Reveal game in Music Quiz (#3220) ([b70c16b](https://github.com/jrhubott/music-assistant-frontend/commit/b70c16bf27e6c51b67a0bdb039d91721d87e1874))
- Show what each music source offers, with live sources in the same list (#3245) ([e758762](https://github.com/jrhubott/music-assistant-frontend/commit/e758762e27e6b372d33703ebabd682ab8176230c))
- Give every settings page the same header (#3244) ([74b7ce5](https://github.com/jrhubott/music-assistant-frontend/commit/74b7ce5d4866186d6867ff30dda2b8e23a69b71e))
- Give every settings page an address of its own (#3243) ([02335a4](https://github.com/jrhubott/music-assistant-frontend/commit/02335a4f50938d9a9f56df324f74afc42f6e650b))
- Rework the Profile page around your theme, language and personal settings (#3227) ([86f18b6](https://github.com/jrhubott/music-assistant-frontend/commit/86f18b6340a46252e352bac6060e500c307d2b17))
- Music, Players and System as hub pages, with audio sources under Music (#3236) ([d529814](https://github.com/jrhubott/music-assistant-frontend/commit/d529814a6b6ea61e1550930a7ebf722386b84c21))
- Give Home Assistant its own settings page (#3234) ([59af737](https://github.com/jrhubott/music-assistant-frontend/commit/59af7379dd6ab3834d9283cec73e8dfb6ac0e6a8))

## 2.11.0.dev202611191302

Built 2026-11-19 13:21 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/debde5ce96798f40dbc42db10b8803193c29f588) (debde5ce9)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/967425ccb219e4cf5517be928fa00e741be953ab) (967425ccb)

### Server: 1 new commit ([compare](https://github.com/jrhubott/music-assistant-server/compare/cbefaeff5cf2...debde5ce9679))

- Party: add a lyrics delay for the karaoke dashboard ([484da8b](https://github.com/jrhubott/music-assistant-server/commit/484da8b8825f8ca76b7b71099b812638556317ac))

### Frontend: 3 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/4a9035241e08...967425ccb219))

- Party dashboard: hold the lyrics back by the party's lyrics delay ([4c5f351](https://github.com/jrhubott/music-assistant-frontend/commit/4c5f3516d8b63a10d4fedbdbec27e999a7b21b5b))
- Party dashboard: count down the line after a musical break ([c651bd6](https://github.com/jrhubott/music-assistant-frontend/commit/c651bd604b99f8d6932e1ea901229fcda982aadf))
- Lyrics: finish the word fill before the next line takes over ([019a3c4](https://github.com/jrhubott/music-assistant-frontend/commit/019a3c4239ca02ddaa57663e24218dd88a61a97b))

## 2.11.0.dev202611190614

Built 2026-11-19 06:33 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/cbefaeff5cf24080f13599a7cc5265c9017c53dd) (cbefaeff5)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/4a9035241e088841bb5cd16c9924546dd0b2e471) (4a9035241)

### Server: 10 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/ce4e64faf01d...cbefaeff5cf2))

- Keep the speaker's player when its headphone zone is back first ([a702f44](https://github.com/jrhubott/music-assistant-server/commit/a702f4496389548e37158cab416c9b7846c21a4a))
- Give the follow handler tests' stub player the mass a config update reads ([9c39d5a](https://github.com/jrhubott/music-assistant-server/commit/9c39d5abfa511763b8f19a38410d7d8c2013fc7c))
- Let Hue lights follow only Sonos speakers, behind a plugin option ([c911dbf](https://github.com/jrhubott/music-assistant-server/commit/c911dbf81d2ec5d839884781d7ff0cb1a1a9f92c))
- Correct small offsets of a followed speaker at render time ([647d0d4](https://github.com/jrhubott/music-assistant-server/commit/647d0d4684ca946142b12148d22a349c7e13030f))
- Publish the player a light follows in its extra attributes ([200b511](https://github.com/jrhubott/music-assistant-server/commit/200b5111efdcc95714639588f8f8f9d76b3b5e74))
- Add a per-light delay for lights that follow a speaker ([8b9bd93](https://github.com/jrhubott/music-assistant-server/commit/8b9bd93da157928e3694519c9af680f7794a2f17))
- Let a light follow its speaker again once its group regroups natively ([67c6c5f](https://github.com/jrhubott/music-assistant-server/commit/67c6c5f026a1ec7a2a7b19448427b451ba32b1f1))
- Refuse playback commands on a light that follows a speaker ([edf9a75](https://github.com/jrhubott/music-assistant-server/commit/edf9a7587d67ad60e5c0611b89fe308e79acbf2f))
- Turn following lights into Sendspin members once their group moves onto Sendspin ([8c91fca](https://github.com/jrhubott/music-assistant-server/commit/8c91fcab4d702d6acbb49c4685252b096e6fe189))
- Let Hue lights follow a speaker that plays over its own protocol ([d2fa40c](https://github.com/jrhubott/music-assistant-server/commit/d2fa40ca2bca96556144358a5a2cb1c81b4b1b2b))

### Frontend: 3 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/e259addc9dc0...4a9035241e08))

- Mark lights that follow a speaker, and say when they cannot follow ([a6627e1](https://github.com/jrhubott/music-assistant-frontend/commit/a6627e1335f90d5bf2dccdb22650b61a23f2180a))
- Show lights that follow a speaker in the audio pipeline ([03052e7](https://github.com/jrhubott/music-assistant-frontend/commit/03052e719b6641848af0a29c88400b732a23aff9))
- feat: show lights in a group apart from its speakers ([b68491b](https://github.com/jrhubott/music-assistant-frontend/commit/b68491b236643df75d375dc8fd72a295a02567ef))

## 2.11.0.dev202611190551

Built 2026-11-19 06:14 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/e493016b53e75e7fe04589e29440fb2a2571ae59) (e493016b5)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/4a9035241e088841bb5cd16c9924546dd0b2e471) (4a9035241)

### Server: 9 new commits ([compare](https://github.com/jrhubott/music-assistant-server/compare/ce4e64faf01d...e493016b53e7))

- Give the follow handler tests' stub player the mass a config update reads ([9c39d5a](https://github.com/jrhubott/music-assistant-server/commit/9c39d5abfa511763b8f19a38410d7d8c2013fc7c))
- Let Hue lights follow only Sonos speakers, behind a plugin option ([c911dbf](https://github.com/jrhubott/music-assistant-server/commit/c911dbf81d2ec5d839884781d7ff0cb1a1a9f92c))
- Correct small offsets of a followed speaker at render time ([647d0d4](https://github.com/jrhubott/music-assistant-server/commit/647d0d4684ca946142b12148d22a349c7e13030f))
- Publish the player a light follows in its extra attributes ([200b511](https://github.com/jrhubott/music-assistant-server/commit/200b5111efdcc95714639588f8f8f9d76b3b5e74))
- Add a per-light delay for lights that follow a speaker ([8b9bd93](https://github.com/jrhubott/music-assistant-server/commit/8b9bd93da157928e3694519c9af680f7794a2f17))
- Let a light follow its speaker again once its group regroups natively ([67c6c5f](https://github.com/jrhubott/music-assistant-server/commit/67c6c5f026a1ec7a2a7b19448427b451ba32b1f1))
- Refuse playback commands on a light that follows a speaker ([edf9a75](https://github.com/jrhubott/music-assistant-server/commit/edf9a7587d67ad60e5c0611b89fe308e79acbf2f))
- Turn following lights into Sendspin members once their group moves onto Sendspin ([8c91fca](https://github.com/jrhubott/music-assistant-server/commit/8c91fcab4d702d6acbb49c4685252b096e6fe189))
- Let Hue lights follow a speaker that plays over its own protocol ([d2fa40c](https://github.com/jrhubott/music-assistant-server/commit/d2fa40ca2bca96556144358a5a2cb1c81b4b1b2b))

### Frontend: 3 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/e259addc9dc0...4a9035241e08))

- Mark lights that follow a speaker, and say when they cannot follow ([a6627e1](https://github.com/jrhubott/music-assistant-frontend/commit/a6627e1335f90d5bf2dccdb22650b61a23f2180a))
- Show lights that follow a speaker in the audio pipeline ([03052e7](https://github.com/jrhubott/music-assistant-frontend/commit/03052e719b6641848af0a29c88400b732a23aff9))
- feat: show lights in a group apart from its speakers ([b68491b](https://github.com/jrhubott/music-assistant-frontend/commit/b68491b236643df75d375dc8fd72a295a02567ef))

## 2.11.0.dev202611190449

Built 2026-11-19 05:09 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/ce4e64faf01d82e8d056de264631f115cfc07f2f) (ce4e64faf)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/e259addc9dc09f6c158d2eb66b713870d0a7bf3b) (e259addc9)

### Server: no new commits

### Frontend: 18 new commits ([compare](https://github.com/jrhubott/music-assistant-frontend/compare/a64dad67dd8d...e259addc9dc0))

- Party dashboard: highlight lyrics word by word ([438d2a4](https://github.com/jrhubott/music-assistant-frontend/commit/438d2a4d934a3bb743447d5dbf19249f0c29ab7f))
- Always show the close chevron on the fullscreen player (#3248) ([41d6ce3](https://github.com/jrhubott/music-assistant-frontend/commit/41d6ce327f8b13068657dcc524d9af9a4b9e43f7))
- System becomes a hub, with all log levels on Diagnostics (#3231) ([00afb7a](https://github.com/jrhubott/music-assistant-frontend/commit/00afb7aa7861337f0ccdb6a784be0e0334c0b6da))
- Library options under Music sources and metadata settings under Metadata sources (#3229) ([40aabe0](https://github.com/jrhubott/music-assistant-frontend/commit/40aabe0bd59ebc4493d9d6d254424b38e872080d))
- Connect Home Assistant from the setup wizard (#3238) ([055302a](https://github.com/jrhubott/music-assistant-frontend/commit/055302a2c42900b9b79263b1f7caab666e74f963))
- Group devices on the Players page and add a Playback page (#3226) ([1079b78](https://github.com/jrhubott/music-assistant-frontend/commit/1079b78e8d6ac9bb8b4e9777434c2590c3225537))
- Offer the apps that play to Music Assistant in the setup wizard (#3237) ([ef77496](https://github.com/jrhubott/music-assistant-frontend/commit/ef774962a14dabe13c226ace9fd6f0b3a523b53d))
- Show the network settings together on one Network page (#3223) ([b8a45d6](https://github.com/jrhubott/music-assistant-frontend/commit/b8a45d6f74d82ad00006907a408cc222c9843eb9))
- Audio analysis and background tasks each get one place in Settings (#3222) ([94d421e](https://github.com/jrhubott/music-assistant-frontend/commit/94d421ebac83a7f3e225218d59b2bcc16a0a2e4e))
- Open the page a plugin serves from the main menu (#3241) ([dea7a0e](https://github.com/jrhubott/music-assistant-frontend/commit/dea7a0e1e51653cf4da33cc037c55757243febb3))
- Fix the volume slider ignoring the mouse on touchscreen PCs (#3242) ([769fe42](https://github.com/jrhubott/music-assistant-frontend/commit/769fe42f8db4c5aebf7f780fdff9d4ad310352e0))
- Split off an output from its own row in the player settings (#3247) ([fd83953](https://github.com/jrhubott/music-assistant-frontend/commit/fd8395337958c90ee6a12b002974d818a74c7857))
- Chunk oversized API commands over remote access (#3160) ([0ff5e50](https://github.com/jrhubott/music-assistant-frontend/commit/0ff5e50cf59002f7ce26e5eceb32460db2135337))
- Open author and narrator pages under Audiobooks, link them in collections (#3235) ([66ccaa2](https://github.com/jrhubott/music-assistant-frontend/commit/66ccaa260d39d3a679526b98a2325de66861e970))
- Show the right items after changing a Discover row's source filter (#3232) ([4e0f7b0](https://github.com/jrhubott/music-assistant-frontend/commit/4e0f7b038181b123769a718663fba8b87a1e2913))
- Leave switched-off EQ bands out of the graph's total line (#3239) ([63dfec7](https://github.com/jrhubott/music-assistant-frontend/commit/63dfec7360648e0c1a18c641e5d7f890ca41017a))
- Drag the Marketplace rows with the mouse (#3230) ([8de6dc1](https://github.com/jrhubott/music-assistant-frontend/commit/8de6dc19675cd296e9c139db37d3ae6dd04ab45b))
- Load no remote images from provider text (#3240) ([3dc7881](https://github.com/jrhubott/music-assistant-frontend/commit/3dc78811fcf49a0b65a9a04d4da156c2b2c6d18e))

## 2.11.0.dev202611190411

Built 2026-11-19 04:35 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/ce4e64faf01d82e8d056de264631f115cfc07f2f) (ce4e64faf)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/a64dad67dd8d5fefbb568816a17d28c7b6dc2c50) (a64dad67d)

## 2.11.0.dev202611181538

Built 2026-11-18 16:04 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/b0775eb0acec3bd180d1d7e0a06e953856271a61) (b0775eb0a)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/4cec1f1240a3312392a2616b2951c931ade4d735) (4cec1f124)

## 2.11.0.dev202611180513

Built 2026-11-18 05:39 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/13eba7e043a631c428edd629b300785194305460) (13eba7e04)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/4cec1f1240a3312392a2616b2951c931ade4d735) (4cec1f124)

## 2.11.0.dev202611180002

Built 2026-11-18 00:18 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/91c0e2eef7002f807096ac179b8fdf99d893a670) (91c0e2eef)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/ba909c45619746df7771d5c254c692fe30256156) (ba909c456)

## 2.11.0.dev202611171550

Built 2026-11-17 16:13 UTC from:

- server [`edge`](https://github.com/jrhubott/music-assistant-server/tree/bbf18ba1b89a25a600b8f93101991e8c6da77f48) (bbf18ba1b)
- frontend [`edge`](https://github.com/jrhubott/music-assistant-frontend/tree/ba909c45619746df7771d5c254c692fe30256156) (ba909c456)

## 2.11.0.dev202611171437

Built 2026-11-17 15:03 UTC from:

- server [`feature/hue-grouped-follow`](https://github.com/jrhubott/music-assistant-server/tree/484413f52b2188bcb8f49f99b18f1366037aab6c) (484413f52)
- frontend [`feature/light-followers`](https://github.com/jrhubott/music-assistant-frontend/tree/a6627e1335f90d5bf2dccdb22650b61a23f2180a) (a6627e133)

## 2.11.0.dev202611170459

Built 2026-11-17 05:20 UTC from:

- server [`feature/hue-grouped-follow`](https://github.com/jrhubott/music-assistant-server/tree/ea8101f0e9239abd09ada434db0829ac79f19bd2) (ea8101f0e)
- frontend [`feature/light-followers`](https://github.com/jrhubott/music-assistant-frontend/tree/dc196c718495b83d06bbd795ffad6f7e62c1bf7b) (dc196c718)
