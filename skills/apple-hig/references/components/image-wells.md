# Image wells

> Source: https://developer.apple.com/design/human-interface-guidelines/image-wells · An editable version of an image view.

## When to use / core idea
- macOS only. After selecting, people can copy/paste or delete its image; they can drag a new image in without selecting first.

## Rules
### Best practices
- **Revert to a default image when necessary** — if the well requires an image, redisplay the default when people clear it.
- **If your image well supports copy and paste, make sure the standard copy and paste menu items are available** — people expect those menu items and standard keyboard shortcuts (see Edit menu in `the-menu-bar`).

## Platform considerations
Not supported: iOS, iPadOS, tvOS, visionOS, watchOS.

## APIs
`NSImageView` (AppKit)

## Related
`image-views, the-menu-bar`
