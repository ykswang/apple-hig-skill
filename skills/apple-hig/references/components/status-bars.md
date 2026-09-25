# Status bars

> Source: https://developer.apple.com/design/human-interface-guidelines/status-bars · Appears along the upper screen edge showing device state (time, cellular carrier, battery level).

## When to use / core idea
- iOS/iPadOS only. Background is transparent by default, so content beneath shows through.

## Rules
### Best practices
- **Obscure content under the status bar** — transparency can hurt readability, and visible controls behind it invite failed interactions. Keep it readable; don't imply content behind it is interactive. Prefer a scroll edge effect to place a blurred view behind it.
- **Consider temporarily hiding the status bar when displaying full-screen media** — for immersion (e.g. Photos hides it when browsing full-screen photos).
- **Avoid permanently hiding the status bar** — otherwise people must leave your app to check time/Wi-Fi. Let people redisplay it with a simple, discoverable gesture (e.g. single tap in Photos).

## Platform considerations
No additional considerations: iOS, iPadOS. Not supported: macOS, tvOS, visionOS, watchOS.

## APIs
`UIStatusBarStyle` (UIKit), `preferredStatusBarStyle` (UIKit), `ScrollEdgeEffectStyle` (SwiftUI), `UIScrollEdgeEffect` (UIKit)

## Related
`scroll-views`
