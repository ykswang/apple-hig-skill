# Rating indicators

> Source: https://developer.apple.com/design/human-interface-guidelines/rating-indicators · A rating indicator uses a series of horizontally arranged graphical symbols — by default, stars — to communicate a ranking level.

## When to use / core idea
- macOS-only control for showing/editing a rank (a style of `NSLevelIndicator`).
- Never displays partial symbols — rounds to whole symbols. Symbols are always equally spaced and don't expand/shrink to fit the component's width.
- For in-app rating prompts, see ratings-and-reviews.

## Rules
### Best practices
- **Make it easy to change rankings** — in a list of ranked items, let people adjust rank inline without navigating to a separate editing screen.
- **If you replace the star with a custom symbol, make sure that its purpose is clear** — stars are highly recognizable; people may not associate other symbols with rating.

## Platform considerations
No additional considerations: macOS. Not supported: iOS, iPadOS, tvOS, visionOS, watchOS.

## APIs
`NSLevelIndicator.Style.rating` (AppKit).

## Related
`ratings-and-reviews, gauges`
