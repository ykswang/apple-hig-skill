# Always On

> Source: https://developer.apple.com/design/human-interface-guidelines/always-on · On devices with an Always On display, the system can keep showing an app's interface when people suspend interaction.

## When to use / core idea
- Always On gives glanceable info in a low-power, privacy-preserving way: display dims and onscreen motion is minimized.
- iPhone 14 Pro / 14 Pro Max: shows Lock Screen items (widgets, Live Activities) when the device is set aside face up and idle.
- Apple Watch: on wrist-down, watch face dims; the app's interface stays visible if it's frontmost or running a background session.
- Both: notifications still display; tapping the display exits Always On.

## Rules
### Best practices
- **Hide sensitive information** — redact personal info casual observers shouldn't see (bank balances, health data), including in notifications.
- **Keep other types of personal information glanceable when it makes sense** — e.g. workout pace/heart rate on Watch, flight arrival or ride-share arrival on iPhone. People can turn off Always On entirely.
- **Keep important content legible and dim nonessential content** — increase dimming on secondary text, images, color fills (e.g. to-do app removes row backgrounds, dims details, keeps titles). Consider removing rich images/large color areas and using dimmed colors.
- **Maintain a consistent layout** — avoid distracting changes when Always On begins/ends and throughout. Prefer transitioning interactive components to an unavailable appearance rather than removing them. Make infrequent, subtle updates (e.g. sports app updates only the score, not play-by-play). Motion is especially distracting on iPhone lying face up.
- **Gracefully transition motion to a resting state; don't stop it instantly** — smooth finish signals the transition and avoids implying an error.

## Platform considerations
No additional considerations: iOS, watchOS. Not supported in iPadOS, macOS, tvOS, visionOS.

## Specs
- Supported iPhones (per page): iPhone 14 Pro, iPhone 14 Pro Max.

## APIs
Designing your app for the Always On state (watchOS apps)

## Related
designing-for-watchos, widgets, live-activities, notifications
