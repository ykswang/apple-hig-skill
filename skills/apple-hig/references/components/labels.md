# Labels

> Source: https://developer.apple.com/design/human-interface-guidelines/labels · A label is a static piece of text that people can read and often copy, but not edit.

## When to use / core idea
- Uneditable text appearing throughout the interface: in buttons (conveys the action — Edit, Cancel, Send), in lists (describes each item, often with a symbol/image), in views (introduces a control or describes an available action/task).
- Editable small text → text-fields; large text (optionally editable) → text-views. Component pages (buttons, menus, lists-and-tables) add text-specific guidance.

## Rules
### Best practices
- **Use a label to display a small amount of text that people don't need to edit.** Use a text field for editable small text; a text view for large text.
- **Prefer system fonts** — labels support plain/styled text and Dynamic Type (where available) by default; if you restyle or use custom fonts, keep text legible.
- **Use system-provided label colors to communicate relative importance** — four label colors (table below).
- **Make useful label text selectable** — e.g., error messages, locations, IP addresses: consider letting people select and copy.

## Platform considerations
No additional considerations: iOS, iPadOS, tvOS, visionOS.
### macOS
- Display uneditable text via `NSTextField` with `isEditable` set false.
### watchOS
- System **date and time text components** show current date, time, or both; configurable formats, calendars, time zones. **Countdown timer text component** shows a precise countdown or count-up; configurable formats.
- System date/timer components automatically adjust presentation to available space and update content without app input.
- Consider using date and timer components in complications.

## Specs
| System color | Example usage | iOS, iPadOS, tvOS, visionOS | macOS |
| --- | --- | --- | --- |
| Label | Primary information | `label` | `labelColor` |
| Secondary label | A subheading or supplemental text | `secondaryLabel` | `secondaryLabelColor` |
| Tertiary label | Text that describes an unavailable item or behavior | `tertiaryLabel` | `tertiaryLabelColor` |
| Quaternary label | Watermark text | `quaternaryLabel` | `quaternaryLabelColor` |

## APIs
`Label` (SwiftUI), `Text` (SwiftUI), `UILabel` (UIKit), `NSTextField` / `isEditable` (AppKit), `UIColor.label`… (UIKit), `NSColor.labelColor`… (AppKit)

## Related
text-fields, text-views, buttons, menus, lists-and-tables, color, typography, complications
