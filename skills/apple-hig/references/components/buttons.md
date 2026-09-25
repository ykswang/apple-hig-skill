# Buttons

> Source: https://developer.apple.com/design/human-interface-guidelines/buttons · A button initiates an instantaneous action.

## When to use / core idea
- A button combines three attributes: **Style** (visual style from size, color, shape), **Content** (symbol/icon, text label, or both), **Role** (system-defined semantic meaning that can affect appearance).
- Button-like components for specific cases: toggles, pop-up-buttons, pull-down-buttons, segmented-controls.

## Rules
### Best practices
- **Make buttons easy for people to use** — enough space around a button to distinguish it visually and to activate it with any input. Hit region at least **44x44 pt** (visionOS **60x60 pt**) for fingertip, pointer, eyes, or remote.
- **Always include a press state for a custom button** — otherwise it feels unresponsive.

### Style
- System buttons provide built-in interaction states, accessibility support, and appearance adaptation; platforms define styles for communicating action hierarchy.
- **In general, use a prominent visual style for the most likely action in a view** — the system applies the accent color to its background. Keep prominent buttons to **one or two per view**; more increases cognitive load.
- **Use style — not size — to distinguish the preferred choice among multiple options** — same-size buttons signal a coherent set; mixed sizes look confusing. Use a more prominent style for the preferred option, less prominent for the rest.
- **Avoid applying a similar color to button labels and content layer backgrounds** — if the content layer is already bright/colorful, prefer the default monochromatic button label appearance (see color › Liquid Glass color).

### Content
- **Ensure that each button clearly communicates its purpose** — symbol/icon, text, or both, depending on platform.
- Note: macOS and visionOS show a tooltip (brief explanatory phrase) after hovering a moment.
- **Try to associate familiar actions with familiar icons** — e.g., `square.and.arrow.up` = share. Consider existing or customized SF Symbols; see icons › Standard icons.
- **Consider using text when a short label communicates more clearly than an icon** — a few words; title-style capitalization; consider starting with a verb (e.g., "Add to Cart").

### Role
- Roles: **Normal** (no specific meaning), **Primary** (default button, most likely choice; uses the app's accent color), **Cancel** (cancels current action), **Destructive** (may destroy data; uses system red).
- **Assign the primary role to the button people are most likely to choose** — it responds to Return; in temporary views (sheet, editable view, alert) the view can close automatically on Return.
- **Don't assign the primary role to a button that performs a destructive action, even if it's the most likely choice** — people sometimes choose prominent buttons without reading.

## Platform considerations
No additional considerations: tvOS.

### iOS, iPadOS
- **Configure a button to display an activity indicator for actions that don't instantly complete** — saves space and explains delay; optionally swap the label (e.g., "Checkout" → "Checking out…"). The system shows the indicator next to the original/alternative label, hiding the button image if any.

### macOS
**Push buttons** — standard macOS button; text, symbol, icon, image, or text + image; can be the default button; can be tinted.
- **Use a flexible-height push button only when you need to display tall or variable-height content** — e.g., two lines of text or a tall icon; same corner radius and padding as regular push buttons. Otherwise use a standard push button.
- **Append a trailing ellipsis to the title when a push button opens another window, view, or app** — signals additional input (e.g., Edit… buttons in Safari AutoFill settings).
- **Consider supporting spring loading** — with a Magic Trackpad, people drag items over the button and force click to activate without dropping; they can keep dragging afterward.

**Square buttons** (gradient buttons) — initiate actions related to a view (e.g., add/remove table rows); contain symbols/icons, not text; can behave like push buttons, toggles, or pop-up buttons; placed close to their view, usually within or beneath it.
- **Use square buttons in a view, not in the window frame** — not for toolbars or status bars; use a toolbar item in toolbars.
- **Prefer using a symbol in a square button** — SF Symbols get appropriate default and interaction coloring automatically.
- **Avoid using labels to introduce square buttons** — purpose is clear from the associated view.

**Help buttons** — circular, consistently sized, contain a question mark; open app-specific help.
- **Use the system-provided help button to display your help documentation.**
- **When possible, open the help topic related to the current context** — e.g., Mail Rules settings → relevant Mail User Guide topic; otherwise open the top level of your help.
- **Include no more than one help button per window.**
- **Position help buttons where people expect to find them** (table below).
- **Use a help button within a view, not in the window frame** — avoid toolbars and status bars.
- **Avoid displaying text that introduces a help button.**

**Image buttons** — display an image, symbol, or icon in a view; can behave like push buttons, toggles, or pop-up buttons.
- **Use an image button in a view, not in the window frame** — in a toolbar use a toolbar item instead.
- **Include about 10 pixels of padding between the image edges and the button edges** — button edges define the clickable area even when invisible. In general, avoid a system-provided border (`isBordered`).
- **If you need to include a label, position it below the image button.**

### visionOS
- Buttons typically have a visible background and play sound for feedback.
- Shapes: icon-only → circle; text-only → rounded rectangle or capsule; icon + text → capsule.
- Four visual interaction states (illustrated). Buttons don't support custom hover effects. Buttons can show a tooltip when looked at briefly; text buttons generally don't need one.
- **Prefer buttons with a discernible background shape and fill** — exception: buttons in a toolbar, context menu, alert, or ornament, where the larger component's shape/material makes them visible. On a glass window use the `thin` material background; floating in space use the glass material.
- **Avoid creating a custom button with a white background fill and black text or icons** — reserved by the system for the toggled state.
- **In general, prefer circular or capsule-shape buttons** — eyes are drawn to corners; rounder shapes are easier to look at steadily. A standalone button → prefer capsule.
- **Provide enough space around a button to make it easy to look at** — centers at least **60 pts apart**; for buttons **60 pts or larger**, add **4 pts** padding so hover effects don't overlap. Usually avoid small or mini buttons in a vertical stack or horizontal row.
- **Choose the right shape for text-labeled buttons in a stack or row** — rounded rectangle in a vertical stack; capsule in a horizontal row.
- **Use standard controls to take advantage of familiar audible feedback sounds** — especially important since visionOS doesn't play haptics.

### watchOS
- All inline buttons use the capsule shape; inline buttons gain a material effect contrasting with the background for legibility.
- **Use a toolbar to place buttons in the corners** — system moves the time and title to accommodate and applies Liquid Glass to toolbar buttons.
- **Prefer buttons that span the width of the screen for primary actions** — if two buttons share a row, use the same height and images or short text titles.
- **Use toolbar buttons to provide either navigation to related areas or contextual actions** for the view's content (additional info or secondary actions).
- **Use the same height for vertical stacks of one- and two-line text buttons.**

## Specs
- Minimum hit region: 44x44 pt (all platforms generally); 60x60 pt in visionOS.
- Prominent buttons: 1–2 per view.
- macOS image button padding: about 10 pixels between image and button edges.
- visionOS spacing: button centers ≥ 60 pt apart; 4 pt padding around buttons ≥ 60 pt.

### macOS help button location
| View style | Help button location |
| --- | --- |
| Dialog with dismissal buttons (like OK and Cancel) | Lower corner, opposite to the dismissal buttons and vertically aligned with them |
| Dialog without dismissal buttons | Lower-left or lower-right corner |
| Settings window or pane | Lower-left or lower-right corner |

### visionOS button sizes (✓ = available)
| Shape | Mini (28 pt) | Small (32 pt) | Regular (44 pt) | Large (52 pt) | Extra large (64 pt) |
| --- | --- | --- | --- | --- | --- |
| Circular | ✓ | ✓ | ✓ | ✓ | ✓ |
| Capsule (text only) |  | ✓ | ✓ | ✓ |  |
| Capsule (text and icon) |  |  | ✓ | ✓ |  |
| Rounded rectangle |  | ✓ | ✓ | ✓ |  |

## APIs
`Button` (SwiftUI), `ButtonBorderShape.circle` / `.roundedRectangle` / `.capsule` (SwiftUI), `Material.thin` (SwiftUI), `UIButton` (UIKit), `NSButton` (AppKit), `NSButton.BezelStyle.flexiblePush`, `NSButton.BezelStyle.smallSquare`, `NSButton.isBordered` (AppKit)

## Related
pop-up-buttons, pull-down-buttons, toggles, segmented-controls, privacy, color, sf-symbols, icons, offering-help, sheets, alerts, toolbars, labels, ornaments, windows, materials
