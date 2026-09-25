# Action button

> Source: https://developer.apple.com/design/human-interface-guidelines/action-button · The Action button gives people quick access to their favorite features on supported iPhone and Apple Watch models.

## When to use / core idea
- Runs App Shortcuts or system functions (e.g., flashlight toggle); on Apple Watch Ultra, supports activity actions including workouts and dives.
- People pick the function at device setup and can change it in Settings. An App Shortcut assigned to it runs like invoking via Siri or Spotlight.
- Treat it as another fast path to a function people use regularly. Alternatives for opening your app: app icon, widgets, complications.

## Rules
### Best practices
- **Support the Action button with a set of your app's essential functions** — e.g., "Start Egg Timer" in a cooking app. Don't offer an App Shortcut that just opens your app; the system already provides it.
- **For each action you support, write a short label that succinctly describes it** — shown in Settings. Title-style capitalization, begin with a verb, present tense, no articles or prepositions, maximum of three words ("Start Race," not "Started Race" or "Start the Race").
- **Prefer letting the system show people how to use the Action button with your app** — system helps configure it automatically; avoid content that repeats Settings guidance or system usage tips.

## Platform considerations
Not supported: iPadOS, macOS, tvOS, visionOS.

### iOS
- **Let people use your actions without leaving their current context** — use Live Activities and custom snippets instead of opening the app (e.g., "Set Timer" prompts for a duration, then launches a countdown Live Activity without opening Clock).

### watchOS
- First press can drop a waypoint, start a dive, or begin a specific workout; subsequent presses support secondary actions (mark a segment, advance to next modality in a multi-part workout).
- **Consider offering a secondary function that supports or advances the primary action people choose** — people press without looking, so the next press must flow logically from the first and fit the context; keep it simple, learnable. Consider carefully before offering more than one secondary function (raises cognitive load).
- **Prefer using subsequent button presses to support additional functionality rather than to stop or conclude a function** — put stopping the main task (vs. pausing) in the interface.
- **Pause the current function when people press the Action button and side button together** — exception: diving apps, where pausing may be dangerous (losing track of depth or time underwater). Unless pausing creates a negative experience, support it.

## APIs
App Shortcuts (App Intents), Live Activities (ActivityKit), snippets (App Intents).

## Related
`app-shortcuts, workouts, digital-crown, live-activities`
