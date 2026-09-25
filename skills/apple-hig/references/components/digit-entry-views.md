# Digit entry views

> Source: https://developer.apple.com/design/human-interface-guidelines/digit-entry-views · Full-screen view prompting people to enter a series of digits (e.g. a PIN) using a digit-specific keyboard.

## When to use / core idea
- tvOS only. Fills the entire screen; optional title and prompt above the line of digits.

## Rules
### Best practices
- **Use secure digit fields** — they show asterisks instead of digits; always use one when asking for sensitive data.
- **Clearly state the purpose of the digit entry view** — title and prompt explain why digits are needed.

## Platform considerations
Not supported: iOS, iPadOS, macOS, visionOS, watchOS.

## APIs
`TVDigitEntryViewController` (TVUIKit)

## Related
`virtual-keyboards`
