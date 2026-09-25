# Windows

> Source: https://developer.apple.com/design/human-interface-guidelines/windows · A window presents UI views and components in your app or game.

## When to use / core idea
- In iPadOS, macOS, visionOS, windows define visual boundaries of app content, separate it from the rest of the system, and enable multitasking within/between apps. They include system frames and controls to open, close, resize, relocate.
- Two conceptual types:
  - *Primary* window — main navigation, content, and associated actions.
  - *Auxiliary* window — a specific task/area; no navigation to other app areas; typically has a close button used after completing the task.
- Content layout: see `layout`; Vision Pro space: `spatial-layout`.

## Rules
### Best practices
- **Make sure that your windows adapt fluidly to different sizes to support multitasking and multiwindow workflows** — see `layout`, `multitasking`.
- **Choose the right moment to open a new window** — good for multitasking/preserving context (Mail opens Compose in a new window so both messages are visible); excessive windows cause clutter and confusion. Avoid opening new windows as default behavior unless it makes sense for your app.
- **Consider providing the option to view content in a new window** — e.g. via a context menu command or the File menu (`OpenWindowAction`).
- **Avoid creating custom window UI** — no custom frames or controls, and don't replicate the system appearance; imperfect matches make the app feel broken.
- **Use the term *window* in user-facing content** — regardless of type; don't use *scene* (implementation term) or other terms.

## Platform considerations
Not supported: iOS, tvOS, watchOS.

### iPadOS
- Presentation depends on the Multitasking & Gestures setting:
  - **Full screen** — windows fill the screen; switch windows (including same app) via the app switcher.
  - **Windowed** — freely resizable; multiple onscreen; reposition and bring to front; system remembers size and placement even after the app closes.
- **Make sure window controls don't overlap toolbar items** — windowed apps show window controls at the leading edge of the toolbar; move leading-edge buttons inward when controls appear.
- **Consider letting people use a gesture to open content in a new window** — e.g. pinch to expand a Notes item into a new window (`collectionView(_:sceneActivationConfigurationForItemAt:point:)` for collection items; `UIWindowScene.ActivationInteraction` for other views).
- Tip: to let people view a single file you can present it without creating your own window, but your app must support multiple windows (`QLPreviewSceneActivationConfiguration`).

### macOS
- People run several apps at once, viewing windows from multiple apps and frequently moving, resizing, minimizing, and revealing them. Games: see Managing your game window for Metal in macOS.
- **Anatomy:** frame + body area. Drag the frame to move; often drag edges to resize. Frame sits above the body and can include window controls and a `toolbars` toolbar; rarely a bottom bar (part of the frame below body content).
- **States:**
  - **Main** — frontmost window the person views; only one per app.
  - **Key** (active window) — accepts input; only one onscreen at a time. Usually the front app's main window, but a floating panel may be key instead. Click a window to make it key; clicking the Dock icon brings all windows forward but only the most recently accessed becomes key.
  - **Inactive** — not in the foreground.
- Appearance per state: key window uses color in close/minimize/zoom buttons; inactive windows and non-key main windows use gray. Inactive windows don't use vibrancy (see `materials`), appearing subdued and farther away.
- Some panels (e.g. Colors, Fonts) become key only when people click the title bar or a component needing keyboard input (e.g. a text field).
- **Make sure custom windows use the system-defined appearances** — people rely on state differences to identify the foreground/input window; system components update background and buttons automatically, custom implementations must do this themselves.
- **Avoid putting critical information or actions in a bottom bar, because people often relocate a window in a way that hides its bottom edge** — if you must, show only a small amount of info related to the window's contents or selection (e.g. Finder status bar: item count, selected count, available disk space). For more info use an inspector (typically trailing side of a split view).

### visionOS
- Two main styles: default (*window*) and volumetric (*volume*); both show 2D and 3D content; multiple can be viewed at once in the Shared Space and a Full Space.
- Also a *plain* style: like default but the upright plane has no glass background (`PlainWindowStyle`).
- System sets the initial position of the first window/volume; people can move them in Shared Space and Full Space.

#### visionOS windows
- Default style: upright plane with unmodifiable *glass* material; close button, window bar, resize controls. Can include a Share button, tab bar, toolbar, and ornaments. Uses dynamic scale by default so apparent size stays consistent regardless of distance (`DefaultWindowStyle`).
- **Prefer using a window to present a familiar interface and to support familiar tasks** — reserve immersive experiences for meaningful content; for bounded 3D content (e.g. game board) consider a volume.
- **Retain the window's glass background** — glass adapts to lighting and uses specular reflections/shadows to convey scale and position. Removing it hurts legibility and element relationships; an opaque background obscures surroundings and feels constricting and heavy.
- **Choose an initial window size that minimizes empty areas within it** — default 1280x720 pt; placed about two meters in front of the wearer, apparent width about three meters. Excess empty space looks unnecessarily large and obscures other content.
- **Aim for an initial shape that suits a window's content** — Keynote wide (slides), Safari tall (webpages); a tower-building game taller than a driving game.
- **Choose a minimum and maximum size for each window to help keep your content looking great** — otherwise people can shrink it until UI overlaps or enlarge it until unusable.
- **Minimize the depth of 3D content you display in a window** — system adds highlights/shadows for depth; 3D content extending too far from the surface is clipped. Use a volume for deeper 3D content.

#### visionOS volumes
- Display 2D or 3D content viewable from any angle; same window-management controls, but the close button and window bar shift to face the viewer as they move around (`VolumetricWindowStyle`).
- **Prefer using a volume to display rich, 3D content** — for familiar UI-centric interfaces, a window generally works best.
- **Place 2D content so it looks good from multiple angles** — perspective changes can make 2D placement look odd; use an attachment to pin 2D content to specific areas of 3D content.
- **In general, use dynamic scaling** — keeps content legible and interactive when far away. For real-world object representation (e.g. retail product) use fixed scaling (the default).
- **Take advantage of the default baseplate appearance to help people discern the edges of a volume** — visionOS 2+: baseplate ("floor") shows a gentle border glow when looked at; helps find edges and the resize control when content doesn't fill the volume. If content is full bleed / fills bounds, or you use a custom baseplate, you may not want the default glow.
- **Consider offering high-value content in an ornament** — visionOS 2+: a volume can have an ornament in addition to toolbar and tab bar. With an attachment anchor (e.g. `topBack`, `bottomFront`) the ornament stays in position relative to the viewer. Avoid placing it on the same edge as a toolbar or tab bar; prefer only one additional ornament.
- **Choose an alignment that supports the way people interact with your volume** — baseplate parallel to the floor suits content with little interaction; tilting to match gaze keeps content usable, even when reclining.

## Specs
- visionOS default window size: 1280x720 pt; initial placement ~2 m in front of wearer; apparent width ~3 m.

## APIs
`Windows` / `WindowGroup` (SwiftUI), `OpenWindowAction` (SwiftUI), `PlainWindowStyle` / `DefaultWindowStyle` / `VolumetricWindowStyle` (SwiftUI), `ornament(visibility:attachmentAnchor:contentAlignment:ornament:)` (SwiftUI), `UIWindow` (UIKit), `UIWindowScene.ActivationInteraction` (UIKit), `collectionView(_:sceneActivationConfigurationForItemAt:point:)` (UIKit), `QLPreviewSceneActivationConfiguration` (Quick Look), `NSWindow` (AppKit)

## Related
`layout, split-views, multitasking, spatial-layout, context-menus, the-menu-bar, toolbars, materials, tab-bars, ornaments, immersive-experiences`
