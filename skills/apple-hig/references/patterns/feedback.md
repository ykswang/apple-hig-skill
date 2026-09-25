# Feedback

> Source: https://developer.apple.com/design/human-interface-guidelines/feedback · Feedback helps people know what's happening, discover what they can do next, understand results of actions, and avoid mistakes.

## When to use / core idea
- Feedback communicates: current status, success/failure of an important task, warnings about actions with negative consequences, opportunities to correct mistakes.
- Match the delivery to the significance: passive status info people check when needed vs. interrupting warnings (e.g. possible data loss). Interruptive channel = `alerts`; tactile = `playing-haptics`; sound = `playing-audio`.

## Rules
### Best practices
- **Make sure all feedback is accessible** — use multiple channels (color, text, sound, haptics) so people get it with the device silenced, looking away, or using VoiceOver.
- **Consider integrating status feedback into your interface** — place it near the items it describes so no action or context change is needed (e.g. Mail toolbar shows latest update and unread count).
- **Use alerts to deliver critical — and ideally actionable — information** — alerts disrupt context; match importance to interruption level; overuse or unimportant alerts lose impact.
- **Warn people when they initiate a task that can cause data loss that's unexpected and irreversible** — don't warn when data loss is the expected result (e.g. Finder doesn't warn on every move to Trash).
- **When it makes sense, confirm that a significant action or task has completed** — e.g. successful Apple Pay transaction; reserve for sufficiently important activities, since people expect success and mainly need to know about failure.
- **Show people when a command can't be carried out and help them understand why** — e.g. Maps explains it can't give directions to and from the same location.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS.
### watchOS
- **Avoid displaying an indeterminate progress indicator — such as a loading indicator — in a watchOS app** — animation makes people think they must keep watching; instead reassure them they'll get a notification when the process completes.

## APIs
Animation and haptics (UIKit)

## Related
`playing-audio, playing-haptics, motion, alerts, progress-indicators`
