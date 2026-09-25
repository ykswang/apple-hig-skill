# Materials

> Source: https://developer.apple.com/design/human-interface-guidelines/materials · A material is a visual effect that creates a sense of depth, layering, and hierarchy between foreground and background elements.

## When to use / core idea
- Materials separate foreground (text, controls) from background (content, solid colors) while letting color pass through, establishing hierarchy and sense of place.
- Two types:
  - **Liquid Glass** — dynamic material forming a distinct functional layer for controls and navigation (tab bars, sidebars) floating above the content layer; content scrolls and peeks through beneath while controls stay legible.
  - **Standard materials** (blur, vibrancy, blending modes) — for visual differentiation/structure *within the content layer*, beneath Liquid Glass.
- Color on glass: see `color` (Liquid Glass color).

## Rules
### Liquid Glass
- **Don't use Liquid Glass in the content layer** — it confuses hierarchy; use standard materials for content-layer elements such as app backgrounds. Exception: content-layer controls with a transient interactive element (sliders, toggles) take on Liquid Glass while activated to emphasize interactivity.
- **Use Liquid Glass effects sparingly** — standard components adopt it automatically; limit custom-control use to the most important functional elements, since overuse distracts from content.
- **Only use clear Liquid Glass for components that appear over visually rich backgrounds** — variants `regular` and `clear`; appearance may change with the person's preferred Liquid Glass look and with Reduce Transparency / Increase Contrast.
  - *Regular*: blurs and adjusts luminosity of background content for legibility; scroll edge effects further blur and reduce opacity of background content. Used by most system components. Use when background may cause legibility issues or components hold significant text (alerts, sidebars, popovers).
  - *Clear*: highly translucent; prioritizes visibility of rich backgrounds. Use for components floating above media (photos, videos) for immersion.
  - Dimming layer for clear glass: if underlying content is bright, consider a dark dimming layer of **35% opacity**. Not needed if content is sufficiently dark or when using AVKit standard media playback controls (they provide their own dimming).

### Standard materials
- **Choose materials and effects based on semantic meaning and recommended usage** — not on the apparent color they impart; system settings can change appearance/behavior.
- **Help ensure legibility by using vibrant colors on top of materials** — system-defined vibrant colors stay legible across contexts (e.g., `systemGray3` symbol on material is hard to see; vibrant color is clear).
- **Consider contrast and visual separation when choosing a material to combine with blur and vibrancy effects** — thicker (more opaque) materials give better contrast for text and fine features; thinner (more translucent) materials help people retain context of background content.

## Platform considerations

### iOS, iPadOS
- Four standard materials for the content layer: `ultraThin`, `thin`, `regular` (default), `thick`.
- Vibrant colors for labels, fills, separators designed per material. Labels and fills have several levels; separators one. Default level = highest contrast; quaternary (when present) = lowest.
- Label vibrancy (usable on any material except quaternary): `UIVibrancyEffectStyle.label` (default), `.secondaryLabel`, `.tertiaryLabel`, `.quaternaryLabel`. In general, avoid quaternary on `thin` and `ultraThin` — contrast too low.
- Fill vibrancy (all materials): `.fill` (default), `.secondaryFill`, `.tertiaryFill`.
- Separator: single default `.separator` vibrancy, works on all materials.

### macOS
- Several standard materials with designated purposes (`NSVisualEffectView.Material`) and vibrant versions of all system colors.
- **Choose when to allow vibrancy in custom views and controls** — test in various contexts to find where vibrancy improves appearance and communication.
- **Choose a background blending mode that complements your interface design** — two modes: *behind window* and *within window* (`NSVisualEffectView.BlendingMode`).

### tvOS
- Liquid Glass throughout navigation elements and system experiences (Top Shelf, Control Center); image views and buttons adopt Liquid Glass when focused.
- Standard materials still available for content-layer structure; thickness sets how much underlying content shows through (see Specs table).

### visionOS
- Windows generally use an unmodifiable system material called *glass* that lets light, the current Environment, virtual content, and surroundings show through; it limits background color range to keep contrast, brightening/darkening with surroundings.
- Note: no distinct Dark Mode; glass adapts automatically to luminance behind it.
- **Prefer translucency to opaque colors in windows** — opacity blocks view and feels constricting.
- **If necessary, choose materials that help you create visual separations or indicate interactivity in your app** — for custom components:
  - `thin` — draws attention to interactive elements like buttons and selected items.
  - `regular` — visually separates sections (sidebar, grouped table view).
  - `thick` — dark element that stays distinct on top of a `regular` background (e.g., text field).
- visionOS applies vibrancy to text, symbols, fills on materials, pulling light/color forward. Three levels:
  - `UIVibrancyEffectStyle.label` — standard text.
  - `.secondaryLabel` — descriptive text (footnotes, subtitles).
  - `.tertiaryLabel` — inactive elements, only when text doesn't need high legibility.

### watchOS
- **Use materials to provide context in a full-screen modal view** — material contrast orients people and distinguishes controls/system elements. Avoid removing or replacing default material backgrounds of modal sheets.

## Specs
| Material (tvOS) | Recommended for |
| --- | --- |
| `ultraThin` | Full-screen views that require a light color scheme |
| `thin` | Overlay views that partially obscure onscreen content and require a light color scheme |
| `regular` | Overlay views that partially obscure onscreen content |
| `thick` | Overlay views that partially obscure onscreen content and require a dark color scheme |

- Clear Liquid Glass dimming layer over bright content: dark, 35% opacity.
- iOS/iPadOS materials: ultraThin, thin, regular (default), thick. Vibrancy levels: labels 4, fills 3, separator 1.

## APIs
`Applying Liquid Glass to custom views` (SwiftUI), `regular` (SwiftUI), `clear` (SwiftUI), `blur` (UIKit), `vibrancy` (UIKit), `blending modes` (AppKit), `Material` (SwiftUI), `thin` (SwiftUI), `ultraThin` (SwiftUI), `UIVibrancyEffectStyle.label` (UIKit), `UIVibrancyEffectStyle.secondaryLabel` (UIKit), `UIVibrancyEffectStyle.tertiaryLabel` (UIKit), `UIVibrancyEffectStyle.quaternaryLabel` (UIKit), `UIVibrancyEffectStyle.fill` (UIKit), `UIVibrancyEffectStyle.secondaryFill` (UIKit), `UIVibrancyEffectStyle.tertiaryFill` (UIKit), `separator` (UIKit), `NSVisualEffectView.Material` (AppKit), `NSVisualEffectView.BlendingMode` (AppKit), `thick` (SwiftUI), `Adopting Liquid Glass` (technologyoverviews), `glassEffect(_:in:)` (SwiftUI), `UIVisualEffectView` (UIKit), `NSVisualEffectView` (AppKit)

## Related
color, accessibility, dark-mode, sliders, toggles, top-shelf
