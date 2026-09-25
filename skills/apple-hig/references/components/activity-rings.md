# Activity rings

> Source: https://developer.apple.com/design/human-interface-guidelines/activity-rings · Activity rings show an individual's daily progress toward Move, Exercise, and Stand goals.

## When to use / core idea
- watchOS: element always contains three rings, colors/meanings matching the Activity app. iOS: a single Move ring (approximation of activity), or all three if an Apple Watch is paired.
- Use only for Move/Exercise/Stand progress of one person in health/fitness contexts; for other data use gauges, progress indicators, or charts.

## Rules
### Best practices
- **Display Activity rings when they're relevant to the purpose of your app** — health/fitness apps (especially those contributing to HealthKit) are expected to show them; e.g., on a workout metrics screen during a session, or on an end-of-workout summary screen.
- **Use Activity rings only to show Move, Exercise, and Stand information** — don't replicate or modify them for other purposes. Never use them for other data types. Never show Move/Exercise/Stand progress in another ring-like element.
- **Use Activity rings to show progress for a single person** — never for more than one person; make it obvious whose progress via a label, photo, or avatar.
- **Always keep the visual appearance of Activity rings the same, regardless of where you display them:**
  - Never change ring colors (no filters, no opacity changes).
  - Always display on a black background.
  - Prefer enclosing rings and background within a circle — adjust the enclosing view's corner radius rather than applying a circular mask.
  - Keep the black background visible around the outermost ring; if needed add a thin black stroke around the outer edge; avoid gradients, shadows, or other effects.
  - Always scale rings appropriately so they don't seem disconnected or out of place.
  - When necessary, design the surrounding interface to blend with the rings; never change the rings to blend with the interface.
- **To display a label or value that's directly associated with an Activity ring, use the colors that match it** — for labels *Move*, *Exercise*, *Stand* and current/goal values (see Specs).
- **Maintain Activity ring margins** — minimum outer margin no less than the distance between rings. Never let other elements crop, obstruct, or encroach on the margin or rings.
- **Differentiate other ring-like elements from Activity rings** — separate other rings with padding, lines, or labels; color and scale also help.
- **Don't send notifications that repeat the same information the Activity app sends** — system already sends progress updates. Don't show an Activity ring element in notifications. Referencing Activity progress is fine if unique to your app.
- **Don't use Activity rings for decoration** — never in labels or background graphics.
- **Don't use Activity rings for branding** — never in your app icon or marketing materials.

## Platform considerations
No additional considerations: iPadOS, watchOS. Not supported: macOS, tvOS, visionOS.

### iOS
- Available via `HKActivityRingView`; appearance changes automatically:
  - Apple Watch paired → all three rings.
  - No Apple Watch → Move ring only, approximating activity from steps and workout info from other apps.
- Activity history can mix both styles (three rings on days exercised with Watch, Move-only otherwise).

## Specs
Label/value colors (RGB):

| Move | Exercise | Stand |
| --- | --- | --- |
| R 250, G 17, B 79 | R 166, G 255, B 0 | R 0, G 255, B 246 |

- Outer margin ≥ distance between rings.
- Background: black.

## APIs
`HKActivityRingView` (HealthKitUI).

## Related
`workouts, gauges, progress-indicators, notifications`
