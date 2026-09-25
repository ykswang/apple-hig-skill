# Widgets

> Source: https://developer.apple.com/design/human-interface-guidelines/widgets · A widget provides quick access to essential information and focused interactions from your app or game in additional contexts.

## When to use / core idea
- Timely, glanceable content plus narrow functionality, shown outside the app: iPhone/iPad Home Screen and Lock Screen, Mac desktop and Notification Center, horizontal/vertical surfaces in visionOS, Smart Stack on Apple Watch.
- Widgets refresh periodically; they do NOT support continuous real-time updates — for frequent, time-limited progress tracking use Live Activities instead.
- Lock Screen widgets behave like watch complications — also follow `complications`.
- Design decisions: which sizes to support, which contexts (devices/system experiences) it appears in, and which rendering modes/color treatments it gets there. WidgetKit supplies default appearances, but consider a custom design per context.

### Anatomy
- **System family widgets**: Small, Medium, Large, Extra large, Extra large portrait; may include one or more interactive elements.
- **Accessory widgets**: Circular, Corner, Inline, Rectangular; very limited information.
- **Appearances**: full-color, monochrome with a tint color, or clear/translucent. System may apply tinted or clear appearance to the widget and its full-color images, symbols, glyphs.
  - iPhone/iPad Home Screen: people pick light, dark, clear, tinted. Light/dark = full color. Clear = system desaturates, adds translucency, highlights, Liquid Glass material. Tinted = system desaturates widget and content, then applies the person's tint color.
  - Apple Vision Pro: 3D object in a frame, full color with glass- or paper-like coating responding to lighting; optional tinted appearance from system-provided palettes.
  - iPad Lock Screen: monochromatic, no tint.
  - iPhone Lock Screen in StandBy: scaled up, background removed; below an ambient-light threshold, rendered monochromatic red.
  - Rectangular accessory: monochromatic without tint on iPhone/iPad Lock Screen; on Apple Watch, complication in full-color and tinted, and in the Smart Stack.
- **Rendering modes**:
  - *Full color* — system family widgets on all platforms; doesn't change your view colors.
  - *Accented* — system family widgets on all platforms and accessory widgets on Apple Watch. Removes background, replaces with tinted color effect (tinted appearance) or Liquid Glass background (clear appearance); splits views into accent group and primary group and applies a solid color to each.
  - *Vibrant* — iPhone/iPad Lock Screen and iPhone StandBy in low light. Desaturates text, images, gauges; colors content for Lock Screen background or macOS desktop. People can tint the Lock Screen; StandBy low light gets red tint.

## Rules
### Best practices
- **Choose simple ideas that relate to your app's main purpose** — include timely content and relevant functionality (e.g., Weather prioritizes current high/low and conditions).
- **Aim to create a widget that gives people quick access to the content they want** — meaningful content, useful actions, deep links; replicating an app icon adds little value.
- **Prefer dynamic information that changes throughout the day** — static-looking content gets demoted; keep content fresh even though updates aren't minute-to-minute.
- **Look for opportunities to surprise and delight** — e.g., unique treatment on birthdays or holidays.
- **Offer widgets in multiple sizes when doing so adds value** — small = typically one piece of information; larger = more layers and actions. Avoid expanding a smaller widget's content just to fill a larger area. One widget in the best-fit size beats all sizes.
- **Balance information density** — sparse looks unnecessary, dense isn't glanceable. Essentials at a glance, detail on a longer look. If too dense, consider a larger size or replacing text with graphics.
- **Display only the information that's directly related to the widget's main purpose** — larger sizes can show more/detailed data but stay centered on the primary purpose.
- **Use brand elements thoughtfully** — brand colors, typefaces, stylized glyphs, without overpowering information or looking out of place. Logo/app icon seldom needed; if one helps (e.g., multi-source content), a small logo in the top-right corner is sufficient.
- **Choose between automatically displaying content and letting people customize displayed information** — e.g., Stocks is configurable; Podcasts shows recent content automatically.
- **Avoid mirroring your widget's appearance within your app** — a lookalike element that doesn't behave like the widget confuses people.
- **Let people know when authentication adds value** — e.g., "Sign in to view reservations" when signed out.

### Updating widget content
- System may adjust update limits depending on various factors.
- **Keep your widget up to date** — match frequency to how often data changes and when people need it (e.g., tidal widget updating hourly is useful). If people check more often than you can update, consider showing when data was last updated.
- **Use system functionality to refresh dates and times in your widget** — preserves update budget. Show content quickly; don't hide stale data behind placeholder content.
- **Use animated transitions to bring attention to data updates** — many SwiftUI views animate by default; standard/custom animations up to **2 seconds**.

### Adding interactivity
- Tap/click launches the app; widgets can include buttons and toggles (e.g., Reminders completion toggles). Interactions outside buttons/toggles launch the app.
- **Offer simple, relevant functionality and reserve complexity for your app.**
- **Ensure that a widget interaction opens your app at the right location** — deep link to related details/actions (e.g., Stocks medium widget opens that symbol's page).
- **Offer interactivity while remaining glanceable and uncluttered** — multiple targets (SwiftUI links, buttons, toggles) OK but avoid app-like layouts; size targets for confident tapping without accidental interactions. Inline accessory widgets offer only one tap target.

### Choosing margins and padding
- Widgets scale across devices; iOS resizes content designed for large devices down to small devices; iPadOS renders at large size then scales down on Home Screen. Use Specs values and Apple Design Resources; build production widgets in SwiftUI.
- **In general, use standard margins to ensure legibility** — standard margin **16 pt** for most widgets; tighter **11 pt** margins can work for content groupings (graphics, buttons, background shapes). Widgets use smaller margins on the Mac desktop and on the Lock Screen (incl. StandBy).
- **Coordinate the corner radius of your content with the corner radius of the widget** — use a SwiftUI container (`ContainerRelativeShape`).

### Displaying text in widgets
- **Prefer using the system font, text styles, and SF Symbols** — custom fonts sparingly and legible at a glance; often works well: custom font for large text, SF Pro for smaller text.
- **Avoid very small font sizes** — generally **≥ 11 pt**; smaller is too hard for many people to read.
- **Avoid rasterizing text** — always use text elements/styles so text scales and VoiceOver can speak it.
- Note: iOS, iPadOS, visionOS widgets support Dynamic Type sizes **Large to AX5** when using `Font` system font or `custom(_:size:)`.

### Using color
- **Use color to enhance a widget's appearance without competing with its content** — asset catalog can also specify colors for the widget's editing-mode UI.
- **Convey meaning without relying on specific colors to represent information** — widgets may be monochromatic (with/without tint), and watchOS may invert colors per watch face; add text and iconography.
- **Use full-color images judiciously** — tinted/clear appearances desaturate images by default; you can opt into full color, but it draws special attention and may feel out of place (e.g., in clear appearance). Consider reserving full-color images for media content (e.g., album art) and making them smaller than the widget.

### Rendering modes
- **Full-color — Support light and dark appearances.** Prefer light backgrounds for light appearance, dark for dark; consider semantic system colors for text/backgrounds, or color variants in the asset catalog.
- **Accented — Group widget components into an accented and a primary group.** iPhone, iPad, Mac: primary and accented content tinted white. Apple Watch: primary white, accented in the watch face color. (`widgetAccentable(_:)`)
- **Vibrant — Offer enough contrast to ensure legibility.** Pixel opacity sets the strength of the blurred background material (fully transparent = material passes through). Pixel brightness sets vibrancy: brighter grays = more contrast, darker = less.
- **Vibrant — Create optimized assets for the best vibrant effect.** Render images, numbers, text at full opacity. White/light gray for most prominent content, darker grays for secondary. Verify contrast in grayscale; use opaque grayscale values, not opacities of white.

### Previews and placeholders
- **Design a realistic preview to display in the widget gallery** — show capabilities of each type/size; real data OK, but use realistic simulated data if real data is slow to load.
- **Design placeholder content that helps people recognize your widget** — static interface components + semi-opaque shapes for dynamic content (rectangles of varying widths for text lines, circles/squares for glyphs/images).
- **Write a succinct widget description** — begin with an action verb ("See the current weather conditions and forecast for a location"); avoid "This widget shows…", "Use this widget to…", "Add this widget"; approachable language, sentence-style capitalization.
- **Group your widget's sizes together, and provide a single description** — so sizes aren't mistaken for different widgets.
- **Consider coloring the Add button** — the gallery's Add button can use your brand color.

## Platform considerations
No additional considerations: macOS. Not supported: tvOS.

### iOS, iPadOS
- Lock Screen widgets follow `complications` principles too; provide useful information, don't treat them only as a launcher. Consider designing complications and Lock Screen widgets in tandem.
- Lock Screen shapes: inline text above the clock; circular and rectangular below the clock.
- **Support the Always-On display on iPhone** — Lock Screen widgets render with reduced luminance; use gray levels with enough contrast and keep content legible.
- **Offer Live Activities to show real-time updates** — widgets don't show real-time info; widgets and Live Activities share frameworks/design, so consider building in tandem and reusing code/components.
- **StandBy and CarPlay**: StandBy shows two small system family widgets side by side, scaled up to fill the Lock Screen. Supporting StandBy also makes widgets work in CarPlay; both use the small system family widget with background removed and scaled to the Widgets screen grid. Glanceable info and large text especially important in CarPlay.
- **Limit usage of rich images or color to convey meaning in StandBy** — scale up and rearrange text for reading at a distance; don't use background colors in StandBy (blend with black background).
- StandBy in low light: monochromatic with red tint.

### visionOS
- Widgets are 3D objects placed on horizontal or vertical surfaces; persist in location across power cycles; consistent real-world scale. Perception depends on size, *mounting style*, *treatment style*.
- Full-color by default; accented rendering mode when people tint them with system palettes. People can customize frame width (elevated style) and widget-specific options. No systemwide light/dark (e.g., Music poster widget offers its own light/dark theme from album art).
- **Adapt your design and content for the spatial experience Apple Vision Pro provides** — widgets live in living rooms, kitchens, offices; e.g., Music poster glanceable across a room; productivity small widget fits on a desk.
- **Test your widgets across the full range of system color palettes and in different lighting conditions** — keep tone, contrast, legibility consistent; if excluding elements from tinting, test every palette.
- **Thresholds**: two level-of-detail thresholds — `simplified` (viewed at a distance) and `default` (nearby). Match widget size to content type and viewing distances.
- **Design a responsive layout that shows the right level of detail for each of the two thresholds** — distance: fewer details, larger type, remove interactive elements (buttons, toggles); nearby: more detail, smaller type; keep shared elements across both.
- **Offer widget family sizes that fit a person's surroundings well** — e.g., small for a desk; extra large for artwork/photography decor.
- **Display content in a way that remains legible from a range of distances** — people can scale widgets **75–125%**; use print principles (hierarchy, strong typography, scale); include high-resolution assets.
- **Mounting styles**:
  - *Elevated* (default; works on horizontal and vertical): on horizontal surfaces always elevated, tilts gently backward, casts soft shadow; on vertical surfaces sits flush like a picture frame.
  - *Recessed*: vertical surfaces only; content set back into surface like a cutout. Not used on horizontal surfaces.
- **Choose the mounting style that fits your content and the experience you want to create** — elevated for content that should stand out (reminders, media, glanceable data); recessed for immersive/ambient content (weather, editorial). You can opt out of a style per widget; recessed-only widgets can't go on horizontal surfaces (e.g., weather window-illusion for large/XL, elevated-only for small).
- Developer note: `supportedMountingStyles(_:)` on `WidgetConfiguration` applies to all widgets in the configuration; use separate configurations to mix single-style and dual-style widgets.
- **Test your elevated widget designs with each system-provided frame width** — you can't change layout per frame width; keep layout balanced for each.
- **Treatment styles**: *paper* — grounded, print-like, whole widget darkens/lightens with lighting; *glass* — lighter layered look separating foreground/background; foreground stays bright and legible regardless of ambient light.
- **Choose the paper style for a print-like look that feels more like a real object in the room** — e.g., Music poster widget as framed artwork.
- **Choose the glass style for information-rich widgets** — foreground in full color unaffected by lighting (e.g., News headlines crisp over soft editorial images).

### watchOS
- **Provide a colorful background that conveys meaning** — Smart Stack default is black; e.g., Stocks red for falling, green for rising.
- **Encourage the system to display or elevate the position of your watchOS widget in the Smart Stack** — provide relevance info (location-based or ongoing system actions like a workout) via RelevanceKit.

## Specs

### System family widget contexts
| Widget size | iPhone | iPad | Mac | Apple Vision Pro |
| --- | --- | --- | --- | --- |
| System small | Home Screen, Today View, StandBy, and CarPlay | Home Screen, Today View, and Lock Screen | Desktop and Notification Center | Horizontal and vertical surfaces |
| System medium | Home Screen and Today View | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System large | Home Screen and Today View | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System extra large | Not supported | Home Screen and Today View | Desktop and Notification Center | Horizontal and vertical surfaces |
| System extra large portrait | Not supported | Not supported | Not supported | Horizontal and vertical surfaces |

### Accessory widget contexts
| Widget size | iPhone | iPad | Apple Watch |
| --- | --- | --- | --- |
| Accessory circular | Lock Screen | Lock Screen | Watch complications and in the Smart Stack |
| Accessory corner | Not supported | Not supported | Watch complications |
| Accessory inline | Lock Screen | Lock Screen | Watch complications |
| Accessory rectangular | Lock Screen | Lock Screen | Watch complications and in the Smart Stack |

### Rendering modes per platform
| Platform | Full-color | Accented | Vibrant |
| --- | --- | --- | --- |
| iPhone | Home Screen, Today view, StandBy and CarPlay (with the background removed) | Home Screen and Today view | Lock Screen, StandBy in low-light conditions |
| iPad | Home Screen and Today view | Home Screen and Today view | Lock Screen |
| Apple Watch | Smart Stack, complications | Smart Stack, complications | Not supported |
| Mac | Desktop and Notification Center | Not supported | Desktop |
| Apple Vision Pro | Horizontal and vertical surfaces | Horizontal and vertical surfaces | Not supported |

### Key values
- Margins: 16 pt standard; 11 pt tighter groupings. Minimum text: 11 pt. Update animations: ≤ 2 s. Dynamic Type: Large–AX5. visionOS scale: 75–125%. Inline accessory: 1 tap target.

### iOS dimensions
| Screen size (portrait, pt) | Small (pt) | Medium (pt) | Large (pt) | Circular (pt) | Rectangular (pt) | Inline (pt) |
| --- | --- | --- | --- | --- | --- | --- |
| 430×932 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 428x926 | 170x170 | 364x170 | 364x382 | 76x76 | 172x76 | 257x26 |
| 414x896 | 169x169 | 360x169 | 360x379 | 76x76 | 160x72 | 248x26 |
| 414x736 | 159x159 | 348x157 | 348x357 | 76x76 | 170x76 | 248x26 |
| 393x852 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 390x844 | 158x158 | 338x158 | 338x354 | 72x72 | 160x72 | 234x26 |
| 375x812 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 375x667 | 148x148 | 321x148 | 321x324 | 68x68 | 153x68 | 225x26 |
| 360x780 | 155x155 | 329x155 | 329x345 | 72x72 | 157x72 | 225x26 |
| 320x568 | 141x141 | 292x141 | 292x311 | N/A | N/A | N/A |

### iPadOS dimensions
| Screen size (portrait, pt) | Target | Small (pt) | Medium (pt) | Large (pt) | Extra large (pt) |
| --- | --- | --- | --- | --- | --- |
| 768x1024 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
| 768x1024  | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 744x1133 | Canvas | 141x141 | 305.5x141 | 305.5x305.5 | 634.5x305.5 |
| 744x1133  | Device | 120x120 | 260x120 | 260x260 | 540x260 |
| 810x1080 | Canvas | 146x146 | 320.5x146 | 320.5x320.5 | 669x320.5 |
| 810x1080  | Device | 124x124 | 272x124 | 272x272 | 568x272 |
| 820x1180 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
| 820x1180  | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 834x1112 | Canvas | 150x150 | 327.5x150 | 327.5x327.5 | 682x327.5 |
| 834x1112  | Device | 132x132 | 288x132 | 288x288 | 600x288 |
| 834x1194 | Canvas | 155x155 | 342x155 | 342x342 | 715.5x342 |
| 834x1194  | Device | 136x136 | 300x136 | 300x300 | 628x300 |
| 954x1373 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
| 954x1373 *  | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 970x1389 * | Canvas | 162x162 | 350x162 | 350x350 | 726x350 |
| 970x1389 *  | Device | 162x162 | 350x162 | 350x350 | 726x350 |
| 1024x1366 | Canvas | 170x170 | 378.5x170 | 378.5x378.5 | 795x378.5 |
| 1024x1366  | Device | 160x160 | 356x160 | 356x356 | 748x356 |
| 1192x1590 * | Canvas | 188x188 | 412x188 | 412x412 | 860x412 |
| 1192x1590 *  | Device | 188x188 | 412x188 | 412x412 | 860x412 |

\* When Display Zoom is set to More Space.

### visionOS dimensions
| Widget | Size in pt | Size in mm (scaled to 100%) |
| --- | --- | --- |
| Small | 158x158 | 268x268 |
| Medium | 338x158 | 574x268 |
| Large | 338x354 | 574x600 |
| Extra large | 450x338 | 763x574 |
| Extra large portrait | 338x450 | 574x763 |

### watchOS dimensions
| Apple Watch size | Size of a widget in the Smart Stack (pt) |
| --- | --- |
| 40mm | 152x69.5 |
| 41mm | 165x72.5 |
| 44mm | 173x76.5 |
| 45mm | 184x80.5 |
| 49mm | 191x81.5 |

## APIs
`full color` (WidgetKit), `accented` (WidgetKit), `vibrant` (WidgetKit), `Preparing widgets for additional platforms, contexts, and appearances` (WidgetKit), `WidgetRenderingMode` (WidgetKit), `Making a configurable widget` (WidgetKit), `Keeping a widget up to date` (WidgetKit), `Animating data updates in widgets and Live Activities` (WidgetKit), `SwiftUI` (SwiftUI), `padding(_:_:)` (SwiftUI), `ContainerRelativeShape` (SwiftUI), `Font` (SwiftUI), `custom(_:size:)` (SwiftUI), `Asset management` (Xcode), `Supporting Dark Mode in your interface` (UIKit), `widgetAccentable(_:)` (SwiftUI), `Optimizing your widget for accented rendering mode and Liquid Glass` (WidgetKit), `Creating accessory widgets and watch complications` (WidgetKit), `ActivityKit` (ActivityKit), `Displaying the right widget background` (WidgetKit), `Updating your widgets for visionOS` (WidgetKit), `simplified` (WidgetKit), `default` (WidgetKit), `Elevated` (WidgetKit), `Recessed` (WidgetKit), `supportedMountingStyles(_:)` (SwiftUI), `WidgetConfiguration` (SwiftUI), `paper` (WidgetKit), `glass` (WidgetKit), `RelevanceKit` (RelevanceKit), `WidgetKit` (WidgetKit), `Developing a WidgetKit strategy` (WidgetKit)

## Related
layout, complications, live-activities, dark-mode, typography, sf-symbols
