# Progress indicators

> Source: https://developer.apple.com/design/human-interface-guidelines/progress-indicators · Progress indicators let people know that your app isn't stalled while it loads content or performs lengthy operations.

## When to use / core idea
- Transient: appear only while an operation runs, disappear on completion. Some help estimate wait time.
- **Determinate** — well-defined duration (e.g., file conversion). Fills a linear or circular track: *progress bars* fill leading → trailing; *circular progress indicators* fill clockwise.
- **Indeterminate** (*activity indicator*, *spinner*) — unquantifiable tasks (loading, syncing complex data); animated image. All platforms support a spinning circular image; macOS also has an indeterminate bar.
- For a static value within a range use a gauge instead.

## Rules
### Best practices
- **When possible, use a determinate progress indicator** — helps people decide to do something else, restart later, or abandon.
- **Be as accurate as possible when reporting advancement in a determinate progress indicator** — consider evening out pace; e.g., 90% in 5 seconds then last 10% in 5 minutes makes people wonder if the app is working and can feel deceptive.
- **Keep progress indicators moving so people know something is continuing to happen** — stationary suggests stall/freeze. If a process stalls, give feedback explaining the problem and what people can do.
- **When possible, switch a progress bar from indeterminate to determinate** — once duration becomes known.
- **Don't switch from the circular style to the bar style** — different shapes/sizes; transitioning disrupts the interface and confuses.
- **If it's helpful, display a description that provides additional context for the task** — accurate and succinct; avoid vague terms like *loading* or *authenticating*.
- **Display a progress indicator in a consistent location** — across platforms and within/between apps.
- **When it's feasible, let people halt processing** — include Cancel if interruption has no negative side effects; if it might (e.g., losing downloaded portion), also provide Pause.
- **Let people know when halting a process has a negative consequence** — if canceling loses progress, show an alert offering to confirm cancellation or resume.

## Platform considerations
No additional considerations: tvOS, visionOS.

### iOS, iPadOS
#### Refresh content controls
- Specialized activity indicator, hidden by default, revealed by dragging down a view (typically a table view) to reload immediately (e.g., Mail Inbox).
- **Perform automatic content updates** — don't make people responsible for every update; refresh regularly.
- **Supply a short title only if it adds value** — usually unnecessary (animation indicates loading). Don't use it to explain how to refresh; give useful info about the content (e.g., Podcasts shows when last updated).

### macOS
- Indeterminate indicators can be bar or circular; both animated.
- **Prefer an activity indicator (spinner) to communicate the status of a background operation or when space is constrained** — small, unobtrusive; good for async background tasks (retrieving messages) and small areas (inside a text field, next to a button).
- **Avoid labeling a spinning progress indicator** — people usually initiated the process, so a label is unnecessary.

### watchOS
- Default: white over the scene's background color; change via tint color. Supports progress bar (left→right), circular (clockwise), and spinner.

## APIs
`ProgressView` (SwiftUI), `UIProgressView` (UIKit), `UIActivityIndicatorView` (UIKit), `UIRefreshControl` (UIKit), `NSProgressIndicator` (AppKit).

## Related
`alerts, gauges, loading, feedback`
