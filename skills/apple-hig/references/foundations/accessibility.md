# Accessibility

> Source: https://developer.apple.com/design/human-interface-guidelines/accessibility · Accessible user interfaces empower everyone to have a great experience with your app or game.

## When to use / core idea
- Applies to every app/game. An accessible interface is **Intuitive** (familiar, consistent interactions), **Perceivable** (never relies on a single method to convey information — sight, hearing, speech, touch), **Adaptable** (supports system accessibility features and personalization).
- Audit with Accessibility Inspector; declare support on the App Store via Accessibility Nutrition Labels.
- Screen-reader details live in `voiceover`; Dynamic Type details in `typography`.

## Rules
### Vision
- Audience: blind, color blind, low vision, light sensitivity, or poor lighting/brightness conditions.
- **Support larger text sizes** — let people enlarge text/icons; ideally at least **200%** (**140%** in watchOS), via custom UI or Dynamic Type.
- **Use recommended defaults for custom type sizes** — follow each platform's default/minimum (see Specs).
- **Bear in mind that font weight can also impact how easy text is to read** — with a thin custom font, aim larger than recommended sizes.
- **Strive to meet color contrast minimum standards** — between foreground text/icons and background; WCAG and APCA are common measures; Accessibility Inspector uses WCAG Level AA values (see Specs). If default colors don't meet the minimum, at least provide a higher-contrast scheme when Increase Contrast is on. With Dark Mode, check contrast in both light and dark.
- **Prefer system-defined colors** — they have accessible variants that adapt to Increase Contrast and light/dark.
- **Convey information with more than color alone** — red-green and blue-orange are hard for color-blind people; add distinct shapes or icons for function and state changes. Consider letting people customize color schemes (e.g., chart colors, game characters).
- **Describe your app's interface and content for VoiceOver** — see `voiceover`.

### Hearing
- Audience: deaf, hard of hearing, or in noisy/public environments.
- **Support text-based ways to enjoy audio and video** — dialogue and crucial info must not be audio-only; let people customize text presentation:
  - *Captions*: textual equivalent of audible info, synced live (cutscenes, video clips).
  - *Subtitles*: onscreen dialogue in preferred language (TV, movies).
  - *Audio descriptions*: spoken narration of visual-only info, placed in natural pauses.
  - *Transcripts*: complete textual description of audible and visual info (podcasts, audiobooks; reviewable/highlightable during playback).
- **Use haptics in addition to audio cues** — pair success chimes, error sounds, game feedback with matching haptics. iOS/iPadOS: Music Haptics and Audio graphs convey music and infographics through vibration/texture.
- **Augment audio cues with visual cues** — especially games and spatial apps with off-screen content; add visual indicators pointing where to interact.

### Mobility
- **Offer sufficiently sized controls** — meet recommended minimum control size per platform (see Specs).
- **Consider spacing between controls as important as size** — about **12 pt** padding around bezeled elements; about **24 pt** around the visible edges of elements without a bezel.
- **Support simple gestures for common interactions** — simplest gesture possible for frequent actions; avoid custom multifinger and multihand gestures.
- **Offer alternatives to gestures** — core functionality reachable via more than one physical interaction; e.g., swipe-to-dismiss also gets a button (or swipe-to-delete also has edit-mode delete buttons).
- **Let people use Voice Control to give guidance and enter information verbally** — label interface elements appropriately.
- **Integrate with Siri and Shortcuts to let people perform tasks using voice alone** — invocable from Siri, Action button (iPhone/Apple Watch), Home Screen shortcuts, Control Center.
- **Support mobility-related assistive technologies** — VoiceOver, AssistiveTouch, Full Keyboard Access, Pointer Control, Switch Control; test support and labeling.

### Speech
- **Let people use the keyboard alone to navigate and interact with your app** — support Full Keyboard Access; avoid overriding system-defined keyboard shortcuts.
- **Support Switch Control** — control via separate hardware, game controllers, or sounds (click, pop) for selecting, tapping, typing, drawing.

### Cognitive
- **Keep actions simple and intuitive** — easy-to-remember, consistent interactions; prefer familiar system gestures/behaviors over custom ones.
- **Minimize use of time-boxed interface elements** — timer auto-dismiss hurts people needing more time and assistive-tech users; prefer dismissal by explicit action.
- **Consider offering difficulty accommodations in games** — e.g., reduce level-completion criteria, adjust reaction time, enable control assistance.
- **Let people control audio and video playback** — avoid autoplay without discoverable start/stop controls; consider a global opt-out of autoplay (`isVideoAutoplayEnabled`).
- **Allow people to opt out of flashing lights in video playback** — respond to the Dim Flashing Lights setting.
- **Be cautious with fast-moving and blinking animations** — excess can distract, cause dizziness, even epileptic episodes. When Reduce Motion is on, reduce automatic and repetitive animations (zooming, scaling, peripheral motion). Also:
  - Tighten animation springs to reduce bounce.
  - Track animations directly with gestures.
  - Avoid animating depth changes in z-axis layers.
  - Replace x/y/z-axis transitions with fades.
  - Avoid animating into and out of blurs.
- **Optimize your app's UI for Assistive Access** — iOS/iPadOS streamlined mode for cognitive disabilities with a default layout/control presentation. When on:
  - Identify core functionality; consider removing noncritical workflows and UI elements.
  - Break multistep workflows into a single interaction per screen.
  - Always ask for confirmation twice for hard-to-recover actions (e.g., deleting a file).

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, watchOS.

### visionOS
- Features include head and hand Pointer Control and Zoom (lens magnifies content beneath it).
- **Prioritize comfort** — immersion increases risk of motion sickness and visual/ergonomic discomfort:
  - Keep elements within field of view; prefer horizontal over vertical layouts (neck strain); avoid demanding attention in different locations in quick succession.
  - Reduce speed and intensity of animated objects, especially in peripheral vision.
  - Be gentle with camera/video motion; avoid the world seeming to move without the person's control.
  - Avoid head-anchored content (feels confining; blocks Pointer Control).
  - Minimize large and repetitive gestures.

## Specs

### Text sizes (custom type styles)
| Platform | Default size | Minimum size |
| --- | --- | --- |
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |

Text enlargement target: ≥ 200% (≥ 140% watchOS).

### Contrast (WCAG Level AA, used by Accessibility Inspector)
| Text size | Text weight | Minimum contrast ratio |
| --- | --- | --- |
| Up to 17 pts | All | 4.5:1 |
| 18 pts | All | 3:1 |
| All | Bold | 3:1 |

### Control sizes
| Platform | Default control size | Minimum control size |
| --- | --- | --- |
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| tvOS | 66x66 pt | 56x56 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

Spacing: ~12 pt around bezeled elements; ~24 pt around visible edges of non-bezeled elements.

## APIs
Accessibility Inspector, Accessibility framework, Voice Control, Switch Control, Assistive Access, Music Haptics (MediaAccessibility), Audio graphs (Accessibility), Flashing lights (MediaAccessibility), Animated images (Accessibility), `UIAccessibility.isVideoAutoplayEnabled` (UIKit), subtitles/alternative audio tracks (AVFoundation)

## Related
inclusion, typography, voiceover, color, dark-mode, playing-haptics, keyboards, siri
