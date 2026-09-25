# Page controls

> Source: https://developer.apple.com/design/human-interface-guidelines/page-controls · A page control displays a row of indicator images, each of which represents a page in a flat list.

## When to use / core idea
- Scrolling row of indicators to navigate a flat, ordered list of pages; handles arbitrary page counts (useful for user-created lists).
- Default: small equidistant dots; solid dot = current page; clipped if too many to fit the window.
- For hierarchical/nonsequential or complex navigation use a **sidebar** or **split view**; for many peer pages consider a **grid**.

## Rules
### Best practices
- **Use page controls to represent movement between an ordered list of pages** — not for hierarchical or nonsequential relationships.
- **Center a page control at the bottom of the view or window** — horizontally centered, near the bottom.
- **Although page controls can handle any number of pages, don't display too many** — more than about **10** dots are hard to count at a glance; for >10 peer pages consider a different arrangement (e.g., grid) allowing any-order navigation.

### Customizing indicators
- Default uses system dot for all indicators; can show a unique image for a specific page (Weather: `location.fill` for current location). Can set a custom default image for all indicators and a different image per page (`preferredIndicatorImage`, `setIndicatorImage(_:forPage:)`).
- **Make sure custom indicator images are simple and clear** — avoid complex shapes; no negative space, text, or inner lines (muddy at tiny sizes). Consider simple SF Symbols or your own icons.
- **Customize the default indicator image only when it enhances the page control's overall meaning** — e.g., `bookmark.fill` if every page contains bookmarks.
- **Avoid using more than two different indicator images in a page control** — one special page may get a unique image; multiple unique images force memorization and look messy.
- **Avoid coloring indicator images** — custom colors reduce current-page contrast and visibility; let the system color indicators.

## Platform considerations
Not supported: macOS.

### iOS, iPadOS
- Control highlights current-page indicator (conveys relative position); with too many indicators it shrinks those at both sides to suggest more pages.
- Interaction: tap or scrub (touch and drag left/right). Tapping leading/trailing side of current indicator → previous/next page; iPadOS pointer can target a specific indicator. Scrubbing opens pages in sequence; scrubbing past either edge jumps to first/last page. (API: tapping = discrete, scrubbing = continuous interaction; `UIPageControl.InteractionState`.)
- **Avoid animating page transitions during scrubbing** — fast scrubbing causes lag and flashes; use animated scrolling transition only for tapping.
- Optional translucent rounded-rectangle background (`backgroundStyle`):
  - **Automatic** — background only during interaction; use when the page control isn't the primary navigational element.
  - **Prominent** — always shown; use only when it's the screen's primary navigational control.
  - **Minimal** — never shown; use to just indicate position without scrubbing feedback.
- **Avoid supporting the scrubber when you use the minimal background style** — no scrubbing feedback; use automatic or prominent if scrubbing is supported.

### tvOS
- **Use page controls on collections of full-screen pages** — designed for full-screen, content-rich peer pages; extra controls make it hard to maintain focus while paging.

### visionOS
- Page controls show available pages and current page, but people don't interact with them.

### watchOS
- Shown at bottom for horizontal pagination, or next to the Digital Crown for a vertical tab view. With vertical tab views, the indicator shows position within the current page and within the set; transitions between scrolling page content and scrolling to other pages.
- **Use vertical pagination to separate multiple views into distinct, purposeful pages** — each page a clear purpose; scroll with the Digital Crown. More effective in watchOS than horizontal pagination or deep hierarchical navigation.
- **Consider limiting the content of an individual page to a single screen height** — encourages distinct purpose and glanceability. Use variable-height pages judiciously, ideally only after fixed-height pages.

## Specs
- Max recommended dots: about **10**.
- Max distinct indicator image types: **2**.

## APIs
`PageTabViewStyle` (SwiftUI), `UIPageControl` (UIKit), `UIPageControl.preferredIndicatorImage`, `setIndicatorImage(_:forPage:)`, `UIPageControl.InteractionState`, `UIPageControl.backgroundStyle` (UIKit).

## Related
`scroll-views, tab-views, sidebars, split-views, sf-symbols, icons`
