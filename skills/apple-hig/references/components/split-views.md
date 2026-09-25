# Split views

> Source: https://developer.apple.com/design/human-interface-guidelines/split-views · A split view manages multiple adjacent panes of content, each containing components such as tables, collections, images, and custom views.

## When to use / core idea
- Typically shows multiple levels of the app's hierarchy at once: selecting an item in the primary pane shows its contents in the secondary pane; an optional tertiary pane shows further content.
- Common for a sidebar: leading pane lists top-level items/collections; secondary/tertiary panes show child collections and item details.
- Rarely, panes provide supplementary functionality around a main view (e.g., Keynote on macOS: slide navigator, presenter notes, inspector around the canvas).
- Alternatives: sidebars, tab-bars; on visionOS, sheets for small requests/simple tasks.

## Rules
### Best practices
- **To support navigation, persistently highlight the current selection in each pane that leads to the detail view** — clarifies relationships between panes and keeps people oriented.
- **Consider letting people drag and drop content between panes** — convenient for moving content across hierarchy levels.

## Platform considerations
### iOS
- **Prefer using a split view in a regular — not a compact — environment** — in compact (e.g., iPhone portrait) multiple panes wrap/truncate content, reducing legibility and usability.
### iPadOS
- Two vertical panes (like Mail) or three (like Keynote).
- **Account for narrow, compact, and intermediate window widths** — iPad windows resize fluidly; ensure logical navigation between panes at every width.
### macOS
- Panes can be arranged vertically, horizontally, or both; dividers between panes can support drag-to-resize.
- **Set reasonable defaults for minimum and maximum pane sizes** — keep the divider visible; if a pane gets too small the divider seems to disappear and is hard to use.
- **Consider letting people hide a pane when it makes sense** — e.g., hide Keynote navigator and presenter notes to focus on editing.
- **Provide multiple ways to reveal hidden panes** — e.g., toolbar button, menu command with keyboard shortcut.
- **Prefer the thin divider style** — 1 pt wide; maximizes content space while remaining easy to use. Avoid thicker styles unless you have a specific need (e.g., both sides show table rows with strong linear elements that make a thin divider hard to distinguish).
### tvOS
- Works well for filtering: choose a filter category in the primary pane, show results in the secondary pane.
- **Choose a split view layout that keeps the panes looking balanced** — default: primary pane one-third of screen width, secondary two-thirds; half-and-half also available.
- **Display a single title above a split view** — describing the content as a whole; don't title each pane.
- **Choose the title's alignment based on the secondary pane's content** — content collection → consider centering the title in the window; single main view of important content → consider placing the title above the primary view to give content more room.
### visionOS
- **To display supplementary information, prefer a split view instead of a new window** — keeps context; new windows may confuse people navigating/repositioning content and require managing view relationships. For small requests or a simple task before returning to the main task, use a sheet.
### watchOS
- The split view displays either the list view or a detail view as a full-screen view.
- **Automatically display the most relevant detail view** — at launch show the most pertinent info (location, time, recent actions).
- **If your app displays multiple detail pages, place detail views in a vertical tab view** — people scroll between tabs with the Digital Crown; a page indicator next to the Crown shows the number of tabs and the current one.

## Specs
- macOS thin divider: 1 pt width.
- tvOS default pane ratio: primary 1/3, secondary 2/3; optional 1/2 + 1/2.

## APIs
`NavigationSplitView` (SwiftUI), `VSplitView`, `HSplitView` (SwiftUI), `UISplitViewController` (UIKit), `NSSplitViewController` (AppKit), `NSSplitView.DividerStyle` (AppKit)

## Related
sidebars, tab-bars, layout, drag-and-drop, sheets, tab-views, designing-for-iphone-duo
