# Right to left

> Source: https://developer.apple.com/design/human-interface-guidelines/right-to-left · Support right-to-left languages like Arabic and Hebrew by reversing your interface as needed to match the reading direction of the related scripts.

## When to use / core idea
- System UI frameworks support RTL by default: system components flip automatically. With system elements and standard layouts you may need no changes.
- Apply these rules when fine-tuning layout or enhancing localizations (currencies, numerals, mathematical symbols) for RTL locales.
- Decision summary: flip things that encode reading direction, order, or forward/backward progress; don't flip things that encode real direction, real-world objects, logos, universal marks, photos/artwork, or the digits within a number.

## Rules

### Text alignment
- **Adjust text alignment to match the interface direction, if the system doesn't do so automatically** — text left-aligned with content in LTR becomes right-aligned in RTL. (Images themselves aren't flipped.)
- **Align a paragraph based on its language, not on the current context** — a paragraph = three or more lines. One- and two-line text blocks follow the current context's direction; paragraphs follow their own language (e.g., an English paragraph stays left-aligned in an RTL UI).
- **Use a consistent alignment for all text items in a list** — reverse alignment of all list items, including items in a different script.

### Numbers and characters
- RTL languages use different number systems: Hebrew uses Western Arabic numerals; Arabic may use Western or Eastern Arabic numerals, varying by country/region and even within one.
- Number-centric apps (e.g., mathematics) should identify the appropriate display per locale; others can generally rely on system-provided number representations.
- **Don't reverse the order of numerals in a specific number** — digits in a specific number ("541", phone number, credit card number) always appear in the same order.
- **Reverse the order of numerals that show progress or a counting direction; never flip the numerals themselves** — e.g., numerals under progress bars, sliders, rating controls reverse order to match the flipped control; also reverse a numeral sequence that communicates a specific order.

### Controls
- **Flip controls that show progress from one value to another** — sliders, progress indicators; also swap the begin/end glyphs (e.g., volume min/max speakers).
- **Flip controls that help people navigate or access items in a fixed order** — in RTL, the back button points right; next/previous buttons flip.
- **Preserve the direction of a control that refers to an actual direction or points to an onscreen area** — a "to the right" control always points right.
- **Visually balance adjacent Latin and RTL scripts when necessary** — Arabic and Hebrew have no uppercase, so they look small next to all-caps Latin in buttons, labels, titles; increasing the RTL font size by about 2 points often works well.

### Images
- **Avoid flipping images like photographs, illustrations, and general artwork** — flipping often changes meaning, and flipping copyrighted images could be a violation. If content is strongly tied to reading direction, consider creating a new version instead.
- **Reverse the positions of images when their order is meaningful** — chronological, alphabetical, favorite order, etc.

### Interface icons
- SF Symbols provide RTL variants and localized symbols for Arabic and Hebrew (and other languages); custom symbols can specify directionality.
- **Flip interface icons that represent text or reading direction** — e.g., left-aligned text bars become right-aligned.
- **Consider creating a localized version of an interface icon that displays text** — e.g., SF Symbols' signature, rich-text, and I-beam pointer symbols have Latin, Hebrew, Arabic versions. If a custom icon uses letters/words for a concept unrelated to reading or writing, consider an alternative image without text.
- **Flip an interface icon that shows forward or backward motion** — motion in reading direction = forward; e.g., speaker sound waves emanate right in LTR, left in RTL.
- **Don't flip logos or universal signs and marks** — flipped logos confuse and can have legal repercussions; always show logos in original form, even with text. Don't flip universal marks like the checkmark.
- **In general, avoid flipping interface icons that depict real-world objects** — unless the object indicates directionality. Clocks work the same everywhere; right-handed tools (e.g., pencil) needn't flip since most people are right-handed, and flipping may confuse.
- **Before merely flipping a complex custom interface icon, consider its individual components and the overall visual balance**:
  - Some components (badge, slash, magnifying glass) must follow a visual design language regardless of localization — SF Symbols uses the same backslash for negation in LTR and RTL.
  - A badge representing actual UI flips if the UI flips. A badge modifying meaning: check whether flipping preserves meaning and visual balance (e.g., flipped cart with plus badge moved to top-left, not left in top-right).
  - Components implying handedness (a tool): consider preserving the tool's orientation while flipping the base image if necessary.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## Specs
- Paragraph threshold: 3 or more lines (align by language); 1–2 line blocks align by context.
- RTL font size vs. all-caps Latin: increase by about 2 pt.

## APIs
Creating custom symbol images for your app (UIKit), Preparing views for localization (SwiftUI), Localization

## Related
layout, inclusion, sf-symbols, icons
