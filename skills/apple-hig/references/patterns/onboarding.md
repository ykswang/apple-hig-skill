# Onboarding

> Source: https://developer.apple.com/design/human-interface-guidelines/onboarding · Onboarding can help people get a quick start using your app or game.

## When to use / core idea
- Ideally people understand the app just by using it; if onboarding is needed, make it fast, fun, and optional.
- Onboarding happens after `launching` completes — it isn't part of the launch experience.
- Alternatives: context-specific tips (TipKit, see `offering-help`) instead of a single flow; an optional separate tutorial.

## Rules
### Best practices
- **Teach through interactivity** — let people safely test an action, discover a feature, or try a game mechanic rather than view instructions.
- **Consider providing a collection of context-specific tips instead of a single onboarding flow** — people learn during their current task, focusing on one action at a time; place instructions near the interface area they refer to.
- **If you need to present a prerequisite onboarding flow, design a brief, enjoyable experience that doesn't require people to memorize a lot of information** — teaching too much overwhelms and reduces retention.
- **If it makes sense to offer a separate tutorial, consider making it optional** — if skipped at first launch, don't present it again on later launches, but keep it easy to find (help, account, or settings area).
- **Keep onboarding content focused on the experience you provide** — don't teach the system or device.

### Additional content
- **Briefly display a splash screen if necessary** — a beautiful, succinct graphic shown just long enough to absorb at a glance without feeling like a delay.
- **Don't let large downloads hinder onboarding** — include enough media/content in the package so people needn't wait for downloads to start interacting (see `launching`).
- **Avoid displaying licensing details within your onboarding flow** — let the App Store show agreements/disclaimers; if you must include them, integrate them in a balanced, nondisruptive way.

### Additional requests
- **Postpone nonessential setup flows or customization steps** — provide reasonable defaults so most people can start immediately.
- **If your app or game needs access to private data or resources before it can function, consider integrating the permission request into your onboarding flow** — explain why and the benefits; otherwise request permission when people first access the dependent function (see `privacy`).
- **Prefer letting people experience your app or game before prompting them for ratings or purchases** — engaged people respond more positively.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## APIs
`TipKit`

## Related
`launching, feedback, offering-help, privacy, ratings-and-reviews`
