# AirPlay

> Source: https://developer.apple.com/design/human-interface-guidelines/airplay · AirPlay lets people stream media wirelessly from iOS, iPadOS, macOS, and tvOS devices to Apple TV, HomePod, and AirPlay-compatible TVs and speakers.

## When to use / core idea
- Wireless streaming (and mirroring) of audio/video to external AirPlay receivers.
- Default to the system media player (`AVPlayerViewController`), which already supports AirPlay, chapters, subtitles, closed captions; build a custom player only if the system one doesn't meet your needs.
- AirPlay icon/name are trademarks: strict rules for display and wording.

## Rules
### Best practices
- **Prefer the system-provided media player** — standard controls, consistent familiar experience, easy to implement; consider a custom video player only if it doesn't meet your needs.
- **Provide content in the highest possible resolution** — HLS playlist must include the full range of resolutions (AVFoundation auto-selects per device); e.g. 720p that looks fine on iPhone looks low quality on a 4K TV.
- **Stream only the content people expect** — avoid streaming background loops and short video experiences that only make sense inside the app.
- **Support both AirPlay streaming and mirroring** — most flexibility.
- **Support remote control events** — enables play/pause/fast forward from Lock Screen, Siri, HomePod.
- **Don't stop playback when your app enters the background or the device locks** — also avoid automatic mirroring; people don't want other device content streamed without explicitly choosing it.
- **Don't interrupt another app's playback unless your app is starting to play immersive content** — launch videos / auto-play inline videos play only on the local device while current playback continues (`ambient` audio session category).
- **Let people use other parts of your app during playback** — app must stay functional; when people navigate away from playback, don't let other in-app videos start and interrupt the stream.
- **If necessary, provide a custom interface for controlling media playback** — custom buttons must match appearance and behavior of system ones, including distinct states for playback starting, occurring, unavailable; use only Apple-provided symbols for controls that initiate AirPlay; place the AirPlay icon in the lower-right corner of the player (iOS 16 / iPadOS 16 and later).

### Using AirPlay icons
- Download icons from Apple Design Resources. Audio icon = triangle below three concentric lines; video icon = triangle below a rounded rectangle.
- Black icon: on white/light backgrounds when other technology icons also appear black.
- White icon: on black/dark backgrounds when other technology icons also appear white.
- Custom color: when other technology icons appear in that same color.
- **Position the AirPlay icon consistently with other technology icons** — if others are shown inside shapes, AirPlay can be too.
- **Don't use the AirPlay icon or name in custom buttons or interactive elements** — use icon and name only in noninteractive ways.
- **Pair the icon with the name *AirPlay* correctly** — name below or beside the icon only if other technologies are referenced that way; use the layout's same font; avoid using the icon within text or as a replacement for the name.
- **Emphasize your app over AirPlay** — AirPlay references less prominent than your app name/identity.

### Referring to AirPlay
- **Use correct capitalization** — one word, uppercase *A* and *P* followed by lowercase; all-uppercase allowed only if the layout uses all-uppercase designations.
- **Always use *AirPlay* as a noun.**
  - ✅ "Use AirPlay to listen on your speaker"; ❌ "AirPlay to your speaker"; ❌ "You can AirPlay with [App Name]".
- **Use terms like *works with*, *use*, *supports*, *compatible*.**
  - ✅ "[App Name] is compatible with AirPlay", "AirPlay-enabled speaker", "You can use AirPlay with [App Name]"; ❌ "[App Name] has AirPlay".
- **Use the name *Apple* with *AirPlay* if desired** — ✅ "Compatible with Apple AirPlay".
- **Refer to AirPlay if appropriate and to add clarity** — for AirPlay-specific content and technical specs; ✅ "[App Name] now supports AirPlay".

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS. Not supported in watchOS.

## APIs
`AVPlayerViewController` (AVKit), HTTP Live Streaming, `usesExternalPlaybackWhileExternalScreenIsActive` (AVFoundation `AVPlayer`), Remote command center events (MediaPlayer), `AVAudioSession.Category.ambient` (AVFAudio)

## Related
playing-video, playing-audio, designing-for-tvos
