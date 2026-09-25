# HealthKit

> Source: https://developer.apple.com/design/human-interface-guidelines/healthkit · HealthKit is the central repository for health and fitness data in iOS, iPadOS, and watchOS.

## When to use / core idea
- Lets your app ask permission to read and write people's health information (e.g., a nutrition app reads weight/activity, writes logged calories).
- **Important:** if your app doesn't provide health and fitness functionality, don't request access to private health data.
- For showing Move/Exercise/Stand progress, use the Activity ring element (see `activity-rings`).

## Rules
### Privacy protection
- You must request permission to access data and take all necessary steps to protect it; clearly show how you use it.
- **Provide a coherent privacy policy** — a URL to a clearly stated policy is required at App Store submission; linked from the App Store page.
- **Request access to health data only when you need it** — e.g., request weight access when people log weight, not at launch. People can change permissions, so request every time you need access.
- **Clarify your app's intent by adding descriptive messages to the standard permission screen** — a few succinct sentences on why you need the data and how people benefit. Avoid custom screens that replicate the standard permission screen's behavior or content.
- **Manage health data sharing solely through the system's privacy settings** — people manage access in Settings > Privacy; don't build in-app screens that affect the flow of health data.

### Activity rings
- The Activity app defines ring position and color, so people recognize the element.
- **Use Activity rings for Move, Exercise, and Stand information only** — don't replicate or modify them for other data; never show Move/Exercise/Stand progress in another ring-like element.
- **Use Activity rings to show progress for a single person** — never for more than one person; make it obvious whose progress it is (label, photo, avatar).
- **Don't use Activity rings for ornamentation** — never in labels or background graphics.
- **Don't use Activity rings for branding** — never in the app icon or marketing materials.
- **Maintain Activity ring and background colors** — never change the rings/background with filters, colors, or opacity; design surrounding UI to blend (e.g., enclose rings in a circle). Always scale rings appropriately so they don't look out of place.
- **Maintain Activity ring margins** — minimum outer margin no less than the distance between rings; never let other elements crop, obstruct, or encroach on the margin or rings. To show inside a circle, adjust the enclosing view's corner radius rather than applying a circular mask.
- **Differentiate other ring-like elements from Activity rings** — if you must include other rings, separate with padding, lines, or labels; color and scale help too.
- **Provide app-specific information only in Activity notifications** — the system already delivers progress updates; don't repeat them and never show an Activity ring element in notifications. Referencing Activity progress is fine if unique to your app.

### Apple Health icon
- Indicates an app works with HealthKit and the Health app. For marketing badge, see "Works with Apple Health".
- **Use only the Apple-provided icon** — don't create or mimic; download from Apple Design Resources.
- **Display the name *Apple Health* close to the Apple Health icon.**
- **Display the Apple Health icon consistently with other health-related app icons** — no smaller than other icons in the same view.
- **Don't use the Apple Health icon as a button** — only to indicate compatibility.
- **Don't alter the appearance of the Apple Health icon** — no masking to change corner radius or make circular; no borders, color overlays, gradients, shadows, or other effects.
- **Maintain a minimum clear space around the Apple Health icon of 1/10 of its height** — don't composite it onto another graphic element.
- **Don't use the Apple Health icon within text or as a replacement for the terms *Health*, *Apple Health*, or *HealthKit*.**
- **Don't display Health app images or screenshots** — copyrighted; can't appear in app or marketing. Use an Activity ring element to show progress instead.

### Editorial guidelines
- **Refer to the Health app as *Apple Health* or *the Apple Health app*.**
- **Don't use the term *HealthKit*** — it's developer-facing; say e.g. "works with the Apple Health app" or "uses data from the Apple Health app."
- **Use correct capitalization when using the term *Apple Health*** — two words, uppercase A and H, rest lowercase; all-caps only to conform to an established all-caps typographic style.
- **Use the system-provided translation of *Health* to avoid confusing people.**

## Platform considerations
No additional considerations: iOS, iPadOS, watchOS. Not supported in macOS, tvOS, or visionOS.

## Specs
- Apple Health icon clear space: minimum 1/10 of icon height.
- Activity ring outer margin: ≥ distance between rings.

## APIs
`HealthKit`, `requestAuthorization(toShare:read:completion:)` (HKHealthStore), `HKActivityRingView` (HealthKitUI)

## Related
activity-rings, privacy
