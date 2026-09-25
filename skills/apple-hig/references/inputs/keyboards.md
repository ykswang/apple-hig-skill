# Keyboards

> Source: https://developer.apple.com/design/human-interface-guidelines/keyboards · A physical keyboard can be an essential input device for entering text, playing games, controlling apps, and more.

## When to use / core idea
- Physical keyboards connect to every device except Apple Watch; Mac users use one constantly, iPad users often; many games work well with one; people may prefer it over a virtual keyboard for lots of text (see `virtual-keyboards`).
- *Keyboard shortcut* = primary key + one or more modifiers (Control, Option, Shift, Command) mapped to a command. In games, a *key binding* is often a single key (see `game-controls`).
- Apple's standard shortcuts work consistently across the system and most apps; apps may add custom shortcuts for their most-used app-specific commands.

## Rules
### Best practices
- **Support Full Keyboard Access when possible** — iOS, iPadOS, macOS, visionOS; navigate/activate windows, menus, controls, system features with only the keyboard. Test by enabling it in Settings › Accessibility (`isFullKeyboardAccessEnabled`).
- iPadOS: supports keyboard navigation in text fields, text views, sidebars (APIs for collection/custom views), but avoid supporting keyboard navigation for controls (buttons, segmented controls, switches); let Full Keyboard Access handle activating controls, reaching all components, and gesture interactions like drag and drop. See `focus-and-selection`.
- **Respect standard keyboard shortcuts** — for a frequent unique action, prefer a custom shortcut over repurposing a standard one. Games: people expect some standard shortcuts (Command–Q to quit) but also want to modify key bindings.

### Standard keyboard shortcuts
- **In general, don't repurpose standard keyboard shortcuts for custom actions** — only consider redefining one whose action makes no sense in your experience (e.g., an app without text editing may repurpose Command–I from Italic to Get Info).
- People expect the shortcuts in the Specs tables to perform the listed actions.

### Custom keyboard shortcuts
- **Define custom keyboard shortcuts for only the most frequently used app-specific commands** — too many makes the app seem hard to learn.
- **Use modifier keys in ways that people expect** — Command+drag moves items as a group; Shift+drag-resize constrains to aspect ratio; holding an arrow key moves the selection by the smallest app-defined unit until released.
- Some languages need modifiers to generate characters (French keyboard: Option-5 = "{"). Command is usually safe; avoid additional modifiers with characters not on all keyboards; if you must use a non-Command modifier, prefer using it only with alphabetic characters.
- **List modifier keys in the correct order** — always Control, Option, Shift, Command.
- **Avoid adding Shift to a shortcut that uses the upper character of a two-character key** — list the upper character: Help = Command-Question mark, not Shift-Command-Slash (Hide Status Bar = Command-Slash).
- **Let the system localize and mirror your keyboard shortcuts as needed** — system localizes primary and modifier keys for the connected keyboard and mirrors in right-to-left layouts. See `right-to-left`.
- **Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command** — e.g., don't use Shift-Command-Z for something unrelated to undo/redo.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS. Not supported: watchOS.

### visionOS
- Holding Command on a connected keyboard shows the shortcut interface: commands grouped in system menu categories (File, Edit, View), like menu bar menus on iPad/Mac, but all relevant categories in one view, listing only available commands that have shortcuts.
- **Write descriptive shortcut titles** — flat lists lose submenu-title context; each title must convey its action alone (`discoverabilityTitle`).
- **Recognize that people see an overlay when they use a physical keyboard with your visionOS app or game** — system shows a virtual keyboard overlay with typing completion and other controls.

## Specs
### Modifier keys
| Modifier key | Symbol | Recommended usage |
| --- | --- | --- |
| Command | ⌘ | Prefer the Command key as the main modifier key in a custom keyboard shortcut. |
| Shift | ⇧ | Prefer the Shift key as a secondary modifier that complements a related shortcut. |
| Option | ⌥ | Use the Option modifier sparingly for less-common commands or power features. |
| Control | ^ (⌃) | Avoid using the Control key as a modifier. The system uses Control in many systemwide features and shortcuts, like moving focus or capturing screenshots. |

Order when combining: Control, Option, Shift, Command.

### Standard keyboard shortcuts
| Primary key | Keyboard shortcut | Action |
| --- | --- | --- |
| Space | Command-Space | Show or hide the Spotlight search field. |
|  | Shift-Command-Space | Varies. |
|  | Option-Command-Space | Show the Spotlight search results window. |
|  | Control-Command-Space | Show the Special Characters window. |
| Tab | Shift-Tab | Navigate through controls in a reverse direction. |
|  | Command-Tab | Move forward to the next most recently used app in a list of open apps. |
|  | Shift-Command-Tab | Move backward through a list of open apps (sorted by recent use). |
|  | Control-Tab | Move focus to the next group of controls in a dialog or the next table (when Tab moves to the next cell). |
|  | Control-Shift-Tab | Move focus to the previous group of controls. |
| Esc | Esc | Cancel the current action or process. |
| Esc | Option-Command-Esc | Open the Force Quit dialog. |
| Eject | Control-Command-Eject | Quit all apps (after changes have been saved to open documents) and restart the computer. |
|  | Control-Option-Command-Eject | Quit all apps (after changes have been saved to open documents) and shut the computer down. |
| F1 | Control-F1 | Toggle full keyboard access on or off. |
| F2 | Control-F2 | Move focus to the menu bar. |
| F3 | Control- F3 | Move focus to the Dock. |
| F4 | Control-F4 | Move focus to the active (or next) window. |
|  | Control-Shift-F4 | Move focus to the previously active window. |
| F5 | Control-F5 | Move focus to the toolbar. |
|  | Command-F5 | Turn VoiceOver on or off. |
| F6 | Control-F6 | Move focus to the first (or next) panel. |
|  | Control-Shift-F6 | Move focus to the previous panel. |
| F7 | Control-F7 | Temporarily override the current keyboard access mode in windows and dialogs. |
| F8 |  | Varies. |
| F9 |  | Varies. |
| F10 |  | Varies. |
| F11 |  | Show desktop. |
| F12 |  | Hide or display Dashboard. |
| Grave accent (`) | Command-Grave accent | Activate the next open window in the frontmost app. |
|  | Shift-Command-Grave accent | Activate the previous open window in the frontmost app. |
|  | Option-Command-Grave accent | Move focus to the window drawer. |
| Hyphen (-) | Command-Hyphen | Decrease the size of the selection. |
|  | Option-Command-Hyphen | Zoom out when screen zooming is on. |
| Left bracket ({) | Command-Left bracket | Left-align a selection. |
| Right bracket (}) | Command-Right bracket | Right-align a selection. |
| Pipe (\|) | Command-Pipe | Center-align a selection. |
| Colon (:) | Command-Colon | Display the Spelling window. |
| Semicolon (;) | Command-Semicolon | Find misspelled words in the document. |
| Comma (,) | Command-Comma | Open the app’s settings window. |
|  | Control-Option-Command-Comma | Decrease screen contrast. |
| Period (.) | Command-Period | Cancel an operation. |
|  | Control-Option-Command-Period | Increase screen contrast. |
| Question mark (?) | Command-Question mark | Open the app’s Help menu. |
| Forward slash (/) | Option-Command-Forward slash | Turn font smoothing on or off. |
| Equal sign (=) | Shift-Command-Equal sign | Increase the size of the selection. |
|  | Option-Command-Equal sign | Zoom in when screen zooming is on. |
| 3 | Shift-Command-3 | Capture the screen to a file. |
|  | Control-Shift-Command-3 | Capture the screen to the Clipboard. |
| 4 | Shift-Command-4 | Capture a selection to a file. |
|  | Control-Shift-Command-4 | Capture a selection to the Clipboard. |
| 8 | Option-Command-8 | Turn screen zooming on or off. |
|  | Control-Option-Command-8 | Invert the screen colors. |
| A | Command-A | Select every item in a document or window, or all characters in a text field. |
|  | Shift-Command-A | Deselect all selections or characters. |
| B | Command-B | Boldface the selected text or toggle boldfaced text on and off. |
| C | Command-C | Copy the selection to the Clipboard. |
|  | Shift-Command-C | Display the Colors window. |
|  | Option-Command-C | Copy the style of the selected text. |
|  | Control-Command-C | Copy the formatting settings of the selection and store on the Clipboard. |
| D | Option-Command-D | Show or hide the Dock. |
|  | Control-Command-D | Display the definition of the selected word in the Dictionary app. |
| E | Command-E | Use the selection for a find operation. |
| F | Command-F | Open a Find window. |
|  | Option-Command-F | Jump to the search field control. |
|  | Control-Command-F | Enter full screen. |
| G | Command-G | Find the next occurrence of the selection. |
|  | Shift-Command-G | Find the previous occurrence of the selection. |
| H | Command-H | Hide the windows of the currently running app. |
|  | Option-Command-H | Hide the windows of all other running apps. |
| I | Command-I | Italicize the selected text or toggle italic text on or off. |
|  | Command-I | Display an Info window. |
|  | Option-Command-I | Display an inspector window. |
| J | Command-J | Scroll to a selection. |
| M | Command-M | Minimize the active window to the Dock. |
|  | Option-Command-M | Minimize all windows of the active app to the Dock. |
| N | Command-N | Open a new document. |
| O | Command-O | Display a dialog for choosing a document to open. |
| P | Command-P | Display the Print dialog. |
|  | Shift-Command-P | Display the Page Setup dialog. |
| Q | Command-Q | Quit the app. |
|  | Shift-Command-Q | Log out the person currently logged in. |
|  | Option-Shift-Command-Q | Log out the person currently logged in without confirmation. |
| S | Command-S | Save a new document or save a version of a document. |
|  | Shift-Command-S | Duplicate the active document or initiate a Save As. |
| T | Command-T | Display the Fonts window. |
|  | Option-Command-T | Show or hide a toolbar. |
| U | Command-U | Underline the selected text or turn underlining on or off. |
| V | Command-V | Paste the Clipboard contents at the insertion point. |
|  | Shift-Command-V | Paste as (Paste as Quotation, for example). |
|  | Option-Command-V | Apply the style of one object to the selection. |
|  | Option-Shift-Command-V | Paste the Clipboard contents at the insertion point and apply the style of the surrounding text to the inserted object. |
|  | Control-Command-V | Apply formatting settings to the selection. |
| W | Command-W | Close the active window. |
|  | Shift-Command-W | Close a file and its associated windows. |
|  | Option-Command-W | Close all windows in the app. |
| X | Command-X | Remove the selection and store on the Clipboard. |
| Z | Command-Z | Undo the previous operation. |
|  | Shift-Command-Z | Redo (when Undo and Redo are separate commands rather than toggled using Command-Z). |
| Right arrow | Command-Right arrow | Change the keyboard layout to current layout of Roman script. |
|  | Shift-Command-Right arrow | Extend selection to the next semantic unit, typically the end of the current line. |
|  | Shift-Right arrow | Extend selection one character to the right. |
|  | Option-Shift-Right arrow | Extend selection to the end of the current word, then to the end of the next word. |
|  | Control-Right arrow | Move focus to another value or cell within a view, such as a table. |
| Left arrow | Command-Left arrow | Change the keyboard layout to current layout of system script. |
|  | Shift-Command-Left arrow | Extend selection to the previous semantic unit, typically the beginning of the current line. |
|  | Shift-Left arrow | Extend selection one character to the left. |
|  | Option-Shift-Left arrow | Extend selection to the beginning of the current word, then to the beginning of the previous word. |
|  | Control-Left arrow | Move focus to another value or cell within a view, such as a table. |
| Up arrow | Shift-Command-Up arrow | Extend selection upward in the next semantic unit, typically the beginning of the document. |
|  | Shift-Up arrow | Extend selection to the line above, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Up arrow | Extend selection to the beginning of the current paragraph, then to the beginning of the next paragraph. |
|  | Control-Up arrow | Move focus to another value or cell within a view, such as a table. |
| Down arrow | Shift-Command-Down arrow | Extend selection downward in the next semantic unit, typically the end of the document. |
|  | Shift-Down arrow | Extend selection to the line below, to the nearest character boundary at the same horizontal location. |
|  | Option-Shift-Down arrow | Extend selection to the end of the current paragraph, then to the end of the next paragraph (include the paragraph terminator, such as Return, in cut, copy, and paste operations). |
|  | Control-Down arrow | Move focus to another value or cell within a view, such as a table. |

### Input source / localization shortcuts
Defined for localized system versions, keyboards, layouts, and input methods; these don't correspond directly to menu commands.

| Keyboard shortcut | Action |
| --- | --- |
| Control-Space | Toggle between the current and last input source. |
| Control-Option-Space | Switch to the next input source in the list. |
| [Modifier key]-Command-Space | Varies. |
| Command-Right arrow | Change keyboard layout to current layout of Roman script. |
| Command-Left arrow | Change keyboard layout to current layout of system script. |

## APIs
`isFullKeyboardAccessEnabled` (AppKit), `Focus-based navigation` (UIKit), `discoverabilityTitle` (UIKit), `KeyboardShortcut` (SwiftUI), `Input events` (SwiftUI), `Handling key presses made on a physical keyboard` (UIKit), `Mouse, Keyboard, and Trackpad` (AppKit)

## Related
`virtual-keyboards, entering-data, pointing-devices, game-controls, focus-and-selection, the-menu-bar, right-to-left, accessibility`
