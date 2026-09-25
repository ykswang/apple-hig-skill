# Dark Mode

> Source: https://developer.apple.com/design/human-interface-guidelines/dark-mode · Dark Mode is a systemwide appearance setting that uses a dark color palette to provide a comfortable viewing experience tailored for low-light environments.

## When to use / core idea
- iOS, iPadOS, macOS, tvOS users often default to Dark Mode and expect every app/game to respect it. Not supported in visionOS or watchOS.
- System applies a dark palette to all screens, views, menus, controls, and may raise perceptual contrast for foreground content.
- Dark palette = dimmer backgrounds, brighter foregrounds; colors are NOT simply inversions of light counterparts (some are, some aren't) — see `color` Specs.

## Rules
### Best practices
- **Avoid offering an app-specific appearance setting** — forces people to adjust multiple settings; app may seem broken when it ignores the systemwide choice.
- **Ensure that your app looks good in both appearance modes** — Auto setting can switch light/dark during the day, even while your app runs.
- **Test your content to make sure that it remains comfortably legible in both appearance modes** — test Dark Mode with Increase Contrast and Reduce Transparency, separately and together; dark text on dark backgrounds may lose legibility; Increase Contrast in Dark Mode can reduce contrast between dark text and dark background.
- **In rare cases, consider using only a dark appearance in the interface** — e.g., immersive media viewing apps (Stocks is dark-only) where UI should recede.

### Dark Mode colors
- **Embrace colors that adapt to the current appearance** — use semantic colors (`labelColor`, `controlColor` in macOS; `separator` in iOS/iPadOS). For custom colors, add a Color Set asset in the asset catalog with bright and dim variants. Avoid hard-coded or non-adapting colors.
- **Aim for sufficient color contrast in all appearances** — minimum **4.5:1**; for custom foreground/background colors strive for **7:1**, especially for small text.
- **Soften the color of white backgrounds** — consider slightly darkening content images with white backgrounds so they don't glow.

### Icons and images
- System uses SF Symbols (auto-adapt) and full-color images optimized for both appearances.
- **Use SF Symbols wherever possible** — tint with dynamic colors or add vibrancy.
- **Design separate interface icons for the light and dark appearances if necessary** — e.g., full moon needs subtle dark outline on light background, none on dark; oil drop needs a slight border on dark background.
- **Make sure full-color images and icons look good in both appearances** — reuse one asset if it works in both; otherwise modify it or create separate light/dark assets combined into a single named image in the asset catalog.

### Text
- System uses vibrancy and increased contrast for text legibility on dark backgrounds.
- **Use the system-provided label colors for labels** — primary, secondary, tertiary, quaternary adapt automatically.
- **Use system views to draw text fields and text views** — they adjust for vibrancy automatically; prefer system views over drawing text yourself.

## Platform considerations
No additional considerations: tvOS. Not supported: visionOS, watchOS.

### iOS, iPadOS
- Two background sets: *base* (dimmer; background interfaces recede) and *elevated* (brighter; foreground interfaces advance) to convey depth when dark interfaces layer.
- **Prefer the system background colors** — backgrounds switch base→elevated automatically for foreground interfaces (popovers, modal sheets); elevated also separates apps in multitasking and windows in multiwindow contexts. Custom backgrounds obscure these distinctions.

### macOS
- *Desktop tinting*: with graphite accent color chosen in General settings, window backgrounds pick up color from the desktop picture.
- **Include some transparency in custom component backgrounds when appropriate** — only for custom components with a visible background or bezel, and only in a neutral (non-colored) state; don't add transparency in colored states, or the color will fluctuate as the window moves or the desktop picture changes.

## Specs
- Contrast: minimum 4.5:1; target 7:1 for custom colors, especially small text.

## APIs
`labelColor` (AppKit), `controlColor` (AppKit), `separator` (UIKit)

## Related
color, materials, typography, accessibility, sf-symbols
