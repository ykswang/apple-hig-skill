# Pop-up buttons

> Source: https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons · A pop-up button displays a menu of mutually exclusive options.

## When to use / core idea
- After people choose an item, the menu closes and the button can update to show the current selection (e.g., Calendar event Repeat interval).
- Use a pull-down button instead to offer actions, allow multiple selection, or include a submenu.

## Rules
### Best practices
- **Use a pop-up button to present a flat list of mutually exclusive options or states** — choices that affect content or the surrounding view. Use a pull-down button if you need to: offer a list of actions; let people select multiple items; include a submenu.
- **Provide a useful default selection** — shown until people choose; when possible, the item most people are likely to want.
- **Give people a way to predict a pop-up button's options without opening it** — e.g., an introductory label or a button label describing its effect.
- **Consider using a pop-up button when space is limited and you don't need to display all options all the time** — space-efficient for a wide array of choices.
- **If necessary, include a Custom option in the menu for additional items useful in some situations** — avoids cluttering the interface with occasionally needed controls; can show explanatory text below the list.

## Platform considerations
No additional considerations: iOS, macOS, visionOS. Not supported: tvOS, watchOS.
### iPadOS
- **Within a popover or modal view, consider using a pop-up button instead of a disclosure indicator for a list item's multiple options** — lets people choose quickly without navigating to a detail view; suits a fairly small, well-defined set of options.

## APIs
`MenuPickerStyle` (SwiftUI), `UIButton.changesSelectionAsPrimaryAction` (UIKit), `NSPopUpButton` (AppKit)

## Related
pull-down-buttons, buttons, menus, tab-views
