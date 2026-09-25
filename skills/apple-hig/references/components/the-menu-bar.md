# The menu bar

> Source: https://developer.apple.com/design/human-interface-guidelines/the-menu-bar · On Mac or iPad, the menu bar at the top of the screen displays the top-level menus of an app or game.

## When to use / core idea
- Mac users rely on the menu bar to learn what an app does and find commands; a consistent menu bar is essential to feel at home in macOS.
- iPad menu bar menus mirror Mac: same order, familiar items. iPadOS keyboard shortcuts follow macOS patterns (see keyboards).
- Menu bar menus share appearance/behavior of all menus — see `menus` for organizing and labeling items.
- Not supported in iOS, tvOS, visionOS, watchOS.

## Anatomy
- Menu order when present: *YourAppName* (short app name) → File → Edit → Format → View → app-specific menus → Window → Help.
- macOS also has the Apple menu on the leading side and menu bar extras on the trailing side.

## Rules
### Best practices
- **Support the default system-defined menus and their ordering** — people expect familiar order; the system often implements standard items (e.g., Edit > Copy enabled when text is selected in a standard text field).
- **Always show the same set of menu items** — helps people learn what the app supports; if an item isn't actionable, disable it instead of hiding it.
- **Represent menu item actions with familiar icons** — use the same icons as the system for Copy, Share, Delete, etc., wherever they appear (see icons › Standard icons).
- **Support the keyboard shortcuts defined for the standard menu items you include** (Copy, Cut, Paste, Save, Print…). Define custom shortcuts only when necessary.
- **Prefer short, one-word menu titles** — display size and menu bar extras affect spacing; one word takes little space and scans easily. If more than one word, use title-style capitalization.

### App menu
- Lists items that apply to the app as a whole, not a task/document/window. Menu bar shows app name in bold to identify the active app.
- **Display the About menu item first** — follow it with a separator so it sits alone in a group.

### File menu
- Manages files/documents. If the app handles no file types, you can rename or eliminate it.

### Edit menu
- Changes content in current document/text container and Clipboard interaction; useful even in non-document apps.
- **Determine whether Find menu items belong in the Edit menu** — e.g., if the app searches for files or other objects, Find may fit better in File.

### Format menu
- Adjusts text formatting attributes; exclude if the app doesn't support formatted text editing.

### View menu
- Customizes appearance of all app windows. Does NOT include items for navigating/managing specific windows (that's the Window menu).
- **Provide a View menu even if your app supports only a subset of the standard view functions** — e.g., only Enter/Exit Full Screen if no tab bar/toolbar/sidebar.
- **Ensure that each show/hide item title reflects the current state of the corresponding view** — toolbar hidden → "Show Toolbar"; visible → "Hide Toolbar".

### App-specific menus
- Appear between View and Window (e.g., Safari's History, Bookmarks).
- **Provide app-specific menus for custom commands** — list commands in the menu bar even if available elsewhere: easier to find, allows keyboard shortcuts, accessible to Full Keyboard Access. Excluding even infrequent/advanced commands risks making them hard to find.
- **As much as possible, reflect your app's hierarchy in app-specific menus** — e.g., Mail: Mailbox, Message, Format (mailboxes contain messages, messages contain formatting).
- **Aim to list app-specific menus in order from most to least general or commonly used** — people expect leading menus to be more specialized than trailing ones. *(sic — as written in source)*

### Window menu
- Navigates, organizes, manages windows. Does NOT customize appearance (View menu) or close windows (File > Close).
- **Provide a Window menu even if your app has only one window** — include Minimize and Zoom so Full Keyboard Access users can invoke them.
- **Consider including menu items for showing and hiding panels** — no need for font panel or text color panel (Format menu lists them).

### Help menu
- At trailing end. With Help Book format, macOS automatically adds a search field at the top.

### Dynamic menu items
- A dynamic item changes behavior when chosen while pressing a modifier (Control, Option, Shift, Command), e.g., Minimize → Minimize All with Option. Use in rare cases.
- **Avoid making a dynamic menu item the only way to accomplish a task** — they're hidden by default; best as shortcuts to advanced actions achievable otherwise.
- **Use dynamic menu items primarily in menu bar menus** — in contextual or Dock menus they're even harder to discover.
- **Require only a single modifier key to reveal a dynamic menu item** — multiple keys are physically awkward and less discoverable.
- macOS automatically sizes menu width to the widest item, including dynamic items.

## Platform considerations
Not supported: iOS, tvOS, visionOS, watchOS.

### iPadOS
- Menu bar shows system and custom menus; revealed by moving pointer to top edge or swiping down. When visible, occupies same vertical space as the status bar.
- **Because the menu bar is often hidden when running full screen, ensure people can access all app functions through its UI** — always offer other ways to do tasks assigned to dynamic menu items (only available with a hardware keyboard). Avoid using the menu bar as a catch-all for functionality that doesn't fit elsewhere.
- **Reserve the YourAppName > Settings menu item for opening your app's page in iPadOS Settings** — link to an internal preferences area with a separate item beneath Settings in the same group; put other custom app-wide configuration options there too.
- **For apps with tab-style navigation, consider adding each tab as a menu item in the View menu** — and consider assigning key bindings to each tab.
- **Consider grouping menu items into submenus to conserve vertical space** — iPad menu rows are taller (easier to tap) and some iPads have small screens; use submenus more often than on Mac.

### macOS
- Apple menu is always first on the leading side; system-defined, can't be modified or removed. Menu bar extras appear at trailing end, space permitting.
- When space is constrained, system prioritizes menus and essential extras; may decrease spacing between titles and truncate them.
- In full-screen mode the menu bar typically hides until the pointer moves to the top of the screen.

#### Menu bar extras
- An icon exposing app-specific functionality in the menu bar while the app runs, even when not frontmost; on the opposite side from app menus. System hides extras when needed to make room for app menus, or when there are too many.
- **Consider using a symbol to represent your menu bar extra** — custom icon or SF Symbol (as-is or customized). Use black and clear colors to define shape; system recolors black areas for dark/light menu bars and selected state.
- **Display a menu — not a popover — when people click your menu bar extra** — unless functionality is too complex for a menu.
- **Let people — not your app — decide whether to put your menu bar extra in the menu bar** — typically via a setting in the app's settings window; consider offering the option during setup for discoverability.
- **Avoid relying on the presence of menu bar extras** — system hides/shows them regularly; you can't predict others shown or your extra's location.
- **Consider exposing app-specific functionality in other ways, too** — e.g., a Dock menu (Control-click Dock icon), which is always available while the app runs.

## Specs
- macOS menu bar height: **24 pt**.
- About item app name: prefer **16 characters or fewer**.

### iPadOS vs macOS menu bar
|  | iPadOS | macOS |
| --- | --- | --- |
| Menu bar visibility | Hidden until revealed | Visible by default |
| Horizontal alignment | Centered | Leading side |
| Menu bar extras | Not available | System default and custom |
| Window controls | In the menu bar when the app is full screen | Never in the menu bar |
| Apple menu | Not available | Always available |
| App menu | About, Services, and app visibility-related items not available | Always available |

### App menu (in order)
| Menu item | Action | Guidance |
| --- | --- | --- |
| About *YourAppName* | Shows About window (copyright, version info). | Prefer short name ≤16 characters. Don't include a version number. |
| Settings… | Opens settings window, or app's page in iPadOS Settings. | App-level settings only; document-specific settings go in File menu. |
| Optional app-specific items | Custom app-level setting/configuration actions. | List after Settings, within the same group. |
| Services (macOS only) | Submenu of system/other-app services for current context. | |
| Hide *YourAppName* (macOS only) | Hides app and its windows, activates most recently used app. | Use the same short app name as About. |
| Hide Others (macOS only) | Hides all other open apps and their windows. | |
| Show All (macOS only) | Shows all other apps' windows behind yours. | |
| Quit *YourAppName* | Quits. Option changes it to Quit and Keep Windows. | Use the same short app name as About. |

### File menu (in order)
| Menu item | Action | Guidance |
| --- | --- | --- |
| New *Item* | Creates new document, file, or window. | *Item* names the type created (Calendar: *Event*, *Calendar*). |
| Open | Opens selected item or presents a picker. | If a separate picker is needed, add ellipsis. |
| Open Recent | Submenu of recent documents; typically has *Clear Menu*. | Show recognizable document/file names, not paths; most recently opened first. |
| Close | Closes current window/document. Option → Close All. In tab-based window, Close Tab replaces Close. | In tab-based windows, consider a Close Window item to close entire window in one click/tap. |
| Close Tab | Closes current tab. Option → Close Other Tabs. | |
| Close File | Closes current file and all its windows. | Consider if app can open multiple views of the same file. |
| Save | Saves current document. | Autosave periodically. For new documents, prompt for name and location. For multiple formats, prefer a pop-up menu in the Save sheet. |
| Save All | Saves all open documents. | |
| Duplicate | Duplicates document, both stay open. Option → Save As. | Prefer Duplicate over Save As, Export, Copy To, Save To (these don't clarify relationship between files). |
| Rename… | Renames current document. | |
| Move To… | Prompts for a new location. | |
| Export As… | Prompts for name, location, format; current document stays open, exported file doesn't open. | Reserve for formats the app doesn't typically handle. |
| Revert To | With autosave: submenu of recent versions + version browser; chosen version replaces current document. | |
| Page Setup… | Panel for printing parameters (paper size, orientation); document can save them. | Include for document-specific print parameters. Global (printer name) or frequently changed (number of copies) params belong in the Print panel. |
| Print… | Opens standard Print panel (print, fax, save as PDF). | |

### Edit menu (top-level, in order)
| Menu item | Action | Guidance |
| --- | --- | --- |
| Undo | Reverses previous operation. | Clarify target, e.g., "Undo Paste and Match Style", "Undo Typing". |
| Redo | Reverses previous Undo. | Clarify target, e.g., "Redo Paste and Match Style", "Redo Typing". |
| Cut | Removes selection to Clipboard (replacing contents). | |
| Copy | Copies selection to Clipboard. | |
| Paste | Inserts Clipboard at insertion point; Clipboard unchanged (repeatable). | |
| Paste and Match Style | Pastes matching surrounding text style. | |
| Delete | Removes selection without Clipboard. | Use "Delete", not Erase or Clear — equivalent to the Delete key, so naming must be consistent. |
| Select All | Selects all selectable content. | |
| Find | Submenu: Find, Find and Replace, Find Next, Find Previous, Use Selection for Find, Jump to Selection. | |
| Spelling and Grammar | Submenu: Show Spelling and Grammar, Check Document Now, Check Spelling While Typing, Check Grammar With Spelling, Correct Spelling Automatically. | |
| Substitutions | Submenu: Show Substitutions, Smart Copy/Paste, Smart Quotes, Smart Dashes, Smart Links, Data Detectors, Text Replacement. | |
| Transformations | Submenu: Make Uppercase, Make Lowercase, Capitalize. | |
| Speech | Submenu: Start Speaking, Stop Speaking. | |
| Start Dictation | Opens dictation; system adds it automatically at bottom of Edit menu. | |
| Emoji & Symbols | Opens Character Viewer; system adds it automatically at bottom of Edit menu. | |

### Format menu (top-level, in order)
| Menu item | Action |
| --- | --- |
| Font | Submenu: Show Fonts, Bold, Italic, Underline, Bigger, Smaller, Show Colors, Copy Style, Paste Style. |
| Text | Submenu: Align Left, Align Center, Justify, Align Right, Writing Direction, Show Ruler, Copy Ruler, Paste Ruler. |

### View menu (top-level, in order)
| Menu item | Action |
| --- | --- |
| Show/Hide Tab Bar | Toggles tab bar above body area in tab-based window. |
| Show All Tabs/Exit Tab Overview | Enters/exits overview of all open tabs (like Mission Control). |
| Show/Hide Toolbar | Toggles toolbar visibility. |
| Customize Toolbar | Opens toolbar customization. |
| Show/Hide Sidebar | Toggles sidebar visibility. |
| Enter/Exit Full Screen | Opens window full-screen in a new space. |

### Window menu (top-level, in order)
| Menu item | Action | Guidance |
| --- | --- | --- |
| Minimize | Minimizes active window to Dock. Option → Minimize All. | |
| Zoom | Toggles between content-appropriate predefined size and user-set size. Option → Zoom All. | Avoid using Zoom to enter/exit full screen (View menu handles it). |
| Show Previous Tab | Shows previous tab. | |
| Show Next Tab | Shows next tab. | |
| Move Tab to New Window | Opens current tab in new window. | |
| Merge All Windows | Combines all windows into one tabbed window. | |
| Enter/Exit Full Screen | Opens window full-screen in new space. | Include here only if the app has no View menu; still keep separate Minimize and Zoom. |
| Bring All to Front | Brings all app windows to front keeping location/size/layering (same as clicking Dock icon). Option → Arrange in Front (tiled). | |
| *Name of open app-specific window* | Brings that window to front. | List open windows alphabetically. Avoid listing panels or other modal views. |

### Help menu
| Menu item | Action | Guidance |
| --- | --- | --- |
| Send *YourAppName* Feedback to Apple | Opens Feedback Assistant. | |
| *YourAppName* Help | With Help Book format, opens built-in Help Viewer. | |
| *Additional Item* | | Separator between primary help and additional items (registration, release notes). Keep total items small; alternatively link to them from help docs. |

## APIs
`CommandMenu` (SwiftUI), `MenuBarExtra` (SwiftUI), `NSStatusBar` (AppKit), `NSHelpManager` (AppKit), `NSMenuItem.isAlternate` (AppKit), UIKit menu bar via "Adding menus and shortcuts to the menu bar and user interface" (UIKit).

## Related
`menus, dock-menus, keyboards, icons, sf-symbols, settings, panels, popovers, status-bars, going-full-screen, offering-help, tab-bars, toolbars, sidebars`
