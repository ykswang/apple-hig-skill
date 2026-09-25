# Steppers

> Source: https://developer.apple.com/design/human-interface-guidelines/steppers · A two-segment control to increase or decrease an incremental value.

## When to use / core idea
- Sits next to a field showing the current value — the stepper itself displays no value.
- Good for small changes needing a few taps/clicks; pair with a text field for wide-ranging values. Alternatives: `pickers`, `text-fields`, `sliders`.

## Rules
### Best practices
- **Make the value that a stepper affects obvious** — people must know which value they're changing.
- **Consider pairing a stepper with a text field when large value changes are likely** — e.g. print dialog number of copies: stepper + text field.

## Platform considerations
No additional considerations: iOS, iPadOS, visionOS. Not supported: watchOS, tvOS.
### macOS
- **For large value ranges, consider supporting Shift-click to change the value quickly** — change by more than the default increment (e.g. 10× the default).

## APIs
`UIStepper` (UIKit), `NSStepper` (AppKit)

## Related
`pickers, text-fields`
