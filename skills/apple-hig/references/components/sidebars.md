# Sidebars

> Source: https://developer.apple.com/design/human-interface-guidelines/sidebars · A sidebar appears on the leading side of a view and lets people navigate between areas of your app or top-level collections of content, like folders and playlists.

## When to use / core idea
- Needs a lot of vertical and horizontal space. When space is limited or you want more screen for other content, a more compact control like a **tab bar** may be better.
- Often you needn't choose: adopt a tab bar style that provides both (sidebar-adaptable). See tab-bars, layout.
- For hierarchies deeper than two levels, use a **split view** with a content list between sidebar and detail.

## Rules
### Best practices
- **Extend visually rich content beneath the sidebar** — in iOS, iPadOS, macOS sidebars can float above content in the Liquid Glass layer. Extend content under it via horizontal scrolling or a *background extension effect* (mirrors adjacent content to appear stretched under the sidebar; `backgroundExtensionEffect()`). Don't stop an image at the sidebar's edge.
- **When possible, let people customize the contents of a sidebar** — which areas appear and in what order.
- **Group hierarchy with disclosure controls if your app has a lot of content** — keeps vertical space manageable.
- **Consider using familiar symbols to represent items in the sidebar** — SF Symbols; for custom icons prefer a custom symbol over a bitmap image.
- **Consider letting people hide the sidebar** — for more content room or less distraction; use platform-familiar interactions: iPadOS edge swipe; macOS show/hide button or Show Sidebar / Hide Sidebar in the View menu. visionOS windows typically expand to fit a sidebar, so hiding is rarely needed. Avoid hiding the sidebar by default (keep it discoverable).
- **In general, show no more than two levels of hierarchy in a sidebar** — deeper → split view with a content list.
- **If you need to include two levels of hierarchy in a sidebar, use succinct, descriptive labels to title each group** — omit unnecessary words.
- **Make sure any sidebar icon colors you choose serve a clear purpose** — default icons use the app accent color. In macOS people can change the system accent color and expect all sidebar icons to follow it — ensure yours do. Sparing fixed colors can clarify meaning or draw attention (e.g., Mail's yellow VIP icon).

## Platform considerations
No additional considerations: tvOS. Not supported: watchOS.

### iOS, iPadOS
- `sidebarAdaptable` tab view style: choose whether sidebar or tab bar shows at launch; both include a button to switch. Adapts per platform and responds automatically to rotation and window resizing.
- Sidebar only: `NavigationSplitView` (sidebar in primary pane) or `UISplitViewController`.
- **Consider using a tab bar first** — more space for content, flexible enough for many apps' main areas; if more areas than fit, the tab bar's convertible sidebar-style appearance exposes less-used content.
- **If necessary, apply the correct appearance to a sidebar** — without SwiftUI, use `UICollectionLayoutListConfiguration.Appearance.sidebar` for a collection view list layout.

### macOS
- Row height, text, and glyph size depend on sidebar size: small, medium, or large. Settable programmatically; people can change it via sidebar icon size in General settings.
- **Consider automatically hiding and revealing a sidebar when its container window resizes** — e.g., shrinking a Mail viewer window collapses its sidebar.
- **Avoid putting critical information or actions at the bottom of a sidebar** — people often move windows so the bottom edge is hidden.

### visionOS
- **If your app's hierarchy is deep, consider using a sidebar within a tab in a tab bar** — for secondary navigation within the tab; prevent sidebar selections from changing which tab is open.

## Specs
- Max hierarchy levels in a sidebar: **two** (general guidance).
- macOS sidebar sizes: small, medium, large.

## APIs
`sidebarAdaptable` (SwiftUI), `NavigationSplitView` (SwiftUI), `ListStyle.sidebar` (SwiftUI), `backgroundExtensionEffect()` (SwiftUI), `UICollectionLayoutListConfiguration` (UIKit), `UISplitViewController` (UIKit), `NSSplitViewController` (AppKit).

## Related
`split-views, tab-bars, layout, disclosure-controls, sf-symbols, color, materials, the-menu-bar`
