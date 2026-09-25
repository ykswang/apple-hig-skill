# Pickers

> Source: https://developer.apple.com/design/human-interface-guidelines/pickers · Displays one or more scrollable lists of distinct values that people can choose from.

## When to use / core idea
- Several system styles, each with different selectable value types and appearance; values and their order depend on device language.
- Choose single or multipart values; date pickers add calendar-view selection and numeric-keypad date/time entry.
- Short list → `pull-down-buttons`; very large set → `lists-and-tables` (adjustable height, tables can have an index).

## Rules
### Best practices
- **Consider using a picker to offer medium-to-long lists of items** — a picker adds too much visual weight for a short list; for very large sets use a list or table.
- **Use predictable and logically ordered values** — many values are hidden before interaction; make them predictable (e.g. alphabetized countries) so people move quickly.
- **Avoid switching views to show a picker** — show it in context, below or near the field being edited; typically at the bottom of a window or in a popover.
- **Consider providing less granularity when specifying minutes in a date picker** — default minute list is 60 values (0–59); an interval must divide evenly into 60, e.g. quarter-hour (0, 15, 30, 45).

## Platform considerations
No additional considerations: visionOS.
### iOS, iPadOS
- Date picker selects date, time, or both via touch, keyboard, or pointer.
- Styles:
  - **Compact** — button showing editable date/time content in a modal view.
  - **Inline** — time only: button that displays wheels; dates and times: inline calendar view.
  - **Wheels** — scrolling wheels; also supports data entry through built-in or external keyboards.
  - **Automatic** — system-determined based on platform and mode.
- Modes:
  - **Date** — months, days of month, years.
  - **Time** — hours, minutes, optional AM/PM.
  - **Date and time** — dates, hours, minutes, optional AM/PM.
  - **Countdown timer** — hours and minutes, max 23 hours 59 minutes; not available in inline or compact styles.
- Values and order depend on device location.
- **Use a compact date picker when space is constrained** — button shows current value in the app's accent color; tap opens a modal calendar-style editor + time picker; people can make multiple edits, then tap outside to confirm.
### macOS
- **Choose a date picker style that suits your app** — two styles: *textual* (limited space, specific date/time selections) and *graphical* (browse days in a calendar, select a date range, or when a clock face look suits the app).
### tvOS
- Pickers available with SwiftUI (`Picker`).
### watchOS
- People navigate picker lists with the Digital Crown for precise selection.
- Lists can use the wheels style; date and time pickers also use wheels.
- Configurable outline, caption, and scrolling indicator.
- For longer lists, the navigation link style shows the picker as a button; tapping shows the options list; people can also scrub options with the Digital Crown without tapping (`navigationLink`).

## APIs
`Picker` (SwiftUI), `DatePicker` (SwiftUI), `navigationLink` PickerStyle (SwiftUI), `UIDatePicker` (UIKit), `UIPickerView` (UIKit), `NSDatePicker` (AppKit)

## Related
`pull-down-buttons, lists-and-tables`
