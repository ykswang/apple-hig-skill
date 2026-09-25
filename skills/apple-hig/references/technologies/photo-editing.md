# Photo editing

> Source: https://developer.apple.com/design/human-interface-guidelines/photo-editing · Photo-editing extensions let people modify photos and videos within the Photos app by applying filters or other changes.

## When to use / core idea
- Edits are always saved in Photos as new files, preserving originals.
- Flow: photo in edit mode → tap extension icon in toolbar → action menu of editing extensions → extension UI in a modal view with a top toolbar → dismiss to confirm/save or cancel and return to Photos.

## Rules
### Best practices
- **Confirm cancellation of edits** — on Cancel, don't discard immediately; ask for confirmation and say edits will be lost. No confirmation needed if no edits have been made.
- **Don't provide a custom top toolbar** — the modal already has one; a second is confusing and wastes content space.
- **Let people preview edits** — show the result before closing the extension and returning to Photos.
- **Use your app icon for your photo editing extension icon** — instills confidence it's from your app.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS. Not supported in tvOS, visionOS, or watchOS.

## APIs
App extensions, `PhotoKit`

## Related
live-photos, toolbars, alerts
