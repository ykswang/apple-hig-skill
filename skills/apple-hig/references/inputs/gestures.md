# Gestures

> Source: https://developer.apple.com/design/human-interface-guidelines/gestures · A gesture is a physical motion a person uses to directly affect an object in an app or game on their device.

## When to use / core idea
- Gestures happen on a touchscreen, in the air (visionOS), or on input devices (trackpad, mouse, remote, game controller with touch surface).
- Every platform supports basic gestures (tap, swipe, drag); people expect them everywhere (see Standard gestures table).
- Custom gestures only for specialized, frequent tasks not covered by standard gestures (games, drawing apps).

## Rules
### Best practices
- **Give people more than one way to interact with your app** — people use voice, keyboard, Switch Control; don't assume anyone can perform a specific gesture. See `accessibility`.
- **In general, respond to gestures in ways that are consistent with people's expectations** — tap activates/selects. Avoid using familiar gestures (tap, swipe) for app-unique actions; avoid unique gestures for standard actions (activating a button, scrolling).
- **Handle gestures as responsively as possible** — immediate feedback that helps predict results and communicates the extent/type of movement needed.
- **Indicate when a gesture isn't available** — otherwise people think the app froze or they're doing it wrong (e.g., locked object being dragged, unavailable button not visibly distinct).

### Custom gestures
- **Add custom gestures only when necessary** — must be: discoverable; straightforward to perform; distinct from other gestures; not the only way to perform an important action.
- **Make custom gestures easy to learn** — offer learning moments; test in real scenarios. If hard to describe with simple language and graphics, it's likely hard to learn.
- **Use shortcut gestures to supplement standard gestures, not replace them** — e.g., keep the Back button in the top toolbar while also supporting edge-swipe back.
- **Avoid conflicting with gestures that access system UI** — e.g., edge swiping in watchOS, hand roll for system overlays in visionOS. Games/immersive experiences may defer the system gesture in specific circumstances.

## Platform considerations
### iOS, iPadOS
- Additional expected gestures (see Specs).
- **Consider allowing simultaneous recognition of multiple gestures if it enhances the experience** — rarely useful outside games; e.g., joystick + fire buttons at once. For touch + Apple Pencil, see `apple-pencil-and-scribble`.

### macOS
- Primary input is keyboard and mouse; standard gestures also on Magic Trackpad, Magic Mouse, or game controller with a touch surface.

### tvOS
- Standard gestures via compatible remote, Siri Remote, or game controller with touch surface. See `remotes`.

### visionOS
- *Indirect* gestures: look at an object to target, then manipulate from a distance with hands (e.g., look at button, tap finger and thumb). Comfortable at any distance; fast focus changes with minimal movement.
- *Direct* gestures: physically touch the object (e.g., tap virtual keyboard keys). Best within reach and for infrequent use (raised arms tire). Direct versions of all standard gestures exist.
- **Support standard gestures everywhere you can** — tap is the first gesture people try after looking at an object.
- **Offer both indirect and direct interactions when possible** — prefer indirect for UI and common components (buttons); reserve direct and custom gestures for objects inviting close-up interaction or specific game motions.
- **Avoid requiring specific body movements or positions for input** — disability, space, environment; if movement is required, support alternative inputs.

#### Designing custom gestures in visionOS
- Requires running in a Full Space and requesting permission for hand data (ARKit).
- **Prioritize comfort** — test ergonomics continually; raised arms even briefly are tiring; repeated similar movements stress muscles and joints.
- **Carefully consider complex custom gestures that involve multiple fingers or both hands** — both hands may not be available; offer a lower-movement alternative.
- **Avoid custom gestures that require using a specific hand** — raises cognitive load; less welcoming to people with strong hand-dominance or limb differences.

#### Working with system overlays in visionOS
- visionOS 2+: look at a palm and gesture to access Home and Control Center overlays; systemwide and reserved. System overlay is the default Control Center access in visionOS 2+; visionOS 1 behavior (looking upward) remains as an accessibility setting.
- **Reserve the area around a person's hand for system overlays and their related gestures** — avoid anchoring content to hands/wrists; if a game needs hand-anchored content, place it outside the immediate hand area to avoid colliding with the Home indicator.
- **Consider deferring the system overlay behavior when designing an immersive app or game** — e.g., virtual hands/gloves; in a Full Space you can require a tap to reveal the Home indicator (`persistentSystemOverlays(_:)`). Apps built for visionOS 1 defer by default in a Full Space (Home indicator appears only after a tap).
- **Use caution when designing custom gestures that involve a rolling motion of the hand, wrist, and forearm** — reserved for revealing system overlays, which always draw above app content and your app isn't notified; test for conflicts.

### watchOS
- Double tap (watchOS 11+): scrolls lists and scroll views, advances vertical tab views. You can set a toggle or button as the primary action in your app, or in a widget/Live Activity shown in the Smart Stack; double tap highlights then performs it. In notifications, double tap acts on the first nondestructive custom action.
- **Avoid setting a primary action in views with lists, scroll views, or vertical tabs** — conflicts with default double-tap navigation.
- **Choose the button that people use most commonly as the primary action in a view** — best in nonscrolling views; e.g., play/pause in media controls.

## Specs
### Standard gestures
| Gesture | Supported in | Common action |
| --- | --- | --- |
| Tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Activate a control; select an item. |
| Swipe | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Reveal actions and controls; dismiss views; scroll. |
| Drag | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Move a UI element. |
| Touch (or pinch) and hold | iOS, iPadOS, tvOS, visionOS, watchOS | Reveal additional controls or functionality. |
| Double tap | iOS, iPadOS, macOS, tvOS, visionOS, watchOS | Zoom in; zoom out if already zoomed in; perform a primary action on Apple Watch Series 9 and Apple Watch Ultra 2. |
| Zoom | iOS, iPadOS, macOS, tvOS, visionOS | Zoom a view; magnify content. |
| Rotate | iOS, iPadOS, macOS, tvOS, visionOS | Rotate a selected item. |

### iOS, iPadOS additional gestures
| Gesture | Common action |
| --- | --- |
| Three-finger swipe | Initiate undo (left swipe); initiate redo (right swipe). |
| Three-finger pinch | Copy selected text (pinch in); paste copied text (pinch out). |
| Four-finger swipe (iPadOS only) | Switch between apps. |
| Shake | Initiate undo; initiate redo. |

### visionOS standard direct gestures
| Direct gesture | Common use |
| --- | --- |
| Touch | Directly select or activate an object. |
| Touch and hold | Open a contextual menu. |
| Touch and drag | Move an object to a new location. |
| Double touch | Preview an object or file; select a word in an editing context. |
| Swipe | Reveal actions and controls; dismiss views; scroll. |
| With two hands, pinch and drag together or apart | Zoom in or out. |
| With two hands, pinch and drag in a circular motion | Rotate an object. |

## APIs
`Setting up access to ARKit data` (visionOS), `persistentSystemOverlays(_:)` (SwiftUI), `handGestureShortcut(_:isEnabled:)` (SwiftUI), `primaryAction` (SwiftUI), `Gestures` (SwiftUI), `UITouch` (UIKit)

## Related
`feedback, eyes, playing-haptics, accessibility, pointing-devices, remotes, game-controls, apple-pencil-and-scribble, keyboards, notifications`
