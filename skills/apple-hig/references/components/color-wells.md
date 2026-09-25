# Color wells

> Source: https://developer.apple.com/design/human-interface-guidelines/color-wells · Lets people adjust the color of text, shapes, guides, and other onscreen elements.

## When to use / core idea
- Tapping/clicking a color well displays a color picker — system-provided or a custom interface you design.

## Rules
### Best practices
- **Consider the system-provided color picker for a familiar experience** — consistent across apps, lets people save a color set accessible from any app, familiar across iOS, iPadOS, macOS.

## Platform considerations
No additional considerations: iOS, iPadOS, visionOS. Not supported: tvOS, watchOS.
### macOS
- Clicking highlights the well (visual confirmation it's active), then opens a color picker; after selection the well updates to show the new color.
- Supports drag and drop: well → well, and color picker → well.

## APIs
`UIColorWell` (UIKit), `UIColorPickerViewController` (UIKit), `NSColorWell` (AppKit), Color Programming Topics.

## Related
`color`
