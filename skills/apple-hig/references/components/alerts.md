# Alerts

> Source: https://developer.apple.com/design/human-interface-guidelines/alerts · An alert gives people critical information they need right away.

## When to use / core idea
- Tell people about a problem, warn that an action might destroy data, or let them confirm a purchase or other important action they initiated.
- Modal view; appearance differs per platform/device.
- Use an **action sheet** for choices related to an intentional action; use in-context indicators for purely informational messages.

## Rules
### Best practices
- **Use alerts sparingly** — they interrupt; each should offer only essential info and useful actions.
- **Avoid using an alert merely to provide information** — non-actionable interruptions are unwelcome; prefer an in-context alternative (e.g., Mail's server-unavailable indicator people can choose to learn more).
- **Avoid displaying alerts for common, undoable actions, even when they're destructive** — e.g., deleting an email/file is intentional and undoable. Do alert for uncommon destructive actions that can't be undone.
- **Avoid showing an alert when your app starts** — make new/important info discoverable instead; for startup problems (e.g., no network) consider cached/placeholder data plus a nonintrusive label.

### Content
- All platforms: title, optional informative text, up to **three** buttons. Extras: text field (iOS, iPadOS, macOS, visionOS); icon and accessory view (macOS, visionOS); suppression checkbox and Help button (macOS).
- **In all alert copy, be direct, and use a neutral, approachable tone** — don't be oblique or accusatory, or mask severity.
- **Write a title that clearly and succinctly describes the situation** — complete and specific, not verbose; what happened, context, why. Avoid uninformative titles ("Error", "Error 329347 occurred") and titles wrapping to **more than two lines**. Complete sentence → sentence-style capitalization + ending punctuation; fragment → title-style capitalization, no ending punctuation.
- **Include informative text only if it adds value** — as short as possible; complete sentences, sentence-style capitalization, appropriate punctuation.
- **Avoid explaining alert buttons** — if needed in rare cases, use *choose* (device/interaction-neutral) and refer to the button by its exact title without quotes.
- **If supported, include a text field only if you need people's input to resolve the situation** — e.g., secure text field for a password.

### Buttons
- **Create succinct, logical button titles** — one or two words describing the result; prefer verbs/verb phrases tied to the alert text ("View All", "Reply", "Ignore"). "OK" for acceptance only in informational alerts; avoid "Yes" and "No". Always "Cancel" for canceling. Title-style capitalization, no ending punctuation.
- **Avoid using OK as the default button title unless the alert is purely informational** — ambiguous; use specific titles like "Erase", "Convert", "Clear", "Delete".
- **Place buttons where people expect** — most likely choice on the trailing side of a row or at the top of a stack. Always put the default button trailing (row) or top (stack). Cancel typically leading (row) or bottom (stack).
- **Use the destructive style to identify a button that performs a destructive action people didn't deliberately choose** — e.g., the Empty Trash confirmation's Empty Trash button is NOT destructive-styled because it fulfills the original intent (pressing Return to confirm is more valuable).
- **If there's a destructive action, include a Cancel button to give people a clear, safe way to avoid the action** — always titled "Cancel"; don't make Cancel the default. To encourage reading, make no button default. For a single-button alert whose button is default, use Done, not Cancel.
- **Provide alternative ways to cancel an alert when it makes sense** — see table in Specs.

## Platform considerations
No additional considerations: tvOS, watchOS.

### iOS, iPadOS
- **Use an action sheet — not an alert — to offer choices related to an intentional action** — e.g., canceling a Mail message: delete edits (or draft), save draft, or return to editing.
- **When possible, avoid displaying an alert that scrolls** — large text sizes can cause scrolling; keep titles short and messages brief/only when necessary.

### macOS
- Shows the app icon automatically (can supply an alternative icon or symbol). Can: let people suppress repeating alerts; append a custom accessory view (`accessoryView`); include a Help button opening help docs.
- **Use a caution symbol sparingly** — overusing `exclamationmark.triangle` dilutes it; use only when extra attention is really needed (e.g., unexpected data loss). Not for tasks whose only purpose is overwriting/removing data (save, empty trash).

### visionOS
- Shared Space: alert appears in front of the app's window, slightly forward on z-axis; stays anchored to the window if moved without dismissing. Full Space: centered in the wearer's field of view.

## Specs
- Max buttons: **3**. Title: ≤ **2 lines**. Button titles: **1–2 words**.
- visionOS accessory view: max height **154 pt**, corner radius **16 pt**.

Alternative cancel methods:

| Action | Platform |
| --- | --- |
| Exit to the Home Screen | iOS, iPadOS |
| Pressing Escape (Esc) or Command-Period (.) on an attached keyboard | iOS, iPadOS, macOS, visionOS |
| Pressing Menu on the remote | tvOS |

## APIs
`alert(_:isPresented:actions:)` (SwiftUI), `UIAlertController` (UIKit), `NSAlert` (AppKit), `NSAlert.accessoryView` (AppKit).

## Related
`modality, action-sheets, sheets, buttons, toggles, spatial-layout, writing`
