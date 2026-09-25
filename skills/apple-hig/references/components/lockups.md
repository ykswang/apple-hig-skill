# Lockups

> Source: https://developer.apple.com/design/human-interface-guidelines/lockups · Lockups combine multiple separate views into a single, interactive unit (tvOS).

## When to use / core idea
- Each lockup = content view + header (above) + footer (below); all three expand and contract together when the lockup gets focus.
- Four types: cards, caption buttons, monograms, posters.

## Rules
### Best practices
- **Allow adequate space between lockups** — focused lockups expand; leave room to avoid overlapping or displacing others.
- **Use consistent lockup sizes within a row or group** — matching widths and heights look better.

### Cards
- Combine header, footer, and content view to present ratings and reviews for media items.

### Caption buttons
- Title and subtitle beneath the button; button contains an image or text.
- When focused, caption buttons must tilt with the swipe motion: vertically aligned → tilt up/down; horizontally aligned → tilt left/right; in a grid → tilt both.

### Monograms
- Identify people, usually cast and crew: circular picture plus name; initials replace the image if unavailable.
- **Prefer images over initials** — images create a more intimate connection.

### Posters
- Image plus optional title and subtitle, hidden until the poster is focused. Any size, but appropriate for the content.

## Platform considerations
Not supported: iOS, iPadOS, macOS, visionOS, watchOS (tvOS only).

## APIs
`TVLockupView`, `TVLockupHeaderFooterView`, `TVCardView`, `TVCaptionButtonView`, `TVMonogramContentView`, `TVPosterView` (TVUIKit)

## Related
designing-for-tvos, layout, image-views, focus-and-selection
