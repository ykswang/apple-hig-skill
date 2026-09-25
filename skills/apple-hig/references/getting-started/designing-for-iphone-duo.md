# Designing for iPhone Duo

> Source: https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo · An app designed for iPhone Duo adapts seamlessly to both displays, providing a continuous experience as the device opens and closes.

## Device characteristics / core idea
- Two displays (inner and outer), each with its own front-facing camera; a center hinge lets people open/close the device and supports many holds and positions. Adaptable layout is more important than ever.
- Apps using standard system components and designed to support resizing adapt to poses automatically with little adjustment.
- It's still iPhone — designing-for-ios patterns and best practices still apply.

### Anatomy
- **Outer display** — used when closed. System places toolbars and tab bars on the side to maximize vertical content space. Controls stay on the side when the device opens in landscape, for consistency between displays.
- **Hinge** — supports a range of poses; reduces space available to content as the device folds.
- **Outer front-facing camera** — in the corner, always visible, vertically aligned with side controls.
- **Inner camera** — behind the display; hidden until the camera is active.

### Device poses
- Partially folded like a book, placed on a surface, standing on its edges (six poses illustrated).
- Don't design a custom layout per pose — use size classes: **compact width for the outer display, regular width for the inner display** covers every pose. Don't reinvent the app when it resizes; let the existing layout expand to available space.
- Preview/test poses with Device Hub in Xcode.

## Rules

### Best practices
- **Build your app to resize** — two displays, many poses, and Split View multitasking mean many sizes. Use size classes, layout margins, safe area insets. Avoid fixed widths and display-specific dependencies.
- **Create a consistent experience across displays** — keep functionality and element state the same. Maintain the information hierarchy, but show an additional level on the larger inner display if it makes sense (e.g., Mail closed: list *or* email; open: both side by side).
- **Maintain the same functionality across device poses** — controls may overflow and content may move/resize, but provide access to the same controls and content in every pose.
- **Follow the system's vertical layout for toolbars, tab bars, and navigation controls** — outer display is wider and shorter than other iPhones, so controls move to the side; on the inner display controls stay on the side in landscape. Standard components get this automatically; refine as needed.
- **Make your game playable in every device pose** — you may lock to portrait or landscape, but fill the screen as the pose changes; keep text and control sizes as consistent as possible. Prefer changing aspect ratio over letterboxing/pillarboxing; if unavoidable, add artwork to the padding area so it feels full screen.

### Dynamic layouts
- Build with layout margins and safe area insets; steer clear of fixed widths or anything tied to a specific display.

#### Reserved regions
Areas content avoids covering or components adapt to (similar to iPad window controls):
- **Outer front-facing camera** — always present; expands into the Dynamic Island for Live Activities. With side controls, system accounts for it automatically.
- **Inner front-facing camera** — present only when the camera is active; UI moves aside to indicate the camera.
- **Folding region** — conditional; when partially open, divides the inner display into multiple usable regions, excluding the center.
- Alerts, context menus, and sheets move automatically for the fold; split views adapt column widths and margins to the inner display's symmetry. For custom components use `ReservedRegion` / `UIView.ReservedRegion`.
- **Adapt your layout when the device folds** — prefer containers that adapt automatically (e.g., Notes split view equalizes pane widths when partially folded). In grids, prefer an even number of columns so content divides cleanly. Use `ReservedRegion` to keep important elements clear of the center if the system doesn't move them.
- **Avoid extreme layout changes as people fold the device** — move only what's necessary to keep elements visible and easy to tap; favor small adjustments over rearrangement.

#### Split views
- Expand on the inner display, collapse to a single pane on the outer display (same as regular vs. compact on other iPhones). Standard split views adapt width and margins to the fold automatically.

#### Arrangement views
- Layout container holding a primary and secondary view, organized dynamically by display size, orientation, and reserved regions.
  - *Split* arrangement: divides area; splits horizontally when wider than tall, vertically when taller than wide. You can limit which axes it uses.
  - *Overlay* arrangement: views stacked; when partially folded, views move to occupy each side; otherwise primary sits atop secondary. You can collapse the secondary view.
- **Consider an arrangement view when your layout already resembles one** — `HStack`/`VStack` → split arrangement; `ZStack` → overlay arrangement.
- **Keep navigation outside of arrangement views** — they lay out content but don't handle navigation; place navigation split views and tab views around them, not within.

### Vertical controls
- Toolbars, tab bars, and navigation controls normally at top/bottom move to the side — except the inner display in portrait, which keeps standard horizontal bars.
- Side controls (top to bottom on outer display trailing edge): Dynamic Island, status bar, toolbar (incl. navigation buttons), tab bar.
- In Split View multitasking on the inner display, each app places controls on its outer edge (left app → left).
- Vertical controls stay aligned with hardware: same position relative to the outer camera, and same side in right-to-left languages.
- **Account for asymmetry in your layouts** — use safe areas so controls (including those on the opposite edge in Split View) don't cover content.
- **Keep controls consistent across device poses** — keep relative positions as similar as possible so people don't relearn where actions live.
- **Follow the standard placement order for toolbar items** — top of the vertical axis: primary navigation (Back, Close), then prominent actions (Done). Keep remaining items in their original groupings; system adds vertical space between items from the former top and bottom bars.
- **Prioritize frequently used toolbar items** — items overflow bottom to top by default; assign visibility priority to whole groups first, then individual items. Preserve frequent actions first (Compose in Mail, New Note in Notes); keep status-bearing items (e.g., badges) visible longer.
- **In general, don't override the default bar placement** — side controls are a core iPhone Duo pattern.
- **Consider using the full display width where bars aren't necessary** — works for visual, immersive, non-scrolling interfaces if nothing conflicts with the Dynamic Island or status bar (e.g., Calculator: 4 columns × 5 on iPhone 16 portrait vs. 5 columns × 4 on iPhone Duo outer display). Can combine: full-width background/header with inset scrollable content.
- **Group related toolbar items instead of spacing them manually** — groups auto-space and adapt; avoid adding fixed spacing.
- **Locate controls near the content they affect** — controls for a non-trailing content area stay with that area (e.g., Mail list controls stay above the leading pane).
- **Provide both a title and a symbol for each toolbar item that isn't text-only** — system picks the representation; title is used in overflow menus and expanded forms.
- **Keep text-based buttons to a minimum** — text labels stay in a horizontal bar; prefer a symbol wherever one works.
- **When space is limited, preserve either the toolbar or tab bar based on the experience** — navigation-focused: move toolbar items to overflow so the tab bar stays (default compression). Task-oriented: minimize the tab bar to preserve toolbar actions (mirrors minimized tab bar on other iPhones).
- **Use the system overflow menu** — move custom overflow actions into it; reserve the ellipsis symbol for overflow and give other menus a distinct symbol.

## APIs
`Preparing your app for iPhone Duo` (technologyoverviews), `Device Hub` (Xcode), `safeAreaInsets` (SwiftUI), `safeAreaInsets` (UIKit), `ReservedRegion` (SwiftUI), `UIView.ReservedRegion` (UIKit), `NavigationSplitView` (SwiftUI), `UISplitViewController` (UIKit), `ArrangementView` (SwiftUI), `UIArrangementViewController` (UIKit), `HStack` (SwiftUI), `VStack` (SwiftUI), `ZStack` (SwiftUI), `ToolbarItemVisibilityPriority` (SwiftUI), `UIBarButtonItemVisibilityPriority` (UIKit), `ToolbarItemGroup` (SwiftUI), `UIBarButtonItemGroup` (UIKit), `Label` (SwiftUI), `UIBarButtonItem` (UIKit), `ToolbarVerticalCompressionBehavior` (SwiftUI), `UIVerticalBarCompressionBehavior` (UIKit), `ToolbarOverflowMenu` (SwiftUI), `additionalOverflowItems` (UIKit)

## Related
designing-for-ios, layout, split-views, toolbars, tab-bars, designing-for-games, multitasking
