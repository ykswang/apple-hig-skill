# Menus

> Source: https://developer.apple.com/design/human-interface-guidelines/menus · A menu reveals its options when people interact with it, a space-efficient way to present commands in an app or game.

## When to use / core idea
- Opening a menu reveals *menu items*, each a command, option, or state affecting the current selection or context. Labeling and organization guidance here applies to all menu types.
- Specialized menus: pop-up-buttons and pull-down-buttons (options related to the button's action), context-menus (few frequent actions for the current view/task), the-menu-bar (macOS/iPadOS: all app commands).

## Rules

### Labels
- A label describes what the item does and may include a symbol if it clarifies meaning. App menu items can show the associated keyboard command; game menu items rarely do (wider input range, game-specific key mappings).
- Note: iOS, iPadOS, visionOS apps can show a few unlabeled symbol/icon-only items depending on layout.
- **For each menu item, write a label that clearly and succinctly describes it** — action items: a verb or verb phrase (View, Close, Select). Let the app's communication style guide tone. (Show/hide or state items: see Toggled items.)
- **To be consistent with platform experiences, use title-style capitalization** — capitalize every word except articles, coordinating conjunctions, and short prepositions; always capitalize the last word. Games may differ but generally prefer it.
- **Remove articles like *a*, *an*, and *the* from labels to save space** — e.g., "View Settings," not "View the Settings."
- **Show people when a menu item is unavailable** — typically dimmed and non-responsive. If all items are unavailable, the menu itself remains available so people can open it and learn its commands.
- **Append an ellipsis (…) to a label when the action requires more information before it can complete** — signals input or additional choices, typically in another view.

### Icons
- **Represent common actions consistently** — use standard icons for Share, Print, Search, etc. (icons › Standard icons).
- **Use menu item icons sparingly and with purpose** — to highlight the most common actions and key features, file system locations, connected devices, visual concepts (rotate/flip image), and user-generated content (folders, documents). Don't display an icon if none clearly represents the item (e.g., no arbitrary icons for days of the week).
- **Apply a uniform visual treatment across menu items in the same group** — icons for all items in a group, or none.

### Organization
- **Prefer listing important or frequently used menu items first** — people scan from the top.
- **Consider grouping logically related items** — e.g., Copy/Cut/Paste; Look Up/Look Down/Look Left. Separate groups with a *separator* (horizontal line or short gap depending on platform/menu type).
- **Prefer keeping all logically related commands in the same group, even if not equally important** — e.g., Paste and Match Style stays with Copy, Cut, Paste.
- **Be mindful of menu length** — long menus take time and attention; consider dividing into separate menus or using a submenu (e.g., difficulty levels under New Game). Exception: user-defined or dynamically generated content (Safari History, Bookmarks) — long menus and scrolling are fine.

### Submenus
- A *submenu* is a subordinate list of closely related items, indicated by a symbol such as a chevron after the item's label; functionally identical to menus.
- **Use submenus sparingly** — each adds complexity and hides items. Consider one when a term appears in more than two items in the same group (e.g., Sort by Date/Score/Time → "Sort by" submenu with Date, Score, Time); use the repeated term in the item label.
- **Limit the depth and length of submenus** — generally a single level; if a submenu has more than about **five items**, consider a new menu.
- **Make sure a submenu remains available even when its nested items are unavailable** — people can still open it to learn its commands.
- **Prefer using a submenu to indenting menu items** — indentation is inconsistent with the system and unclear.

### Toggled items
- A single toggled item can communicate current state and let people change it instead of listing one item per state.
- **Consider using a changeable label that describes an item's current state** — e.g., one item switching Show Map ↔ Hide Map.
- **Include a verb if a changeable label isn't clear enough** — e.g., "HDR On/Off" is ambiguous; use "Turn HDR On/Turn HDR Off."
- **If necessary, display both menu items instead of one toggled item** — e.g., Take Account Online and Take Account Offline, with only the applicable one available.
- **Consider using a checkmark to show that an attribute is currently in effect** — e.g., Format > Font styles.
- **Consider offering a menu item that removes multiple toggled attributes at once** — e.g., Plain removes all formatting.

### In-game menus
- Control gameplay and set game-wide settings.
- **Let players navigate in-game menus using the platform's default interaction method** — touch in iOS/iPadOS; direct and indirect gestures in visionOS.
- **Make sure menus remain easy to open and read on all supported platforms** — scaling to smaller (especially mobile) screens can make menus too small; modify tap target sizes and consider alternative ways to communicate content (see typography, game-controls › Touch controls).

## Platform considerations
No additional considerations: macOS, tvOS, watchOS.

### iOS, iPadOS
- Three menu layouts (`preferredElementSize`):
  - **Small** — top row of **four** items showing symbol/icon only (no label), above a list of remaining items.
  - **Medium** — top row of **three** items showing symbol/icon above a short label, above a list of remaining items.
  - **Large (default)** — all items in a list.
- **Choose a small or medium layout when it can help streamline choices** — medium for three important, frequent actions (e.g., Notes: Scan, Lock, Pin); small only for closely related actions typically grouped (Bold, Italic, Underline, Strikethrough), each with a recognizable symbol that works without a label.

### visionOS
- Menus can use the iOS/iPadOS small or large layouts. Menus can be presented from 3D content via a SwiftUI view; apply a breakthrough effect so the menu stays visible when other content occludes it. As in macOS, an open menu can extend outside the window's bounds.
- **Prefer displaying a menu near the content it controls** — people look at an item before tapping and may miss its effect if content is far away.
- **Prefer the subtle breakthrough effect in most cases** — blends with surroundings, preserving legibility, depth, and context. `automatic` applies `subtle` when a menu overlaps 3D content. `prominent` shows the menu over the entire scene but can disrupt and potentially cause discomfort. `none` fully occludes the menu behind 3D content (e.g., puzzle game with barriers) but may make it hard to see and access.

## Specs
- Submenu depth: generally 1 level; consider a new menu if a submenu exceeds about 5 items.
- Submenu trigger heuristic: a term repeated in more than two items in a group.
- iOS/iPadOS layouts: Small = 4 icon-only items in top row; Medium = 3 icon+label items in top row; Large = full list (default).

## APIs
`preferredElementSize` (UIKit), `breakthrough effect` (SwiftUI), `automatic` (SwiftUI), `subtle` (SwiftUI), `prominent` (SwiftUI), `none` (SwiftUI), `Menu` (SwiftUI), `Menus and shortcuts` (UIKit), `Menus` (AppKit)

## Related
pop-up-buttons, pull-down-buttons, context-menus, the-menu-bar, edit-menus, icons, settings, typography, game-controls, designing-for-games
