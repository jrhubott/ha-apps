# Changelog

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
