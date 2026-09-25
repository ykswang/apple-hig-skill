# Launching

> Source: https://developer.apple.com/design/human-interface-guidelines/launching · A streamlined launch experience helps people start using your app or game immediately.

## When to use / core idea
- Launching starts when someone opens the app/game, includes any initial download, and ends when the first screen is ready. Afterward you may offer `onboarding`.
- Launch screen (iOS, iPadOS, tvOS) ≠ splash screen (branding graphic) ≠ onboarding. macOS, visionOS, watchOS don't require launch screens.

## Rules
### Best practices
- **Launch instantly** — people sometimes don't want to wait more than a couple of seconds.
- **If the platform requires it, provide a launch screen** — iOS, iPadOS, tvOS show it immediately and quickly replace it with the first screen, making the experience feel fast.
- **If you need a splash screen, consider displaying it at the beginning of your onboarding flow** — a splash screen succinctly communicates branding/other info; without onboarding, show it as soon as launching completes.
- **Restore the previous state when your app restarts so people can continue where they left off** — avoid making people retrace steps; restore granular details (scroll position, window state and location).

### Launch screens (not applicable: macOS, visionOS, watchOS)
- **Downplay the launch experience** — not onboarding, not a splash screen, not artistic expression; sole function is to make the app feel quick and immediately ready.
- **Design a launch screen that's nearly identical to the first screen of your app or game** — differing elements cause an unpleasant flash; if the app first shows a solid color, the launch screen shows only that color; match the device's current orientation and appearance mode.
- **Avoid including text on your launch screen, even if your first screen displays text** — launch screen content is static, so text won't be localized.
- **Don't advertise** — not a branding opportunity; avoid looking like a splash screen or "About" window; no logos/branding unless they're a fixed part of the first screen.

## Platform considerations
No additional considerations: macOS, watchOS.
### iOS, iPadOS
- **Launch in the appropriate orientation** — if both portrait and landscape are supported, use the device's current orientation; if only one, launch in it and let people rotate; a landscape-only UI must work whether the device is rotated left or right (see `layout`).
### tvOS
- The launch screen is static (unlike layered images elsewhere in tvOS).
- **In a live-viewing app, consider automatically starting playback soon after people start the app** — e.g. start new or recently viewed live content after a few seconds of inactivity (see `live-viewing-apps`).
### visionOS
- **Consider launching in the Shared Space even if your app is fully immersive** — a Shared Space window gives context while loading and a control to open the Full Space; people prefer choosing when to transition, especially with other apps running (see `immersive-experiences`).

## APIs
Specifying your app's launch screen (Xcode), Responding to the launch of your app (UIKit)

## Related
`onboarding, loading, layout, live-viewing-apps, immersive-experiences, images`
