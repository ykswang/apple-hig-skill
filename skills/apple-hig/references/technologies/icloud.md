# iCloud

> Source: https://developer.apple.com/design/human-interface-guidelines/icloud · iCloud lets people seamlessly access their content — photos, videos, documents, and more — from any device without explicit synchronization.

## When to use / core idea
- Core principle is transparency: people don't need to know where content resides; they assume they always have the latest version.
- Store user-created content, app state, and settings people want everywhere; for games, consider GameSave for save data.

## Rules
### Best practices
- **Make it easy to use your app with iCloud** — people turn on iCloud in Settings and expect apps to work automatically. If people might want a choice, show a simple option on first launch: iCloud for all data or not at all.
- **Avoid asking which documents to keep in iCloud** — people expect all content there; automate file-management tasks where possible.
- **Keep content up to date when possible** — balance against storage and bandwidth. For very large documents, it may be better to let people control when updates download; then indicate when a newer version is available in iCloud. Provide subtle feedback if a document download takes more than a few seconds.
- **Respect iCloud storage space** — finite and paid; store info people create and understand; avoid app resources or regenerable content. iCloud backups include every app's Documents folder, so be picky about what goes there.
- **Make sure your app behaves appropriately when iCloud is unavailable** — no alert needed when iCloud is off or in Airplane Mode; it may help to unobtrusively note that changes won't reach other devices until access is restored.
- **Keep app state information in iCloud** — e.g., last page viewed in a magazine app. Only sync settings people want applied to all devices (some suit work vs. home).
- **Warn about the consequences of deleting a document** — deletion removes it from iCloud and all devices; show a warning and ask for confirmation.
- **Make conflict resolution prompt and easy** — resolve automatically where possible; otherwise an unobtrusive notification to differentiate and choose versions, as early as possible.
- **Include iCloud content in search results.**
- **For games, consider saving player progress in iCloud** — GameSave syncs save data across devices and offers built-in alerts for offline/conflict issues, or use its data with custom UI.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## APIs
`CloudKit`, `GameSave`

## Related
file-management, settings, alerts
