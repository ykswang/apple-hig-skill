# Settings

> Source: https://developer.apple.com/design/human-interface-guidelines/settings · People expect apps and games to just work, but appreciate ways to customize the experience to fit their needs.

## When to use / core idea
- System Settings app (all platforms): appearance, network, accounts, accessibility, language/region; on some platforms also per-app settings (location access, microphone/camera, notifications, Siri, Search integration).
- Custom in-app settings area: general settings affecting the whole experience (interface style, game-saving behavior).
- Task-specific options: put them within the task itself, so people don't leave the experience.

## Rules
### Best practices
- **Aim to provide default settings that give the best experience to the largest number of people** — e.g. auto-maximize game performance for the device rather than asking players at launch; good defaults mean no adjustment before enjoying the app.
- **Minimize the number of settings you offer** — too many make the experience less approachable and settings hard to find.
- **Make settings available in ways people expect** — with a physical keyboard, Command-Comma (,) opens app settings; in games, players often use Esc (Escape).
- **Avoid using settings to ask for setup information you can get in other ways** — e.g. auto-detect a connected controller/accessory; detect whether Dark Mode is on.
- **Respect people's systemwide settings and avoid including redundant versions of them in your custom settings area** — global options (accessibility accommodations, scrolling behavior, authentication methods) belong to system Settings; custom copies imply system settings may not apply and that your version might affect other apps.

### General settings
- **Put general, infrequently changed settings in your custom settings area** — people must suspend what they're doing to open it; e.g. window configuration (apps), game-saving behavior or keyboard mappings (games), account options (both).

### Task-specific options
- **When possible, prefer letting people modify task-specific options without going to your settings area** — e.g. show/hide parts of the view, reorder a collection, filter a list — put these in the screens they affect; a separate settings area disconnects them from context and hides results until the task resumes.
- Note: in games, players adjust their approach to a task as part of gameplay, not as a settings option.

### System settings
- **Add only the most rarely changed options to the system-provided Settings app** — if you add them, consider a button in your interface that opens Settings directly.

## Platform considerations
No additional considerations: iOS, iPadOS, tvOS, visionOS.
### macOS
- Choosing Settings in the App menu opens your custom settings window, typically with a toolbar of buttons switching between *panes* of related settings.
- **Include a settings item in the App menu** — avoid settings buttons in a window's toolbar (takes space from frequent essential commands); for document-level options, add the item to the File menu (see `the-menu-bar`).
- **Dim a settings window's minimize and maximize buttons** — Command–Comma (,) reopens it quickly, so no need for the Dock; the window sizes to the current pane, so no need to expand.
- **In your settings window, use a noncustomizable toolbar that remains visible and always indicates the active toolbar button** — a stable interface helps navigation among settings areas.
- **Update the window's title to reflect the currently visible pane** — with no multiple panes, title it *App Name* Settings.
- **Restore the most recently viewed pane** — people often adjust related settings more than once.
### watchOS
- Apps and games don't add custom settings to the system Settings app; instead consider a small number of essential options at the bottom of the main view, or a More menu to reconfigure objects.

## APIs
`Settings` (SwiftUI), `UserDefaults` (Foundation), Preference Panes, Improving your game's graphics performance and settings (Metal)

## Related
`onboarding, the-menu-bar, managing-notifications, keyboards`
