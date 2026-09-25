# Watch faces

> Source: https://developer.apple.com/design/human-interface-guidelines/watch-faces · The view people choose as their primary view in watchOS.

## When to use / core idea
- Heart of watchOS: shown on every wrist raise, customized with complications; people can set up different faces per activity/context.
- watchOS 7+: people can share configured faces (e.g. fitness instructor shares a Gradient face with custom color + health complications); recipients get the setup without configuring.
- Apps can offer shareable faces from within the app, a website, Messages, Mail, or social media — helps introduce people to your complications and app.

## Rules
### Best practices
- **Help people discover your app by sharing watch faces that feature your complications** — ideally support multiple complications to showcase a curated experience; some faces let you specify system accent color, images, or styles. If your app isn't installed, the system prompts people to install it.
- **Display a preview of each watch face you share** — get one by emailing the face to yourself from the iOS Watch app; preview includes an illustrated device bezel (suitable for websites, watchOS and iOS apps); optionally composite a high-fidelity hardware bezel from Apple Design Resources instead.
- **Aim to offer shareable watch faces for all Apple Watch devices** — California, Chronograph Pro, Gradient, Infograph, Infograph Modular, Meridian, Modular Compact, Solar Dial are Series 4 and later; Explorer is Series 3 (with cellular) and later. If you use one, consider a similar configuration on a face available on Series 3 and earlier; label each shareable face with supported devices.
- **Respond gracefully if people choose an incompatible watch face** — system sends your app an error on Series 3 or earlier; consider immediately offering an alternative compatible configuration instead of showing an error, and tell people (with previews) they might receive an alternative face.

## Platform considerations
Not supported: iOS, iPadOS, macOS, tvOS, visionOS.

## APIs
Sharing an Apple Watch face (ClockKit)

## Related
`complications`
