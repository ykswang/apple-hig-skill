# App Clips

> Source: https://developer.apple.com/design/human-interface-guidelines/app-clips · An App Clip is a lightweight version of your app or game that provides an instantly available on-the-go or demo experience.

## When to use / core idea
- Delivers a fast task solution or a demo without downloading the full app; stays on device for a limited time, preserves privacy.
- Launch points: App Clip Code (best — recognizable, trusted), NFC tag, QR code; Siri Suggestions (location-based), Maps, Smart App Banners, App Clip cards in Safari, links shared in Messages; since iOS 17, links/App Clip previews in other apps.
- Choose for in-the-moment tasks over a finite time (rent a bike, advance coffee order, order from a food truck poster, pay at a restaurant table, museum AR/audio commentary).
- Also choose to let people try an app/game before purchase or subscription (game demo with tutorial + first level, free workout + meditation, create/save a document).
- Installing the full app replaces the App Clip; subsequent invocations launch the app.

## Rules
### Designing your App Clip
- **Allow people to complete a task or a demo in your App Clip** — don't require the full app to finish the demo, task, or a game level.
- **Focus on essential features** — reserve advanced/complex features for the app; demos show essential features that convey the app/game.
- **Don't use App Clips solely for marketing purposes** — must provide real value; don't advertise, don't display ads.
- **Avoid using web views in your App Clip** — use native components; if only web is available, offer a link to your website instead.
- **Design a linear, easy-to-use, and focused user interface** — no tab bars, complex navigation, or settings; minimize screens and entry forms.
- **On launch, show the most relevant part of your App Clip** — skip unnecessary steps; go to what fits the context.
- **Ensure people can use your App Clip immediately** — include all required assets, omit splash screens, never make people wait on launch.
- **Ensure your App Clip is small** — faster launch, esp. on limited bandwidth; remove unused code/assets; avoid downloading additional data.
- **Make the App Clip shareable** — links shared in Messages launch it; support links to specific points; encourage sharing.
- **Make it easy to pay for a service or product** — consider Apple Pay for express checkout and shipping info without typing.
- **Avoid requiring people to create an account before they can benefit from your App Clip** — consider no account or ask after task completion; if required, minimize info (e.g. Sign in with Apple).
- **Provide a familiar, focused experience in your app** — after install, don't add steps; e.g. don't require logging in again when moving from App Clip to app.

### Preserving privacy
- System limits App Clips (e.g. no background operations).
- **Limit the amount of data you store and handle yourself** — store securely; don't rely on previously stored data (system may delete the App Clip and its data between launches); store login info securely off device.
- **Consider offering Sign in with Apple** — keeps login info off device, preserves privacy.
- **Offer a secure way to pay for services or goods that also respects people's privacy** — e.g. Apple Pay.

### Showcasing your app
- App Clips don't appear on the Home screen and aren't user-managed; system removes them after inactivity.
- System aids discovery: App Clip card offers launch or App Store page; on first launch a system app banner at top links to the App Store. You can also show an overlay to download the full app.
- **Don't compromise the user experience by asking people to install the full app** — for on-the-go clips, consider if the card and system banner suffice; for demos, let people fully experience the demo first.
- **Pick the right time to recommend your app** — at task completion or natural pause, show `SKOverlay`.
- **Recommend your app in a nonintrusive, polite way** — don't ask repeatedly or interrupt tasks; push notifications aren't a good way to ask; clearly communicate additional features.

### Limiting notifications
- App Clips can schedule/receive notifications for up to 8 hours after launch.
- **Only ask for permission to use notifications for an extended period if it's really needed** — if functionality spans more than a day, explicitly request permission (e.g. car rental return reminder).
- **Keep notifications focused** — no purely promotional notifications; only in response to explicit user action; maybe none if the task completes in the clip.
- **Use notifications to help people complete a task** — directly related to the task (e.g. scheduled food delivery).

### Creating App Clips for businesses
- Platform providers can configure multiple App Clip experiences in App Store Connect powered by a single App Clip, branded per business/location.
- **Use consistent branding** — business's brand front and center; tone down your own.
- **Consider multiple businesses** — handle use across multiple businesses/locations at once; e.g. switch between recent businesses/locations, verify location at launch.

### Creating content for an App Clip card
- **Be informative** — image communicates features, tasks, or content.
- **Prefer photography and graphics** — avoid UI screenshots; use images showing value or a photo of the business/point of interest.
- **Avoid using text** — header image text isn't localizable, hard to read, less aesthetic.
- **Adhere to image requirements** — 1800x1200 px PNG or JPEG, no transparency.
- **Use concise copy** — title and subtitle both required; title ≤30 characters, subtitle ≤56 characters.
- **Pick a verb for the action button that best fits your App Clip** — *View* for media or informational/educational content; *Play* for games; *Open* for all others.

### App Clip Codes
- Always use Apple-provided designs and follow size, placement, printing guidelines. Two designs: badge with App Clip logo, or without logo when space is at a premium. Default color pair or custom foreground/background.
- Variants: *scan-only* (camera icon center; scan with Camera app or Code Scanner in Control Center) and *NFC-integrated* (iPhone icon center; hold device near or use NFC Tag Reader in Control Center; also scannable by camera).
- Use NFC-integrated when people can physically reach the code: restaurant tabletop, near a register, storefront window, signage, gift card/coupon.
- Use scan-only when physically inaccessible or digital: posters/print ads, signage behind counter or unreachable in a storefront, digital displays, emails, social media images.
- **Include the App Clip logo when space allows** — if clear space can't be met, use the no-logo design. Also use no-logo design on disposable paper/plastic items and items associated with gambling or drinking (playing cards, poker chips, bar coasters). Logo always appears below the code in the badge design; never use the App Clip logo on its own.
- **Place your App Clip Code on a flat or cylindrical surface only** — on cylinders, code width ≤ one-sixth of circumference (60°).
- **Help your App Clip Code remain as flat as possible** — avoid deformable materials (paper, plastic, fabric); on bags/flexible boxes attach a rigid card; stickers must adhere well to flat surfaces.
- **Place your App Clip Code in a location that helps ensure reliable scanning** — enough light for scan-only codes; don't require wide-angle scanning.
- **Make sure the App Clip Code is unobstructed** — no text, logos, images over it; never animate or dim it.
- **Display the App Clip Code in an upright position** — don't rotate it or angle the center glyph.
- **Don't create App Clip Codes that are too small** — see Specs.
- **Provide enough space between an App Clip Code and adjacent codes, graphics, or materials** — minimum clear space = space between center glyph and the circular code; leave enough space next to other machine-readable codes.

### Using clear messaging
- Add a clear, simple call to action about how to launch, especially with the no-logo design (e.g. next to code in email/poster).
- Scan-only CTAs: "Scan to [what people can do]." / "Scan using the camera on your iPhone or iPad to [what people can do]."
- NFC-integrated CTAs: "Scan to [what people can do]." / "Hold your iPhone near the [object name] to launch an App Clip that [what people can do]."
- **Adhere to Guidelines for Using Apple Trademarks when referring to your App Clip and App Clip Codes** — no Apple trademarks in your app name or images; always title case *App Clips* and *App Clip Code*.

### Customizing your App Clip Code
- Create codes with App Store Connect or the App Clip Code Generator CLI.
- **Always use the generated App Clip Code** — don't design your own or modify it; no filters, color changes, glows, shadows, gradients, reflections. When scaling, keep aspect ratio and scale all attributes (e.g. stroke widths).
- **Choose colors with enough contrast that ensure accurate scanning** — three colors: foreground, background, and a generated third color. Tools offer default pairs or custom colors; tools refuse to generate codes with poor color choices and can suggest a foreground color for a custom background.

### Printing guidelines
- Always test printed codes before distribution for scannability from a variety of angles. Print yourself or via a professional service.
- **Use high-quality, non-textured print materials** — matte finishes; avoid shine, gloss, reflective/holographic overlays, thin laminates; use matte laminate if laminating; UV-resistant materials/coatings outdoors; flexographic printing for professional services; inkjet for desktop printing.
- **Use high-resolution images and printer settings** — see Specs; consider leveling/calibrating the printer; avoid poor color channel alignment, inaccurate gamma, artifacts, elliptical/distorted codes; on receipt printers print as close to the paper's maximum bounds as possible.
- **Use correct color settings when you convert the generated SVG file to a CMYK image** — see Specs.
- **If you're using a printer that only prints in grayscale, only generate grayscale App Clip Codes** — color codes printed in grayscale are less reliable.
- **For NFC-integrated App Clip Codes, choose Type 5 NFC tags** — ≥35 mm diameter or equivalent.
- **If you create large batches of App Clip Codes, thoroughly test your printing workflow and verify printed codes** — small inexpensive test runs; print templates with padded regions showing the encoded invocation URL and SVG filename per code. Keep a file mapping SVG files to invocation URLs; careful file management, versioning, change tracking.

### Verifying your printer's calibration
- Apple provides printer calibration test sheets.
- **Verify print quality of your chosen color pair with the test sheet showing text boxes for each default color pair** — print at the right scale per instructions.
- **Verify your printer's grayscale settings by printing the test sheet showing two grayscale bars** — light or missing grays mean calibration needed or printer unsuitable.

### Legal requirements
- Only Apple-provided codes from App Store Connect or the Generator CLI that follow these guidelines are approved; they indicate availability of an App Clip. Apple may update the design at its discretion.
- Stop displaying the code if the App Clip is no longer active.
- Don't use the App Clip Code (incl. Apple Logo, App Clip mark, code designs) in your company or product name; don't seek copyright/trademark registration for them.
- Don't use codes in ways that damage Apple/App Clips goodwill, infringe third-party rights, or cause source confusion. Apple retains all IP rights.
- Don't add a symbol to generated App Clip Codes.
- Don't translate Apple trademarks — keep them in English in any language; with Apple's approval, legal notice and credit lines (not trademarks) may be translated for materials outside the U.S.

## Platform considerations
No additional considerations: iOS, iPadOS. Not supported in macOS, tvOS, visionOS, watchOS.

## Specs
| Item | Value |
|---|---|
| Notification window | up to 8 hours after launch |
| App Clip card image | 1800x1200 px, PNG or JPEG, no transparency |
| Card title / subtitle | ≤30 / ≤56 characters |
| Cylindrical placement | code width ≤ 1/6 of circumference (60°) |

| Type | Minimum size |
|---|---|
| Printed communications | Minimum diameter 3/4 inch (1.9 cm) |
| Digital communications | Minimum 256×256 px; PNG or SVG |
| NFC-integrated App Clip Code | Embedded NFC tag ≥35 mm diameter or equivalent; e.g. 35 mm tag → printed code ≥1.37 in (3.48 cm) diameter |

- Distance-to-code-size ratio: no more than 20:1; prefer 10:1. E.g. scanned from 40 in (101 cm) → ≥4 in (10.16 cm) diameter.
- Near a QR code or other scannable item: App Clip Code at least that item's size.
- Clear space: equal to the space between the center glyph and the circular code.
- Printing: rasterize SVG at ≥600 ppi; print at ≥300 dpi.
- Color conversion: generated SVGs are sRGB; convert to CMYK with relative colorimetric (media-relative) intent; "Generic CMYK ICC profile" on CMYK printers, "Gracol 2013 ICC profile" on CMYKOV printers; color tolerance CIELab Delta E 2.5.
- NFC tag: Type 5, ≥35 mm diameter or equivalent.

## APIs
App Clips (AppClip framework), `SKOverlay` (StoreKit), App Clip Code Generator (CLI), App Store Connect

## Related
apple-pay, sign-in-with-apple, nfc, notifications
