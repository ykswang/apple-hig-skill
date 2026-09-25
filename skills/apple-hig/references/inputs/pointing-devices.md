# Pointing devices

> Source: https://developer.apple.com/design/human-interface-guidelines/pointing-devices · People can use a pointing device like a trackpad or mouse to navigate the interface and initiate actions.

## When to use / core idea
- Mac: people combine a pointing device with a keyboard. iPad and Apple Vision Pro: pointer is an additional input that doesn't replace touch, eyes, or gestures.

## Rules
### Best practices
- **Be consistent when responding to mouse and trackpad gestures** — e.g., "Swipe between pages" behaves the same for document pages, webpages, images.
- **Avoid redefining systemwide trackpad gestures** — even in games, people expect gestures for Dock or Mission Control; Mac users can customize systemwide gestures.
- **Provide a consistent experience in your app, whether people are using gestures, eyes, a pointing device, or a keyboard** — no separate interactions per mode.
- **Let people use the pointer to reveal and hide controls that automatically minimize or fade out** — e.g., hover over minimized Safari toolbar in iPadOS to reveal it; move pointer to show/hide full-screen video playback controls.
- **Provide a consistent experience when people press and hold a modifier key while interacting with objects in your app** — e.g., Option-drag duplicates whether dragging by touch or pointer.

## Platform considerations
No additional considerations: iOS. Not supported: tvOS, watchOS.

### iPadOS
- Pointer adapts to context with rich visual feedback; supplements touch.
- **Allow multiple selection in custom views when necessary** — iPadOS 15+: click-drag expands into a selection rectangle; standard nonlist collection views support it by default; custom views must implement it (`UIBandSelectionInteraction`).
- **Distinguish between pointer and finger input only if it provides value** — e.g., video scrubber: drag playhead by touch or pointer, but pointer can click a precise seek destination.

#### Pointer shape and content effects
- Default pointer shape is a circle; can take system-defined or custom shapes over specific elements (I-beam over text entry).
- *Content effect*: the element under the pointer changes appearance; pointer keeps its shape or transforms to integrate with the element.
- **Highlight** — pointer becomes a translucent rounded rectangle behind the control with gentle parallax. Default for bar buttons, tab bars, segmented controls, edit menus.
- **Lift** — subtle parallax + elevation: pointer fades beneath, element scales up with shadow below and soft specular highlight on top. Default for app icons and Control Center buttons.
- **Hover** — generic effect applying custom scale, tint, or shadow; doesn't transform the default pointer shape.

#### Pointer accessories
- Secondary visual indicators combinable with any pointer (e.g., small arrows showing a resizable axis) (`UIPointerAccessory`).
- **Use clear, simple images to create custom accessories** — they're small; avoid detail.
- **Consider using the accessory transition to signal a change in an element's state or behavior** — system animates appearance and shape/position transitions; e.g., `plus` → `circle.slash` when add becomes unavailable.

#### Pointer magnetism
- Elements appear to attract the pointer when moving near (pointer transforms on reaching the hit region, which extends beyond visible bounds) and when flicking (system predicts the target from trajectory and pulls toward its center).
- Default magnetism: lift elements (app icons) and highlight elements (bar buttons); not hover elements (no shape transform, so magnetism would feel like lost control). Also applied to text-entry areas to prevent skipping lines during selection.

#### Standard pointers and effects
- **When possible, support the system-provided content effects** — align with each effect's intent:
  - Highlight: small element with a transparent background.
  - Lift: small element with an opaque background.
  - Hover: large elements; customize scale, tint, shadow as needed.
- **Prefer the system-provided pointer appearances for standard buttons and text-entry areas.**
- **Add padding around interactive elements to create comfortable hit regions** — too small feels like it needs extra precision; too large feels sticky. About 12 pt padding around elements with a bezel; about 24 pt around the visible edges of elements without a bezel.
- **Create contiguous hit regions for custom bar buttons** — gaps make the pointer briefly revert to default shape between buttons.
- **Specify the corner radius of a nonstandard element that receives the lift effect** — default uses system corner radius; supply radius for other shapes (e.g., circle) (`UIPointerShape.roundedRect(_:radius:)`).

#### Customizing pointers
- **Prefer system-provided pointer effects for custom elements that behave like standard elements** — e.g., custom toolbar buttons without highlight seem broken.
- **Use pointer effects in consistent ways throughout your app** — e.g., same experience in every drawing area.
- **Avoid creating gratuitous pointer and content effects** — purely decorative effects distract and irritate.
- **Keep custom pointer shapes simple** — signal the available action without drawing attention; must be instantly understood.
- **Consider enhancing the pointer experience by displaying custom annotations that provide useful information** — e.g., X/Y values over a graph; Keynote shows width/height while resizing an image.
- **Avoid displaying instructional text with a pointer** — makes the app seem complicated; prioritize interface clarity.
- **Consider the interplay of shadow, scale, and element spacing when defining custom hover effects** — reserve scaling for elements with room to grow (not table rows); for tightly spaced elements use tint without scale and shadow. Don't use shadow without scale — unscaled elements don't appear closer despite implied elevation.

### macOS
- Supports many customizable mouse/trackpad interactions: people can turn non-primary clicks/gestures on or off, choose regions for secondary click, and select finger combinations/movements for gestures (see Specs).
- Standard pointer styles communicate an element's interactive state or a drag result (see Specs).

### visionOS
- People can attach a pointing device or keyboard and keep using eyes and hands. Looking at an element then moving the pointer focuses the element under the pointer — no app work needed.
- Where people look determines pointer context; shifting gaze to another window moves pointer context there.
- With gesture-capable devices (trackpad, mouse), the pointer hides during gestures and reappears where people are looking when moved.

## Specs
### iPadOS hit-region padding
- Elements with a bezel: ~12 pt padding on all sides.
- Elements without a bezel: ~24 pt padding around visible edges.

### macOS standard clicks and gestures
| Click or gesture | Expected behavior | Mouse | Trackpad |
| --- | --- | --- | --- |
| Primary click | Select or activate an item, such as a file or button. | ● | ● |
| Secondary click | Reveal contextual menus. | ● | ● |
| Scrolling | Move content up, down, left, or right within a view. | ● | ● |
| Smart zoom | Zoom in or out on content, such as a web page or PDF. | ● | ● |
| Swipe between pages | Navigate forward or backward between individually displayed pages. | ● | ● |
| Swipe between full-screen apps | Navigate forward or backward between full-screen apps and spaces. | ● | ● |
| Mission Control (double-tap the mouse with two fingers or swipe up on the trackpad with three or four fingers) | Activate Mission Control. | ● | ● |
| Lookup and data detectors (force click with one finger or tap with three fingers) | Display a lookup window above selected content. |  | ● |
| Tap to click | Perform the primary click action using a tap rather than a click. |  | ● |
| Force click | Click then press firmly to display a Quick Look window or lookup window above selected content. Apply a variable amount of pressure to affect pressure-sensitive controls, such as variable speed media controls. |  | ● |
| Zoom in or out (pinch with two fingers) | Zoom in or out. |  | ● |
| Rotate (move two fingers in a circular motion) | Rotate content, such as an image. |  | ● |
| Notification Center (swipe from the edge of the trackpad) | Display Notification Center. |  | ● |
| App Exposé (swipe down with three or four fingers) | Display the current app's windows in Exposé. |  | ● |
| Launchpad (pinch with thumb and three fingers) | Display the Launchpad. |  | ● |
| Show Desktop (spread with thumb and three fingers) | Slide all windows out of the way to reveal the desktop. |  | ● |

### macOS standard pointers
| Pointer (appearance) | Name | Meaning | AppKit API (`NSCursor`) |
| --- | --- | --- | --- |
| Diagonal arrow up-left | Arrow | Standard pointer for selecting and interacting with content and interface elements. | `arrow` |
| Closed gloved hand | Closed hand | Dragging to reposition the display of content within a view—for example, dragging a map around in Maps. | `closedHand` |
| Arrow with small menu square | Contextual menu | A contextual menu is available for the content below the pointer. Generally shown only when the Control key is pressed. | `contextualMenu` |
| Plus symbol | Crosshair | Precise rectangular selection is possible, such as when viewing an image in Preview. | `crosshair` |
| Arrowhead with circled X | Disappearing item | A dragged item will disappear when dropped. If the item references an original item, the original is unaffected (e.g., dragging a mailbox out of the Mail favorites bar doesn't remove it). | `disappearingItem` |
| Arrowhead with circled plus | Drag copy | Duplicates a dragged—not moved—item when dropped. Appears when pressing Option during a drag. | `dragCopy` |
| Curved arrow up-right | Drag link | Creates an alias of the selected file when dropped; alias points to the unmoved original. Appears when pressing Option and Command during a drag. | `dragLink` |
| Opposing vertical braces | Horizontal I beam | Selection and insertion of text is possible in a horizontal layout, such as a TextEdit or Pages document. | `iBeam` |
| Open gloved hand | Open hand | Dragging to reposition content within a view is possible. | `openHand` |
| Arrowhead with do-not-enter symbol | Operation not allowed | A dragged item can't be dropped in the current location. | `operationNotAllowed` |
| Gloved hand, index finger extended | Pointing hand | The content beneath the pointer is a URL link to a webpage, document, or other item. | `pointingHand` |
| Horizontal bar, down arrow | Resize down | Resize or move a window, view, or element downward. | `resizeDown` |
| Vertical bar, left arrow | Resize left | Resize or move a window, view, or element to the left. | `resizeLeft` |
| Vertical bar, left and right arrows | Resize left/right | Resize or move a window, view, or element to the left or right. | `resizeLeftRight` |
| Vertical bar, right arrow | Resize right | Resize or move a window, view, or element to the right. | `resizeRight` |
| Horizontal bar, up arrow | Resize up | Resize or move a window, view, or element upward. | `resizeUp` |
| Horizontal bar, up and down arrows | Resize up/down | Resize or move a window, view, or element upward or downward. | `resizeUpDown` |
| Opposing horizontal braces | Vertical I beam | Selection and insertion of text is possible in a vertical layout. | `iBeamCursorForVerticalLayout` |

## APIs
`UIBandSelectionInteraction` (UIKit), `UIPointerAccessory` (UIKit), `UIPointerShape.roundedRect(_:radius:)` (UIKit), `arrow` (AppKit), `closedHand` (AppKit), `contextualMenu` (AppKit), `crosshair` (AppKit), `disappearingItem` (AppKit), `dragCopy` (AppKit), `dragLink` (AppKit), `iBeam` (AppKit), `openHand` (AppKit), `operationNotAllowed` (AppKit), `pointingHand` (AppKit), `resizeDown` (AppKit), `resizeLeft` (AppKit), `resizeLeftRight` (AppKit), `resizeRight` (AppKit), `resizeUp` (AppKit), `resizeUpDown` (AppKit), `iBeamCursorForVerticalLayout` (AppKit), `Input events` (SwiftUI), `Pointer interactions` (UIKit), `Mouse, Keyboard, and Trackpad` (AppKit)

## Related
`entering-data, keyboards, gestures, focus-and-selection, eyes, apple-pencil-and-scribble`
