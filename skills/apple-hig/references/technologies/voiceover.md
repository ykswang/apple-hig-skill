# VoiceOver

> Source: https://developer.apple.com/design/human-interface-guidelines/voiceover · VoiceOver is a screen reader that lets people experience your app's interface without needing to see the screen.

## When to use / core idea
- Helps people who are blind or have low vision access information and navigate when they can't see the display.
- Supported in apps and games on Apple platforms, and in Unity apps/games via Apple's Unity plug-ins. See also `accessibility`.
- You inform VoiceOver via alternative text describing the interface and content.

## Rules
### Descriptions
- **Provide alternative labels for all key interface elements** — labels aren't visible onscreen; system controls have generic default labels, so provide more descriptive ones conveying your app's functionality; label all custom elements; keep descriptions up to date as UI/content change.
- **Describe meaningful images** — describe only what the image itself conveys (VoiceOver already reads surrounding captions).
- **Make charts and other infographics fully accessible** — concise description of what each conveys; make interactions that reveal more/different info available to VoiceOver too (accessibility APIs can represent custom interactive elements). See `charts`.
- **Exclude purely decorative images from VoiceOver** — respects people's time, reduces cognitive load.

### Navigation
- **Use titles and headings to help people navigate your information hierarchy** — the title is the first thing announced on a page/screen; make titles unique and succinct about content and purpose; use accurate section headings.
- **Specify how elements are grouped, ordered, or linked** — find relationships that are visual only (proximity, alignment) and describe them to VoiceOver. VoiceOver reads in the reading order of the active language/locale (US English: top-to-bottom, left-to-right). E.g., group each image with its own caption so they're read together, rather than reading all images and then all captions.
- **Inform VoiceOver when visible content or layout changes occur** — unexpected changes invalidate people's mental map; report them.
- **Support the VoiceOver rotor when possible** — identify headings, links, and other content types so people can navigate by them; the rotor can also bring up the braille keyboard.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, watchOS.
### visionOS
- **Be mindful that custom gestures aren't always accessible** — with VoiceOver on, apps defining custom gestures don't receive hand input by default (so people can explore by voice). People can opt out via Direct Gesture mode, which disables standard VoiceOver gestures and lets apps process hand input directly.

## APIs
Accessibility modifiers (SwiftUI), `accessibilityHidden(_:)` (SwiftUI), `accessibilityElement` (AppKit `NSAccessibility`), `isAccessibilityElement` (UIKit), `shouldGroupAccessibilityChildren` (NSObject), `AccessibilityNotification` (Accessibility), `AccessibilityRotorEntry` (SwiftUI), `UIAccessibilityCustomRotor` (UIKit), `NSAccessibilityCustomRotor` (AppKit)

## Related
accessibility, inclusion, charts, images, gestures
