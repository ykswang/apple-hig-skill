# Edit menus

> Source: https://developer.apple.com/design/human-interface-guidelines/edit-menus · An edit menu lets people change selected content in the current view and offers related commands like Copy, Select, Translate, and Look Up.

## When to use / core idea
- Applies to text and other selectable content: images, files, objects (contact cards, charts, map locations). In iOS, iPadOS, visionOS the system detects the selected data type and may add a related action (e.g., address → *Get directions*).
- Platform appearance:
  - **iOS** — compact horizontal list on touch and hold or double-tap to select; a trailing chevron expands it into a context menu.
  - **iPadOS** — touch reveals the compact horizontal style; keyboard or pointing device opens it directly as a context menu.
  - **macOS** — editing commands in a context menu during editing and in the menu bar's Edit menu.
  - **visionOS** — pinch and hold opens a horizontal bar, or it can open as a context menu.
  - **tvOS, watchOS** — editing is rare; no system edit menu.

## Rules
### Best practices
- **Prefer the system-provided edit menu** — custom menus with the same commands are redundant and confusing (standard commands: `UIResponderStandardEditActions`).
- **Let people reveal an edit menu using the system-defined interactions they already know** — touch and hold, pinch and hold (visionOS), secondary click with trackpad/keyboard; no custom interactions for standard tasks.
- **Offer commands relevant in the current context, removing or dimming commands that don't apply** — no Copy/Cut without a selection; no Paste when nothing to paste.
- **List custom commands near relevant system-provided ones** — e.g., custom formatting commands after system ones in the format section. Avoid overwhelming people with too many custom commands.
- **When it makes sense, let people select and copy noneditable text** — e.g., image captions, social status. In general let people copy content text, but not control labels.
- **Support undo and redo when possible** — edit menus don't confirm actions, so undo/redo enables recovery.
- **In general, avoid implementing other controls that perform the same functions as edit menu items** — redundant controls crowd the interface.
- **Differentiate different types of deletion commands when necessary** — Delete = pressing the Delete key; Cut copies to the pasteboard before deleting.

### Content
- **Create short labels for custom commands** — verbs or short verb phrases.

## Platform considerations
No additional considerations: visionOS. Not supported: tvOS, watchOS.
### iOS, iPadOS
- **Ensure your edit menu works well in both styles** — compact horizontal (Multi-Touch) and vertical (keyboard/pointing device; see menus › iOS, iPadOS).
- **Adjust an edit menu's placement, if necessary** — default is above or below the insertion point/selection with a pointer to the target. You can't change the menu's shape or pointer, but can reposition it to avoid covering important content or UI.
### macOS
- For item order in the app's Edit menu, see the-menu-bar › Edit menu.

## APIs
`UIEditMenuInteraction` (UIKit), `UIResponderStandardEditActions` (UIKit), `NSMenu` (AppKit)

## Related
menus, context-menus, the-menu-bar, undo-and-redo, labels, gestures
