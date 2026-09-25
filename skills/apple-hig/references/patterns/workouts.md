# Workouts

> Source: https://developer.apple.com/design/human-interface-guidelines/workouts · A great workout or fitness experience encourages people to engage with their current activity and helps them track progress on their devices.

## When to use / core idea
- Apple Watch is worn during many workouts; iPhone/iPad carried for walking, wheelchair pushing, running; larger/stationary devices (iPad Pro, Mac, Apple TV) are used for live or recorded workout sessions alone or with others.
- Build workout experiences for Apple Watch, iPhone, or iPad using device activity data and familiar components for fitness metrics. See `activity-rings`.

## Rules
### Best practices
- **In a watchOS fitness app, use workout sessions to provide useful data and relevant controls** — during active sessions watchOS keeps showing the app between wrist raises; show key data (elapsed/remaining time, calories burned, distance) and relevant controls (lap or interval markers).
- **Avoid distracting people from a workout with information that's not relevant** — e.g. no workout list or other app areas mid-workout. Common watchOS arrangement (as in Workout): left screen = controls (End, Resume, New, Segment); middle = metrics (elapsed time, active calories, heart rate, average pace, elevation); right = Now Playing music.
- **Use a distinct visual appearance to indicate an active workout** — real-time updating metrics page signals an active session; further distinguish it with a unique layout.
- **Provide workout controls that are easy to find and tap** — easy pause, resume, stop; clear feedback when a session starts or stops.
- **Help people understand the health information your app records if sensor data is unavailable during a workout** — e.g. water may block heart-rate readings but distance swum and calories can still be recorded; for *Swimming* or *Other* workout types, explain using language similar to the Workout app, e.g.:
  - "GPS is not used during a Pool Swim, and water may prevent a heart-rate measurement, but Apple Watch will still track your calories, laps, and distance using the built-in accelerometer."
  - "In this type of workout, you earn the calorie equivalent of a brisk walk anytime sensor readings are unavailable."
  - "GPS will only provide distance when you do a freestyle stroke. Water might prevent a heart-rate measurement, but calories will still be tracked using the built-in accelerometer."
- **Provide a summary at the end of a session** — confirms the workout finished and shows recorded info; consider including Activity rings to show current progress.
- **Discard extremely brief workout sessions** — if it ends a few seconds after starting, discard automatically or ask whether to record it.
- **Make sure text is legible for when people are in motion** — large font sizes, high-contrast colors, most important info easiest to read.
- **Use Activity rings correctly** — Apple-designed element whose ring colors and meanings match the Activity app; use only for their documented purpose.

## Platform considerations
No additional considerations: iOS, iPadOS, watchOS. Not supported: macOS, tvOS, visionOS.

## APIs
WorkoutKit, Workouts and activity rings (HealthKit)

## Related
`activity-rings`
