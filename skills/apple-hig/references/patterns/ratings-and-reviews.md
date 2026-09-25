# Ratings and reviews

> Source: https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews · People often view an app's or game's ratings and reviews before downloading it.

## When to use / core idea
- A great overall experience is the best way to earn positive ratings; also choose the right moment to ask — e.g. based on launch count/frequency, features explored, or tasks completed.
- People can always rate your app within the App Store.

## Rules
### Best practices
- **Ask for a rating only after people have demonstrated engagement with your app or game** — e.g. after completing a level or significant task; avoid first launch or onboarding (no opinion yet; may prompt negative feedback).
- **Avoid interrupting people while they're performing a task or playing a game** — ask at natural breaks or stopping points.
- **Avoid pestering people** — repeated requests irritate and can hurt opinion; consider at least a week or two between requests, prompting again after additional engagement.
- **Prefer the system-provided prompt** — iOS, iPadOS, macOS offer a consistent, nonintrusive prompt; the system checks for previous feedback and, if none, asks for a rating and optional written review. People respond or dismiss with a single tap/click and can opt out for all apps. System limits the prompt to three occurrences per app within a 365-day period.
- **Weigh the benefits of resetting your summary rating against the potential disadvantage of showing fewer ratings** — on a new version you can reset the summary; ratings then reflect the current version but fewer overall ratings can discourage downloads.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## Specs
- System prompt cap: 3 times per app per 365 days.
- Suggested spacing between requests: at least a week or two.

## APIs
`RequestReviewAction` (StoreKit), Reset app summary rating (App Store Connect)

## Related
`onboarding`
