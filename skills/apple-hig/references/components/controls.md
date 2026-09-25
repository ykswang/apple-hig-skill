# Controls

> Source: https://developer.apple.com/design/human-interface-guidelines/controls · Provides quick access to a feature of your app from Control Center, the Lock Screen, or the Action button.

## When to use / core idea
- A control is a button or toggle. Control buttons perform an action, link to a specific area of your app, or launch a camera experience on a locked device. Control toggles switch between two states (on/off).
- People add controls to Control Center (press and hold an empty area), the Lock Screen (customize Lock Screen), and the Action button (Settings app).

## Rules
### Anatomy
- Symbol image (SF Symbol or custom) + title + optional value. Symbol = what it does; title = what it relates to (e.g. light name); value = state (on/off).
- Display by location:
  - Control Center: symbol; at larger sizes also title and value.
  - Lock Screen: symbol only.
  - iPhone Action button: press and hold shows symbol in the Dynamic Island plus value (if present).

### Best practices
- **Offer controls for actions that provide the most benefit without having to launch your app** — e.g. starting a Live Activity from a control to track progress.
- **Update controls when someone interacts with them, when an action completes, or remotely with a push notification** — reflect state accurately and show if an action is still in progress.
- **Choose a descriptive symbol that suggests the behavior of the control** — title/value may not display, so the symbol must convey the action. For toggles provide symbols for both on and off (e.g. `door.garage.open` / `door.garage.closed`).
- **Use symbol animations to highlight state changes** — toggles: animate on↔off transitions; buttons with duration actions: animate indefinitely while performing, stop when complete (`Symbols`, `SymbolEffect`).
- **Select a tint color that works with your app's brand** — applied to a toggle's symbol in on state, and to value + symbol in the Dynamic Island when run from the Action button.
- **Help people provide additional information the system needs to perform an action** — if configuration is required (e.g. which light), prompt when first added; people can reconfigure anytime (`promptsForUserConfiguration()`).
- **Provide hint text for the Action button** — shown on press to explain what press-and-hold does; use verbs (e.g. "Hold for Silent") (`controlWidgetActionHint(_:)`).
- **If your control title or value can vary, include a placeholder** — shown in the controls gallery (Control Center/Lock Screen) and before assigning to the Action button.
- **Hide sensitive information when the device is locked** — consider having the system redact title and value; specify whether to redact symbol state too — if so, the system redacts title and value and shows the symbol in its off state.
- **Require authentication for actions that affect security** — e.g. unlock to lock/unlock a house door or start a car (`IntentAuthenticationPolicy`).

### Camera experiences on a locked device
- iOS 18+: a control can launch directly to your app's camera experience while locked; any task beyond capture requires authentication/unlock (`LockedCameraCapture`).
- **Use the same camera UI in your app and your camera experience** — familiarity and seamless transition to further tasks (posting, editing).
- **Provide instructions for adding the control.**

## Platform considerations
No additional considerations: iOS, iPadOS, macOS. Not supported: watchOS, tvOS, visionOS.

## APIs
WidgetKit, `LockedCameraCapture`, `promptsForUserConfiguration()` (SwiftUI), `controlWidgetActionHint(_:)` (SwiftUI), `IntentAuthenticationPolicy` (App Intents), `SymbolEffect` (Symbols)

## Related
`widgets, action-button, live-activities, sf-symbols, branding`
