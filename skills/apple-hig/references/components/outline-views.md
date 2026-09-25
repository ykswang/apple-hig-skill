# Outline views

> Source: https://developer.apple.com/design/human-interface-guidelines/outline-views · An outline view presents hierarchical data in a scrolling list of cells organized into columns and rows.

## When to use / core idea
- At least one column holds primary hierarchical data (parent containers and children); add columns for supplementary attributes (sizes, modification dates). Parents have disclosure triangles that expand to reveal children (e.g., Finder list view).
- Works well for text-based content; often on the leading side of a split view with related content opposite.
- For non-hierarchical data use a table (lists-and-tables); see also column-views.

## Rules
### Best practices
- **Use a table instead of an outline view to present data that's not hierarchical.**
- **Expose data hierarchy in the first column only** — other columns show attributes of the primary-column data.
- **Use descriptive column headings to provide context** — nouns or short noun phrases, title-style capitalization, no punctuation (especially no trailing colon). Always provide headings in a multi-column outline view; in a single-column view without a heading, use a label or other means to give context.
- **Consider letting people click column headings to sort** — ascending/descending by that column; secondary-column sorting can happen behind the scenes. Clicking the primary column heading sorts at each hierarchy level (e.g., Finder sorts top-level folders, then items within each). Clicking an already-sorted heading re-sorts in the opposite direction.
- **Let people resize columns** — to reveal data wider than the column.
- **Make it easy to expand or collapse nested containers** — e.g., Finder: clicking a folder's triangle expands only that folder; Option-clicking expands all its subfolders.
- **Retain people's expansion choices** — store expansion state and restore it next time.
- **Consider using alternating row colors in multi-column outline views** — helps track row values across columns, especially in wide views.
- **Let people edit data if it makes sense** — single-click a cell to edit; double-click may do something different (e.g., single-click file name to rename, double-click to open). Can also let people reorder, add, remove rows if useful.
- **Consider using a centered ellipsis to truncate cell text instead of clipping** — preserves beginning and end, making content more recognizable.
- **Consider offering a search field for lengthy outline views** — windows built around an outline view often put one in the toolbar.

## Platform considerations
Not supported: iOS, iPadOS, tvOS, visionOS, watchOS (macOS only).

## APIs
`OutlineGroup` (SwiftUI), `NSOutlineView` (AppKit)

## Related
column-views, lists-and-tables, split-views, search-fields, disclosure-controls
