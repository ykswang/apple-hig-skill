# Image views

> Source: https://developer.apple.com/design/human-interface-guidelines/image-views · An image view displays a single image — or sometimes an animated sequence of images — on a transparent or opaque background.

## When to use / core idea
- Image can be stretched, scaled, sized to fit, or pinned to a location. Typically not interactive.
- For interactive images use a button; for icons use SF Symbols or interface icons; for editable images on macOS use an image well.

## Rules
### Best practices
- **Use an image view when the primary purpose of the view is simply to display an image** — in rare interactive cases, configure a system button to display the image rather than adding button behaviors to an image view.
- **If you want to display an icon in your interface, consider using a symbol or interface icon instead of an image view** — SF Symbols are vector, renderable with various colors/opacities; an interface icon (glyph/template image) is typically a bitmap whose nontransparent pixels receive color. Both can use people's accent colors.

### Content
- Supports PNG, JPEG, PDF, etc. (see images).
- **Take care when overlaying text on images** — hurts image clarity and text legibility; ensure contrast, consider a text shadow or background layer.
- **Aim to use a consistent size for all images in an animated sequence** — prescaling avoids system scaling; when the system must scale, performance is better if all images share size and shape.

## Platform considerations
No additional considerations: iOS, iPadOS.

### macOS
- **If your app needs an editable image view, use an image well** — supports copy, paste, drag, and Delete key to clear.
- **Use an image button instead of an image view to make a clickable image** — contains an image/icon and initiates an instantaneous app-specific action.

### tvOS
- Many images combine multiple transparent layers for depth (see images › Layered images).

### visionOS
- Image views in windows can show 2D and stereoscopic images and spatial photos. With RealityKit you can display any image type outside image views next to 3D content, or generate a spatial scene from a 2D image (`ImagePresentationComponent`). See images › visionOS; windows › visionOS for other 3D content.

### watchOS
- **Use SwiftUI to create animations when possible** — alternatively WatchKit can animate an image sequence in an image element (`WKImageAnimatable`).

## APIs
`Image` (SwiftUI), `UIImageView` (UIKit), `NSImageView` (AppKit), `ImagePresentationComponent` (RealityKit), `WKImageAnimatable` (WatchKit).

## Related
`images, image-wells, buttons, sf-symbols, icons, windows`
