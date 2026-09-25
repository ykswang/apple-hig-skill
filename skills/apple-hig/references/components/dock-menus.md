# Dock menus

> Source: https://developer.apple.com/design/human-interface-guidelines/dock-menus · On a Mac, secondary-clicking an app's or game's Dock icon reveals a Dock menu with system-provided and custom items.

## When to use / core idea
- System-provided items vary depending on whether the app is open (e.g., Safari: view a current window, create a new window).
- iOS/iPadOS don't support Dock menus; the analog is home-screen-quick-actions (long press an icon on the Home Screen or in the Dock).
- As with all menus, label items succinctly and organize them logically (see menus).

## Rules
### Best practices
- **Make custom Dock menu items available in other places, too** — not everyone uses the Dock menu; offer the same commands in menu bar menus or the interface.
- **Prefer high-value custom items** — e.g., list all currently or recently open windows; consider a few actions most useful when the app isn't frontmost or has no open windows (Mail: Get New Mail, compose new message, plus open windows).

## Platform considerations
Not supported: iOS, iPadOS, tvOS, visionOS, watchOS (macOS only).

## APIs
`applicationDockMenu(_:)` (AppKit)

## Related
menus, home-screen-quick-actions, the-menu-bar
