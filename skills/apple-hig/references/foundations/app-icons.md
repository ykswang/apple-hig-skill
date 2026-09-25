# App icons

> Source: https://developer.apple.com/design/human-interface-guidelines/app-icons · A unique, memorable icon expresses your app's or game's purpose and personality and helps people recognize it at a glance.

## When to use / core idea
- App icon appears on the Home Screen and throughout the system (search, notifications, Settings, share sheets); keep identity consistent across all platforms.
- Prefer layered icons over a flattened image — the system applies environment/interaction-responsive effects per platform.
- For in-app interface icons/glyphs see `icons`; for symbols see `sf-symbols`.

## Rules
### Layer design
- iOS, iPadOS, macOS, watchOS: background layer + one or more foreground layers; system adds Liquid Glass attributes (specular highlights, refraction, translucency) that adapt with size, are consistent across platforms, and may differ between system versions.
- tvOS: **2–5 layers**; on focus the icon elevates, sways with remote finger movement, surface illuminates; layer separation + transparency produce parallax depth.
- visionOS: background layer + **one or two** layers on top, forming a 3D object that subtly expands when viewed; system adds inter-layer shadows and uses upper layers' alpha channel for an embossed look.
- Workflow: craft foreground layers in your design tool. iOS/iPadOS/macOS/watchOS → import into **Icon Composer** (define background, place foreground, apply specular/refraction, annotate default/dark/mono variants, preview across system versions, export for Xcode). tvOS/visionOS → add layers to an image stack in Xcode; preview with Parallax Previewer / Parallax Exporter plug-in (Apple Design Resources).
- **Prefer clearly defined edges in foreground layers** — avoid soft/feathered edges so system highlights and shadows look best.
- **Vary opacity in foreground layers to increase the sense of depth and liveliness** — e.g., Photos' translucent pieces. Import fully opaque layers and adjust transparency in Icon Composer to preview interplay with system effects.
- **Design a background that both stands out and emphasizes foreground content** — gradients must respond well to system lighting. Icon Composer supports solid colors and gradients, so custom background images are usually unnecessary; any imported background must be full-bleed and opaque.
- **Prefer vector graphics when bringing layers into Icon Composer** — SVG or PDF; outline artwork and convert text to outlines. For mesh gradients and raster artwork, prefer PNG (lossless).

### Icon shape
- iOS, iPadOS, macOS: square, system masks to rounded corners matching system UI and device bezel. tvOS: rectangular with concentric rounded edges. visionOS, watchOS: square, system applies circular mask.
- **Produce appropriately shaped, unmasked layers** — square for iOS/iPadOS/macOS/visionOS/watchOS, rectangular for tvOS. Pre-masked layers degrade specular highlights and make edges jagged.
- **Keep primary content centered to avoid truncation when the system adjusts corners or applies masking** — especially visionOS and watchOS; use grids in the production templates (Apple Design Resources).

### Design
- Embrace simplicity: one core concept expressed with a minimal number of shapes; fine details look busy with system shadows/highlights and vanish at small sizes. Prefer a simple background (solid color or gradient); no need to fill the whole canvas.
- **Provide a visually consistent icon design across all the platforms your app supports** — prevents mistaking it for multiple apps.
- **Consider basing your icon design around filled, overlapping shapes** — overlapping solid shapes with transparency and blurring convey depth (vs. outline-only shapes).
- **Include text only when it's essential to your experience or brand** — text isn't accessible or localizable, is often too small, clutters, and app name often appears nearby. A mnemonic (e.g., first letter) can help; avoid nonessential words ("Watch", "Play") and context terms ("New", "For visionOS"). tvOS: put text above other layers so parallax doesn't crop it.
- **Prefer illustrations to photos and avoid replicating UI components** — photos don't work across appearances, small sizes, or layers. Avoid extremely thin line weights and sharp corners (lose detail at small sizes). Don't replicate standard UI components or use app screenshots.
- **Don't use replicas of Apple hardware products** — copyrighted.

### Visual effects
- **Let the system handle blurring and other visual effects** — don't bake in specular highlights, inter-layer drop shadows, bevels, blurs, glows; custom effects are static and conflict with dynamic system ones. If you include any, use intentionally and test in Icon Composer, a simulated device in Device Hub, or a physical device.
- **Create layer groupings to apply effects to multiple layers at once** — Icon Composer groups expose extra Liquid Glass options (specular highlights, refraction, translucency).

### Appearances
- iOS, iPadOS, macOS: people choose default, dark, clear, or tinted Home Screen icons. Provide variants for every appearance; system generates any you omit.
- **Keep your icon's features consistent across appearances** — same core visual features; avoid variants that swap elements in and out.
- **Design dark and tinted icons that feel at home beside system app icons and widgets** — can keep default palette, but dark is more subdued, clear and tinted even more; must stay visible, legible, recognizable.
- **Use your light app icon as the basis for your dark icon** — complementary colors reflecting the default; avoid excessively bright images; color backgrounds generally give the greatest contrast in dark icons.
- **Consider offering alternate app icons** — iOS, iPadOS, tvOS, and compatible apps in visionOS can let people pick an alternate in app settings (e.g., team icons). Keep each closely related to your content; avoid ones mistakable for another app.
- Note: iOS/iPadOS alternate icons need their own dark, clear, and tinted variants; all icons/variants are subject to App Review Guidelines.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS.

### tvOS
- **Include a safe zone to ensure the system doesn't crop your content** — focus scaling/motion may crop edges; safe zone varies by image size, layer depth, motion; foreground layers are cropped more than background layers.

### visionOS
- **Avoid adding a shape that's intended to look like a hole or concave area to the background layer** — system shadows/highlights make it stand out instead of recede.

### watchOS
- **Avoid using black for your icon's background** — lighten it so the icon doesn't blend into the display background.

## Specs
| Platform | Layout shape | Icon shape after system masking | Layout size | Style | Appearances |
| --- | --- | --- | --- | --- | --- |
| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
| tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800x480 px | Layered (Parallax) | N/A |
| visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |
| watchOS | Square | Circular | 1088x1088 px | Layered | N/A |

- System automatically scales icons to smaller variants (Settings, notifications, etc.).
- Layers: tvOS 2–5; visionOS background + 1–2.
- Color spaces: sRGB (color); Gray Gamma 2.2 (grayscale); Display P3 (wide-gamut, iOS, iPadOS, macOS, tvOS, watchOS only).
- Layer file formats: SVG/PDF preferred; PNG for mesh gradients and raster.

## APIs
Icon Composer (Xcode), app icon asset catalog / image stacks (Xcode), Parallax Previewer, Parallax Exporter

## Related
icons, images, dark-mode, branding, materials
