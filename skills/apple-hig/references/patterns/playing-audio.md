# Playing audio

> Source: https://developer.apple.com/design/human-interface-guidelines/playing-audio · People expect rich audio experiences that automatically adjust when the context changes on the device.

## When to use / core idea
- Audio outputs: internal/external speakers, headphones, Bluetooth, AirPlay. Controls: volume buttons, iPhone Ring/Silent switch, headphone controls, Control Center volume slider, third-party accessory controls. Sound must behave as expected as volume/output change.
- **Silence**: silent mode silences unexpected sounds (ringtones, message tones) and nonessential sounds (keyboard clicks, sound effects, game soundtracks, audible feedback); only explicitly initiated audio plays (media playback, alarms, audio/video messaging).
- **Volume**: people expect volume settings to affect all system sound (music, in-app effects) regardless of adjustment method; exception: iPhone ringer volume, adjustable separately in Settings.
- **Headphones**: on connect, sound reroutes automatically without interruption; on disconnect, playback pauses immediately.

## Rules
### Best practices
- **Adjust levels automatically when necessary — don't adjust the overall volume** — adjust relative, independent levels for a good mix; the system volume always governs final output.
- **Permit rerouting of audio when possible** — e.g. living room stereo, car radio, Apple TV; support unless there's a compelling reason not to.
- **Use the system-provided volume view to let people make audio adjustments** — includes a volume slider and an output-rerouting control; slider appearance is customizable.
- **Choose an audio category that fits the way your app or game uses sound** — category determines mixing, background play, and response to the Ring/Silent switch; e.g. don't stop other apps' music unnecessarily (see Specs).
- **Respond to audio controls only when it makes sense** — OK when actively playing audio, in a clear audio-related context, or connected to a Bluetooth/AirPlay device; otherwise avoid halting another app's audio when people activate a control.
- **Avoid repurposing audio controls** — don't redefine their meaning; if you don't support a control, don't respond to it.
- **Consider creating custom audio player controls only if you need to offer commands that the system doesn't support** — e.g. custom skip increments, or related content like a sports score.
- **Let other apps know when your app finishes playing temporary audio** — flag the audio session so interrupted apps know when to resume.

### Handling interruptions
- Most apps rely on default interruption behavior; you can customize.
- **Determine how to respond to audio-session interruptions** — e.g. recording apps can ask not to be interrupted by an incoming call unless it's accepted. VoIP apps must end a call when people close the iPad Smart Folio while using the built-in mic (closing mutes the mic and interrupts the session); restarting the session on reopening risks unmuting the mic without people's knowledge (privacy). Inspect the interruption to decide.
- **When an interruption ends, determine whether to resume audio playback automatically** — interruptions are *resumable* (incoming call) or *nonresumable* (new music playlist). Media apps playing when interrupted should check for resumable before continuing; games needn't check and can resume automatically (audio plays without explicit user choice).

## Platform considerations
### iOS, iPadOS
- **Use the system's sound services to play short sounds and vibrations.**
### macOS
- Notification sounds mix with other audio by default.
### tvOS
- The system plays audio only when people initiate it (in-app interactions, device calibration); no sounds accompany alerts or notifications.
### visionOS
- Subtle, expressive sounds provide feedback when people look at and gesture on virtual objects. *Spatial Audio* combines algorithms with knowledge of physical surroundings so sound seems to come from specific locations.
- Important: avoid communicating important information using only sound (all platforms); always provide additional ways (see `accessibility`).
- Now Playing app audio pauses automatically when its window closes; non-Now Playing app audio can duck when people look away to another app.
- **Prefer playing sound** — people generally keep sound on; silent apps (especially in immersive moments) feel lifeless or broken; create meaningful sounds aiding navigation and spatial understanding.
- **Design custom sounds for custom UI elements** — system elements play sound to help locate them and give interaction feedback; do the same for custom elements.
- **Use Spatial Audio to create an intuitive, engaging experience** — works especially well fully immersive; *ambient audio* = pervasive sounds anchoring people in a virtual world; *audio source* = sound from a specific object; consider using both.
- **Consider defining a range of places from which your app sounds can originate** — e.g. sound from a moving window keeps coming from the window.
- **Consider varying sounds that people could perceive as repetitive over time** — e.g. system virtual keyboard subtly varies pitch and volume; randomize a file's pitch and volume at playback rather than creating multiple files.
- **Decide whether you need to play sound that's fixed to the wearer or tracked by the wearer** — *fixed*: perceived as pointed at the wearer regardless of gaze/object movement; *tracked*: perceived from a specific object, changing with distance. Generally use tracked for realism; fixed can fit (e.g. Mindfulness envelops the wearer).
### watchOS
- The system manages playback; apps can play short clips while active in the foreground, or longer audio that continues after wrist-down or app switch.
- **Use the recommended encoding values for media assets** — 64 kbps HE-AAC (High-Efficiency Advanced Audio Coding).
- **Consider presenting a Now Playing view so people can control current or recently played audio without leaving your app** — shows the current source (possibly another app on Apple Watch or iPhone), automatically selecting current or most recent source.

## Specs
Audio session categories:

| Category | Meaning | Behavior |
| --- | --- | --- |
| Solo ambient | Sound isn't essential, but it silences other audio (e.g. game with a soundtrack). | Responds to the silence switch. Doesn't mix with other sounds. Doesn't play in the background. |
| Ambient | Sound isn't essential, and it doesn't silence other audio (e.g. game letting people play another app's music instead of its soundtrack). | Responds to the silence switch. Mixes with other sounds. Doesn't play in the background. |
| Playback | Sound is essential and might mix with other audio (e.g. audiobook, language-learning app used after leaving the app). | Doesn't respond to the silence switch. May or may not mix with other sounds. Can play in the background. |
| Record | Sound is recorded (e.g. note-taking app's audio recording mode; may switch to playback to play notes). | Doesn't respond to the silence switch. Doesn't mix with other sounds. Can record in the background. |
| Play and record | Sound is recorded and played, potentially simultaneously (e.g. audio messaging, video calling). | Doesn't respond to the silence switch. May or may not mix with other sounds. Can record and play in the background. |

- watchOS audio encoding: 64 kbps HE-AAC.

## APIs
`MPVolumeView` (MediaPlayer), `AVAudioSession`, `AVAudioSession.Category`, `notifyOthersOnDeactivation`, `shouldResume`, Handling audio interruptions (AVFAudio), Audio Services (AudioToolbox), Playing Background Audio, Adding a Now Playing View (WatchKit), Configuring your app for media playback (AVFoundation), MusicKit

## Related
`playing-video, feedback, accessibility, multitasking, immersive-experiences`
