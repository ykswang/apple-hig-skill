# Entering data

> Source: https://developer.apple.com/design/human-interface-guidelines/entering-data · When you need information from people, make it easy for them to provide it without making mistakes.

## When to use / core idea
- Minimize what people must supply by pre-gathering as much information as possible.
- Support all available input methods so people can choose what works for them.
- Prefer selection components (pickers, menus) over free text; see `text-fields`, `virtual-keyboards`, `keyboards`.

## Rules
### Best practices
- **Get information from the system whenever possible** — don't ask for data you can gather automatically (e.g. from settings) or by getting permission (location, calendar).
- **Be clear about the data you need** — use a placeholder prompt (e.g. "username@company.com") or an introductory label ("Email"); prefill reasonable defaults to minimize decisions and speed entry.
- **Use a secure text-entry field when appropriate** — for sensitive data, obscure input (typically a small filled circle per character). tvOS: a `digit-entry-views` can obscure numerals. visionOS: system text field shows data to the wearer only; secure fields automatically blur when streamed via AirPlay.
- **Never prepopulate a password field** — always ask people to enter it or use biometric/keychain authentication (see `managing-accounts`).
- **When possible, offer choices instead of requiring text entry** — choosing from lists is easier than typing even with a keyboard; consider a picker, menu, or other selection component.
- **As much as possible, let people provide data by dragging and dropping it or by pasting it** — eases entry and feels integrated with the system.
- **Dynamically validate field values** — verify as soon as values are entered and give immediate feedback; for numeric data consider a number formatter (accepts only numeric values; can display decimal places, percentage, currency).
- **When data entry is necessary, make sure people understand that they must provide the required data before they can proceed** — e.g. enable a Next/Continue button only after required data is entered.

## Platform considerations
No additional considerations: iOS, iPadOS, tvOS, visionOS, watchOS.
### macOS
- **Consider using an expansion tooltip to show the full version of clipped or truncated text in a field** — behaves like a regular tooltip, appearing when the pointer rests on the field; available to macOS apps including iOS/iPadOS apps running on Mac (see `offering-help`).

## APIs
`SecureField` (SwiftUI), `isSecureDigitEntry` (TVUIKit), `Input events` (SwiftUI)

## Related
`text-fields, virtual-keyboards, keyboards, digit-entry-views, managing-accounts, offering-help, pickers, menus`
