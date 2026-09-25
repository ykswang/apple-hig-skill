# Collections

> Source: https://developer.apple.com/design/human-interface-guidelines/collections · A collection manages an ordered set of content and presents it in a customizable, highly visual layout.

## When to use / core idea
- Generally ideal for image-based content.
- For text, consider a table/list instead (lists-and-tables).

## Rules
### Best practices
- **Use the standard row or grid layout whenever possible** — defaults are a horizontal row or grid, which people expect. Avoid custom layouts that confuse or draw undue attention.
- **Consider using a table instead of a collection for text** — textual info is simpler to view and digest in a scrollable list.
- **Make it easy to choose an item** — use adequate padding around images so focus/hover effects are easy to see and content doesn't overlap.
- **Add custom interactions when necessary** — defaults: tap to select, touch and hold to edit, swipe to scroll; add gestures for custom actions if required.
- **Consider using animations to provide feedback when people insert, delete, or reorder items** — standard animations available; custom animations also possible.

## Platform considerations
No additional considerations: macOS, tvOS, visionOS. Not supported: watchOS.
### iOS, iPadOS
- **Use caution when making dynamic layout changes** — changes must make sense and be easy to track; if possible, avoid changing the layout while people are viewing/interacting with it, unless responding to an explicit action.

## APIs
`UICollectionView` (UIKit), `NSCollectionView` (AppKit)

## Related
lists-and-tables, image-views, layout
