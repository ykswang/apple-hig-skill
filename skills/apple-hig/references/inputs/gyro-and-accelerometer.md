# Gyroscope and accelerometer

> Source: https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer · On-device gyroscopes and accelerometers supply data about a device's movement in the physical world.

## When to use / core idea
- Real-time motion-based experiences in iOS, iPadOS, and watchOS apps and games; tvOS apps can use gyroscope data from the Siri Remote.
- Accessing motion data requires copy explaining why; the system shows it in a permission request the first time the app tries to access the data, where people grant or deny.

## Rules
- **Use motion data only to offer a tangible benefit to people** — e.g., fitness feedback on activity/health, enhanced gameplay. Avoid gathering data simply to have it.
- **Outside of active gameplay, avoid using accelerometers or gyroscopes for the direct manipulation of your interface** — motion gestures can be hard to replicate precisely, physically challenging for some people, and affect battery usage.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## APIs
`Core Motion` (Core Motion), `Getting processed device-motion data` (Core Motion)

## Related
`feedback, privacy, remotes`
