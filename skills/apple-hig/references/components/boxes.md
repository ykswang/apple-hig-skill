# Boxes

> Source: https://developer.apple.com/design/human-interface-guidelines/boxes · A box creates a visually distinct group of logically related information and components.

## When to use / core idea
- By default uses a visible border or background color to separate contents; can include a title.

## Rules
### Best practices
- **Prefer keeping a box relatively small compared with its containing view** — as it nears the size of the window/screen it communicates separation less effectively and crowds other content.
- **Consider using padding and alignment to communicate additional grouping within a box** — nested boxes make the interface feel busy and constrained.

### Content
- **Provide a succinct introductory title if it helps clarify the box's contents** — also helps VoiceOver users predict the content.
- **If you need a title, write a brief phrase describing the contents** — sentence-style capitalization; avoid ending punctuation, except in a settings pane, where you append a colon.

## Platform considerations
No additional considerations: visionOS. Not supported: tvOS, watchOS.
### iOS, iPadOS
- By default, boxes use the secondary and tertiary background colors.
### macOS
- By default, the box's title appears above it.

## APIs
`GroupBox` (SwiftUI), `NSBox` (AppKit)

## Related
layout, color
