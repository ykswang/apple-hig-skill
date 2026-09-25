# Layout

> Source: https://developer.apple.com/design/human-interface-guidelines/layout · A consistent layout that adapts across display sizes, orientations, and multitasking configurations helps people understand and enjoy your app or game on all their devices.

## When to use / core idea
- Layout gives structure from the moment an app opens; familiar control/content relationships let people discover features immediately and feel at home on each platform.
- Use SwiftUI or Auto Layout so the interface adapts to system-defined environment characteristics (iOS, iPadOS, tvOS, visionOS).
- Apple Design Resources provides templates and layout guides for all platforms.
- For 3D/spatial placement in visionOS see spatial-layout; for RTL mirroring see right-to-left.

## Rules

### Visual hierarchy
- **Order content by relative importance** — people scan in reading order (top to bottom, leading to trailing); put most important items near the top and leading side. For RTL, prefer standard system components that adapt automatically.
- **Align elements to make them easier to scan, and use indentation to convey hierarchy** — aligned items read as related; indented items read as subordinate to the item they follow.
- **Group related items to clearly express related information or functions** — use negative space, container shapes, or separator lines.
- **Use progressive disclosure to make layouts cleaner and easier to interact with** — disclosure triangles, menus, or nested views reduce initial content; scrollable sections showcase more content (especially media apps: video, music, books).
- **Differentiate controls from content** — use Liquid Glass for controls on platforms that support it. Instead of a solid or semi-opaque background beneath controls, use a scroll edge effect to elevate controls above content (see scroll-views). Extend full-screen background content underneath sidebars, toolbars, and tab bars to fill the entire screen or window.
  - If full-bleed background art gets covered by sidebars/inspectors, use a background extension effect (flips and blurs the image, mirroring it beneath adjacent components).

### Adaptability
- Common characteristics to handle: regular/compact horizontal and vertical size classes; different screen sizes; orientations and aspect ratios; system features like the Dynamic Island; external displays, Display Zoom, resizable windows on iPad and Mac; text-size changes; locale features (LTR/RTL direction, date/time/number formatting, font variation, text length).
- **Design a layout that adapts gracefully and consistently** — stay familiar across rotation, window resizing, added displays, device switches. Respect system-defined safe areas, margins, and guides; use layout modifiers to fine-tune. Even orientation-locked apps (e.g., landscape-only games) must resize well across devices and window sizes.
- **Be prepared for text-size changes** — support Dynamic Type: horizontally adjacent views may need to stack vertically; rows/containers must grow so text isn't cropped or overlapping; single-line rows may need to grow to multiple lines. Unity games: use Apple's accessibility plug-in.
- **Preview your app on multiple devices, using different size classes, localizations, and text sizes** — test the largest and smallest layouts first; use Device Hub simulated devices to check clipping (e.g., iPad resizing, iPhone Mirroring on Mac).
- **When necessary, scale background artwork in response to display changes** — don't change the artwork's aspect ratio; scale it to fill the screen completely (avoid cropping/letterboxing/pillarboxing artifacts). Very wide/short or tall/narrow windows mean background art often must extend beyond the typical visible area.

### Size classes (iOS, iPadOS)
- Each dimension is *compact* or *regular*: horizontal = narrow (compact) vs. wide (regular); vertical = short (compact) vs. tall (regular).
- System sets size classes from device type, window configuration, and multitasking state (full screen, Slide Over, mirrored from iPhone to Mac). Apps can be in every combination.
- **Determine layout based on size classes, not device type or orientation** — orientation and idiom don't tell you available space. Size classes also cover freely resized windows (iPhone Mirroring on macOS, iPad multitasking, iPad apps on macOS).
- **Consider all possible combinations of size classes** — e.g., a layout designed only for iPhone landscape (regular width, compact height) may waste vertical space on iPad landscape at regular height; designing only for compact portrait may leave extra space at regular width.
- **Keep functionality the same as size classes change, and keep layout changes recognizable and familiar to the platform** — don't change functionality based on space; you may change how much is visible (e.g., switch tab bar → sidebar, expose items otherwise in an overflow menu). The idiom stays the same when resizing — keep the layout familiar to that platform.

### Guides and safe areas
- *Layout guide*: rectangular region for positioning, aligning, and spacing content; system guides apply standard margins and restrict text width for readability; custom guides allowed.
- *Safe area*: region of a window not covered at the edge by hardware features or other views (toolbar, tab bar, status bar). Respecting it is essential so system UI and hardware (e.g., Dynamic Island) don't obstruct content and controls.

## Platform considerations
No additional considerations: iOS, iPadOS.

### macOS
- **Avoid placing controls or critical information at the bottom of a window** — people often move windows so the bottom edge is below the screen.
- **Avoid displaying content behind the camera housing at the top edge of the window** (`NSPrefersDisplaySafeAreaCompatibilityMode`).

### tvOS
- **Adhere to the screen's safe area** — inset primary content 60 pt from top and bottom, 80 pt from the sides, so content is visible regardless of TV compatibility settings or overscan.
- **Include appropriate padding between focusable elements** — focused elements grow (UIKit focus APIs); ensure focused elements don't overlap important information.
- Grids: use appropriate spacing between unfocused rows/columns to prevent overlap on focus. `UICollectionViewFlowLayout` auto-determines column count from content width and spacing.
- **Include additional vertical spacing for titled rows** — space between the bottom of the previous unfocused row and the center of the title, and between the bottom of the title and the top of the row's unfocused items.
- **Use consistent spacing** — inconsistent spacing stops looking like a grid and is harder to scan.
- **Make partially hidden content look symmetrical** — keep partially offscreen content the same width on each side of the screen.

### visionOS
- Content can live in a window, a bounded 3D volume, or an immersive space; this guidance covers windows/volumes (see spatial-layout, windows).
- **In general, support resizing** — resizing is standard (as in macOS, iPadOS); layout must adapt; prefer keeping content horizontally centered at very large sizes. You may set min/max sizes for windows, volumes, and attached UI (ornaments) to prevent overlap when small and unwieldiness when large, but don't use them to prevent resizing (e.g., Safari's navigation-bar ornament has a fixed max size).
- **Use 3D content sparingly in windows** — windows can show 3D at a fixed depth; reserve for meaningful moments alongside 2D (e.g., inline rocket model). Inset inline 3D within the window so it doesn't collide with content/controls or poke unpredictably outside the edge. For larger models or mostly-3D views, consider a volume or immersive space.
- **Display supplemental content in an adjacent window, not in an ornament** — ornaments are for app-specific interactive controls (toolbars, playback controls); open a new window next to the current one (`defaultWindowPlacement(_:)`).
- **Include enough space around controls for them to be easy to interact with** — keep controls identifiable and prevent the hover effect from obscuring content; e.g., place button centers at least 60 pt apart.

### watchOS
- **Avoid placing more than two or three controls side by side in your interface** — at most three glyph buttons or two text buttons per row. Full-width text buttons are usually better; two side-by-side short-text buttons work if the screen doesn't scroll.
- **Support autorotation in views people might want to show others** — e.g., showing an image to a friend or a QR code to a reader, instead of sleeping the display on wrist flip (`isAutorotating`).

## Specs

### tvOS safe area
| Edge | Inset |
| --- | --- |
| Top | 60 pt |
| Bottom | 60 pt |
| Leading / trailing sides | 80 pt |

### tvOS grids
| Columns | Unfocused content width | Horizontal spacing | Minimum vertical spacing |
| --- | --- | --- | --- |
| 2 | 860 pt | 40 pt | 100 pt |
| 3 | 560 pt | 40 pt | 100 pt |
| 4 | 410 pt | 40 pt | 100 pt |
| 5 | 320 pt | 40 pt | 100 pt |
| 6 | 260 pt | 40 pt | 100 pt |
| 7 | 217 pt | 40 pt | 100 pt |
| 8 | 184 pt | 40 pt | 100 pt |
| 9 | 160 pt | 40 pt | 100 pt |

### Other values
- visionOS: button centers at least 60 pt apart.
- watchOS: max 3 glyph buttons or 2 text buttons in a row.

Note: the current HIG no longer publishes per-device screen-size tables here; lay out by size class and safe-area layout guides instead. (Widget and Live Activity pages still list per-device dimensions.)

## APIs
`backgroundExtensionEffect()` (SwiftUI), `UIBackgroundExtensionView` (UIKit), `UITraitChangeObservable` (UIKit), `UserInterfaceSizeClass` (SwiftUI), `UILayoutGuide` (UIKit), `NSLayoutGuide` (AppKit), `SafeAreaRegions` (SwiftUI), Positioning content relative to the safe area (UIKit), `NSPrefersDisplaySafeAreaCompatibilityMode` (Info.plist), About focus interactions for Apple TV (UIKit), `UICollectionViewFlowLayout` (UIKit), `defaultWindowPlacement(_:)` (SwiftUI), Positioning and sizing windows (visionOS), `isAutorotating` (WatchKit), Composing custom layouts with SwiftUI (SwiftUI), Device Hub (Xcode), Apple.Accessibility Unity plug-in

## Related
right-to-left, spatial-layout, layout-and-organization, typography, scroll-views, materials, windows, multitasking, tab-bars, sidebars, ornaments, eyes, buttons
