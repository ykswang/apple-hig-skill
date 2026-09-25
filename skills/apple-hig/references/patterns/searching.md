# Searching

> Source: https://developer.apple.com/design/human-interface-guidelines/searching · People use various search techniques to find content on their device, within an app, and within a document or file.

## When to use / core idea
- In-app search: people expect a `search-fields`; personalize with recent searches, suggestions, completions, or corrections based on earlier searches.
- Scoping/filtering by attributes (creation date, file size, file type): see scope bars and tokens in `search-fields`.
- In-document search: implement find-in-window/page in iOS, iPadOS, macOS apps.
- Systemwide: Spotlight (iOS, iPadOS, macOS) finds content across apps and the web; index your content so people find it without opening your app.

## Rules
### Best practices
- **If search is important, give it a primary position in your app or view** — e.g. Notes: search field in the bottom `toolbars` with other key actions; tab-bar apps (Photos, Apple TV): a dedicated search tab.
- **Aim to make your app's content searchable through a single location** — one clearly identified place; for clearly distinct sections, a local search can still help (e.g. iOS Music: search filters the current view of songs/albums).
- **Clearly display the current scope of a search** — descriptive placeholder text, a scope bar, or a title (e.g. Mail always references the mailbox being searched).
- **Provide suggestions to make searching easier** — recent searches before typing, predictive suggestions while typing.
- **Take privacy into consideration before displaying search history** — others might see it; if shown, provide a way to clear it.

### Systemwide search
- **Make your app's content searchable in Spotlight** — make content indexable and specify descriptive attributes (*metadata*) that Spotlight extracts, stores, and organizes.
- **Define metadata for custom file types you handle** — supply a Spotlight File Importer plug-in describing your format's metadata.
- **Use Spotlight to offer advanced file-search capabilities within the context of your app** — e.g. a button that starts a Spotlight search from the current selection, showing results or a filtered subset in a custom view.
- **Prefer using the system-provided open and save views** — they include a built-in search field for searching/filtering the entire system (see `file-management`).
- **Implement a Quick Look generator if your app produces custom file types** — lets Spotlight and other apps preview your documents.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## APIs
`searchSuggestions(_:)` (SwiftUI), `CSImportExtension` (Core Spotlight), Adding your app's content to Spotlight indexes (Core Spotlight), Quick Look

## Related
`search-fields, toolbars, tab-bars, file-management`
