# Context menus

> Source: https://developer.apple.com/design/human-interface-guidelines/context-menus · A context menu provides access to functionality directly related to an item, without cluttering the interface.

## When to use / core idea
- Convenient access to frequently used, item-specific commands; hidden by default, so people may not know it exists.
- Revealed by: touch or pinch and hold (visionOS, iOS, iPadOS); Control-click (macOS, iPadOS); secondary click on a Magic Trackpad (macOS, iPadOS).
- Alternatives: edit-menus (iOS/iPadOS text/selection), menus, pop-up-buttons, pull-down-buttons.

## Rules
### Best practices
- **Prioritize relevancy when choosing items** — not for advanced or rarely used items; include commands most likely needed in context (e.g., Mail Inbox message: reply, move — not edit content, manage mailboxes, filter).
- **Aim for a small number of menu items** — long menus are hard to scan and scroll.
- **Support context menus consistently throughout your app** — inconsistent support makes people unsure where it works.
- **Always make context menu items available in the main interface, too** — e.g., Mail iOS toolbar; macOS menu bar lists all commands including context-menu ones.
- **If you need submenus, keep them to one level** — more than one level is hard to navigate; give submenus intuitive titles that predict contents.
- **Hide unavailable menu items, don't dim them** — context menus show only relevant actions. macOS exception: Cut, Copy, Paste may appear unavailable.
- **Aim to place the most frequently used items where people encounter them first** — people read from the part nearest their finger/pointer; since the menu may open above or below content, you may need to reverse item order.
- **Show keyboard shortcuts in your app's main menus, not in context menus** — redundant.
- **Follow best practices for using separators** — group items; generally no more than about **three groups**.
- **In iOS, iPadOS, and visionOS, warn people about context menu items that can destroy data** — list destructive items (Delete, Remove) at the end and mark them destructive; system can show them in red text.

### Content
- Context menus seldom show a title; each item needs a short label that clearly describes what it does (see menus › Labels).
- **Include a title only if it clarifies the menu's effect** — e.g., multiple selected Mail messages + Mark button: title states the number of selected messages.
- **Represent menu item actions with familiar icons** — use the same icons as the system for actions like Copy, Share, Delete (see icons › Standard icons).

## Platform considerations
No additional considerations: tvOS. Not supported: watchOS.
### iOS, iPadOS
- **Provide either a context menu or an edit menu for an item, but not both** — confusing to people and hard for the system to detect intent.
- **In iPadOS, consider using a context menu to let people create a new object** — revealed by long press or secondary click with trackpad/keyboard (e.g., Files: new folder from context menu in the space between items).
- Context menus can show a preview of the content near the command list; people can choose a command, or in some cases tap the preview to open it or drag it elsewhere.
- **Prefer a graphical preview that clarifies the target of the commands** — e.g., Notes/Mail show a condensed version of the actual content.
- **Ensure your preview looks good as it animates** — the preview emerges from the content while the screen dims; match the preview's clipping path to the image shape so contours (e.g., rounded corners) don't appear to change during animation.
### macOS
- Sometimes called a *contextual* menu.
### visionOS
- **Consider using a context menu instead of a panel or inspector window for frequently used functionality** — fewer separate views/windows keeps the space uncluttered.
- **In general, avoid letting a context menu's height exceed the window's height** — it could obscure system components above/below the window (window-management controls, Share menu). Tailor item count to usage: specialist in-depth apps may justify many commands; simple apps benefit from short menus.

## APIs
`contextMenu(menuItems:)` (SwiftUI), `UIContextMenuInteraction` (UIKit), `UIContextMenuInteractionDelegate` (UIKit), `UIMenuElement.Attributes.destructive` (UIKit), `NSMenu.popUpContextMenu(_:with:for:)` (AppKit)

## Related
menus, edit-menus, pop-up-buttons, pull-down-buttons, icons
