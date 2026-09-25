# Multitasking

> Source: https://developer.apple.com/design/human-interface-guidelines/multitasking · Lets people switch quickly from one app to another, performing tasks in each.

## When to use / core idea
- People expect multitasking and may think something's wrong without it. With rare exceptions (some games, Apple Vision Pro apps in a Full Space), every app must work well with multitasking.
- You don't know when multitasking starts, so always be prepared to save and restore context.

## Rules
### Best practices
- **Pause activities that require people's attention or active participation when they switch away** — e.g. games, media; on return, continue as if they never left.
- **Respond smoothly to audio interruptions** — e.g. phone call, Siri-initiated playlist:
  - Primary audio interruptions (music, podcasts, audiobooks): pause audio indefinitely.
  - Shorter interruptions (e.g. GPS directions): temporarily lower volume or pause, then resume original volume/playback when it ends (see `playing-audio`).
- **Finish user-initiated tasks in the background** — e.g. downloading assets, processing video; complete tasks needing no further input before suspending.
- **Use notifications sparingly** — notify on completion of important or time-sensitive tasks people started; avoid notifications for routine/secondary tasks — let people check on return (see `managing-notifications`).

## Platform considerations
Not supported: watchOS.
### iOS
- Multitasking lets people use FaceTime or watch video in Picture in Picture while using another app; app switcher to change apps.
### iPadOS
- People view/interact with windows of multiple apps simultaneously; an app can support multiple open windows.
- Full-screen apps: occupy the screen; switch windows via the app switcher.
- Windowed apps: resizable, arrangeable (macOS-like); system window controls for tiling, full screen, minimize, close; frontmost window identified by colored window controls and a drop shadow on windows behind (see `windows`).
- Videos and FaceTime can play in a Picture in Picture overlay in either mode.
- Note: apps don't control multitasking configurations or receive any indication of them — adapt gracefully to different screen sizes (see `layout`, `windows`).
### macOS
- Multitasking is the default; open windows get drop shadows (layered look) and other effects distinguishing window states (see `windows`).
### tvOS
- People can play or browse content while playing movies/TV shows in Picture in Picture (where supported).
### visionOS
- Multiple apps run in the Shared Space; people view and switch between windows and volumes.
- Only one window is active at a time; looking at another window makes it active while the previous one becomes more translucent and recedes along the z-axis. Closing an app window backgrounds the app without quitting.
- Note: closing the Now Playing app's window automatically pauses audio; people can resume from Control Center without opening the window.
- **Avoid interfering with the system-provided multitasking behavior** — visionOS applies a feathered mask to the window people look away from; don't change the appearance of a window's edges.
- **Don't pause a window's video playback when people look away from it** — as in macOS, playback continues while people work in another window.
- **Be prepared for situations where your audio can duck** — unless your app is the Now Playing app, its audio can duck when people look away to another app.

## APIs
Responding to the launch of your app (UIKit), Multitasking on iPad, Mac, and Apple Vision Pro (UIKit)

## Related
`layout, windows, playing-video, playing-audio, managing-notifications`
