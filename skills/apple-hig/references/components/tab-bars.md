# Tab bars

> Source: https://developer.apple.com/design/human-interface-guidelines/tab-bars · A tab bar lets people navigate between top-level sections of your app.

## When to use / core idea
- Shows the different types of information/functionality an app provides; switches sections while preserving each section's navigation state.
- For actions on the current view use a **toolbar**. For complex information structures consider a **sidebar** or a tab bar that adapts to a sidebar.

## Rules
### Best practices
- **Use a tab bar to support navigation, not to provide actions** — e.g., Clock's Alarm, Stopwatch, Timer tabs; controls acting on current view belong in a toolbar.
- **Make sure the tab bar is visible when people navigate to different sections of your app** — hiding it makes people forget where they are. Exception: a modal view covering it (temporary, self-contained).
- **Use the appropriate number of tabs required to help people navigate your app** — weigh complexity of more tabs vs. need for frequent access; fewer tabs are easier. Where available, consider a sidebar or a sidebar-adaptable tab bar for complex structures.
- **Avoid overflow tabs** — when horizontal space limits visible tabs, the trailing tab becomes a More tab (iOS, iPadOS) listing the rest; hidden content is harder to reach/notice, so limit these scenarios.
- **Don't disable or hide tab bar buttons, even when their content is unavailable** — inconsistent availability feels unstable; if a section is empty, explain why.
- **Include tab labels to help with navigation** — beneath or beside the icon; describe the content/functionality; use single words whenever possible.
- **Consider using SF Symbols to provide familiar, scalable tab bar icons** — adapt automatically to regular vs. compact bars: icons above labels in compact views, side by side in regular views. Prefer filled symbols or icons for platform consistency. Custom icon dimensions: Apple Design Resources.
- **Use a badge to indicate that critical information is available** — red oval with white text (number or exclamation point) for new/updated info warranting attention. Reserve for critical info to avoid diluting meaning (see notifications).
- **Avoid applying a similar color to tab labels and content layer backgrounds** — with bright, colorful content, prefer a monochromatic tab bar or an accent color with sufficient differentiation (see color › Liquid Glass color).

## Platform considerations
No additional considerations: macOS. Not supported: watchOS.

### iOS
- Floats above content at the bottom of the screen; items rest on a Liquid Glass background letting content peek through.
- With an attached accessory (e.g., Music's MiniPlayer), you can minimize the tab bar and move the accessory inline when people scroll down; tapping a tab or scrolling to top exits the minimized state (`TabBarMinimizeBehavior`, `UITabBarController.MinimizeBehavior`).
- Can include a dedicated search tab at the trailing end (see search-fields).

### iPadOS
- Tab bar appears near the top of the screen, either fixed or with a button to convert it to a sidebar (`tabBarOnly`, `sidebarAdaptable`). For a sidebar without tab-bar conversion, use a navigation split view instead of a tab view.
- **Prefer a tab bar for navigation** — access to most-used sections; for complex apps offer conversion to a sidebar for wider navigation options.
- **Let people customize the tab bar** — add frequently used items / remove less used ones (e.g., a favorite playlist in Music). If people can select tabs, aim for a default list of **five or fewer** to preserve continuity between compact and regular sizes (`TabViewCustomization`, `UITab.Placement`).

### tvOS
- Highly customizable: tint/color/image for background; font for tab items (different font for selected); tints for selected/unselected items; button icons like settings and search.
- Default: translucent, only selected tab opaque; when focused via remote, selected tab gets a drop shadow.
- Overflow: system truncates the rightmost item with a fade from the right side; if enough items to scroll, also a truncating fade from the left.
- **Be aware of tab bar scrolling behaviors** — by default the tab bar scrolls offscreen when the tab has a single main view (TV app's Watch Now, Movies, TV Show, Sports, Kids). Exception: split view screens (TV Library, Settings) keep the tab bar pinned at top while panes scroll. Pressing Menu on the remote always returns focus to the tab bar at top.
- **In a live-viewing app, organize tabs in a consistent way** — order: Live content → Cloud DVR or other recorded content → Other content (see live-viewing-apps).

### visionOS
- Always vertical, floating at a fixed position relative to the window's leading side. Expands automatically when people look at it; look + tap opens a tab. When expanded it can temporarily obscure content behind it.
- **Supply a symbol and a text label for each tab** — symbol always visible; labels revealed on look. Keep labels short for at-a-glance reading.
- **If it makes sense in your app, consider using a sidebar within a tab** — for deep hierarchies; prevent sidebar selections from changing the open tab.

## Specs
- tvOS tab bar height: **68 pt**; top edge **46 pt** from top of screen (neither can be changed).
- iPadOS customizable tab bar default: **≤5** tabs.
- Badge: red oval, white text, number or exclamation point.

## APIs
`TabBarMinimizeBehavior` (SwiftUI), `UITabBarController.MinimizeBehavior` (UIKit), `tabBarOnly` (SwiftUI), `sidebarAdaptable` (SwiftUI), `navigation split view` (SwiftUI), `TabViewCustomization` (SwiftUI), `UITab.Placement` (UIKit), `TabView` (SwiftUI), `TabViewBottomAccessoryPlacement` (SwiftUI), `Enhancing your app’s content with tab navigation` (SwiftUI), `UITabBar` (UIKit), `Elevating your iPad app with a tab bar and sidebar` (UIKit)

## Related
`tab-views, toolbars, sidebars, materials, search-fields, sf-symbols, notifications, color, live-viewing-apps`
