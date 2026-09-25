# Managing notifications

> Source: https://developer.apple.com/design/human-interface-guidelines/managing-notifications · Notifications give people timely, important information whether the device is locked or in use.

## When to use / core idea
- You must get permission before sending any notification; people can change it in Settings and silence all notifications (except government alerts in some locales).
- **Focus** filters notifications during reserved time (sleeping, working, reading, driving); **delivery scheduling** lets people receive alerts immediately or in a summary at chosen times. People pick contacts/apps that break through a Focus, and may allow all Time Sensitive alerts.
- Important: a Focus may delay the alert, but the notification itself is available as soon as it arrives.
- Notification types: *communication* (direct communications like calls, messages — adopt SiriKit intents; the system uses the sender to decide delivery) vs. *noncommunication* (everything else — you must specify a system-defined interruption level).
- For notification UI, see `notifications`.

## Rules
### Best practices
- **Build trust by accurately representing the urgency of each notification** — be realistic with interruption levels; don't use high urgency for low-priority info (people can turn off all notifications).
- **Use the Time Sensitive interruption level only for notifications that are relevant in the moment** — event happening now or within an hour. The system explains Time Sensitive on first arrival with a way to turn it off, and periodically lets people re-evaluate it.

### Sending marketing notifications
- Don't send marketing/promotional content via notifications unless people explicitly agree (e.g. subscription offer, live game event offer).
- **Never use the Time Sensitive interruption level to send a marketing notification** — marketing must never break through Focus or scheduled delivery.
- **Get people's permission if you want to send them promotional or marketing notifications** — explicit permission first, via an alert, modal view, or other interface describing the info types with a clear opt in/out.
- **Make sure people can manage their notification settings within your app** — provide an in-app settings screen to change informational/marketing choices (see `settings`).

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS.
### watchOS
- iPhone notification settings apply to the same apps on Apple Watch by default; managed in the Apple Watch app on iPhone, or per-notification (Mute 1 Hour, Turn off Time Sensitive) by swiping left on an arriving notification.

## Specs
Interruption levels (noncommunication notifications):
- *Passive* — viewable at leisure (e.g. restaurant recommendation).
- *Active* (default) — nice to know on arrival (e.g. favorite team's score update).
- *Time Sensitive* — directly impacts the person, needs immediate attention (e.g. account security issue, package delivery).
- *Critical* — urgent health/safety info demanding immediate attention; extremely rare, typically from governmental/public agencies or health/home management apps. Requires an entitlement.

| Interruption level | Overrides scheduled delivery | Breaks through Focus | Overrides Ring/Silent switch on iPhone and iPad |
| --- | --- | --- | --- |
| Passive | No | No | No |
| Active | No | No | No |
| Time Sensitive | Yes | Yes | No |
| Critical | Yes | Yes | Yes |

## APIs
`UNNotificationInterruptionLevel`, `UNNotificationContentProviding` (User Notifications), `INSendMessageIntent` (Intents/SiriKit), User Notifications framework

## Related
`privacy, settings, notifications`
