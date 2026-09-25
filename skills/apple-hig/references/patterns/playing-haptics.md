# Playing haptics

> Source: https://developer.apple.com/design/human-interface-guidelines/playing-haptics · Haptics engage people's sense of touch and bring familiarity with the physical world into your app or game.

## When to use / core idea
- The system plays haptics alongside visual/audio feedback: switches, sliders, pickers play haptics automatically on supported iPhones; Apple Watch Taptic Engine plays built-in patterns combined with an audible tone; Mac Force Touch trackpad can play haptics during drags or force clicks (e.g. changing media control speed).
- External devices: game controllers in iPadOS, macOS, tvOS, visionOS apps/games; Apple Pencil Pro and some trackpads with certain iPad models.
- Use to complement other feedback (see `feedback`), not replace it.

## Rules
### Best practices
- **Use system-provided haptic patterns according to their documented meanings** — people recognize standard haptics; if a pattern's documented use doesn't fit, don't repurpose it — use a generic pattern or create a custom one, where supported.
- **Use haptics consistently throughout your app or game** — build a clear causal relationship between haptic and action; e.g. don't reuse a mission-failure pattern for level completion.
- **Prefer using haptics to complement other feedback in your app or game** — harmonize visual, audio, tactile; match haptic intensity and sharpness to the accompanying animation; sound can be synchronized with haptics.
- **Avoid overusing haptics** — occasional can feel right, frequent becomes tiresome; user-test for balance; the best haptics may go unnoticed but are missed when off.
- **In most apps, prefer playing short haptics that complement discrete events** — long-running haptics suit gameplay flows but in apps dilute meaning and distract; on Apple Pencil Pro continuous/long haptics don't clarify writing/drawing and can make holding it less pleasant.
- **Make haptics optional** — let people turn off or mute them; app must still be enjoyable without them.
- **Be aware that playing haptics might impact other user experiences** — ensure vibrations don't disrupt camera, gyroscope, or microphone use.

### Custom haptics
- Games often use custom haptics; nongame apps less commonly, for richer experiences. Patterns can vary dynamically with input/context (e.g. stronger impact jumping from a tree than in place; collisions feel different from approaching footsteps).
- Building blocks: *Transient* events — brief, compact taps/impulses (e.g. tapping the Flashlight button on the Home Screen). *Continuous* events — sustained vibrations (e.g. Messages lasers effect).
- Control *sharpness* (abstracts the waveform; conveys intent — soft/rounded/organic vs. crisp/precise/mechanical) and *intensity* (strength). Combine event types, vary sharpness/intensity, optionally add audio (Core Haptics).

## Platform considerations
### iOS
- Use standard components (`toggles`, `sliders`, `pickers`) that play system haptics by default.
- When it makes sense, use a feedback generator for predefined patterns:
  - *Notification* — outcome of a task/action (e.g. depositing a check, unlocking a vehicle).
  - *Impact* — physical metaphor complementing visuals (tap when a view snaps into place, thud when heavy objects collide).
  - *Selection* — feedback while a UI element's values are changing.
### macOS
- With a Magic Trackpad, provide one of three patterns in response to a drag or force click (see Specs).
### watchOS
- Apple Watch Series 4 and later: Digital Crown haptic feedback; by default linear haptic detents while rotating; some system controls (e.g. table views) provide detents as new items scroll on screen.
- watchOS haptics each convey a specific meaning (see Specs).

## Specs
macOS Force Touch / Magic Trackpad patterns:

| Haptic feedback pattern | Description |
| --- | --- |
| Alignment | Indicates alignment of a dragged item — e.g. dragging a shape into alignment with another in a drawing app; scaling to fit specific dimensions; positioning at a preferred location; reaching beginning/end or min/max of e.g. a video scrubber. |
| Level change | Indicates movement between discrete pressure levels — e.g. pressing a video player's fast-forward button changes playback speed with feedback at each pressure level. |
| Generic | General feedback when other patterns don't apply. |

watchOS haptic types:

| Haptic | Meaning |
| --- | --- |
| Notification | Something significant or out of the ordinary happened and requires attention; also played when a local or remote notification arrives. |
| Up | An important value increased above a significant threshold. |
| Down | An important value decreased below a significant threshold. |
| Success | An action completed successfully. |
| Failure | An action failed. |
| Retry | An action failed but can be retried. |
| Start | An activity started (e.g. timer or any explicitly start/stop activity); Stop usually follows. |
| Stop | An activity the person previously started stopped (e.g. timer). |
| Click | Sensation of a dial clicking to communicate progress at predefined increments/intervals; overuse diminishes utility and overlapping clicks confuse. |

## APIs
Core Haptics (incl. Playing Haptics on Game Controllers, Delivering Rich App Experiences with Haptics), `UIFeedbackGenerator` (UIKit), `NSHapticFeedbackPerformer` (AppKit), `WKHapticType` (WatchKit)

## Related
`feedback, gestures, game-controls, apple-pencil-and-scribble, toggles, sliders, pickers, digital-crown`
