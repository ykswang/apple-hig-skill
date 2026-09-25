# Nearby interactions

> Source: https://developer.apple.com/design/human-interface-guidelines/nearby-interactions · Nearby interactions support on-device experiences that integrate the presence of people and objects in the nearby environment.

## When to use / core idea
- Builds on people's innate awareness of their surroundings — e.g., bring iPhone close to HomePod mini to transfer audio.
- Requires Ultra Wideband-capable devices and the Nearby Interaction framework. People grant permission for their device to interact while using your app. Privacy: randomly generated device identifiers last only for the app-initiated session.

## Rules
### Best practices
- **Consider a task from the perspective of the physical world to find inspiration for a nearby interaction** — e.g., initiating a song transfer by bringing devices together feels rooted in the physical world.
- **Use distance, direction, and context to inform an interaction** — prioritize nearby, contextually relevant info; e.g., share sheet combines frequent/recent contacts with U1-chip device data to suggest the closest contact the person is facing.
- **Consider how changes in physical distance can guide a nearby interaction** — feedback should sharpen with proximity (finding AirTag: directional arrow transitions to a pulsing circle as you get closer).
- **Provide continuous feedback** — uninterrupted updates on direction and proximity that respond to movement (Find My).
- **Consider using multiple feedback types to create a holistic experience** — transition fluidly among visual, audible, haptic; visual while people look at the screen, audible and haptic while they engage with the environment.
- **Avoid using a nearby interaction as the only way to perform a task** — provide alternatives.

### Device usage
- **Encourage people to hold the device in portrait orientation** — landscape reduces accuracy and availability of distance/direction. If only portrait is supported during the feature, prefer implicit visual cues; when possible avoid explicitly telling people to hold in portrait.
- **Design for the device's directional field of view** — sensor field of view is similar to the Ultra Wide camera on iPhone 11 and later; outside it you may get distance but not relative direction.
- **Help people understand how intervening objects can affect the nearby interaction experience in your app** — people, animals, or large objects between devices reduce accuracy/availability; consider advice in onboarding or tutorials.

## Platform considerations
No additional considerations: iPadOS. Not supported: macOS, tvOS, visionOS.

### iOS
- On iPhone, APIs provide a peer device's distance and direction.

### watchOS
- On Apple Watch, APIs provide a peer device's distance only; all participating watchOS apps must be in the foreground.

## APIs
`Nearby Interaction` (Nearby Interaction)

## Related
`feedback, playing-haptics`
