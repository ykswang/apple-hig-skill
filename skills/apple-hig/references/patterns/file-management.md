# File management

> Source: https://developer.apple.com/design/human-interface-guidelines/file-management · Some apps support documents and files that people expect to manage throughout the system.

## When to use / core idea
- Document-based apps (Pages, Keynote, Photos, Preview) help people create, edit, save documents, often with custom browsing.
- People also browse files outside such apps: Finder on Mac; Files app on iPhone, iPad, Apple Vision Pro. watchOS and tvOS have no document-browsing interface.
- Quick Look lets people preview (and sometimes interact with) files: listen to audio previews, mark up photos, rotate/scale 3D files.

## Rules
### Creating and opening files
- **Use app menus and keyboard shortcuts to give people convenient ways to create and open documents** — commands like New/Open appear in the iPadOS shortcuts interface (hold Command on a hardware keyboard) and in the macOS File menu. Regardless of shortcuts, include an Add (+) button to create a new document; in macOS put the add action in the File menu (see `the-menu-bar`).
- **If your app requires a custom file browser, support people's understanding of the platform's file system** — you may open to the most relevant location (Documents/iCloud folder, most recent location), but let people view the rest of the file system.

### Saving work
- **Help people be confident that their work is always preserved unless they cancel or delete it** — avoid requiring explicit saves; autosave periodically while editing and when closing a file or switching apps.
- **Hide file extensions by default, but let people view them if they choose** — reflect the current choice in all save/open interfaces.

### Quick Look previews
- **Use a Quick Look viewer to let people preview a file even when your app can't open it** — preview unsupported attachments without leaving your app.
- **Consider implementing a Quick Look generator if your app produces custom file types** — lets Finder, Files, Spotlight, and other apps preview your documents.

## Platform considerations
No additional considerations: tvOS, visionOS, watchOS.
### iOS, iPadOS
**Document launcher** (iOS 18 / iPadOS 18+): system full-screen experience to browse, open, create files, highlighting the app's theme. Three customizable parts:
- *Title card*: app title (system-provided) + two app-specific buttons (you set primary/secondary text and functions).
- Background image behind the title card, plus *accessories* (images) around it.
- Sheet with a file browser and optional app-specific toolbar controls.
- **Assign the title card's buttons to your app's most important functions** — primary typically creates a new document; secondary offers additional options (e.g. Numbers: Start Writing / Choose a Template).
- **Provide a background that's clearly distinct from the accessories and title card** — solid color, gradient, or pattern; avoid complex images/patterns that distract.
- **Be mindful of accessory placement** — accessories may sit in front of and behind the title card for depth, but app name and both buttons must stay clearly visible; avoid clutter; test across supported screen sizes and orientations.
- **Use animation sparingly** — too much motion confuses/disorients; consider gentle, repeating animations (e.g. accessory that breathes or sways softly); see `motion`.

**File provider app extension**: custom interface for importing, exporting, opening, moving your app's documents in other apps (*app extension* = installable code extending a system area).
- **When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context** — e.g. only PDFs for a PDF editor; consider showing modification dates, sizes, local vs. remote.
- **Let people select a destination when exporting and moving documents** — unless you use a single directory, allow navigating your hierarchy; consider allowing new subdirectories.
- **Avoid including a custom top toolbar** — the extension loads in a modal view that already has a toolbar; a second one confuses and wastes space.
- Apps can also let people browse and open files from other apps (document browser).
### macOS
**Custom file management** — use the default file browser unless you have an important reason to create a custom one.
- **Make your custom file-opening interface convenient** — e.g. "open recent" besides "open", filter criteria, multi-document open; in an open panel, retitle the Open button to reflect the task (e.g. Insert).
- **Provide a save interface to let people change a file's name, format, or location** — new documents are titled "Untitled" until renamed; default browsing to a logical location; if multiple formats are supported, let people choose one.
- **Consider extending the functionality of the Save dialog** — add a custom accessory view with useful options (e.g. Mail's "include attachments").

**Finder Sync extensions** (apps syncing local and remote files): show sync status badges in Finder, custom contextual menu items (favoriting, password-protection), custom toolbar buttons for global actions (initiate sync).
- **Help people avoid losing work if they turn off autosaving** — autosave is off when "Ask to keep changes when closing documents" is on in Desktop & Dock settings; then show unsaved changes and present a save dialog on close, quit, log out, or restart.
- **When autosaving is off, make sure people know when a document has unsaved changes** — show a dot on the window's close button and next to the document name in the Window menu; don't show the dot when autosave is on (implies action needed). Regardless of autosave, you may append "Edited" to the title-bar title; remove it as soon as autosave or explicit save occurs.

## APIs
`DocumentGroupLaunchScene` (SwiftUI), Documents (SwiftUI), File Provider, Finder Sync, Quick Look, Adding a document browser to your app (UIKit)

## Related
`toolbars, the-menu-bar, printing, motion`
