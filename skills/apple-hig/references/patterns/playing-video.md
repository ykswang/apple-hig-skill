# Playing video

> Source: https://developer.apple.com/design/human-interface-guidelines/playing-video · People expect to enjoy rich video experiences on their devices, regardless of the app or game they're using.

## When to use / core idea
- System video players embed playback in iOS, iPadOS, macOS, tvOS, visionOS; you can also offer content through the TV app.
- System players support aspect-ratio playback modes and (in most platforms) Picture in Picture (PiP). Default mode by aspect ratio (people can switch):
  - *Aspect-fill* (full-screen): scales to fill display, may crop edges — default for wide video (2:1 through 2.40:1).
  - *Aspect* (fit-to-screen): whole video visible with letterbox/pillarbox as needed — default for standard (4:3, 16:9, up to 2:1) and ultrawide (above 2.40:1).
- visionOS and tvOS player adds *transport controls* (subtitles, audio language; actions like add to library, favorite) and below them *content tabs* (Info, Episodes, Chapters). In visionOS transport controls appear as an `ornaments`.

## Rules
### Best practices
- **Use the system video player to give people a familiar and convenient experience** — if a custom player is truly required, model its behavior and interface on the system player; slight divergence frustrates because habitual interactions become uncertain.
- **Always display video content at its original aspect ratio** — embedded letterbox/pillarbox padding prevents correct scaling, makes video smaller in both full-screen and fit-to-screen modes, and breaks edge-to-edge non-full-screen contexts (e.g. PiP on iPad). E.g. on iPhone Xs, a padded 4:3 or 21:9 video displays smaller than an unpadded one relative to the AVKit safe area.
- **Provide additional information when it adds value** — iOS, iPadOS, tvOS, visionOS: image, title, description, etc.; restrict it so it doesn't obscure playback.
- **Support the interactions people expect, regardless of the input device they're using to control playback** — e.g. Space on a connected keyboard plays/pauses on Apple Vision Pro, Mac, iPhone, iPad, Apple TV; familiar Siri Remote gestures on Apple TV (see `keyboards`, `remotes`).
- **If people need to access playback options or content-specific information in your tvOS app, consider adding a transport control or a custom content tab** — only the most useful actions/info; actions take no more than a step or two; succinct content. Transport control for playback actions (e.g. favoriting); custom content tabs for supplementary info or recommendations.
- **Avoid allowing audio from different sources to mix as viewers switch between modes** — mixing happens when a source mishandles secondary audio (e.g. video in PiP muted → game plays music full-screen → video unmuted → game audio must yield).

### Integrating with the TV app
- The TV app gives global access to favorite, recent, recommended content; starting playback opens and transitions to your app.
- **Ensure a smooth transition to your app** — TV app fades to black and doesn't show your launch screen; immediately present your own black screen before playing/resuming.
- **Show the expected content immediately** — go from black screen straight into content; no splash, detail screens, intro animations, or other barriers. If an interstitial is unavoidable, Select steps through it and Play skips it to start playback.
- **Avoid asking people if they want to resume playback** — resume automatically without confirmation.
- **Play or pause playback when people press Space on a connected Bluetooth keyboard.**
- **Make sure content plays for the correct viewer** — if the TV app specifies a profile, switch to it automatically before playback; if not specified, ask the viewer to choose one before playback so it's available in future.
- **Use the previous end time when resuming playback of a long video clip.**

#### Loading content
- **Avoid displaying loading screens when possible** — if loading takes more than two seconds, consider a black loading screen with a centered activity spinner and no surrounding content.
- **Start playback immediately** — show the loading screen only until enough content loads to begin; load the rest in the background.
- **Minimize loading screen content** — minimal branding/images, keep the black background for a seamless transition.

#### Exiting playback
- After exiting, people stay in your app (not the TV app); avoid disorientation.
- **Show a contextually relevant screen** — detail view for the content just watched with a resume option; otherwise a menu listing this content, or your main menu.
- **Be prepared for an immediate exit** — prepare the exit view as soon as possible after receiving a playback notification.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS.
### tvOS
- **Defer to content when displaying logos or noninteractive overlays above video** — small, unobtrusive logo or countdown timer may be OK; avoid large distracting overlays. Some devices are prone to image retention: keep overlays short and prefer translucent SDR graphics over bright, opaque content.
- **Show interactive overlays gracefully** — for quizzes, surveys, progress check-ins: implement a minimum delay of 0.5 seconds to pause media and display the overlay; give a clear way to dismiss and resume.
### visionOS
- **Help people stay comfortable when playing video in your app** — let people choose when to start; use a small, resizable playback window; keep surroundings visible during playback.
- **In a fully immersive experience, avoid letting virtual content obscure playback or transport controls** — the system places the player at a predictable optimal location; keep virtual content from occluding the controls in the ornament near the bottom of the player.
- **Avoid automatically starting a fully immersive video playback experience** — people need control and warning.
- **Create a thumbnail track if you want to support scrubbing** — thumbnails each 160 px wide (HLS Trick Play).
- **Avoid expanding an inline video player to fill a window** — in a window, controls are in the same plane as the player (not a floating ornament); inline video must be 2D, and window content should remain visible around it so people don't expect immersive playback.
- **Use a RealityKit video player if you need to play video in a view like a splash screen or a transitional view** — no playback controls or system integration (dimming, view anchoring) needed; handles correct aspect ratio for 2D and 3D and supports closed captions; can play video as an effect on a custom view/object surface.
### watchOS
- The system manages playback; apps play short clips only while active in the foreground — inline via a movie element or in a separate interface.
- **Keep video clips short** — prefer no longer than 30 seconds (disk space, wrist-raise fatigue).
- **Use the recommended sizes and encoding values for media assets** — avoid scaling clips (hurts performance and appearance). See Specs.
- **Avoid creating a poster image that looks like a system control** — people must understand tapping a movie element plays it.
- **Consider creating a poster image that represents a video clip's contents** — tapping replaces it with inline playback; a relevant poster helps people decide; avoid unrelated posters or ones mistakable for controls.

## Specs
- Aspect-fill default: 2:1 through 2.40:1. Aspect (fit) default: 4:3, 16:9, up to 2:1, and above 2.40:1.
- tvOS: loading screen only if loading > 2 seconds; interactive overlay minimum delay 0.5 seconds.
- visionOS scrubbing thumbnails: 160 px wide.
- watchOS clips: ≤ 30 seconds preferred.

watchOS media encoding (audio values apply to movies and audio-only assets):

| Attribute | Value |
| --- | --- |
| Video codec | H.264 High Profile |
| Video bit rate | 160 kbps at up to 30 fps |
| Resolution (full screen) | 208x260 px (portrait orientation) |
| Resolution (16:9) | 320x180 px (landscape orientation) |
| Audio | 64 kbps HE-AAC |

## APIs
`resizeAspectFill` (AVFoundation), `resizeAspect` (AVFoundation), `externalMetadata` (AVFoundation), `silenceSecondaryAudioHintNotification` (avfaudio), `HTTP Live Streaming (HLS) Authoring Specification for Apple Devices > Trick Play` (http-live-streaming), `AVPlayerViewController` (AVKit), `RealityKit` (RealityKit), `VideoPlayer` (AVKit), `Configuring your app for media playback` (AVFoundation), `AVKit` (AVKit)

## Related
`playing-audio, feedback, ornaments, keyboards, remotes, live-viewing-apps, immersive-experiences`
