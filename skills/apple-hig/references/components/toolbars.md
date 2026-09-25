# Toolbars

> Source: https://developer.apple.com/design/human-interface-guidelines/toolbars · A toolbar provides convenient access to frequently used commands, controls, navigation, and search.

## When to use / core idea
- One or more sets of controls arranged horizontally along the top or bottom edge of a view, grouped into logical sections.
- Acts on content in the view, facilitates navigation, orients people. Three content types: title of current view; navigation controls (back/forward, search fields); actions/bar items (buttons, menus).
- Use a **tab bar** instead when navigating between areas of an app. In iOS a navigation-specific toolbar is sometimes called a navigation bar.

## Rules
### Best practices
- **Choose items deliberately to avoid overcrowding** — each item must be distinguishable and activatable. Define which items move to the overflow menu as width shrinks.
- System automatically adds an overflow menu in macOS/iPadOS when items don't fit. Don't add an overflow menu manually; avoid layouts that overflow by default.
- **Add a More menu to contain additional actions** — put less important actions there; try to fit all actions in the toolbar first and add the More menu only if really needed.
- **In iPadOS and macOS apps, consider letting people customize the toolbar to include their most common items** — especially for apps with many items, advanced functionality not everyone needs, or long usage sessions (e.g., a range of editing actions).
- **Reduce the use of toolbar backgrounds and tinted controls** — custom backgrounds can interfere with system background effects. Let the content layer inform toolbar color/appearance; use `ScrollEdgeEffectStyle` when needed to distinguish toolbar from content.
- **Avoid applying a similar color to toolbar item labels and content layer backgrounds** — if content is already bright/colorful, prefer the default monochromatic toolbar appearance (see color › Liquid Glass color).
- **Prefer using standard components in a toolbar** — standard buttons, text fields, headers, footers have corner radii concentric with bar corners; custom components must also be concentric.
- **Consider temporarily hiding toolbars for a distraction-free experience** — do it contextually and offer reliable ways to restore hidden elements (see going-full-screen; visionOS: immersive-experiences).

### Titles
- **Provide a useful title for each window** — confirms location and differentiates multiple open windows. If a title is redundant you can leave the title area empty (e.g., Notes with one window; separate note windows get titled with the first line of content).
- **Don't title windows with your app name** — it conveys nothing about content hierarchy or the window/area.
- **Write a concise title** — a word or short phrase distilling the window's purpose; keep it **under 15 characters** to leave room for controls.

### Navigation
- Navigation toolbar appears at the top of a window to move through a content hierarchy; often includes a search field.
- **Use the standard Back and Close buttons** — Back retraces hierarchy; Close closes a modal view. Prefer the standard symbols; don't use a text label saying *Back* or *Close*. Custom versions must look the same, behave as expected, match your interface, and be consistent throughout the app.

### Actions
- **Provide actions that support the main tasks people perform** — prioritize most-wanted commands (often most frequent, or those mapping to the highest-level/most important objects).
- **Make sure the meaning of each control is clear** — no guessing. Prefer simple, recognizable symbols over text, except for actions like *edit* not well represented by symbols (see icons › Standard icons).
- **Prefer system-provided symbols without borders** — familiar, auto coloring/vibrancy, consistent interaction. Borders (e.g., outlined circle symbols) are unnecessary: the section is a visible container and the system defines hover/selection states.
- **Use the `.prominent` style for key actions such as Done or Submit** — separates and tints for a clear focal point. Specify only one primary action, on the trailing side.

### Item groupings
- Three locations:
  - **Leading edge** — back / show-hide sidebar at far leading edge, then view title; next to title an optional document menu (Duplicate, Rename, Move, Export…). Leading items aren't customizable (always available).
  - **Center area** — common controls; title may appear here if not leading. In macOS/iPadOS, customizable (add/remove/rearrange) and auto-collapse into the system overflow menu as the window shrinks.
  - **Trailing edge** — important always-available items, inspector buttons, optional search field, More menu (holds extra items, supports customization), primary action like Done. Remains visible at all window sizes.
- Pin items to leading/center/trailing and insert space between items where appropriate.
- **Group toolbar items logically by function and frequency of use** — e.g., Keynote: presentation-level, playback, object insertion sections.
- **Group navigation controls and critical actions like Done, Close, or Save in dedicated, familiar, and visually distinct sections** — e.g., back/forward on leading edge, tools + More on trailing edge (not all in one trailing group).
- **Keep consistent groupings and placement across platforms.**
- **Minimize the number of groups** — too many feel cluttered even on iPad/Mac; aim for a **maximum of three**.
- **Keep actions with text labels separate** — a text-labeled action next to a symbol action can look like one combined action; multiple text buttons can run together. Insert fixed space between them (`UIBarButtonItem.SystemItem.fixedSpace`).

## Platform considerations
No additional considerations: tvOS.

### iOS
- **Prioritize only the most important items for inclusion in the main toolbar area** — space is very limited; put the rest in a More menu.
- **Use a large title to help people stay oriented as they navigate and scroll** — large title transitions to standard when scrolling begins and back to large at the top (`prefersLargeTitles`).

### iPadOS
- **Consider combining a toolbar with a tab bar** — they can share the same horizontal space at the top, useful for navigating a few main areas while keeping full width for content (see layout, windows).

### macOS
- Toolbar sits in the window frame at the top, below or integrated with the title bar. Window titles can display inline with controls; toolbar items don't include a bezel.
- **Make every toolbar item available as a command in the menu bar** — people can customize or hide the toolbar, so it can't be the only place for a command. Conversely, don't give every menu item a toolbar item.

### visionOS
- System toolbar appears along the bottom edge of a window, above window-management controls, in a parallel plane slightly in front of the window on the z-axis.
- Uses a variable blur in the bar background to keep items legible over scrolling content while glass stays uniform.
- Each item may use a symbol or a text label; looking at a symbol item reveals its text label.
- **Prefer using a system-provided toolbar** — familiar, optimized for eye and hand input, auto-positioned relative to the window.
- **Avoid creating a vertical toolbar** — tab bars are vertical in visionOS; a vertical toolbar would confuse.
- **Try to prevent windows from resizing below the width of the toolbar** — no menu bar in visionOS, so the toolbar must reliably expose essential controls at any size.
- **If your app can enter a modal state, consider offering contextually relevant toolbar controls** — e.g., multistep photo editing; reinstate standard toolbar controls on exit.
- **Avoid using a pull-down menu in a toolbar** — hard to discover, clutters, and at the bottom edge may obscure window controls below it (see pull-down-buttons).

### watchOS
- Toolbar buttons can go in the top corners or along the bottom; above scrolling content they stay visible as content scrolls under them (`topBarLeading`, `topBarTrailing`, `bottomBar`).
- A button can also be placed in the scrolling view; hidden by default until people scroll up (people scroll to top frequently, so discovery is automatic) (`primaryAction`).
- **Use a scrolling toolbar button for an important action that isn't a primary app function** — e.g., Mail's New Message at the top of the Inbox list.

## Specs
- Window/toolbar title: under **15 characters**.
- Toolbar groups: maximum of **three** (general aim).
- Primary (`.prominent`) actions: **one**, trailing side.

## APIs
Toolbars (SwiftUI), `ToolbarItemPlacement.topBarLeading` / `.topBarTrailing` / `.bottomBar` / `.primaryAction` (SwiftUI), `ScrollEdgeEffectStyle` (SwiftUI), `UIToolbar` (UIKit), `UINavigationBar.prefersLargeTitles` (UIKit), `UIBarButtonItem.SystemItem.fixedSpace` (UIKit), `NSToolbar` (AppKit).

## Related
`sidebars, tab-bars, layout, buttons, search-fields, menus, icons, sf-symbols, color, going-full-screen, immersive-experiences, pull-down-buttons, windows, the-menu-bar`
