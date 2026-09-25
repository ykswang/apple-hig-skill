# Path controls

> Source: https://developer.apple.com/design/human-interface-guidelines/path-controls · A path control shows the file system path of a selected file or folder.

## When to use / core idea
- macOS only. E.g., Finder View > Show Path Bar shows the selected item's path (or the window folder's path if nothing is selected) at the bottom of the window.
- Two styles:
  - **Standard** — linear list of root disk, parent folders, selected item, each with icon and name. If too long, hides names between first and last items. If editable, people can drag an item onto it to select and show its path.
  - **Pop up** — like a pop-up button showing selected item's icon and name; clicking opens a menu with root disk, parent folders, selected item. If editable, the menu adds a Choose command; dragging an item onto it also selects it.

## Rules
### Best practices
- **Use a path control in the window body, not the window frame** — not for toolbars or status bars. Finder's path control is at the bottom of the window body, not in the status bar.

## Platform considerations
Not supported: iOS, iPadOS, tvOS, visionOS, watchOS.

## APIs
`NSPathControl` (AppKit).

## Related
`file-management, pop-up-buttons`
