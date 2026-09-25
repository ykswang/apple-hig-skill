# Home Screen quick actions

> Source: https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions · Home Screen quick actions let people perform app-specific actions from the Home Screen.

## When to use / core idea
- Menu revealed by touch and hold on an app icon (on 3D Touch devices, pressing with increased pressure). E.g., Mail: open Inbox or VIP, search, new message. The menu also lists system items for removing the app and editing the Home Screen.
- Each action: title, interface icon on the left or right (depending on the app's Home Screen position), optional subtitle. Title and subtitle are always left-aligned in left-to-right languages.
- Actions can update dynamically (e.g., Messages: most recent conversations).
- macOS analog: dock-menus.

## Rules
### Best practices
- **Create quick actions for compelling, high-value tasks** — e.g., Maps: search nearby, directions home. People expect every app to provide at least one useful quick action; you can provide a total of **four**.
- **Avoid making unpredictable changes to quick actions** — dynamic updates (location, recent activity, time of day, settings changes) must change in predictable ways.
- **For each quick action, provide a succinct title that instantly communicates the result** — e.g., "Directions Home," "Create New Contact," "New Message." Add a subtitle for more context (Mail shows unread status). Don't include the app name or extraneous info; keep text short to avoid truncation; account for localization.
- **Provide a familiar interface icon for each quick action** — prefer SF Symbols (see icons › Standard icons). For custom icons, use the Quick Action Icon Template in Apple Design Resources for iOS and iPadOS.
- **Don't use an emoji in place of a symbol or interface icon** — emojis are full color; quick action symbols are monochromatic and adapt to Dark Mode for contrast.

## Platform considerations
No additional considerations: iOS, iPadOS. Not supported: macOS, tvOS, visionOS, watchOS.

## Specs
- Maximum quick actions: 4 (expect at least 1).

## APIs
`Add Home Screen quick actions` (UIKit)

## Related
menus, sf-symbols, icons, dock-menus
