# Charting data

> Source: https://developer.apple.com/design/human-interface-guidelines/charting-data · Presenting data in a chart can communicate information with clarity and appeal.

## When to use / core idea
- Charts communicate complex info without much text and add visual interest/personality; range from glanceable graphics to rich interactive centerpieces.
- Use for data-driven tasks: analyzing trends (historical or predicted), visualizing current state of a changing process/system/quantity, comparing items (or one item over time) across categories.
- Not every dataset needs a chart: if you only need to provide data (not convey info or aid analysis), consider a scrollable, searchable, sortable list or table instead.
- For chart components (marks, axes, etc.) see `charts`.

## Rules
### Best practices
- **Use a chart when you want to highlight important information about a dataset** — charts are visually prominent and draw attention; clearly communicate what people can learn.
- **Keep a chart simple, letting people choose when they want additional details** — too much data overwhelms and obscures relationships; consider revealing data/functionality gradually (levels of detail, subsets); to teach an interactive chart, consider several versions each with more functionality.
- **Make every chart in your app accessible** — besides visual descriptions, provide accessibility labels describing chart values/components and accessibility elements that help people interact with the chart (see `charts` accessibility).

### Designing effective charts
- **In general, prefer using common chart types** — e.g. bar, line; people likely already know how to read them.
- **If you need to create a chart that presents data in a novel way, help people learn how to interpret the chart** — e.g. Activity animates each ring individually at Watch pairing to map rings to move/exercise/stand.
- **Examine the data from multiple levels or perspectives to find details you can display to enhance the chart** — macro: totals/averages; mid-level: useful subsets; individual points: call attention to specific values.
- **Aid comprehension by adding descriptive text to the chart** — titles, subtitles, annotations emphasize key info and actionable takeaways; a brief headline/summary (e.g. Weather's "Chance of light rain in the next hour") aids glanceability. A summary doesn't replace accessibility labels.
- **Match the size of a chart to its functionality, topic, and level of detail** — large enough to comfortably show details, labels, annotations and support intended interactivity (changing scope, exploring perspectives); small charts suit glanceable info about one item or a preview of a larger version shown elsewhere.
- **Prefer consistency across multiple charts, deviating only when you need to highlight differences** — different types/styles for similar-purpose charts imply they're unrelated; consistency lets learning transfer. Consider different types/styles to highlight meaningful differences.
- **Maintain continuity among multiple charts that use the same data** — use one chart type and consistent colors, annotations, layouts, descriptive text to signal same dataset (e.g. Health Trends small chart → expanded version keeps style, colors, marks, annotations).

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## APIs
`Swift Charts` (Charts framework)

## Related
`charts`
