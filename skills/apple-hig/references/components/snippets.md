# Snippets

> Source: https://developer.apple.com/design/human-interface-guidelines/snippets · When someone performs a task with Siri or an App Shortcut, a snippet shows the result or asks for confirmation.

## When to use / core idea
- Compact views shown in response to actions via Siri, Spotlight, or the Shortcuts app; presented by including one with an app intent (e.g. weather forecast, progress toward a daily goal).
- Two types: *confirmation* (confirm/cancel, may include options affecting the result) and *result* (information, no further action needed). An intent showing a snippet always shows a result; confirmation is optional.
- For info changing over time use `live-activities` instead.

## Rules
### Anatomy
- **Dialogue** — app intent dialogue spoken by Siri; system includes the text by default above the custom view.
- **Custom view** — visually communicates the info; may include buttons to modify content, get more info, or take another action. Max height 400 pt.
- **System-provided button(s)** — confirmation: secondary Cancel + primary button with customizable label; result: single Done button that dismisses.

### Best practices
- **Ensure legibility** — sufficient contrast between custom content and the system background in light and dark appearances; consistent content margins.
- **Keep content concise** — custom views no taller than the 400 pt maximum; account for text size varying with the preferred text size setting. For more detail in a result snippet, deep-link into your app.
- **Choose a descriptive label for a confirmation snippet's primary button** — system-provided (`ConfirmationActionName`) or custom; e.g. "Order" beats "OK"/"Proceed". Default if unspecified: **Continue**.
- **Communicate a snippet's purpose visually** — don't rely on dialogue text; spoken dialogue is essential eyes-free, but prefer omitting it from the visual representation and convey info in the custom view (don't duplicate dialogue and view content).

## Platform considerations
No additional considerations: iOS, iPadOS, macOS. Not supported: tvOS, visionOS, watchOS.

## Specs
- Custom view max height: 400 pt.

## APIs
`app intent` (App Intents), `Displaying static and interactive snippets` (App Intents), `system provides` (App Intents), `App Intents` (App Intents)

## Related
`siri, app-shortcuts, live-activities`
