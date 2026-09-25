# Images

> Source: https://developer.apple.com/design/human-interface-guidelines/images · To make sure your artwork looks great on all devices you support, learn how the system displays content and how to deliver art at the appropriate scale factors.

## When to use / core idea
- Covers resolution/scale factors, file formats, and platform-specific imagery (tvOS layered/parallax images, visionOS scaling and spatial photos, watchOS autoscaling PDFs).
- A *point* is an abstract unit: on 2D platforms it maps to a variable number of pixels; in visionOS it's an angular value so content scales with distance from the viewer.
- *Scale factor* = pixels per point: @1x = 1:1 (1 px = 1 pt), @2x = 2:1, @3x = 3:1 (e.g., a 10x10 px circle @1x is 20x20 px @2x, 30x30 px @3x).

## Rules
### Resolution
- **Provide high-resolution assets for all bitmap images in your app, for every device you support** — append "@1x", "@2x", or "@3x" to filenames in the asset catalog (see Specs; more scale factors in `layout`).
- **In general, design images at the lowest resolution and scale them up to create high-resolution assets** — for resizable vector shapes, place control points at whole values so they align cleanly at 1x and therefore at 2x/3x.

### Best practices
- **Include a color profile with each image** — see `color` (Color management).
- **Always test images on a range of actual devices** — may appear pixelated, stretched, or compressed.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS.

### tvOS
- Layered images + transparency + scaling + motion are central to the Apple TV experience.
- *Parallax*: focused element elevates to the foreground, gently sways, surface illuminates/shines; after inactivity, out-of-focus content dims and the focused element expands. Layered images are required for parallax.
- *Layered image*: **2–5** distinct layers; layers nearer the surface elevate and scale over lower layers for a 3D effect.
- Important: tvOS app icon MUST be a layered image; for other focusable images (incl. Top Shelf) layered images are strongly encouraged but optional.
- Embed layered images or fetch them from a server at runtime. Developer note: server-delivered images must be runtime layered images (`.lcr`), generated from LSR or Photoshop files with Xcode's `layerutil` tool; don't embed `.lcr` in the app.
- **Use standard interface elements to display layered images** — standard views and focus APIs (e.g., `FocusState`) give automatic parallax.
- **Identify logical foreground, middle, and background elements** — foreground: prominent elements (game character, text on album cover/poster); middle: secondary content and effects like shadows; background: opaque backdrop that doesn't upstage.
- **Generally, keep text in the foreground** — unless you want to obscure it.
- **Keep the background layer opaque** — higher layers may vary opacity, but a non-opaque background layer produces an error.
- **Keep layering simple and subtle** — parallax should be almost unnoticeable; excessive 3D is unrealistic and jarring.
- **Leave a safe zone around the foreground layers of your image** — scaling/motion on focus may crop layers; see `app-icons`.
- **Always preview layered images** — via Xcode, Parallax Previewer (macOS), or Parallax Exporter (Photoshop plug-in) throughout design; watch scaling/clipping; finally preview on an actual TV.

### visionOS
- Images viewed at a far wider size range than other platforms; system dynamically scales resolution; image pixels may not map 1:1 to screen pixels because images can sit at angles.
- **Create a layered app icon** — **2–3** layers moving at subtly different rates when focused; see `app-icons`.
- **Prefer vector-based art for 2D images** — avoid bitmaps that may look poor when scaled up (Core Animation layers: see "Drawing sharp layer-based content in visionOS").
- **If you need to use rasterized images, balance quality with performance as you choose a resolution** — @2x looks fine at common distances but isn't dynamically scaled and may not be sharp up close. Higher resolutions increase file size and may hurt runtime performance, especially **over @6x**. Above @2x, apply high-quality image filtering (`CALayer.filters`).
- **Spatial photos and spatial scenes** (RealityKit): *spatial photo* = stereoscopic photo with spatial metadata (iPhone 15 Pro or later, Apple Vision Pro, other compatible cameras). *Spatial scene* = 3D image generated from a 2D image with head-movement-responsive parallax.
- **Make sure spatial photos render correctly in your app** — use stereo HEIC; with spatial metadata, visionOS recognizes it as spatial and applies treatments that reduce stereo-viewing discomfort.
- **Prefer the feathered glass background effect to display text over spatial photos** — adds contrast and blurs detail (`GlassBackgroundEffect`).
- **Take visual comfort into consideration when you make spatial photos from existing 2D content** — metadata like disparity adjustment changes perceived 3D and can cause discomfort from some viewing positions.
- **Display spatial photos and spatial scenes in standalone views** — avoid inline with other content; use a separate view (sheet, window). If stereoscopic images must be inline, add generous spacing around them.
- **Use spatial scenes in your app for specific moments** — each can take up to several seconds to generate (e.g., Photos offers an explicit action). Avoid showing too many at once; use scroll views, pagination, or explicit actions.
- **When displaying immersively, prefer minimal UI** — e.g., Spatial Gallery: one item, small caption, single Back button, swipe to navigate.
- **Prefer displaying larger spatial scenes that you center in someone's field of view** — smaller scenes give less parallax.

### watchOS
- **In general, avoid transparency to keep image files small** — if always composited on the same solid color, include the background in the image. Exception: transparency is required for template images (complication images, menu icons, other interface icons) since the system uses it to apply color.
- **Use autoscaling PDFs to let you provide a single asset for all screen sizes** — design for 40mm and 42mm screens at 2x; WatchKit scales per device (see Specs).

## Specs

### Scale factors
| Platform | Scale factors |
| --- | --- |
| iPadOS, watchOS | @2x |
| iOS | @2x and @3x |
| visionOS | @2x or higher (see visionOS) |
| macOS, tvOS | @1x and @2x |

### Formats
| Image type | Format |
| --- | --- |
| Bitmap or raster work | De-interlaced PNG files |
| PNG graphics that don't require full 24-bit color | An 8-bit color palette |
| Photos | JPEG files, optimized as necessary, or HEIC files |
| Stereo or spatial photos | Stereo HEIC |
| Flat icons, interface icons, and other flat artwork that requires high-resolution scaling | PDF or SVG files |

### watchOS autoscaling PDF (designed at 40mm/42mm @2x)
| Screen size | Image scale |
| --- | --- |
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm | 100% |
| 44mm | 110% |
| 45mm | 119% |
| 49mm | 119% |

### Other values
- tvOS layered images: 2–5 layers. visionOS app icon: 2–3 layers. visionOS raster: performance concern especially above @6x.

## APIs
Images (SwiftUI), `UIImageView` (UIKit), `NSImageView` (AppKit), `FocusState` (SwiftUI), `layerutil` (Xcode CLI), `.lcr` runtime layered images, `CALayer.filters` (Core Animation), `ImagePresentationComponent` (RealityKit), `GlassBackgroundEffect` (SwiftUI), spatial metadata (ImageIO), WatchKit

## Related
layout, color, app-icons, top-shelf, focus-and-selection
