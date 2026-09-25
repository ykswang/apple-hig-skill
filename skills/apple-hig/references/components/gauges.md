# Gauges

> Source: https://developer.apple.com/design/human-interface-guidelines/gauges · A gauge displays a specific numerical value within a range of values.

## When to use / core idea
- Shows a current value in a range and can add context about the range (e.g., temperature gauge with high/low text and a color spectrum).
- Alternatives: progress indicators (task progress), activity rings (Move/Exercise/Stand only), macOS level indicators (capacity, rating, relevance), rating-indicators.

## Anatomy
- Circular or linear path representing the range; current value maps to a point on it.
- **Standard** style: an indicator shows the value's location. **Capacity** style: a fill stops at the value's location.
- **Accessory** variant (circular/linear, standard/capacity) looks like watchOS complications — good for iOS Lock Screen widgets and anywhere echoing complications.
- macOS also has level indicators, some visually similar to gauges.

## Rules
### Best practices
- **Write succinct labels that describe the current value and both endpoints of the range** — not every style shows all labels, but VoiceOver reads visible labels.
- **Consider filling the path with a gradient to help communicate the purpose of the gauge** — e.g., red→blue for hot→cold.

## Platform considerations
No additional considerations: iOS, iPadOS, visionOS, watchOS. Not supported: tvOS.

### macOS
- Level indicator displays a value in a range; configurable as capacity, rating, or (rarely) relevance.
- Capacity style, two forms:
  - **Continuous** — horizontal translucent track filling with a solid bar.
  - **Discrete** — horizontal row of separate, equally sized rectangular segments; segment count = total capacity; segments fill completely, never partially.
- **Consider using the continuous style for large ranges** — large ranges make discrete segments too small to be useful.
- **Consider changing the fill color to inform people about significant parts of the range** — default fill is green for both capacity styles; change color at levels like very low, very high, or just past middle. Change the whole indicator's color, or use the *tiered* state to show several colors in one indicator (e.g., red → yellow → green segments).
- Rating style: see rating-indicators.
- Relevance style (rarely used): shaded horizontal bar, e.g., in search results to visualize relevance when sorting/comparing.

## APIs
`Gauge` (SwiftUI), `NSLevelIndicator` (AppKit).

## Related
`ratings-and-reviews, rating-indicators, progress-indicators, widgets, complications`
