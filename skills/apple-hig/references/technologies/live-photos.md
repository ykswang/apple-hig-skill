# Live Photos

> Source: https://developer.apple.com/design/human-interface-guidelines/live-photos · Live Photos captures memories as a sound- and motion-rich interactive experience that adds vitality to still photos.

## When to use / core idea
- Camera captures extra frames and audio before and after the photo; people press a Live Photo to see it come to life.
- Apps that display, edit, or share photos must preserve the consistent Live Photo experience or fall back to a still.

## Rules
### Best practices
- **Apply adjustments to all frames** — effects/adjustments must apply to the entire Live Photo; if unsupported, offer converting to a still photo.
- **Keep Live Photo content intact** — same visual treatment and interaction model across apps; don't disassemble and present frames or audio separately.
- **Implement a great photo sharing experience** — let people preview the entire Live Photo before sharing; always offer sharing as a traditional photo.
- **Clearly indicate when a Live Photo is downloading and when the photo is playable** — progress indicator during download, and indication when complete.
- **Display Live Photos as traditional photos in environments that don't support Live Photos** — don't replicate the experience; show a still.
- **Make Live Photos easily distinguishable from still photos** — best via a hint of movement; there are no built-in motion effects, so design custom ones. When movement isn't possible, show the system-provided badge above the photo (with or without "Live" text). Never include a playback button that could be read as video playback.
- **Keep badge placement consistent** — same location on every photo; typically a corner looks best.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS. Not supported in watchOS.
### visionOS
- People can view a Live Photo but can't capture one.

## APIs
`PHLivePhoto` (PhotoKit), `LivePhotosKit JS`

## Related
photo-editing, activity-views
