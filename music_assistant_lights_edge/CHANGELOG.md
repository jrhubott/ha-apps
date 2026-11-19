# Changelog

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
