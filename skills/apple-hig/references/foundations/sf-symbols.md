# SF Symbols

> Source: https://developer.apple.com/design/human-interface-guidelines/sf-symbols · Thousands of consistent, highly configurable symbols that integrate with the San Francisco system font, automatically aligning with text in all weights and sizes.

## When to use / core idea
- Use a symbol wherever interface icons appear: toolbars, tab bars, context menus, within text.
- Availability of symbols and features depends on target OS; features introduced in a given year aren't available on earlier OS versions.
- Terms prohibit using symbols (or confusingly similar images) in app icons, logos, or any trademarked use — use custom artwork there (see app-icons, icons).
- Create custom symbols only when SF Symbols lacks what you need.

## Rules

### Rendering modes
- Symbol paths are organized into layers (e.g., `cloud.sun.rain.fill`: primary = cloud, secondary = sun and rays, tertiary = raindrops).
- **Monochrome** — one color on all layers; paths render in that color or as transparent shapes within color-filled paths.
- **Hierarchical** — one color, opacity varied by each layer's hierarchical level (e.g., cloud fully opaque, sun ~50%, raindrops ~25%).
- **Palette** — two or more colors, one per layer; with only two colors on a three-level symbol, secondary and tertiary share a color.
- **Multicolor** — intrinsic colors that enhance meaning (e.g., `leaf` green, `trash.slash` red for data loss); some layers can take other colors.
- Using system-provided colors in any mode ensures adaptation to accessibility accommodations, vibrancy, and Dark Mode.
- **Confirm that a symbol's rendering mode works well in every context** — size and background contrast affect legibility of details; the automatic setting gives the preferred mode, but check where another mode improves legibility.

### Gradients
- SF Symbols 7+: gradient rendering produces a smooth linear gradient from a single source color; works in all rendering modes, with system and custom colors, and on custom symbols. Renders at any size but looks best at larger sizes.

### Variable color
- Represents a changing characteristic (capacity, strength) in any rendering mode by coloring layers as a value crosses thresholds between 0 and 100%. E.g., `speaker.wave.3`: 0 waves colored at no sound, then 1/2/3; thresholds are system-defined by the number of nonzero states.
- Layers can opt out (the speaker body doesn't change). Any number of layers can support variable color.
- **Use variable color to communicate change — don't use it to communicate depth** — use Hierarchical rendering for depth and hierarchy.

### Weights and scales
- 9 weights (ultralight to black), each matching a San Francisco font weight for precise weight matching with adjacent text.
- 3 scales: small, medium (default), large — defined relative to the SF cap height. Scale adjusts emphasis vs. adjacent text without breaking weight matching at the same point size.
- 27 total weight/scale combinations per symbol.

### Design variants
- Outline (most common; no solid areas, resembles text), fill (solid areas within some shapes), slash, and enclosed (circle, square, rectangle); enclosed and slash often combine with outline or fill.
- Use slash to show an item/action is unavailable; fill to indicate selection.
- Language/script variants: Latin, Arabic, Hebrew, Hindi, Thai, Chinese, Japanese, Korean, Cyrillic, Devanagari, several Indic numeral systems — adapt automatically to device language (see right-to-left).
- Outline suits toolbars, lists, and symbols alongside text. Enclosing shapes improve legibility at small sizes. Fill gives more emphasis — good for iOS tab bars, swipe actions, and accent-colored selection.
- Often the containing view picks the variant (iOS tab bar prefers fill; toolbar takes outline), so you needn't specify.

### Animations
- Work on all SF Symbols and custom symbols, in all rendering modes, weights, and scales. Control playback (run once or indefinitely until a condition), speed, and reverse-before-repeat.
- **Appear** — gradually emerges into view.
- **Disappear** — gradually recedes out of view.
- **Bounce** — brief elastic scale up or down then returns; plays once by default; communicates an action occurred or is needed.
- **Scale** — changes size and persists until a new scale is set or effect removed; draws attention to a selected item or gives feedback on choice.
- **Pulse** — varies opacity over time; pulses only layers annotated to pulse (optionally all); for ongoing activity until a condition is met.
- **Variable color** — incrementally varies layer opacity; *cumulative* (changes persist per layer until cycle ends) or *iterative* (one layer at a time); for progress or ongoing activity (playback, connecting, broadcasting). Options: autoreverse; hide inactive layers instead of dimming. Layer arrangement: *open loop* (linear, ends don't meet) vs. *closed loop* (complete shape, e.g., circular progress) — closed loop gives seamless continuous playback.
- **Replace** — swaps symbols across weights and rendering modes; configurations: *Down-up* (out scales down, in scales up — state change), *Up-up* (both scale up — state change with forward progression), *Off-up* (out hides immediately, in scales up — emphasizes next available state/action).
- **Magic Replace** — smart transition between related shapes (slashes draw on/off, badges appear/disappear or replace independently). Default replace animation; between unrelated symbols falls back to down-up (fallback direction customizable).
- **Wiggle** — moves back and forth along a directional axis; highlights an easily overlooked change or call to action, or reinforces meaning (e.g., an arrow's direction).
- **Breathe** — smoothly increases/decreases presence (opacity and size) for status changes or ongoing activity like recording; pulse changes opacity only.
- **Rotate** — rotates whole symbol or parts (By Layer, e.g., desk fan blades only) to indicate in-progress work or imitate real behavior.
- **Draw On / Draw Off** — SF Symbols 7+; draws along a path through guide points, offscreen→onscreen (On) or reverse (Off); all layers at once, staggered, or one at a time; for progress (download) or reinforcing meaning (directional arrow).
- **Apply symbol animations judiciously** — no hard limit, but too many overwhelm and distract.
- **Make sure that animations serve a clear purpose in communicating a symbol's intent** — each type has a discrete meaning; consider how people interpret it and whether combinations confuse.
- **Use symbol animations to communicate information more efficiently** — visual feedback and complex info in little space.
- **Consider your app's tone when adding animations** — align with brand identity, style, and tone.

### Custom symbols
- Start by exporting the template of a similar symbol, then modify in a vector editor.
- Copyrighted symbols depicting Apple products/features can be displayed but not customized; the SF Symbols app badges them with an Info icon and describes restrictions in the inspector.
- *Annotating* assigns a color or hierarchical level (primary/secondary/tertiary) to each layer; different instances can use different rendering modes.
- **Use the template as a guide** — match system symbols in level of detail, optical weight, alignment, position, perspective. Aim for simple, recognizable, inclusive, directly related to the action/content.
- **Assign negative side margins to your custom symbol if necessary** — aids optical horizontal alignment when badges or other elements widen a symbol (e.g., stack of folders, some badged). Use the naming pattern including configuration, e.g., "left-margin-Regular-M".
- **Optimize layers to use animations with custom symbols** — annotate layers in the SF Symbols app; Z-order sets variable color order; animate front-to-back or back-to-front; use layer groups so related layers move together.
- **Test animations for custom symbols** — test all presets. Draw whole shapes: e.g., for a `person.2.fill`-like symbol, draw the full left person plus an offset path of the right person annotated as an erase layer, instead of a cutout — preserves layer info for animation.
- **Avoid making custom symbols that include common variants, such as enclosures or badges** — use the SF Symbols app's component library to create variants consistently.
- **Provide alternative text labels for custom symbols** — accessibility descriptions for VoiceOver.
- **Don't design replicas of Apple products** — copyrighted; and you can't customize symbols identified as Apple features/products.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## Specs
| Property | Values |
| --- | --- |
| Rendering modes | 4: monochrome, hierarchical, palette, multicolor |
| Weights | 9: ultralight → black (match SF font weights) |
| Scales | 3: small, medium (default), large — relative to SF cap height |
| Weight × scale combinations | 27 |
| Variable color range | 0–100% thresholds |
| Gradients, Draw On/Off | SF Symbols 7 and later |
| Symbol animations (see motion) | SF Symbols 5 and later |
| Custom margin naming | e.g., `left-margin-Regular-M` |

## APIs
`renderingMode(_:)` (SwiftUI), `imageScale(_:)` (SwiftUI), `UIImage.SymbolScale` (UIKit), `NSImage.SymbolConfiguration` (AppKit), `SymbolEffect` (Symbols), Symbols framework, Configuring and displaying symbol images in your UI (UIKit), Creating custom symbol images for your app (UIKit)

## Related
typography, icons, right-to-left, branding, voiceover, motion, app-icons, color
