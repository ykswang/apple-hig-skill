# Charts

> Source: https://developer.apple.com/design/human-interface-guidelines/charts · Organize data in a chart to communicate information with clarity and visual appeal.

## When to use / core idea
- An effective chart highlights a few key pieces of information in a dataset to help people gain insights and decide (e.g., weather effects on plans, stock trends, fitness progress).
- For deciding whether/how to chart in your experience, see `charting-data`; implement with Swift Charts.
- For showing a single value in a range, consider gauges / progress indicators / activity rings instead.

## Anatomy
- **Mark**: visual representation of a data value. Supply one or more data series; choose a mark type (bar, line, point…) to set chart style. Depicting values = *plotting*; area containing marks = *plot area*.
- **Scale**: maps data values (numbers, dates, categories) to visual attributes (position, color, height).
- **Axis**: frame of reference; many charts have a horizontal and vertical axis at plot edges, each representing a variable (time, amount, category).
- **Ticks**: reference points on an axis (e.g., 0, 50%, 100%). **Grid lines** extend from ticks across the plot area to help estimate values.
- **Labels** name axes, grid lines, ticks, marks; **accessibility labels** describe elements for assistive tech. Also titles, subtitles, annotations, and a **legend** for non-positional properties (color/shape per category).

## Rules
### Marks
- **Choose a mark type based on the information you want to communicate about the data.**
  - *Bar*: compare values across categories or parts of a whole; over time, best when each value is a sum (e.g., total steps per day).
  - *Line*: change over time; a line connects all values in one series; slope shows magnitude of change and trends.
  - *Point*: individual values as distinct marks; show relationships between two properties, outliers, clusters.
- **Consider combining mark types when it adds clarity to your chart** — e.g., points on a line to show trend plus individual values.

### Axes
- **Use a fixed or dynamic axis range depending on the meaning of your chart** — *fixed*: bounds never change; use when specific min/max are meaningful for all data (battery charge 0%–100%). *Dynamic*: bounds vary with data; use when values vary widely and marks should fill the plot area (Health Steps Y-axis upper bound tracks the period's max).
- **Define the value of the lower bound based on mark type and chart usage** — zero works well for bar charts (compare relative heights); but zero can hide meaningful differences, e.g., a heart-rate chart where resting vs. active differences lie far from zero.
- **Prefer familiar sequences of values in the tick and grid-line labels for an axis** — 0, 5, 10… reads instantly; 1, 6, 11… follows the same rule but is uncommon and slows people down.
- **Tailor the appearance of grid lines and labels to a chart's use cases** — too many overwhelm, too few hinder estimation. Consider context, supported interactions, tasks; e.g., if people can inspect points interactively, use fewer grid lines and light label colors.

### Descriptive content
- **Write descriptions that help people understand what a chart does before they view it** — information-rich titles and labels describing purpose/functionality; especially important for VoiceOver users and people with certain cognitive disabilities.
- **Summarize the main message of your chart to help make it approachable and useful for everyone** — e.g., Weather's title and subtitle succinctly describe next-hour precipitation.

### Best practices
- **Establish a consistent visual hierarchy that helps communicate the relative importance of various chart elements** — data most prominent; descriptions and axes provide context without competing.
- **In a compact environment, maximize the width of the plot area to give people enough space to comfortably examine a chart** — keep vertical-axis labels as short as possible without losing clarity; consider describing units elsewhere (e.g., title) and placing a longer axis label (e.g., category name) inside the plot area when it doesn't obscure data.
- **Make every chart in your app accessible** — support VoiceOver; supply accessibility labels and enhance with Audio Graphs (tones representing values and trend, plus high-level text summaries).
- **Let people interact with the data when it makes sense, but don't require interaction to reveal critical information** — e.g., Stocks shows performance for a chosen period (1 day, 3 months, 5 years); dragging a vertical indicator reveals values.
- **Make it easy for everyone to interact with a chart** — if marks are too small to target with finger/pointer, consider expanding the hit target to the entire plot area and let people scrub.
- **Make an interactive chart easy to navigate when using keyboard commands (including full keyboard access) or Switch Control** — by default these visit elements linearly (e.g., data-file order). Two customizations: (1) accessibility APIs (e.g., `accessibilityRespondsToUserInteraction(_:)`) to define a logical, predictable path (e.g., along the X axis); (2) for very large datasets, let focus move among subsets of values. Both also improve VoiceOver even for non-interactive charts.
- **Help people notice important changes in a chart** — animate mark/axis changes, but also highlight them in other ways for VoiceOver users and people who turn off animations (`UIAccessibility.Notification`, `NSAccessibility.Notification`).
- **Align a chart with surrounding interface elements** — e.g., align chart's leading edge with other views; show vertical grid-line labels on their trailing side; consider moving the Y axis to the trailing side so tick labels don't protrude; anchor an orphan-looking label to a grid line with a tick.

### Color
- Color clarifies, evokes brand, provides continuity (see color › Inclusive color).
- **Avoid relying solely on color to differentiate between different pieces of data or communicate essential information in a chart** — supplement with shapes or patterns (e.g., Health blood pressure: red circle for systolic, black/white diamond for diastolic).
- **Aid comprehension by adding visual separation between contiguous areas of color** — e.g., separators between differently colored segments in a stacked bar (iPhone Storage).

### Enhancing the accessibility of a chart
- Swift Charts provides a default Audio Graphs implementation and a default accessibility element per mark (or group) describing its value.
- **Consider using Audio Graphs to give VoiceOver users more information about your chart** — customize with a chart title and descriptive summary. Without Audio Graphs, you must provide an overview: chart type (bar, line…), what each axis represents, upper/lower axis bounds.
- Important: unlike an image (one label), a chart often needs a label for each important or interactive element. Decide whether to describe each mark or groups of marks; sometimes one succinct high-level label suffices (e.g., small chart inside a button that reveals a detailed version).
- **Write accessibility labels that support the purpose of your chart** — Maps elevation chart summarizes changes over portions of the route; Health Steps labels each bar because exact counts are the purpose.
- Label-writing guidelines:
  - **Prioritize clarity and comprehensiveness** — a bare value is rarely enough; add context (date, location) without repeating info available elsewhere (e.g., axis name from Audio Graphs/overview). Context first, then succinct details.
  - **Avoid using subjective terms** — no "rapidly", "gradually", "almost"; use actual values.
  - **Maximize clarity in data descriptions by avoiding potentially ambiguous formats and abbreviations** — "June 6" not "6/6"; "60 minutes"/"60 meters" not "60m".
  - **Describe what the chart's details represent, not what they look like** — identify what each series means, not its colors.
  - **Be consistent throughout your app when referring to a specific axis** — e.g., always mention X axis first.
- **Hide visible text labels for axes and ticks from assistive technologies** — VoiceOver users get values/trends via accessibility labels and Audio Graphs.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS.

### watchOS
- **In general, avoid requiring complex chart interactions in your watchOS app** — prefer glanceable info and simple interactions that add value; use a companion app on another platform for more detail and interaction (e.g., Heart Rate on watch shows today; Health on iPhone shows multiple periods and per-mark inspection).

## APIs
Swift Charts (`Charts`), Audio Graphs (Accessibility), `accessibilityRespondsToUserInteraction(_:)` (SwiftUI), `UIAccessibility.Notification` (UIKit), `NSAccessibility.Notification` (AppKit).

## Related
`charting-data, color, accessibility, gauges, activity-rings, progress-indicators`
