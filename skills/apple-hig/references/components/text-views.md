# Text views

> Source: https://developer.apple.com/design/human-interface-guidelines/text-views · A text view displays multiline, styled text content, which can optionally be editable.

## When to use / core idea
- Any height; scrolls when content overflows. Default: leading-aligned, system label color. In iOS, iPadOS, visionOS, selecting an editable text view shows a keyboard.
- Offers the most options for specialized text display and input. For small amounts of text use a **label**, or a **text field** if editable.

## Rules
### Best practices
- **Use a text view when you need to display text that's long, editable, or in a special format.**
- **Keep text legible** — creative fonts/colors/alignments must not hurt readability; adopt Dynamic Type; test with accessibility options such as bold text (see accessibility, typography).
- **Make useful text selectable** — e.g., error messages, serial numbers, IP addresses: consider allowing select and copy.

## Platform considerations
No additional considerations: macOS, visionOS, watchOS.

### iOS, iPadOS
- **Show the appropriate keyboard type** — match the keyboard to the content type to streamline entry (see virtual-keyboards).

### tvOS
- Text views can display text, but because text input is minimal by design, tvOS uses text fields for editable text.

## APIs
`Text` (SwiftUI), `UITextView` (UIKit), `NSTextView` (AppKit).

## Related
`labels, text-fields, combo-boxes, accessibility, typography, virtual-keyboards`
