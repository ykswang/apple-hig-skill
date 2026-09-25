# Tab views

> Source: https://developer.apple.com/design/human-interface-guidelines/tab-views · A tab view presents multiple mutually exclusive panes of content in the same area, switched with a tabbed control.

## When to use / core idea
- For closely related areas of content within a window (primarily macOS). Alternatives: segmented control (iOS/iPadOS), pop-up button when there are too many panes, tab bars for app-level navigation.

## Rules
### Best practices
- **Use a tab view to present closely related areas of content** — strong visual enclosure; people expect tabs' contents to be similar/related.
- **Make sure the controls within a pane affect content only in the same pane** — panes are mutually exclusive and must be fully self-contained.
- **Provide a label for each tab that describes the contents of its pane** — generally nouns or short noun phrases (a verb phrase may make sense in some contexts); title-style capitalization.
- **Avoid using a pop-up button to switch between tabs** — tabs need one click/tap and show all choices at once; a pop-up button needs two and hides choices. A pop-up button is reasonable when there are too many panes to display as tabs.
- **Avoid providing more than six tabs in a tab view** — more is overwhelming and causes layout issues; if you need six or more, consider another approach (e.g., each tab as a view option in a pop-up button menu).

### Anatomy
- Tabbed control sits on the top edge of the content area. You can hide it (appropriate when switching panes programmatically); then the content area can be borderless (solid or transparent), bezeled, or bordered with a line.
- **In general, inset a tab view by leaving a margin of window-body area on all sides** — clean look and room for unrelated controls. Extending to the window edges is possible but unusual.

## Platform considerations
Not supported: iOS, iPadOS, tvOS, visionOS.
### iOS, iPadOS
- For similar functionality, consider a segmented control instead.
### watchOS
- Tab views are displayed using page controls (`TabView`).

## APIs
`TabView` (SwiftUI), `NSTabView` (AppKit)

## Related
tab-bars, segmented-controls, pop-up-buttons, page-controls
