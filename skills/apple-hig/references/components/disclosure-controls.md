# Disclosure controls

> Source: https://developer.apple.com/design/human-interface-guidelines/disclosure-controls · Disclosure controls reveal and hide information and functionality related to specific controls or views.

## When to use / core idea
- Two kinds: **disclosure triangle** (shows/hides content associated with a view or list of items, e.g., Keynote export advanced options, Finder list view hierarchy) and **disclosure button** (shows/hides functionality associated with a specific control, e.g., macOS Save sheet expanding beside the Save As field).

## Rules
### Best practices
- **Use a disclosure control to hide details until they're relevant** — put the most-used controls at the top of the disclosure hierarchy (always visible); hide advanced functionality by default.

### Disclosure triangles
- Points inward from the leading edge when content is hidden; points down when visible. Click/tap toggles; the view expands/collapses to fit.
- **Provide a descriptive label when using a disclosure triangle** — indicate what's disclosed, e.g., "Advanced Options."

### Disclosure buttons
- Points down when content is hidden; points up when visible. Click/tap toggles; the view expands/collapses to fit.
- **Place a disclosure button near the content that it shows and hides** — establish a clear relationship between control and expanded choices.
- **Use no more than one disclosure button in a single view** — multiple add complexity and confusion.

## Platform considerations
No additional considerations: macOS. Not supported: tvOS, watchOS.
### iOS, iPadOS, visionOS
- Available via the SwiftUI `DisclosureGroup` view.

## APIs
`DisclosureGroup` (SwiftUI), `NSButton.BezelStyle.disclosure` (AppKit), `NSButton.BezelStyle.pushDisclosure` (AppKit)

## Related
outline-views, lists-and-tables, buttons
