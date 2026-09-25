# App Shortcuts

> Source: https://developer.apple.com/design/human-interface-guidelines/app-shortcuts · Gives people access to your app's key functions or content throughout the system.

## When to use / core idea
- Initiated via Siri, Spotlight, the Shortcuts app, the Action button (iPhone/Apple Watch), or squeezing Apple Pencil.
- Part of your app → available immediately after install (before first launch); can later reflect people's choices (e.g. FaceTime recent contacts).
- Built on App Intents; each App Shortcut includes one or more actions (e.g. lights off + lock doors at bedtime). **Up to 10 App Shortcuts per app.**
- Via App Intents, people can also build their own custom shortcuts in the Shortcuts app, combining actions across apps.
- For common domain functionality, prefer app schemas (Apple Intelligence); App Shortcuts suit unique features/custom content not covered by app schemas.

## Rules
### Best practices
- **To surface common types of app functionality throughout the system, consider adopting app schemas instead** — apps in common domains make actions/content available to Apple Intelligence so Siri and system experiences surface them contextually without individual App Shortcuts (see `siri`).
- **Offer App Shortcuts for your app's most common and important tasks** — straightforward tasks completable without leaving context work best; opening your app is OK if it eases multistep tasks.
- **Add flexibility by letting people choose from a set of options** — a single optional value (parameter) when it makes sense, e.g. "Start [morning, daily, sleep] meditation." Use predictable, familiar values — people don't see the list.
- **Ask for clarification in response to a request that's missing optional information** — e.g. suggest most recent or time-of-day-based option; if one is most likely, present it as default with a short list of alternatives.
- **Keep voice interactions simple** — if the phrase feels complicated aloud, it's too hard to remember/say (e.g. "Start [sleep] meditation with nature sounds" implies two parameters). Ask for absolutely required extra info in a subsequent step.
- **Make App Shortcuts discoverable in your app** — consider occasional tips when people perform common actions (`SiriTipUIView`).

### Responding to App Shortcuts
- Responses: Siri-spoken dialogue plus custom visuals:
  - `snippets` — custom views for static info or dialog options (weather, order confirmation).
  - `live-activities` — continuous access to info that changes over time (timers, countdowns until an event completes) (`LiveActivityIntent`).
- **Provide enough detail for interaction on audio-only devices** — AirPods, HomePod; include all critical info in the full dialogue text (`init(full:supporting:systemImageName:)`).

### Editorial guidelines
- **Provide brief, memorable activation phrases and natural variants** — must include your app name, but can be creative (Keynote: "Create a Keynote", "Add a new presentation in Keynote") (`AppShortcutPhrase`).
- **When referring to App Shortcuts or the Shortcuts app, always use title case and make sure that *Shortcuts* is plural.**
- **When referring to individual shortcuts (not App Shortcuts or the Shortcuts app), use lowercase** — e.g. "Run a shortcut by asking Siri…".

## Platform considerations
No additional considerations: visionOS, watchOS. Not supported: tvOS.
### iOS, iPadOS
- Appear in Spotlight's Top Hit area when people search for your app, or in the Shortcuts area below. Each has an SF Symbol you choose, or a preview image of the linked item.
- **Order shortcuts based on importance** — your order sets initial appearance in Spotlight and the Shortcuts app; put most generally useful first. System later prioritizes most frequently used.
### macOS
- App Shortcuts not supported; App Intents actions are, and people can build custom shortcuts with them in Shortcuts on Mac.

## APIs
App Intents, SiriKit, `AppShortcutPhrase` (App Intents), `SiriTipUIView` (App Intents), `LiveActivityIntent` (App Intents), `IntentDialog.init(full:supporting:systemImageName:)` (App Intents), app schema domains (App Intents)

## Related
`siri, snippets, live-activities, action-button, apple-pencil-and-scribble, sf-symbols`
