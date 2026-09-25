# Loading

> Source: https://developer.apple.com/design/human-interface-guidelines/loading · The best content-loading experience finishes before people become aware of it.

## When to use / core idea
- Applies whenever an app or game loads assets, levels, or other content; design loading so it doesn't disrupt the experience.
- Use `progress-indicators` for waits beyond a moment or two: *determinate* when duration is known, *indeterminate* when not. For startup, see `launching`.

## Rules
### Best practices
- **Show something as soon as possible** — an empty wait reads as a problem; consider placeholder text, graphics, or animations replaced as content arrives.
- **Let people do other things in your app or game while they wait for content to load** — load in the background (e.g. game loads while players read about the next level or use an in-game menu).
- **If loading takes an unavoidably long time, give people something interesting to view while they wait** — gameplay hints, tips, new features; gauge remaining time accurately to avoid too little time with placeholder content or having to repeat it.
- **Improve installation and launch time by downloading large assets in the background** — consider Background Assets to schedule downloads (level packs, 3D models, textures) right after install, during updates, or at other nondisruptive times.

### Showing progress
- **Clearly communicate that content is loading and how long it might take to complete** — ideally instant; if more than a moment or two, use system progress indicators (determinate if duration known, indeterminate otherwise).
- **For games, consider creating a custom loading view** — standard indicators may feel out of place; use custom animations/elements matching the game's style.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS.
### watchOS
- **As much as possible, avoid showing a loading indicator in your watchOS experience** — aim to display content immediately; if content needs a second or two, a loading indicator is better than a blank screen.

## APIs
Background Assets framework, Improving the player experience for games with large downloads (GameKit)

## Related
`launching, progress-indicators`
