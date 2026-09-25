# Combo boxes

> Source: https://developer.apple.com/design/human-interface-guidelines/combo-boxes · Combines a text field with a pull-down button in a single control.

## When to use / core idea
- People can type a custom value or click the button to choose from predefined values.
- A custom entered value is NOT added to the list of choices.
- macOS only.

## Rules
### Best practices
- **Populate the field with a meaningful default value from the list** — field can be empty, but best when default refers to the hidden choices; needn't be the first list item.
- **Use an introductory label to let people know what types of items to expect** — generally title-style capitalization, ending with a colon (see `labels`).
- **Provide relevant choices** — offer the most likely choices alongside custom entry.
- **Make sure list items aren't wider than the text field** — too-wide items may be truncated and hard to read.

## Platform considerations
Not supported: iOS, iPadOS, tvOS, visionOS, watchOS.

## APIs
`NSComboBox` (AppKit)

## Related
`text-fields, pull-down-buttons, labels`
