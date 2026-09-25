# Pull-down buttons

> Source: https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons · A pull-down button displays a menu of items or actions that directly relate to the button's purpose.

## When to use / core idea
- After people choose an item, the menu closes and the app performs the action.
- Clarifies the button's target or customizes its behavior without extra buttons — e.g., Add button → choose what to add; Sort button → choose sort attribute; Back button → choose a specific location to revisit.
- For mutually exclusive non-command choices, use a pop-up button instead.

## Rules
### Best practices
- **Use a pull-down button to present commands or items directly related to the button's action.**
- **Avoid putting all of a view's actions in one pull-down button** — primary actions must be easily discoverable.
- **Balance menu length with ease of use** — list a minimum of **three items** so opening it feels worthwhile; for one or two items consider alternatives (buttons for actions, toggles/switches for selections). Too many items slow people down.
- **Display a succinct menu title only if it adds meaning** — usually the button content plus descriptive items suffice.
- **Let people know when a menu item is destructive, and ask them to confirm their intent** — menus show destructive actions in red text; on choosing one, the system shows an action sheet (iOS) or popover (iPadOS) to confirm or cancel; its different location and deliberate dismissal help prevent accidental data loss.
- **Include an interface icon with a menu item when it provides value** — icon/image appears after the label; SF Symbols stay aligned with text at every scale.

## Platform considerations
No additional considerations: macOS, visionOS. Not supported: tvOS, watchOS.
### iOS, iPadOS
- Note: a pull-down menu can also be revealed by a gesture on a button (e.g., iOS 14+ Safari: touch and hold the Tabs button → New Tab, Close All Tabs).
- **Consider using a More pull-down button for items that don't need prominent positions** — saves space but can hinder discoverability; the ellipsis icon doesn't help predict contents. Weigh size convenience against discoverability.

## APIs
`MenuPickerStyle` (SwiftUI), `UIControl.showsMenuAsPrimaryAction` (UIKit), `NSPopUpButton.pullsDown` (AppKit)

## Related
pop-up-buttons, buttons, menus, action-sheets, popovers, icons, sf-symbols, toggles
