# Scroll views

> Source: https://developer.apple.com/design/human-interface-guidelines/scroll-views · A scroll view lets people view content that's larger than the view's boundaries by moving the content vertically or horizontally.

## When to use / core idea
- No appearance of its own; may show a translucent *scroll indicator* after scrolling begins. Indicators give feedback; in iOS, iPadOS, macOS, visionOS, watchOS they show whether visible content is near beginning, middle, or end.
- Pair with page controls for page-by-page content; watchOS uses tab views for paging.

## Rules
### Best practices
- **Support default scrolling gestures and keyboard shortcuts** — people expect systemwide behavior; custom scrolling must keep the expected elastic indicator behavior.
- **Make it apparent when content is scrollable** — indicators aren't always visible; e.g., show partial content at the view edge.
- **Avoid putting a scroll view inside another scroll view with the same orientation** — unpredictable, hard to control. Horizontal inside vertical (or vice versa) is fine.
- **Consider supporting page-by-page scrolling if it makes sense for your content** — page size typically the current view height/width; to keep context, subtract an overlap unit (a line of text, row of glyphs, part of a picture) (`PagingScrollTargetBehavior`).
- **In some cases, scroll automatically to help people find their place** — when:
  - An operation selects content or places the insertion point in a hidden area (e.g., found search text → scroll it into view).
  - People start entering info at a location not visible (scroll back to the insertion point when typing begins).
  - The pointer moves past the view edge during selection (follow the pointer).
  - People select, scroll elsewhere, then act on the selection (scroll selection into view before performing the operation).
  - In all cases scroll only as much as necessary to retain context (if part of a selection is visible, don't scroll the whole selection into view).
- **If you support zoom, set appropriate maximum and minimum scale values** — e.g., zooming text until one character fills the screen rarely makes sense.

### Scroll edge effects
- iOS, iPadOS, macOS: visual separation between elements like toolbars and scrolling content behind them. With custom bars you may add it manually for extra clarity, or change style from automatic to **hard** (more opaque blur with defined edge) or **soft** (variable blur, softer fade).
- **Prefer the automatic scroll edge effect style** — gives more opaque separation for top toolbars with many controls, text outside Liquid Glass controls, and pinned table headers. If using soft, thoroughly test legibility in varied contexts.
- **Only use a scroll edge effect when a scroll view is behind floating interface elements** — not decorative; doesn't block/darken like an overlay; exists to keep controls distinct.
- **Apply one scroll edge effect per view** — in iPad/Mac split views each pane can have its own; keep them consistent in height for alignment.

## Platform considerations
### iOS, iPadOS
- **Consider showing a page control when a scroll view is in page-by-page mode** — shows count and current page (e.g., Weather locations). Don't also show the scroll indicator on the same axis (redundant).

### macOS
- Scroll indicator = *scroll bar*.
- **If necessary, use small or mini scroll bars in a panel** — when space is tight in panels coexisting with other windows; use the same size for all controls in that panel.

### tvOS
- Views scroll but aren't distinct objects with indicators; system auto-scrolls to keep focused items visible.

### visionOS
- Indicator has a small, fixed size (efficient scrolling without large movements). Predictable location: vertically centered at the trailing edge for vertical scrolling; horizontally centered at the window's bottom edge for horizontal.
- Appears at the window edge when people swipe content. Looking at the indicator and dragging enables a *jog bar* that controls scrolling speed, not position; tick marks speed up/slow down to give acceleration feedback.
- **If necessary, account for the size of the scroll indicator** — slightly thicker than iOS; with tight margins, increase them to prevent overlap.

#### Look to Scroll
- People scroll with their eyes by looking near the scroll view boundary (top/bottom for vertical, sides for horizontal), e.g., bottom of a Safari window, or an album at the trailing edge in Music. Works alongside gestures (`ScrollInputKind.look`).
- **Support Look to Scroll for reading or browsing views** — off by default; add per scroll view for hands-free comfort.
- **Avoid using Look to Scroll for secondary content** — not for views with UI controls or dense info needing quick, precise scrolling (Notes: main view yes, notes list no).
- **Maintain consistency across content** — if one view supports it, support all similar views (e.g., all video collection views).
- **Define clear scroll areas within your app** — prefer full-width/full-height scroll views; if inset (like Notes), provide clear boundaries.
- **If your app uses custom scroll effects or animations, remove them before supporting Look to Scroll** — scroll-position-driven effects (parallax, animations) cause unexpected behavior.

### watchOS
- **Prefer vertically scrolling content** — Digital Crown scrolls vertically when content is taller than the display.
- **Use tab views to provide page-by-page scrolling** — vertically stacked tab views give full-screen pages navigated with the Digital Crown; a page indicator next to the Crown shows position within page and set.
- **When displaying paged content, consider limiting the content of an individual page to a single screen height** — clarifies purpose, more glanceable. Long pages still work: the page indicator expands into a scroll indicator. Use variable-height pages judiciously, after fixed-height pages when possible.

## APIs
`ScrollView` (SwiftUI), `PagingScrollTargetBehavior` (SwiftUI), `ScrollEdgeEffectStyle` (SwiftUI), `ScrollInputKind` / `.look` (SwiftUI), `UIScrollView` (UIKit), `UIScrollEdgeEffect.Style` (UIKit), `NSScrollView` (AppKit), `NSScrollEdgeEffectStyle` (AppKit), `WKPageOrientation` (WatchKit).

## Related
`page-controls, gestures, pointing-devices, toolbars, materials, tab-views, panels, split-views`
