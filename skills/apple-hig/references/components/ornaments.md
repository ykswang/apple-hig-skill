# Ornaments

> Source: https://developer.apple.com/design/human-interface-guidelines/ornaments · In visionOS, an ornament presents controls and information related to a window without crowding or obscuring the window's contents.

## When to use / core idea
- Floats in a plane parallel to its window, slightly in front along the z-axis. Moves with the window, keeping relative position; stays unchanged when window content scrolls.
- Can appear on any window edge; can contain buttons, segmented controls, other views.
- The system builds toolbars, tab bars, and video playback controls as ornaments; use a custom ornament only for custom components.

## Rules
### Best practices
- **Consider using an ornament for frequently needed controls or information in a consistent location that doesn't clutter the window** — e.g., Music Now Playing controls.
- **In general, keep an ornament visible** — hiding can make sense when people dive into content (watching video, viewing a photo), but people usually want consistent access.
- **If you need multiple ornaments, prioritize the window's overall visual balance** — consider constraining the total number to avoid visual weight and complexity; relocate a removed ornament's elements into the main window.
- **Aim to keep an ornament's width the same or narrower than the associated window** — wider ornaments can interfere with a tab bar or other vertical content on the window's side.
- **Consider using borderless buttons in an ornament** — default background is glass, so buttons may not need visible borders; the system applies the hover effect automatically when people look at them.
- **Use system-provided toolbars and tab bars unless you need custom components** — they automatically appear as ornaments.

## Platform considerations
Not supported: iOS, iPadOS, macOS, tvOS, watchOS (visionOS only).

## APIs
`ornament(visibility:attachmentAnchor:contentAlignment:ornament:)` (SwiftUI), `Toolbars` (SwiftUI), `TabView` (SwiftUI)

## Related
layout, toolbars, tab-bars, materials, eyes, buttons, windows
