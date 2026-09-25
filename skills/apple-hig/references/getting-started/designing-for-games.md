# Designing for games

> Source: https://developer.apple.com/design/human-interface-guidelines/designing-for-games · How to integrate fundamental platform characteristics and patterns so a game feels at home on all Apple devices.

## When to use / core idea
- Cross-platform guidance for creating or porting games; pair with the per-platform pages (designing-for-ios/ipados/macos/tvos/visionos/watchos).

## Rules

### Jump into gameplay
- **Let people play as soon as installation completes** — include as much playable content as possible in the initial install while keeping download time to **30 minutes or less**; download additional content in the background.
- **Provide great default settings** — use device info to choose defaults (resolution that makes graphics look great, automatic recognition of paired accessories and game controllers, player's accessibility settings). Support the platform's most common interaction methods.
- **Teach through play** — integrate configuration and onboarding into a playable tutorial that engages quickly and makes players feel successful. Consider offering any written tutorial as a reference resource, not a prerequisite for gameplay.
- **Defer requests until the right time** — don't bombard people with requests before play. Sensor or data access (e.g., hand-tracking) requires permission first; integrate the request into the scenario needing the data (e.g., ask to track hands between the opening cutscene and first hand-controlled action). Let people spend quality time with the game before asking for a rating or review.

### Look stunning on every display
- **Make sure text is always legible** — good contrast with background and at least the platform's minimum text size (table below).
- **Make sure buttons are always easy to use** — too small or too close together frustrates players; buttons in iOS must be at least 44x44 pt for touch (table below).
- **Prefer resolution-independent textures and graphics** — if not possible, match game resolution to device resolution. In visionOS, prefer vector-based art that looks good as the system dynamically scales it across distances and angles.
- **Integrate device features into your layout** — accommodate rounded corners, camera housing, etc.; rely on platform-provided safe areas when possible.
- **Make sure in-game menus adapt to different aspect ratios** (e.g., 16:10, 19.5:9, 4:3) — menus stay legible and usable on every device and, if supported, in both orientations on iPhone/iPad, without obscuring content. Consider dynamic layouts with relative constraints; avoid fixed layouts as much as possible; create custom device-specific layouts only when necessary.
- **Design for the full-screen experience** — full-screen mode in macOS, iOS, iPadOS hides other apps and system UI; in visionOS a game in a Full Space can completely surround people.

### Enable intuitive interactions
- **Support each platform's default interaction method** — touch on iPhone; keyboard + mouse/trackpad on Mac; eyes and hands with indirect/direct gestures in visionOS. Pay special attention to control sizing and menu behavior, especially when moving from pointer-based to touch-based.
- **Support physical game controllers, while also giving people alternatives** — every platform except watchOS supports them; not every player can use one, so offer alternative ways to interact.
- **Offer touch-based game controls that embrace the touchscreen on iPhone and iPad** — let players interact directly with game elements and use virtual controls overlaid on game content.

### Welcome everyone
- **Prioritize perceivability** — content must be perceivable via sight, hearing, or touch. E.g., avoid relying solely on color for important details; cutscenes need descriptive subtitles or other ways to read content. Covers text sizes, color and effects, motion, interactions, buttons.
- **Help players personalize their experience** — no universal configuration; let players customize type size, game control mapping, motion intensity, sound balance. Use built-in Apple accessibility technologies (system frameworks or Unity plug-ins).
- **Give players the tools they need to represent themselves** — for avatars, names, descriptions, support the spectrum of self-identity and represent as many human characteristics as possible.
- **Avoid stereotypes in your stories and characters** — e.g., don't depict enemies as a certain race, gender, or cultural heritage; review to remove biases; references to real-life cultures and languages must be respectful.

### Adopt Apple technologies
- **Integrate Game Center** (Apple's social gaming network, all platforms) — progress, achievements, leaderboards, challenges, multiplayer; helps discovery across devices and connecting with friends.
- **Let players pick up their game on any of their devices** — support GameSave to save state and resume on another device via iCloud account.
- **Support haptics to help players feel the action** — Core Haptics composes custom haptic patterns, optionally with custom audio; available in iOS, iPadOS, tvOS, visionOS and on many game controllers.
- **Use Spatial Audio to immerse players** — provide multichannel audio so audio adapts automatically to the device.
- **Take advantage of Apple technologies to enable unique gameplay mechanics** — AR, machine learning, HealthKit, location, camera, microphone.

## Specs

### Text size
| Platform | Default text size | Minimum text size |
| --- | --- | --- |
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

### Button size
| Platform | Default button size | Minimum button size |
| --- | --- | --- |
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

### Interaction methods
| Platform | Default interaction methods | Additional interaction methods |
| --- | --- | --- |
| iOS | Touch | Game controller |
| iPadOS | Touch | Game controller, keyboard, mouse, trackpad, Apple Pencil |
| macOS | Keyboard, mouse, trackpad | Game controller |
| tvOS | Remote | Game controller, keyboard, mouse, trackpad |
| visionOS | Touch | Game controller, keyboard, mouse, trackpad, spatial game controller |
| watchOS | Touch | – |

### Other values
- Initial download time: 30 minutes or less.
- Example aspect ratios to support: 16:10, 19.5:9, 4:3.

## APIs
`GameKit` (Game Center), `GameSave`, `Core Haptics`, `HealthKit`, Apple Unity plug-ins

## Related
designing-for-ios, designing-for-ipados, designing-for-macos, designing-for-tvos, designing-for-visionos, designing-for-watchos, loading, launching, onboarding, settings, privacy, ratings-and-reviews, typography, buttons, images, layout, menus, going-full-screen, game-controls, gestures, pointing-devices, accessibility, inclusion, game-center, icloud, playing-haptics, playing-audio, technologies, apple-in-app-purchase
