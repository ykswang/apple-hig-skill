# Digital Crown

> Source: https://developer.apple.com/design/human-interface-guidelines/digital-crown · The Digital Crown is an important hardware input for Apple Vision Pro and Apple Watch.

## When to use / core idea
- On both devices people use it to interact with the system; only on Apple Watch can apps use it (visionOS apps don't receive Digital Crown information directly).
- Apple Vision Pro system uses: adjust volume; adjust immersion in a portal, an Environment, or an app/game in a Full Space (see `immersive-experiences`); recenter content in front of the person; open Accessibility settings; exit an app and return to the Home View.
- Apple Watch (watchOS 10+): primary navigation input — Smart Stack widgets on the watch face, vertical movement through apps on the Home Screen, switching vertically paginated tabs, scrolling lists and variable-height pages. Rotation also drives data inspection and standard/custom controls.
- Apps don't respond to Digital Crown presses — watchOS reserves them (e.g., revealing the Home Screen).
- Most Apple Watch models provide haptic feedback: by default, linear haptic *detents* (taps) per specific distance turned; some system controls (table views) give detents as new items scroll on screen.

## Rules
- **Anchor your app's navigation to the Digital Crown** — use vertically oriented list, tab, and scroll views; back crown interactions with corresponding touch screen interactions.
- **Consider using the Digital Crown to inspect data in contexts where navigation isn't necessary** — e.g., World Clock advances time of day at a selected location.
- **Provide visual feedback in response to Digital Crown interactions** — e.g., pickers change displayed value; if tracking turns directly, update UI programmatically. Without feedback people assume the crown does nothing.
- **Update your interface to match the speed with which people turn the Digital Crown** — people expect precise control; avoid updating content so fast that selecting values is difficult.
- **Use the default haptic feedback when it makes sense in your app** — turn off detents if they don't fit (e.g., don't match your animation). Tables can use linear detents instead of row-based detents — better when row heights vary significantly.

## Platform considerations
Not supported: iOS, iPadOS, macOS, tvOS.

## APIs
`WKCrownDelegate` (WatchKit).

## Related
`feedback, action-button, immersive-experiences`
