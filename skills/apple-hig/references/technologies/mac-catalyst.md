# Mac Catalyst

> Source: https://developer.apple.com/design/human-interface-guidelines/mac-catalyst · Mac Catalyst creates a Mac version of your iPad app so people can enjoy the experience in a new environment.

## When to use / core idea
- Best candidates: iPad apps that already support **drag and drop** (carries over), **keyboard navigation and shortcuts** (Mac users expect both), **multitasking** (Split View, Slide Over, Picture in Picture scaling lays groundwork for Mac window resizing), **multiple windows** (multiple scenes → multiple Mac windows).
- Possibly unsuitable if essential features need gyroscope, accelerometer, rear camera, HealthKit, ARKit, or the primary function is marking, handwriting, or navigation.
- Automatic macOS support: pointer interactions and keyboard focus/navigation, window management, toolbars, rich text interaction (copy/paste, contextual editing menus), file management, menu bar menus, app settings in the system Settings app.
- System UI gets a more Mac-like appearance: split view, file browser, activity view, form sheet, contextual actions, color picker.
- Must go beyond displaying the iPad layout in a Mac window, regardless of idiom. Alternative: a native macOS app (see `designing-for-macos`).

## Rules
### Choose an idiom
- Xcode defaults to "Scale Interface to Match iPad" (*iPad idiom*): consistent with macOS without major layout changes, but views/text scale to 77% (17pt baseline → 13pt), so slightly less detailed.
- Once the app feels at home with the iPad idiom, consider the *Mac idiom*: more detailed text/artwork, more Mac-like views, possibly better performance and lower power for graphics-intensive apps. Most beneficial for apps with lots of text, detailed artwork, or animation; costs extra layout/text/image work.
- **When you adopt the Mac idiom, thoroughly audit your app's layout, and plan to make changes to it** — consider a separate asset catalog for Mac assets.
- **Adjust font sizes as needed** — Mac idiom renders text at 100%, which can look too large; use text styles, avoid fixed font sizes.
- **Make sure views and images look good in the Mac version of your app** — Mac idiom renders views at 100%, showing more detail.
- Developer note: unscaled views report different metrics; avoid fixed font, view, or layout sizes.
- **Limit your appearance customizations to standard macOS appearance customizations that are the same or similar to those available in iPadOS** — not all iPadOS control customizations exist on macOS.

### Navigation
- iPad components: split views (2–3 columns: primary/sidebar, optional supplementary, secondary content), tab bars (flat, persistent bottom bar), page controls (dots showing position in flat page list).
- If your iPad app uses a tab bar, consider a split view with a sidebar or a segmented control on Mac:
  - Sidebar lists top-level items that can disclose children; each tab's content lives in the sidebar; using a sidebar on both iPad and Mac gives a consistent layout.
  - Generally a split view works better than a segmented control; a segmented control can work on Mac for a flat hierarchy.
- **Make sure people retain access to important tab-bar items in the Mac version of your app** — list top-level items in the macOS View menu.
- **Offer multiple ways to move between pages** — add Next and Previous buttons in addition to swipe gestures.

### Inputs
- iPadOS conventions are touch-based; macOS conventions are keyboard- and mouse-based. Most gestures convert automatically (see Specs).
- Developer note: pinch and rotate touches go to the view under the pointer, not the view under each touch.

### App icons
- **Create a macOS version of your app icon** — lifelike macOS rendering style while staying harmonious across platforms.

### Layout
- Consider: splitting a single column into multiple columns; using regular-width/regular-height size classes and reflowing content side by side as the window resizes; presenting an inspector beside main content instead of a popover.
- **Consider moving controls from the main UI of your iPad app to your Mac app's toolbar** — also list their commands in menu bar menus.
- **As much as possible, adopt a top-down flow** — important actions/content near the top; put iPad toolbar controls in the Mac window toolbar.
- **Relocate buttons from the side and bottom edges of the screen** — reachability doesn't apply on Mac; move elsewhere or into the toolbar.

### Menus
- Mac users expect all commands in the persistent menu bar; iPad users find commands in the UI or the Command-key shortcut interface.
- Pop-up and pull-down button menus automatically take a macOS appearance.
- Context menus convert automatically; consider adding more — Mac users expect every object to offer a context (contextual) menu of relevant actions.
- Developer notes: `UIKeyCommand` for menu keyboard shortcuts; `UIMenuBuilder` + `UICommand` to add/remove custom app menus.

## Platform considerations
No additional considerations: iPadOS, macOS. Not supported in iOS, tvOS, visionOS, or watchOS.

## Specs
- iPad idiom scale: 77% (iPadOS 17pt baseline text → 13pt on macOS). Mac idiom: 100%.

| iPadOS gesture… | Translates to mouse interaction |
| --- | --- |
| Tap | Left or right click |
| Touch and hold | Click and hold |
| Pan | Left click and drag |

| iPadOS gesture… | Translates to trackpad gesture |
| --- | --- |
| Tap | Click |
| Touch and hold | Click and hold |
| Pan | Click and drag |
| Pinch | Pinch |
| Rotate | Rotate |

## APIs
Mac Catalyst (UIKit), `UIKeyCommand`, `UIMenuBuilder`, `UICommand` (UIKit)

## Related
designing-for-macos, split-views, tab-bars, page-controls, segmented-controls, toolbars, the-menu-bar, context-menus, pop-up-buttons, pull-down-buttons, app-icons, layout
