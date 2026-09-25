# Virtual keyboards

> Source: https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards · On devices without physical keyboards, system virtual keyboards let people enter data.

## When to use / core idea
- Virtual keyboards can offer key sets optimized for the task (e.g. email: "@", period, even ".com"). They don't support keyboard shortcuts.
- You can replace the system keyboard with a custom *input view* for app-specific entry (in-app only). In iOS, iPadOS, tvOS you can also ship a *custom keyboard* app extension usable systemwide.

## Rules
### Best practices
- **Choose a keyboard that matches the type of content people are editing** — e.g. numbers and punctuation for numeric data. Specifying semantic content type lets the system pick a matching keyboard and refine corrections (`keyboardType(_:)`, `textContentType(_:)`, `UIKeyboardType`, `UITextContentType`).
- Available keyboard types (iPhone):

| Type | Keys |
| --- | --- |
| ASCII capable | 26 letters, Shift, Delete, Numbers, Space, Return; suggestions; Dictation |
| ASCII capable number pad | 10 numbers (2–9 with phone letters), Delete |
| Decimal pad | 10 numbers (with phone letters), Delete, period |
| Default | 26 letters, Shift, Delete, Numbers, Space, Return; suggestions; Emoji, Dictation |
| Email address | 26 letters, Shift, Delete, Numbers, Space, period, @, Return; suggestions; Emoji |
| Name phone pad | 26 letters, Shift, Delete, Numbers, Space, Return; suggestions; Emoji, Dictation |
| Number pad | 10 numbers (with phone letters), Delete |
| Numbers and punctuation | 10 numbers, 15 punctuation, secondary punctuation, Delete, Letters, Space, Return; suggestions; Dictation |
| Phone pad | 10 numbers (with phone letters), Delete, plus/star/hash key |
| Twitter | 26 letters, Shift, Delete, Numbers, Space, @, hash; suggestions; Emoji, Dictation |
| URL | 26 letters, Shift, Delete, Numbers, period, slash, .com, Return; suggestions; Emoji |
| Web search | 26 letters, Shift, Delete, Numbers, Space, period, Go; suggestions; Emoji, Dictation |

- **Consider customizing the Return key type if it helps clarify the text-entry experience** — default derives from keyboard type; e.g. use a search Return key when initiating search (`submitLabel(_:)`, `UIReturnKeyType`).

### Custom input views
- Replaces the system keyboard while people are in your app (e.g. Numbers' numeric entry view in spreadsheets) (`ToolbarItemPlacement`, `inputViewController`).
- **Make sure your custom input view makes sense in the context of your app** — people should understand its benefit, or they'll wonder why they can't get the system keyboard back.
- **Play the standard keyboard sound while people type** — familiar feedback; people can disable keyboard sounds in Settings > Sounds (`playInputClick()`).

### Custom keyboards
- iOS, iPadOS, tvOS: app extension replaces the system keyboard. After enabling in Settings, usable in any app **except secure text fields and phone number fields**; people can enable multiple and switch anytime.
- Use for unique systemwide functionality (novel input method, unsupported language). For in-app only, prefer a custom input view.
- **Provide an obvious and easy way to switch between keyboards** — people expect Globe-key-like behavior (Globe replaces the Emoji key when multiple keyboards are available).
- **Avoid duplicating system-provided keyboard features** — Emoji/Globe and Dictation keys may appear beneath the keyboard automatically; you can't affect them; don't repeat them.
- **Consider providing a keyboard tutorial in your app** — how to choose, activate, use, and switch back to the standard keyboard. Avoid displaying help content within the keyboard itself.

## Platform considerations
Not supported: macOS.
### iOS, iPadOS
- **Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface** — keeps important UI (fields, buttons) visible and not covered by the keyboard.
- **Place custom controls above the keyboard thoughtfully** — input accessory view (e.g. Numbers calculation controls) must be relevant to the current task. If other views use Liquid Glass or your view looks out of place, apply Liquid Glass to the container; a standard toolbar adopts Liquid Glass automatically. Use the keyboard layout guide and standard padding (`ToolbarItemPlacement`, `inputAccessoryView`, `UIKeyboardLayoutGuide`).
### tvOS
- Linear virtual keyboard appears when selecting a text field with the Siri Remote; with other devices a grid keyboard screen appears and content layout adapts automatically.
- Digit entry views show a digit-specific keyboard (see `digit-entry-views`).
### visionOS
- System keyboard supports direct and indirect gestures and appears in a separate, movable window; no need to account for its location in layouts.
### watchOS
- A text field shows a keyboard if the screen is large enough; otherwise dictation or Scribble. You can't change keyboard type but can set content type (`textContentType(_:)`) for suggestions.
- People can also enter text via a nearby paired iPhone.

## APIs
`keyboardType(_:)` (SwiftUI), `textContentType(_:)` (SwiftUI), `submitLabel(_:)` (SwiftUI), `ToolbarItemPlacement` (SwiftUI), `UIKeyboardType` (UIKit), `UITextContentType` (UIKit), `UIReturnKeyType` (UIKit), `inputViewController` (UIKit), `inputAccessoryView` (UIKit), `UIKeyboardLayoutGuide` (UIKit), `playInputClick()` (UIKit)

## Related
`entering-data, keyboards, layout, digit-entry-views, text-fields`
