# Sliders

> Source: https://developer.apple.com/design/human-interface-guidelines/sliders · A horizontal track with a thumb that people adjust between a minimum and maximum value.

## When to use / core idea
- Track between minimum and thumb fills with color as value changes; optional left/right icons illustrate min/max meaning.
- Supplement with `text-fields` and `steppers` for exact values; alternatives: `steppers`, `pickers`. Not for audio volume on iOS (use a volume view).

## Rules
### Best practices
- **Customize a slider's appearance if it adds value** — track color, thumb image and tint, left/right icons; e.g. image-size slider with small image icon left, large right.
- **Use familiar slider directions** — horizontal: minimum on leading side, maximum on trailing; vertical: minimum at bottom, maximum at top (e.g. 0% leading → 100% trailing).
- **Consider supplementing a slider with a corresponding text field and stepper** — especially for wide ranges: shows exact value, allows specific entry; stepper increments in whole values.

## Platform considerations
Not supported: tvOS.
### iOS, iPadOS
- **Don't use a slider to adjust audio volume** — use a volume view (customizable, includes volume-level slider and active audio output device control). See `playing-audio`.
### macOS
- Can include tick marks to pinpoint values.
- Linear slider (with/without ticks): thumb is a narrow lozenge; track from min to thumb filled with color; often has supplementary min/max icons.
- Circular slider: thumb is a small circle; tick marks appear as evenly spaced dots around the circumference.
- **Consider giving live feedback as the value of a slider changes** — real-time results (e.g. Dock icons scale while adjusting the Size slider).
- **Choose a slider style that matches peoples' expectations** — horizontal for fixed start/end (e.g. opacity 0–100%); circular when values repeat or continue indefinitely (e.g. rotation 0–360°; spins: four rotations = four spins = 1440°).
- **Consider using a label to introduce a slider** — sentence-style capitalization, ending with a colon (see `labels`).
- **Use tick marks to increase clarity and accuracy** — convey scale, locate specific values.
- **Consider adding labels to tick marks for even greater clarity** — numbers or words; don't label every mark unless needed; often min and max suffice; for nonlinear values (e.g. Energy Saver) use periodic labels. Also provide a tooltip showing the thumb's value on pointer hover.
### visionOS
- **Prefer horizontal sliders** — side-to-side gestures are easier than up-and-down.
### watchOS
- Horizontal track shown as discrete steps or a continuous bar, representing a finite range; buttons on each side change the value by a predefined amount.
- **If necessary, create custom glyphs to communicate what the slider does** — system default is plus and minus signs.

## APIs
`Slider` (SwiftUI), `UISlider` (UIKit), `NSSlider` (AppKit)

## Related
`steppers, pickers, text-fields, playing-audio, labels, offering-help`
