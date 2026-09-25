# Lists and tables

> Source: https://developer.apple.com/design/human-interface-guidelines/lists-and-tables · Lists and tables present data in one or more columns of rows.

## When to use / core idea
- Represent data organized in groups or hierarchies; support selecting, adding, deleting, reordering. Available on all platforms.
- Lists often express an app's information hierarchy for navigation (e.g., iOS Settings); many apps put a table in a split view (e.g., Mail on iPadOS/macOS).
- Productivity apps use multicolumn, sortable tables for data attributes.
- Items varying widely in size or many images → collections. Hierarchical data on macOS → outline-views.

## Rules
### Best practices
- **Prefer displaying text in a list or table** — the row format makes text easy to scan; for widely varying item sizes or many images, consider a collection.
- **Let people edit a table when it makes sense** — people appreciate reordering even if they can't add/remove. In iOS and iPadOS, people must enter edit mode before selecting table items.
- **Provide appropriate feedback when people select a list item** — navigation-through-hierarchy tables persistently highlight the selected row to clarify the path; option lists highlight briefly, then add an image such as a checkmark.

### Content
- **Keep item text succinct so row content is comfortable to read** — minimizes truncation and wrapping. For lots of text per item, consider listing titles only and revealing content in a detail view.
- **Consider ways to preserve readability of text that might get clipped or truncated** — e.g., in narrow/resizable tables, a middle ellipsis preserves beginning and end.
- **Use descriptive column headings in a multicolumn table** — nouns or short noun phrases, title-style capitalization, no ending punctuation. For a single-column table without a heading, use a label or header for context.

### Style
- **Choose a table or list style that coordinates with your data and platform** — e.g., iOS/iPadOS grouped style (headers, footers, extra space between groups); watchOS elliptical style (items appear to roll off a rounded surface when scrolling); macOS bordered style (alternating row backgrounds for large tables).
- **Choose a row style that fits the information you need to display** — e.g., small leading image plus brief label; use built-in row styles such as `UIListContentConfiguration` (rows, headers, footers in iOS, iPadOS, tvOS).

## Platform considerations
### iOS, iPadOS, visionOS
- **Use an info button only to reveal more information about a row's content** — in a row it's called a *detail disclosure button* and doesn't support hierarchical navigation; to drill into a row's subviews use a disclosure indicator accessory control.
- **Avoid adding an index to a table that displays trailing controls like disclosure indicators** — an index (vertical alphabet letters on the trailing side for jumping to sections) conflicts with trailing controls; people may activate one when using the other.
### macOS
- **When it provides value, let people click a column heading to sort** — clicking an already-sorted heading re-sorts in the opposite direction.
- **Let people resize columns** — to focus on areas or reveal clipped data.
- **Consider using alternating row colors in a multicolumn table** — helps track values across columns, especially in wide tables.
- **Use an outline view instead of a table view to present hierarchical data** — outline views add disclosure triangles for nested levels.
### tvOS
- **Confirm that images near a table still look good as each row highlights and slightly increases in size when focused** — focused row corners can become rounded; account for this when preparing images and don't add your own masks to round corners.
### watchOS
- **When possible, limit the number of rows** — short lists scan easier, but people sometimes expect long lists (e.g., many podcast subscriptions); list the most relevant items and provide a way to view more.
- **Constrain the length of detail views if you want to support vertical page-based navigation** — swiping vertically among detail items works only when detail views are short; if details scroll, it doesn't work.

## APIs
`List` (SwiftUI), `Tables`/`Table` (SwiftUI), `ListStyle` (SwiftUI), `UITableView` (UIKit), `UIListContentConfiguration` (UIKit), `UITableViewCell.AccessoryType.disclosureIndicator` (UIKit), `NSTableView` (AppKit)

## Related
collections, outline-views, split-views, layout, buttons
