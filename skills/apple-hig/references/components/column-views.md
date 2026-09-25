# Column views

> Source: https://developer.apple.com/design/human-interface-guidelines/column-views · A column view (also called a *browser*) lets people view and navigate a data hierarchy using a series of vertical columns.

## When to use / core idea
- Each column = one hierarchy level with rows of items; parent items with children are marked with a triangle icon. Selecting a parent shows its children in the next column; people navigate down to a leaf and back up to explore other branches.
- Consider it for deep hierarchies where people navigate back and forth frequently between levels and don't need the sorting a list or table provides (e.g., Finder column view).
- Note: for hierarchical content in iPadOS or visionOS, consider a split view.

## Rules
### Best practices
- **Show the root level of your data hierarchy in the first column** — people can scroll back to it to restart from the top.
- **Consider showing information about the selected item when there are no nested items to display** — e.g., Finder shows a preview plus creation date, modification date, file type, size.
- **Let people resize columns** — especially when item names are too long for the default column width.

## Platform considerations
Not supported: iOS, iPadOS, tvOS, visionOS, watchOS (macOS only).

## APIs
`NSBrowser` (AppKit)

## Related
lists-and-tables, outline-views, split-views
