# Modality

> Source: https://developer.apple.com/design/human-interface-guidelines/modality · Presents content in a separate, dedicated mode that prevents interaction with the parent view and requires an explicit action to dismiss.

## When to use / core idea
- Use modality to: ensure people receive (and act on) critical info; let people confirm/modify their most recent action; perform a distinct, narrowly scoped task without losing context; provide immersion or concentration on a complex task.
- Components: `alerts` (all platforms), plus platform-specific `activity-views`, `sheets`, confirmation dialogs / `action-sheets`. For distinct tasks iOS/iPadOS/macOS use `sheets` or `popovers`; iPadOS, macOS, visionOS may use a separate window.
- Full-screen modal: temporary experience (media viewing) or distinct multistep task (editing). Nonmodal full-screen → `going-full-screen`; visionOS immersion → `immersive-experiences`.

## Rules
### Best practices
- **Present content modally only when there's a clear benefit** — it removes context and requires dismissal; use only when it helps focus or choices affecting content/device.
- **Aim to keep modal tasks simple, short, and streamlined** — complex modal tasks make people lose track of the suspended task, especially when the prior context is obscured.
- **Take care to avoid creating a modal experience that feels like an app within your app** — view hierarchies in a modal make retracing steps hard; if subviews are needed, provide a single path and avoid buttons that could be mistaken for the dismiss button.
- **Consider using a full-screen modal style for in-depth content or a complex task** — minimizes distractions for videos, photos, camera views, multistep tasks (document markup, photo editing). visionOS: in the Shared Space it fills a window; in a Full Space it can become more immersive.
- **Always give people an obvious way to dismiss a modal view** — follow platform conventions: iOS, iPadOS, watchOS — button in the top toolbar or swipe down; macOS, tvOS — button in the main content view.
- **When necessary, help people avoid data loss by getting confirmation before closing a modal view** — whether via gesture or button, if user-generated content could be lost, explain and offer resolutions (e.g. iOS action sheet with a save option).
- **Make it easy to identify a modal view's task** — title naming the task, or text describing it/providing guidance, helps people keep their place.
- **Let people dismiss a modal view before presenting another one** — multiple visible modals add clutter and cognitive load, especially stacked; an alert may appear above all content including modals, but never display more than one alert at a time.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## APIs
Presentation modifiers (SwiftUI), `UIModalPresentationStyle` (UIKit), Modal Windows and Panels (AppKit)

## Related
`sheets, alerts, popovers, action-sheets, activity-views, going-full-screen, immersive-experiences`
