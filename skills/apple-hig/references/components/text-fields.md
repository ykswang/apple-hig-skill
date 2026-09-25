# Text fields

> Source: https://developer.apple.com/design/human-interface-guidelines/text-fields · A rectangular area in which people enter or edit small, specific pieces of text.

## When to use / core idea
- Small amounts of info (name, email). Larger text → `text-views`. Text + list of choices on macOS → `combo-boxes`.

## Rules
### Best practices
- **Use a text field to request a small amount of information, such as a name or an email address** — use a text view for larger input.
- **Show a hint in a text field to help communicate its purpose** — placeholder text (e.g. "Email", "Password") when empty; since it disappears on typing, a separate label can remind people of the purpose.
- **Use secure text fields to hide private data** — always use one for sensitive data such as passwords (`SecureField`).
- **To the extent possible, match the size of a text field to the quantity of anticipated text** — size signals how much to enter.
- **Evenly space multiple text fields** — enough space so each field clearly pairs with its label; stack vertically when possible; use consistent widths (e.g. first/last name one width, address/city another).
- **Ensure that tabbing between multiple fields flows as people expect** — logical focus sequence; system usually handles it automatically.
- **Validate fields when it makes sense** — e.g. alert on non-digits in a digits-only field. Timing depends on context: email → validate when people switch to another field; user name/password → validate before they switch.
- **Use a number formatter to help with numeric data** — restricts to numeric values; can format decimal places, percentage, currency. Don't assume presentation — formatting varies by locale.
- **Adjust line breaks according to the needs of the field** — default clips overflow; alternatives: wrap at character or word level, or truncate with ellipsis at beginning, middle, or end.
- **Consider using an expansion tooltip to show the full version of clipped or truncated text** — appears on pointer hover like a regular tooltip.
- **In iOS, iPadOS, tvOS, and visionOS apps, show the appropriate keyboard type** — e.g. numbers, URLs (see `virtual-keyboards`).
- **Minimize text entry in your tvOS and watchOS apps** — long text/many fields are time-consuming; gather info more efficiently, e.g. with buttons.

## Platform considerations
No additional considerations: tvOS, visionOS.
### iOS, iPadOS
- **Display a Clear button in the trailing end of a text field to help people erase their input** — avoids repeated Delete taps.
- **Use images and buttons to provide clarity and functionality in text fields** — custom images at either end, or a system button (e.g. Bookmarks). Generally leading end = field's purpose; trailing end = additional features.
### macOS
- **Consider using a combo box if you need to pair text input with a list of choices.**
### watchOS
- **Present a text field only when necessary** — whenever possible prefer a list of options over text entry.

## APIs
`TextField` (SwiftUI), `SecureField` (SwiftUI), `UITextField` (UIKit), `NSTextField` (AppKit)

## Related
`text-views, combo-boxes, entering-data, virtual-keyboards, offering-help`
