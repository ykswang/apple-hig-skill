# iMessage apps and stickers

> Source: https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers · iMessage apps help people share content, collaborate, and play games in a conversation; stickers are images people use to decorate a conversation.

## When to use / core idea
- Available within Messages conversations and in effects in Messages and FaceTime.
- Build as a standalone app or as an app extension of your iOS/iPadOS app.
- Two views: compact (below the transcript, ~keyboard height) and expanded (most of the window).

## Rules
### Best practices
- **Prefer providing one primary experience in your iMessage app** — people are mid-conversation; make it immediately understandable. For multiple functions or content collections, consider a separate iMessage app for each.
- **Consider surfacing content from your iOS or iPadOS app** — e.g., shareable shopping list or trip itinerary, or a simple collaborative task (where to eat, which movie).
- **Present essential features in the compact view** — most frequently used items there; reserve additional content/features for expanded view.
- **In general, let people edit text only in the expanded view** — compact view is about keyboard-sized; show the keyboard in expanded view so content stays visible.
- **Create stickers that are expressive, inclusive, and versatile** — static or short animations; legible against a wide range of backgrounds and when rotated or scaled; transparency helps integrate with text, photos, other stickers.
- **For each sticker, provide a localized alternative description** — spoken by VoiceOver.

### Stickers
- Messages supports small, regular, and large stickers. Pick one size for all stickers in a pack; don't mix sizes within a pack. Displayed in a grid arranged per size.
- Provide @3x images; system downscales to @2x/@1x at runtime if needed.

## Platform considerations
No additional considerations: iOS, iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.

## Specs
### Icon sizes
- Icon appears in Messages, App Store, notifications, Settings, and (after install) the Messages app drawer. Supply square-cornered icons per extension; system applies the rounded mask.

| Usage | @2x (pixels) | @3x (pixels) |
| --- | --- | --- |
| Messages, notifications | 148x110 | - |
|  | 143x100 | - |
|  | 120x90 | 180x135 |
|  | 64x48 | 96x72 |
|  | 54x40 | 81x60 |
| Settings | 58x58 | 87x87 |
| App Store | 1024x1024 | 1024x1024 |

### Sticker sizes

| Sticker size | @3x dimensions (pixels) |
| --- | --- |
| Small | 300x300 |
| Regular | 408x408 |
| Large | 618x618 |

- Sticker file must be 500 KB or smaller.

| Format | Transparency | Animation |
| --- | --- | --- |
| PNG | 8-bit | No |
| APNG | 8-bit | Yes |
| GIF | Single-color | Yes |
| JPEG | No | No |

## APIs
`Messages` framework, `MSStickerSize` (Messages)

## Related
app-icons, voiceover
