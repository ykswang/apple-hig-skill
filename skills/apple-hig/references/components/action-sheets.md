# Action sheets

> Source: https://developer.apple.com/design/human-interface-guidelines/action-sheets · An action sheet is a modal view that presents choices related to an action people initiate.

## When to use / core idea
- Offers choices tied to an intentional action (e.g., canceling a Mail draft → Delete Draft / Save Draft).
- vs. **alert**: an alert confirms/cancels but offers no additional related choices, and is usually unexpected (problem or situation change). vs. **menu** (iOS/iPadOS): menus appear when people choose to reveal them.
- SwiftUI: confirmation dialog presentation modifier on all platforms; UIKit: `UIAlertController.Style.actionSheet` in iOS, iPadOS, tvOS.

## Rules
### Best practices
- **Use an action sheet — not an alert — to offer choices related to an intentional action.**
- **Use action sheets sparingly** — they interrupt the current task; overuse lowers attention.
- **Aim to keep titles short enough to display on a single line** — long titles are hard to read and may truncate or require scrolling.
- **Provide a message only if necessary** — title plus action context usually suffices.
- **If necessary, provide a Cancel button that lets people reject an action that might destroy data** — at the bottom of the sheet (upper-left corner in watchOS). SwiftUI confirmation dialogs include Cancel by default.
- **Make destructive choices visually prominent** — use the destructive button style and place destructive buttons at the top, where most noticeable.

## Platform considerations
No additional considerations: macOS, tvOS. Not supported: visionOS.

### iOS, iPadOS
- **Use an action sheet — not a menu — to provide choices related to an action** — people expect action sheets after actions needing clarification; menus appear when people reveal them.
- **Avoid letting an action sheet scroll** — more buttons = more effort; scrolling risks accidental taps.

### watchOS
- System style: title, optional message, Cancel button, one or more additional buttons; appearance varies by device.
- **Avoid displaying more than four buttons in an action sheet, including the Cancel button** — Cancel is required, so aim for no more than three additional choices.

## Specs
watchOS button styles:

| Style | Meaning |
| --- | --- |
| Default | No special meaning. |
| Destructive | Destroys user data or performs a destructive action. |
| Cancel | Dismisses the view without taking any action. |

- watchOS: max **4** buttons including Cancel (≤3 additional choices).

## APIs
`confirmationDialog(_:isPresented:titleVisibility:actions:)` (SwiftUI), `ButtonRole.destructive` (SwiftUI), `UIAlertController.Style.actionSheet` (UIKit), `UIAlertAction.Style.destructive` (UIKit).

## Related
`modality, sheets, alerts, menus`
