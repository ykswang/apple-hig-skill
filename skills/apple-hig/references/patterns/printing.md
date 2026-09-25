# Printing

> Source: https://developer.apple.com/design/human-interface-guidelines/printing · iOS, iPadOS, macOS, and visionOS apps can integrate system print functionality when it makes sense, adding custom printer- and document-specific options if necessary.

## When to use / core idea
- Use system print UI; add custom options only where the system doesn't provide them.
- Standard entry points: macOS File menu Print item; iOS/iPadOS toolbar button opening an `action-sheets`.

## Rules
### Best practices
- **Make printing discoverable** — place Print in standard locations: macOS File menu; iOS/iPadOS toolbar button opening an action sheet. In a macOS toolbar, consider a Print button as an optional item people add when customizing the toolbar.
- **Present a printing option only when it's possible** — if nothing onscreen to print or no printers available: dim Print in the macOS File menu; remove Print from the iOS/iPadOS action sheet; dim or hide custom print buttons.
- **Present relevant printing options** — e.g. page range, multiple copies, double-sided (when the printer supports them) via the system-provided view.

## Platform considerations
No additional considerations: iOS, iPadOS, visionOS. Not supported: tvOS, watchOS.
### macOS
- **If your macOS app offers app-specific print options that the system doesn't offer, consider creating a custom category for the print panel** — default categories include Layout, Paper Handling, Media & Quality; give yours a unique name (e.g. your app name). E.g. Keynote: print presenter notes, slide backgrounds, skipped slides.
- **If your app supports document-specific page settings, consider presenting a page setup dialog** — *page setup dialog* holds rarely changed per-document settings: page size, orientation, scaling. Avoid reimplementing system features (e.g. page orientation, reverse-order printing).
- **Make sure interdependencies between options are clear** — e.g. double-sided printing makes printing on transparencies unavailable.
- **Separate advanced features from frequently used features** — consider a disclosure control hiding advanced options; label them *Advanced Options*.
- **Consider letting people preview the effect of a setting** — e.g. update a thumbnail when a tone control changes.
- **Consider storing modified settings with the document** — at minimum keep print settings until the document closes.

## APIs
`UIPrintInteractionController` (UIKit), `NSDocument` (AppKit)

## Related
`file-management, the-menu-bar, action-sheets, toolbars`
