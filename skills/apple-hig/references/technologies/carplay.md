# CarPlay

> Source: https://developer.apple.com/design/human-interface-guidelines/carplay · CarPlay lets people get directions, make calls, message, listen to music, and more from the car's built-in display while staying focused on the road.

## When to use / core idea
- CarPlay apps install on iPhone via the App Store; icons appear on the CarPlay Home screen when iPhone connects to the vehicle.
- Designed for drivers while driving: features must let people perform tasks quickly with minimal interaction.
- UI is built from system-defined templates per app type (audio, communication, navigation, fueling, etc.); app supplies content, iOS renders it. System handles screen resolutions and input hardware (touchscreens, knobs, touch pads). See CarPlay App Programming Guide.

## Rules
### iPhone interactions
- **Eliminate app interactions on iPhone when CarPlay is active** — use car controls/display; any required iPhone setup must happen before the vehicle is in motion.
- **Never lock people out of CarPlay because the connected iPhone requires input** — must work when iPhone is inaccessible (bag, trunk); problems needing iPhone can be resolved after the vehicle stops.
- **Make sure your app works without requiring people to unlock iPhone** — most use CarPlay with iPhone locked.

### Audio
- Your app coexists with other audio (car radio, navigation voice prompts).
- **Let people choose when to start playback** — avoid auto-play unless the app plays a single audio source or is resuming interrupted audio; don't start an audio session until ready to play (it silences other sources like the radio).
- **Start playback as soon as audio has sufficiently loaded** — system keeps the selection highlighted with a spinning activity indicator until your app signals ready.
- **Display the Now Playing screen when audio is ready to play** — don't delay playback for descriptive info; load it in the background and show when available.
- **Resume audio playback after an interruption only when it's appropriate** — temporary (phone call) is resumable; permanent (Siri-initiated playlist) is not. After a resumable interruption, resume if audio was actively playing when it began.
- **When necessary, automatically adjust audio levels, but don't change the overall volume** — adjust relative levels for mix; people control final output volume.

### Layout
- System scales icons and interfaces per display so they appear at roughly the same size.
- **Provide useful, high-value information in a clean layout that's easy to scan from the driver's seat** — no nonessential details or unnecessary embellishments.
- **Maintain an overall consistent appearance throughout your app** — similar functions look similar.
- **Ensure that primary content stands out and feels actionable** — larger items seem more important and are easier to tap; place most important content and controls in the upper half of the screen.

### Color
- **In general, prefer a limited color palette that coordinates with your app logo** — subtle brand color.
- **Avoid using the same color for interactive and noninteractive elements.**
- **Test your app's color scheme under a variety of lighting conditions in an actual car** — time of day, weather, window tint; bright colors at night, low-contrast colors washing out in direct sunlight; adjust for most use cases.
- **Ensure your app looks great in both dark and light environments** — CarPlay supports both and may switch automatically based on lighting.
- **Choose colors that help you communicate effectively with everyone** — see inclusive color.

### Icons and images
- CarPlay supports landscape and portrait displays and @2x (low resolution) and @3x (high resolution) scale factors.
- **Supply high-resolution images at @2x and @3x for all CarPlay artwork** — system picks and scales per display.
- **Mirror your iPhone app icon** — no second design needed.
- **Don't use black for your icon's background** — lighten it or add a border so it doesn't blend into the display background.

### Error handling
- Handle errors gracefully; report only when absolutely necessary.
- **Report errors in CarPlay, not on the connected iPhone** — never direct people to pick up iPhone to read or resolve an error.

## Platform considerations
No additional considerations: iOS. Not supported in iPadOS, macOS, tvOS, visionOS, watchOS.

## Specs
Common CarPlay screen sizes:

| Dimensions (pixels) | Aspect ratio |
|---|---|
| 800x480 | 5:3 |
| 960x540 | 16:9 |
| 1280x720 | 16:9 |
| 1920x720 | 8:3 |

CarPlay app icon:

| @2x (pixels) | @3x (pixels) |
|---|---|
| 120x120 | 180x180 |

## APIs
CarPlay framework templates (see CarPlay App Programming Guide)

## Related
color, app-icons, playing-audio, dark-mode, layout
