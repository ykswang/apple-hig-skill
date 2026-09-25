# Token fields

> Source: https://developer.apple.com/design/human-interface-guidelines/token-fields · A token field is a type of text field that can convert text into *tokens* that are easy to select and manipulate.

## When to use / core idea
- macOS only. E.g., Mail's address fields convert each recipient name into a token that can be selected, dragged to reorder, or moved to another field.
- Can show a suggestion list while typing; selecting a suggestion inserts it as a token.
- Individual tokens can have a contextual menu with info or editing options (Mail: edit name, mark as VIP, view contact card…).
- Tokens can also represent search terms (see search-fields).

## Rules
### Best practices
- **Add value with a context menu** — additional options or info about a token.
- **Consider providing additional ways to convert text into tokens** — default trigger is typing a comma; add shortcuts such as pressing Return.
- **Consider customizing the delay the system uses before showing suggested tokens** — default is immediate, which can distract while typing; adjust to a comfortable delay.

## Platform considerations
Not supported: iOS, iPadOS, tvOS, visionOS, watchOS.

## APIs
`NSTokenField` (AppKit).

## Related
`text-fields, search-fields, context-menus`
