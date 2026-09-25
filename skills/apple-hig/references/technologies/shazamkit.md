# ShazamKit

> Source: https://developer.apple.com/design/human-interface-guidelines/shazamkit · ShazamKit supports audio recognition by matching an audio sample against the ShazamKit catalog or a custom audio catalog.

## When to use / core idea
- Example features: graphics matching the genre of currently playing music; closed captions or sign language synced with audio for people with hearing disabilities; syncing in-app experiences with virtual content (online learning, retail).
- If you need the microphone for samples, you must request access and explain why (see `privacy`).

## Rules
### Best practices
- **Stop recording as soon as possible** — people don't expect the mic to stay on; record only as long as needed to get the sample.
- **Let people opt in to storing your app's recognized songs to their iCloud library** — get approval first, even though the Music Recognition control and Shazam app show your app as the source.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## APIs
`ShazamKit`

## Related
privacy, icloud
