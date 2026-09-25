# Focus and selection

> Source: https://developer.apple.com/design/human-interface-guidelines/focus-and-selection · Focus helps people visually confirm the object that their interaction targets.

## When to use / core idea
- Focus enables simplified, component-based navigation with a remote, game controller, or keyboard.
- Focusing often also selects, except where automatic selection would cause a distracting context shift (e.g., opening a new view). In tvOS, selecting (opening/activating) a focused item needs a separate gesture.
- Platform appearance: iPadOS and macOS draw a ring or highlight; tvOS generally uses the parallax effect (depth, liveliness). Effects + interactions = *focus system/model*.
- visionOS gaze feedback is the *hover effect*, unrelated to focus (see `eyes`).

## Rules
### Best practices
- **Rely on system-provided focus effects** — precisely tuned, consistent, predictable. Consider custom focus effects only if absolutely necessary.
- **Avoid changing focus without people's interaction** — people must re-find the focused item. Exception: when moving focus with a discrete directional device (keyboard, remote, game controller) and the focused item disappears, move focus to a nearby item within one discrete step. Otherwise, hide the focus indicator when the focused object disappears.
- **Be consistent with the platform as you help people bring focus to items in your app** — iPadOS/macOS: full keyboard access reaches controls, so support focus only for content elements (list items, text fields, search fields), not buttons, sliders, toggles. tvOS: people reach every element by directional gestures/arrow keys, so every element must be focusable.
- **Indicate focus using visual appearances that are consistent with the platform** — iPadOS/macOS lists: focused items = white text + accent-color background highlight; unfocused = standard text color + gray background highlight.
- **In general, use a focus ring for a text or search field, but use a highlight in a list or collection** — a ring can work for cell-filling items like photos, but full-row highlight is usually easier to view.

## Platform considerations
Not supported: iOS, watchOS.

### iPadOS
- iPadOS 15+ focus system supports keyboard navigation of text fields, text views, sidebars, collection views, and custom views.
- Similar to tvOS (move indicator, then select), but tvOS uses *directional focus* (same interaction reaches everything), while iPadOS uses *focus groups* (areas like sidebar, grid, list):
  - Tab moves focus among focus groups.
  - Arrow keys move directionally among items within the same focus group.
- Focus indicators: *halo* (focus ring — customizable outline; for custom views and fully opaque content in collection/list cells, e.g., an image) or *highlighted* appearance (text uses accent color; not a focus effect; automatic when selecting a collection view cell with content configurations).
- **Customize the halo focus effect when necessary** — system infers halo from item shape; refine for rounded corners or Bézier shapes; adjust position if occluded/clipped (e.g., keep a badge above the halo; prevent parent-view clipping) (`UIFocusHaloEffect`).
- **Ensure that focus moves through your custom views in ways that make sense** — Tab moves through groups in reading order (leading→trailing, top→bottom). To move down a vertical stack of custom views before moving trailing, identify the stack container as one focus group (`focusGroupIdentifier`).
- **Adjust the priority of an item to reflect its importance within a focus group** — a group's *primary item* receives focus when the group does; raise priority to make an item primary (`UIFocusGroupPriority`).

### tvOS
- **In a full-screen experience, let people use gestures to interact with the content, not to move focus** — full-screen items don't show focus.
- **Avoid displaying a pointer** — use the focus model for menus and interface elements; free-form movement may suit gameplay (hidden-object search, flying). If a pointer is required, make it highly visible and integrated.
- **Design your interface to accommodate components in various focus states** — up to five visually distinct states (below). Focus often increases scale: supply assets at the larger focused size so they stay sharp, and ensure the enlarged item doesn't crowd surroundings.

### visionOS
- Supports the same focus system as iPadOS and tvOS for connected keyboards or game controllers. Gaze uses the hover effect, not focus.

## Specs
tvOS focus states:

| State | Description |
| --- | --- |
| Unfocused | Viewer hasn't brought focus to the item; less prominent than focused items. (Button: small drop shadow very close to content, translucent background infused with content colors, high-contrast text.) |
| Focused | Viewer brings focus to the item; stands out via elevation to the foreground, illumination, and animation. (Button: larger, deeper drop shadow, opaque white background, black text.) |
| Highlighted | Viewer chooses the focused item; instant visual feedback, e.g., button briefly inverts colors and animates before transitioning to selected. (Same size as unfocused, slightly raised shadow, opaque white background, black text.) |
| Selected | Viewer has chosen/activated the item, e.g., heart button filled when selected, empty when deselected. (Same size as unfocused, small shadow, opaque white background, black text.) |
| Unavailable | Viewer can't focus or choose the item; appears inactive. (Same size, no drop shadow, rests on content, translucent background tinted by nearby content, low-contrast text.) |

## APIs
`UICollectionView` (UIKit), `NSTableView` (AppKit), `UIFocusHaloEffect` (UIKit), `UICollectionViewCell` (UIKit), `focusGroupIdentifier` (UIKit), `UIFocusGroupPriority` (UIKit), `Adding user-focusable elements to a tvOS app` (UIKit), `Focus Attributes` (tvml), `Focus-based navigation` (UIKit), `About focus interactions for Apple TV` (UIKit)

## Related
`eyes, keyboards, remotes, images, pointing-devices`
