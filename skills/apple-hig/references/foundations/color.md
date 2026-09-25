# Color

> Source: https://developer.apple.com/design/human-interface-guidelines/color · Judicious use of color can enhance communication, evoke your brand, provide visual continuity, communicate status and feedback, and help people understand information.

## When to use / core idea
- Prefer system colors: they look good on various backgrounds and appearance modes and adapt automatically to vibrancy and accessibility settings.
- Custom colors can express personality — but must supply light/dark/increased-contrast variants.
- *Dynamic system colors* (iOS, iPadOS, macOS, visionOS) are defined by purpose (background levels, labels, links, separators), not by value, and adapt to light/dark.
- Related: `dark-mode` (appearance), `materials` (Liquid Glass), `accessibility` (contrast ratios).

## Rules
### Best practices
- **Avoid using the same color to mean different things** — e.g., if brand color marks interactive borderless buttons, don't use the same/similar color on noninteractive text.
- **Make sure all your app's colors work well in light, dark, and increased contrast contexts** — use system colors when possible. Custom colors need light and dark variants, each with an increased-contrast option giving significantly higher differentiation. Even if shipping a single appearance, provide both light and dark colors to support Liquid Glass adaptivity.
- **Test your app's color scheme under a variety of lighting conditions** — bright surroundings make colors look darker/muted; dark environments make them bright/saturated; in visionOS, surrounding walls/objects and reflected light change perception.
- **Test your app on different devices** — True Tone adjusts white point (reading/photo/video/gaming apps can strengthen or weaken via `UIWhitePointAdaptivityStyle`); test tvOS on multiple HD and 4K TV brands and settings; test Mac color profiles (P3, sRGB) via System Settings > Displays.
- **Consider how artwork and translucency affect nearby colors** — e.g., Maps: light scheme in map mode, dark in satellite mode; colors look different behind or on translucent elements like toolbars.
- **If your app lets people choose colors, prefer system-provided color controls where available** — consistent UX and saved color sets across apps (`ColorPicker`).

### Inclusive color
- **Avoid relying solely on color to differentiate between objects, indicate interactivity, or communicate essential information** — also use text labels or glyph shapes.
- **Avoid using colors that make it hard to perceive content in your app** — insufficient contrast; color-blind-indistinguishable combinations (see `accessibility`).
- **Consider how the colors you use might be perceived in other countries and cultures** — e.g., red = danger in some cultures, positive elsewhere (Stocks: rising = green in English, red in Chinese).

### System colors
- **Avoid hard-coding system color values in your app** — documented values are design references; actual values change between releases and environments. Use APIs like `Color`.
- **Avoid redefining the semantic meanings of dynamic system colors** — e.g., don't use `separator` as text color or `secondaryLabel` as a background.

### Liquid Glass color
- Liquid Glass has no inherent color by default; it takes color from content behind it. You can tint some elements (colored/stained glass) to emphasize a control such as a primary call to action — the system uses this for prominent button styling. Symbols/labels on glass can also be colored.
- Small elements (toolbars, tab bars) adapt glass between light and dark per underlying content; their symbols/text are monochromatic by default (darker over light content, lighter over dark). Larger elements (sidebars) are more opaque for legibility and richer content.
- **Apply color sparingly to the Liquid Glass material, and to symbols or text on the material** — reserve for status indicators or primary actions. To emphasize primary actions, color the background, not symbols/text (system applies accent color to prominent buttons like Done). Refrain from coloring the background of multiple controls.
- **Avoid using similar colors in control labels if your app has a colorful background** — with colorful backgrounds/rich content, prefer monochromatic toolbars and tab bars or an accent color with sufficient differentiation. In mostly monochromatic apps, brand color as accent color works well.
- **Be aware of the placement of color in the content layer** — avoid overlapping similar colors in content and controls; ensure the default/resting state (e.g., top of scrollable content) stays clearly legible even if colorful content scrolls under controls intermittently.

### Color management
- *Color space* (a.k.a. *gamut*) represents colors of a *color model* (RGB, CMYK); common: sRGB, Display P3. *Color profile* maps colors to numeric values; images embed it so devices reproduce colors correctly.
- **Apply color profiles to your images** — sRGB produces accurate colors on most displays.
- **Use wide color to enhance the visual experience on compatible displays** — P3 gives richer, more saturated colors. When appropriate, use Display P3 profile at **16 bits per pixel (per channel)** and export as **PNG**. Designing wide-color images/selecting P3 colors requires a wide color display.
- **Provide color space–specific image and color variations if necessary** — very similar P3 colors may be indistinguishable on sRGB, and P3 gradients may clip; provide per-color-space variants in the asset catalog.

## Platform considerations

### iOS, iPadOS
- Two dynamic background sets, each with primary/secondary/tertiary: *grouped* (`systemGroupedBackground`, `secondarySystemGroupedBackground`, `tertiarySystemGroupedBackground`) for grouped table views; otherwise *system* (`systemBackground`, `secondarySystemBackground`, `tertiarySystemBackground`).
- Hierarchy: primary = overall view; secondary = grouping within the overall view; tertiary = grouping within secondary elements.
- Foreground dynamic colors:

| Color | Use for… | UIKit API |
| --- | --- | --- |
| Label | A text label that contains primary content. | `label` |
| Secondary label | A text label that contains secondary content. | `secondaryLabel` |
| Tertiary label | A text label that contains tertiary content. | `tertiaryLabel` |
| Quaternary label | A text label that contains quaternary content. | `quaternaryLabel` |
| Placeholder text | Placeholder text in controls or text views. | `placeholderText` |
| Separator | A separator that allows some underlying content to be visible. | `separator` |
| Opaque separator | A separator that doesn't allow any underlying content to be visible. | `opaqueSeparator` |
| Link | Text that functions as a link. | `link` |

### macOS
Dynamic system colors (also in the Developer palette of the standard Color panel):

| Color | Use for… | AppKit API |
| --- | --- | --- |
| Alternate selected control text color | The text on a selected surface in a list or table. | `alternateSelectedControlTextColor` |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | `alternatingContentBackgroundColors` |
| Control accent | The accent color people select in System Settings. | `controlAccentColor` |
| Control background color | The background of a large interface element, such as a browser or table. | `controlBackgroundColor` |
| Control color | The surface of a control. | `controlColor` |
| Control text color | The text of a control that is available. | `controlTextColor` |
| Current control tint | The system-defined control tint. | `currentControlTint` |
| Unavailable control text color | The text of a control that's unavailable. | `disabledControlTextColor` |
| Find highlight color | The color of a find indicator. | `findHighlightColor` |
| Grid color | The gridlines of an interface element, such as a table. | `gridColor` |
| Header text color | The text of a header cell in a table. | `headerTextColor` |
| Highlight color | The virtual light source onscreen. | `highlightColor` |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | `keyboardFocusIndicatorColor` |
| Label color | The text of a label containing primary content. | `labelColor` |
| Link color | A link to other content. | `linkColor` |
| Placeholder text color | A placeholder string in a control or text view. | `placeholderTextColor` |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | `quaternaryLabelColor` |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | `secondaryLabelColor` |
| Selected content background color | The background for selected content in a key window or view. | `selectedContentBackgroundColor` |
| Selected control color | The surface of a selected control. | `selectedControlColor` |
| Selected control text color | The text of a selected control. | `selectedControlTextColor` |
| Selected menu item text color | The text of a selected menu. | `selectedMenuItemTextColor` |
| Selected text background color | The background of selected text. | `selectedTextBackgroundColor` |
| Selected text color | The color for selected text. | `selectedTextColor` |
| Separator color | A separator between different sections of content. | `separatorColor` |
| Shadow color | The virtual shadow cast by a raised object onscreen. | `shadowColor` |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | `tertiaryLabelColor` |
| Text background color | The background color behind text. | `textBackgroundColor` |
| Text color | The text in a document. | `textColor` |
| Under page background color | The background behind a document's content. | `underPageBackgroundColor` |
| Unemphasized selected content background color | The selected content in a non-key window or view. | `unemphasizedSelectedContentBackgroundColor` |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | `unemphasizedSelectedTextBackgroundColor` |
| Unemphasized selected text color | Selected text in a non-key window or view. | `unemphasizedSelectedTextColor` |
| Window background color | The background of a window. | `windowBackgroundColor` |
| Window frame text color | The text in the window's title bar area. | `windowFrameTextColor` |

- **App accent colors** (macOS 11+): your accent color customizes buttons, selection highlighting, sidebar icons — applied only when General > Accent color is *multicolor*. Otherwise the person's chosen color replaces yours, except sidebar icons with a fixed color you specify (they carry meaning, so aren't overridden). See `sidebars`.

### tvOS
- **Consider choosing a limited color palette that coordinates with your app logo** — subtle brand color that defers to content.
- **Avoid using only color to indicate focus** — subtle scaling and responsive animation are the primary focus indicators.

### visionOS
- **Use color sparingly, especially on glass** — windows use system glass material through which surroundings show and affect legibility of colorful content; use color to call attention to important info or show relationships.
- **Prefer using color in bold text and large areas** — color in lightweight text or small areas is harder to see.
- **In a fully immersive experience, help people maintain visual comfort by keeping brightness levels balanced** — make content fully bright only when the rest of the context is bright; avoid a bright object on a very dark/black background, especially if it flashes or moves.
- visionOS system colors use the default **dark** color values.

### watchOS
- **Use background color to support existing content or supply additional information** — e.g., Activity ring infographic backgrounds match ring color. Use only when communicating something, not as mere flourish. Avoid full-screen background color in long-lived views (workout, audio playback).
- **Recognize that people might prefer graphic complications to use tinted mode instead of full color** — system may render images, gauges, text in a single color based on the wearer's selection (see `complications`).

## Specs

### System colors (RGB; design reference only — use APIs, don't hard-code)
| Name | SwiftUI API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
| --- | --- | --- | --- | --- | --- |
| Red | `red` | 255, 56, 60 | 255, 66, 69 | 233, 21, 45 | 255, 97, 101 |
| Orange | `orange` | 255, 141, 40 | 255, 146, 48 | 197, 83, 0 | 255, 160, 86 |
| Yellow | `yellow` | 255, 204, 0 | 255, 214, 0 | 161, 106, 0 | 254, 223, 67 |
| Green | `green` | 52, 199, 89 | 48, 209, 88 | 0, 137, 50 | 74, 217, 104 |
| Mint | `mint` | 0, 200, 179 | 0, 218, 195 | 0, 133, 117 | 84, 223, 203 |
| Teal | `teal` | 0, 195, 208 | 0, 210, 224 | 0, 129, 152 | 59, 221, 236 |
| Cyan | `cyan` | 0, 192, 232 | 60, 211, 254 | 0, 126, 174 | 109, 217, 255 |
| Blue | `blue` | 0, 136, 255 | 0, 145, 255 | 30, 110, 244 | 92, 184, 255 |
| Indigo | `indigo` | 97, 85, 245 | 109, 124, 255 | 86, 74, 222 | 167, 170, 255 |
| Purple | `purple` | 203, 48, 224 | 219, 52, 242 | 176, 47, 194 | 234, 141, 255 |
| Pink | `pink` | 255, 45, 85 | 255, 55, 95 | 231, 18, 77 | 255, 138, 196 |
| Brown | `brown` | 172, 127, 94 | 183, 138, 102 | 149, 109, 81 | 219, 166, 121 |

visionOS system colors use the default dark values.

### iOS, iPadOS system gray colors (RGB)
| Name | UIKit API | Default (light) | Default (dark) | Increased contrast (light) | Increased contrast (dark) |
| --- | --- | --- | --- | --- | --- |
| Gray | `systemGray` | 142, 142, 147 | 142, 142, 147 | 108, 108, 112 | 174, 174, 178 |
| Gray (2) | `systemGray2` | 174, 174, 178 | 99, 99, 102 | 142, 142, 147 | 124, 124, 128 |
| Gray (3) | `systemGray3` | 199, 199, 204 | 72, 72, 74 | 174, 174, 178 | 84, 84, 86 |
| Gray (4) | `systemGray4` | 209, 209, 214 | 58, 58, 60 | 188, 188, 192 | 68, 68, 70 |
| Gray (5) | `systemGray5` | 229, 229, 234 | 44, 44, 46 | 216, 216, 220 | 54, 54, 56 |
| Gray (6) | `systemGray6` | 242, 242, 247 | 28, 28, 30 | 235, 235, 240 | 36, 36, 38 |

SwiftUI equivalent of `systemGray` is `gray`.

### Wide color export
- Display P3 profile, 16 bits per pixel (per channel), PNG.

## APIs
`UIWhitePointAdaptivityStyle` (Bundle Resources), `ColorPicker` (SwiftUI), `Color` (SwiftUI), `separator` (UIKit), `secondary text label` (UIKit), `systemGroupedBackground` (UIKit), `secondarySystemGroupedBackground` (UIKit), `tertiarySystemGroupedBackground` (UIKit), `systemBackground` (UIKit), `secondarySystemBackground` (UIKit), `tertiarySystemBackground` (UIKit), `label` (UIKit), `secondaryLabel` (UIKit), `tertiaryLabel` (UIKit), `quaternaryLabel` (UIKit), `placeholderText` (UIKit), `opaqueSeparator` (UIKit), `link` (UIKit), `alternateSelectedControlTextColor` (AppKit), `alternatingContentBackgroundColors` (AppKit), `controlAccentColor` (AppKit), `controlBackgroundColor` (AppKit), `controlColor` (AppKit), `controlTextColor` (AppKit), `currentControlTint` (AppKit), `disabledControlTextColor` (AppKit), `findHighlightColor` (AppKit), `gridColor` (AppKit), `headerTextColor` (AppKit), `highlightColor` (AppKit), `keyboardFocusIndicatorColor` (AppKit), `labelColor` (AppKit), `linkColor` (AppKit), `placeholderTextColor` (AppKit), `quaternaryLabelColor` (AppKit), `secondaryLabelColor` (AppKit), `selectedContentBackgroundColor` (AppKit), `selectedControlColor` (AppKit), `selectedControlTextColor` (AppKit), `selectedMenuItemTextColor` (AppKit), `selectedTextBackgroundColor` (AppKit), `selectedTextColor` (AppKit), `separatorColor` (AppKit), `shadowColor` (AppKit), `tertiaryLabelColor` (AppKit), `textBackgroundColor` (AppKit), `textColor` (AppKit), `underPageBackgroundColor` (AppKit), `unemphasizedSelectedContentBackgroundColor` (AppKit), `unemphasizedSelectedTextBackgroundColor` (AppKit), `unemphasizedSelectedTextColor` (AppKit), `windowBackgroundColor` (AppKit), `windowFrameTextColor` (AppKit), `red` (SwiftUI), `orange` (SwiftUI), `yellow` (SwiftUI), `green` (SwiftUI), `mint` (SwiftUI), `teal` (SwiftUI), `cyan` (SwiftUI), `blue` (SwiftUI), `indigo` (SwiftUI), `purple` (SwiftUI), `pink` (SwiftUI), `brown` (SwiftUI), `systemGray` (UIKit), `systemGray2` (UIKit), `systemGray3` (UIKit), `systemGray4` (UIKit), `systemGray5` (UIKit), `systemGray6` (UIKit), `gray` (SwiftUI), `UIColor` (UIKit), `Color` (AppKit)

## Related
dark-mode, accessibility, materials, sidebars, complications, branding
