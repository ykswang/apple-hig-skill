# Search fields

> Source: https://developer.apple.com/design/human-interface-guidelines/search-fields · A search field lets people search a collection of content for specific terms they enter.

## When to use / core idea
- An editable text field with a Search icon, a Clear button, and placeholder text. Can use a **scope bar** and **tokens** to filter/refine scope.
- Access patterns differ per platform based on app goals/design. For systemwide search see `searching`; for macOS token entry see `token-fields`.

## Rules
### Best practices
- **Use placeholder text to help people know what they can search for** — reinforce scope or educate about searchable content types.
- **If possible, start search immediately when a person types** — continuously refined results feel responsive.
- **Consider showing suggested search terms** — recent searches before searching, predictive suggestions while typing; speeds search even if search doesn't start immediately.
- **Simplify search results** — most relevant first to minimize scrolling; consider categorizing results.
- **Consider letting people filter search results** — e.g., a scope bar in the results content area.

### Scope bars and tokens
- *Scope bar*: control for filtering/adjusting search scope. *Token*: visual representation of a search term that can be selected and edited, acting as a filter for additional terms. Usable before or after searching.
- **Use a scope bar to filter among clearly defined search categories** — broader → narrower (Mail on iPhone: all mailboxes → current mailbox).
- **Default to a broader scope and let people refine it as they need** — broader scope gives context for the full result set.
- **Use tokens to filter by common search terms or items** — a token encapsulates a term as one selectable/editable item; can clarify a term (a specific contact in Mail) or focus on attributes (photos in Messages).
- **Consider pairing tokens with search suggestions** — people may not know which tokens exist.

## Platform considerations
No additional considerations: visionOS.

### iOS
- Three entry-point placements: a tab in a tab bar; a toolbar (bottom or top); inline with content. Choose by layout, content, navigation.

#### Search as a tab
- Keeps search visible and available across sections. Two styles:
  - **Standard tab** — uniform with other tabs; tapping navigates to a search landing page with a field at top.
  - **Button appearance** — separate button; tapping focuses the field and shows the keyboard immediately.
- **Choose the standard tab style to provide suggestions, promote discovery, and encourage exploration** — dedicated landing page can show content/suggestions before typing; great for rich, explorable content (e.g., Apple TV genres/categories).
- **Choose the button appearance to help people quickly find what they need** — keyboard appears with field above it; transient, returns people to their previous tab on exit; ideal when search should resolve quickly.

#### Search in a toolbar
- Bottom toolbar: expanded field or toolbar button depending on space; tapping animates into a field above the keyboard.
- Top toolbar (navigation bar): appears as a toolbar button; tapping animates into a field above the keyboard, or at the top if no room at bottom.
- **Place search at the bottom if there's room** — add to an existing toolbar or a new toolbar where it's the only item; good whenever search is a priority (Settings: only item; Mail, Notes: alongside other controls).
- **Place search at the top when it's important to defer to content at the bottom of the screen, or there's no bottom toolbar** — when covering content would interfere with a primary function (e.g., Wallet's pass stack at bottom).

#### Search as an inline field
- **Place search as an inline field when its position alongside the content it searches strengthens that relationship** — shows search applies to that view, not globally; useful with multiple search fields or when location defines scope (Music: main search is a tab, library uses inline filter).
- **When at the top, position an inline search field above the list it searches, and consider pinning it to the top toolbar when scrolling** — keeps it distinct from search elsewhere.

### iPadOS, macOS
- Similar placement and behavior; keep search consistent if the app ships on both.
- **Put a search field at the trailing side of the toolbar for many common uses** — especially split-view apps searching multiple columns (Mail, Notes, Voice Memos); keeps selection visible in detail view. Also when results appear in the detail view (Freeform filters boards).
- **Include search at the top of the sidebar when filtering content or navigation there** — e.g., Settings filters sidebar sections multiple levels deep; useful with a rich detail view needing clear separation.
- **Include search as an item in the sidebar or tab bar when you want an area dedicated to discovery** — for rich suggestions/categories/content (Music, TV); always available while switching sections.
- **In a search field in a dedicated area, consider immediately focusing the field when a person navigates to the area** — exception: on iPad with only a virtual keyboard, leave it unfocused so the keyboard doesn't unexpectedly cover the view.
- **Account for window resizing with the placement of the search field** — iPad field resizes fluidly like Mac; in compact iPad views place search where most contextually useful (Notes, Mail: above the content-list column).

### tvOS
- Search screen: specialized keyboard screen with results in a fully customizable view beneath the keyboard (`UISearchController`).
- **Provide suggestions to make searching easier** — people don't want to type much; offer popular, context-specific, and recent searches.

### watchOS
- Tapping the field shows a full-screen text-input control; returns to the field only after Cancel or Search.

## APIs
`searchable(text:placement:prompt:)` (SwiftUI), "Adding a search interface to your app" / "Scoping a search operation" (SwiftUI), `UISearchBar` (UIKit), `UISearchTextField` (UIKit), `UISearchController` (UIKit), `NSSearchField` (AppKit).

## Related
`searching, token-fields, tab-bars, toolbars, sidebars, text-fields, virtual-keyboards`
