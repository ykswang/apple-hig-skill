# Live-viewing apps

> Source: https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps · Prioritize live content and create fun, fluid interactions that encourage immersion in the live-viewing experience.

## When to use / core idea
- For apps streaming live TV/content: in every screen, draw attention to live content and make it distinguishable from video-on-demand (VOD) at a glance.
- Typically includes an electronic program guide (EPG) and may include cloud DVR. See `playing-video`, `remotes`.

## Rules
### Best practices
- **Feature live content prominently and make it easy to access** — minimize time from launch to playback; live content in the first tab means no more than one tap to start.
- **Let people tap once — or not at all — to start playback** — e.g. Watch Now button over featured/recently viewed live content; on tap it disappears immediately and full-screen playback replaces the UI.
- **Make sure live content looks live** — playing it is best; also mark it, e.g. a "Live" collection row with a badge, symbol, or sash on each item.
- **Consider indicating the progress of currently playing live content** — progress bar or other indicator of how much remains.
- **Give people additional actions and viewing alternatives** — playback is always the primary action; also record, restart, download, etc., in the same order everywhere (e.g. Watch, Start Over, Record, Favorite); show other airtimes so people can schedule viewing.
- **Consider using a content footer for browsing channels during playback** — browse without leaving playback. If used:
  - Give it a subtle treatment (e.g. darkening) to keep text legible and items distinct from the video behind.
  - Make the currently playing item's thumbnail identifiable (badge it or tint its progress bar).
  - Match footer categories to the EPG's.
  - Make invoke/dismiss simple and predictable (e.g. swipe up to invoke → swipe down to dismiss).
- **Provide instant visual feedback when people change channels** — confirms arrival at the desired channel and buys time for the stream to load.
- **Match audio to the current context** — audio continues while browsing with live content playing in the background; when people navigate away from the live tab, stop audio.

### EPG experience
- **Prominently display current information and make it easy to return to playback** — current program, channel, and time easy to spot on opening the EPG.
- **Make browsing the EPG effortless** — easy paging, scrolling, jumping; consider a My Channels or Favorites group.
- **Group content into familiar categories to help people find it more easily** — e.g. Movies, TV Shows, Kids, Sports, Popular; use the same categories in the content footer.
- **Let people browse the EPG without leaving their current content** — keep playing in picture-in-picture or in the background.

### Cloud DVR
- **Let people start and stop recording from the info panel** — while live-streaming, reveal info panel to record immediately.
- **Let people record a future program in a view that provides details about the content** — offer recording only that program or all future episodes.
- **Help people adapt the recording experience to their needs** — e.g. only current episode, only new episodes, only games with specific teams.
- **Allow playback and other content-specific actions within your cloud DVR area** — in content detail views, let people play or delete and, if applicable, adjust recording settings.
- **Consider offering a control that lets people manage cloud DVR settings** — e.g. delete watched recordings or content older than a number of days; ideally offer automatic storage management that overwrites oldest or already-viewed content.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## Related
`remotes, playing-video, launching`
