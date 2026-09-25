# Segmented controls

> Source: https://developer.apple.com/design/human-interface-guidelines/segmented-controls · A linear set of two or more segments, each of which functions as a button.

## When to use / core idea
- Segments usually equal width; contain text or images (like `buttons`); optional text labels beneath segments or beneath the whole control.
- Offers a single choice from a set, or in macOS single or multiple choices (Keynote: alignment = single; font attributes bold/italic/underline = multiple; toolbar control shows/hides panes).
- Can also be momentary action buttons with no selection state (e.g. Mail's Reply, Reply all, Forward) — `isMomentary` / `NSSegmentedControl.SwitchTracking.momentary`.
- Alternatives: `tab-bars` (iOS, separate app sections), `tab-views` (macOS main-window view switching), `split-views` (tvOS filtering).

## Rules
### Best practices
- **Use a segmented control to provide closely related choices that affect an object, state, or view** — e.g. inspector attributes for a selection; toolbar actions on the current view.
- **Consider a segmented control when it's important to group functions together, or to clearly show their selection state** — grouping is preserved regardless of view size/placement; selection is visible at a glance.
- **Keep control types consistent within a single segmented control** — don't assign actions to segments in a selection-state control; don't show selection state in an action control.
- **Limit the number of segments in a control** — aim for no more than about five to seven in a wide interface, no more than about five on iPhone.
- **In general, keep segment size consistent** — equal widths feel balanced; keep icon and title widths consistent too.

### Content
- **Prefer using either text or images — not a mix of both — in a single segmented control** — mixing feels disconnected and confusing.
- **As much as possible, use content with a similar size in each segment** — equal-width segments look bad when only some are filled.
- **Use nouns or noun phrases for segment labels** — title-style capitalization; a text-labeled control doesn't need introductory text.

## Platform considerations
Not supported: watchOS.
### iOS, iPadOS
- **Consider a segmented control to switch between closely related subviews** — e.g. Calendar New Event sheet: Event / Reminder. For completely separate app sections, use a tab bar instead.
### macOS
- **Consider using introductory text to clarify the purpose of a segmented control** — with symbols/icons you could add a label below each segment; if the app has tooltips, provide one per segment.
- **Use a tab view in the main window area — instead of a segmented control — for view switching** — a tab view looks like a box + segmented control. Consider segmented controls for view switching in a toolbar or inspector pane.
- **Consider supporting spring loading** — with Magic Trackpad, people drag items over a segment and force click to activate it without dropping; they can continue dragging afterward.
### tvOS
- **Consider using a split view instead of a segmented control on screens that perform content filtering** — easier to move between content and filters; a segmented control may be harder to reach depending on placement.
- **Avoid putting other focusable elements close to segmented controls** — segments are selected when focus moves to them (not on click), so nearby focusables get focused accidentally.
### visionOS
- Looking at an icon-based segmented control shows a tooltip with the descriptive text you supply.

## APIs
`segmented` PickerStyle (SwiftUI), `UISegmentedControl` (UIKit), `NSSegmentedControl` (AppKit), `isMomentary` (UIKit), `NSSegmentedControl.SwitchTracking.momentary` (AppKit)

## Related
`buttons, tab-bars, tab-views, boxes, split-views`
