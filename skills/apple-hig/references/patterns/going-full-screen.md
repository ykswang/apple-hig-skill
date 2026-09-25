# Going full screen

> Source: https://developer.apple.com/design/human-interface-guidelines/going-full-screen · iPhone, iPad, and Mac full-screen modes expand a window to fill the screen, hiding system controls for a distraction-free environment.

## When to use / core idea
- Offer full screen for games, media viewing (videos, photo slideshows), or in-depth tasks that benefit from no distractions.
- Apple TV and Apple Watch have no full-screen mode (apps already fill the screen). Apple Vision Pro has none: people enlarge windows or use the Digital Crown to hide passthrough for immersion (see `immersive-experiences`).

## Rules
### Best practices
- **Support full-screen mode when it makes sense for your experience** — people want it to concentrate or be immersed; consider it for games, media, in-depth tasks.
- **If necessary, adjust your layout in full-screen mode, but don't programmatically resize your window** — keep essential content prominent and use extra space (e.g. adjust proportions without changing which items appear); keep adjustments subtle to stay consistent and avoid jarring transitions.
- **Continue to provide access to essential features and controls so people can complete their task without exiting full-screen mode** — e.g. media playback controls persistently available or easy to reveal.
- **Except in games, let people reveal the Dock while your iPadOS or macOS app is in full-screen mode** — preserve quick access to other apps. In games, you can ask iPadOS to ignore an initial swipe up from the bottom edge, or hide the Dock entirely in macOS.
- **After people switch away from your full-screen experience, help them resume where they left off when they return** — e.g. auto-pause a game or slideshow when people leave.
- **Let people choose when to exit full-screen mode** — don't end it automatically on switching experiences or finishing an activity (game, movie).
- **Prioritize content by temporarily hiding toolbars and navigation controls** — when content is primary (full-screen photos, reading); let people restore them with a familiar gesture/action (tap, swipe down, move cursor to top of screen); keep controls visible when essential for navigation or tasks. visionOS windows can hide toolbars, but people expect different immersive experiences there (see `immersive-experiences`).

## Platform considerations
Not supported: tvOS, visionOS, watchOS.
### iOS, iPadOS
- **Consider deferring system gestures to prevent accidental exits in a full-screen app or game** — by default the Home Screen indicator auto-hides shortly after switching to your app and reappears on interaction with the bottom of the screen, allowing one swipe to exit; retain this whenever possible. If it causes unexpected exits, you can require two swipes instead of one.
### macOS
- **Use the system-provided full-screen experience** — works in all contexts, e.g. automatically accommodates the camera housing at the top-center of some Mac screens.
- **In a game, don't change the display mode when players go full screen** — people expect control of display mode, and changing it doesn't improve performance.
- **Always let people choose when to enter full-screen mode** — prefer the window's Enter Full Screen button, View menu item, or Control-Command-F; avoid a custom menu of window modes. Games may also provide a custom `toggles` to switch full screen on/off.

## APIs
`preferredScreenEdgesDeferringSystemGestures` (SwiftUI), `preferredScreenEdgesDeferringSystemGestures` (UIKit), `hideDock` (AppKit), `toggleFullScreen(_:)` (AppKit), `Managing your game window for Metal in macOS` (metal), `fullScreenCover(item:onDismiss:content:)` (SwiftUI), `NSScreen` (AppKit), `NSWindow.CollectionBehavior` (AppKit)

## Related
`layout, multitasking, windows, the-menu-bar, immersive-experiences, toggles`
