# Notifications

> Source: https://developer.apple.com/design/human-interface-guidelines/notifications · Gives people timely, high-value information they can understand at a glance.

## When to use / core idea
- Requires people's consent first; people then use settings to choose styles and delivery times per urgency (see `managing-notifications`).
- For error messages use `alerts`, not notifications.

## Rules
### Anatomy
- Styles (platform-dependent): banner/view on Lock Screen, Home Screen, Home View, or desktop; badge on an app icon; item in Notification Center.
- Communication notifications (calls, messages) can use a distinct interface with prominent contact images (*avatars*) and group names instead of the app icon.

### Best practices
- **Provide concise, informative notifications.**
- **Avoid sending multiple notifications for the same thing, even if someone hasn't responded** — fills Notification Center; people may turn off all your notifications.
- **Avoid sending a notification that tells people to perform specific tasks within your app** — offer notification actions for simple tasks instead; instructions are hard to remember after dismissal.
- **Use an alert — not a notification — to display an error message.**
- **Handle notifications gracefully when your app is in the foreground** — notifications don't appear, but your app gets the info; present it discoverably but not distractingly (increment a badge, subtly insert data; e.g. Mail just adds the message to the unread list).
- **Avoid including sensitive, personal, or confidential information in a notification** — may be visible to others.

### Content
- Title shows at the top. Communication notifications: system shows sender's name in the title area. Noncommunication: system shows your app name if you provide no title.
- **Create a short title if it provides context for the notification content** — brief, glanceable (especially Apple Watch); use for headline, event name, email subject. If only a generic title is possible (e.g. "New Document"), let the system show the app name. Title-style capitalization, no ending punctuation.
- **Write succinct, easy-to-read notification content** — complete sentences, sentence case, proper punctuation; don't truncate (system does it).
- **Provide generically descriptive text to display when notification previews aren't available** — when previews are hidden, system shows only app icon + default title *Notification*; body like "Friend request", "New comment", "Reminder", "Shipment"; sentence-style capitalization (`hiddenPreviewsBodyPlaceholder`).
- **Avoid including your app name or icon** — system shows a large app icon at the leading edge; communication notifications show the sender's contact image badged with a small app icon.
- **Consider providing a sound to supplement your notifications** — custom (short, distinctive, professionally produced) or system alert sound. Don't rely on sound for important info. You can't provide vibration programmatically (`UNNotificationSound`).

### Notification actions
- Customizable detail view with **up to four buttons** to act without opening the app (e.g. Calendar Snooze).
- **Provide beneficial actions that make sense in the context of your notification** — common, time-saving tasks; short, title-case label describing the result; no app name or extraneous info; brief to avoid truncation; consider localization.
- **Avoid providing an action that merely opens your app** — tapping the notification already does that.
- **Prefer nondestructive actions** — if destructive, give enough context; system gives destructive actions a distinct appearance.
- **Provide a simple, recognizable interface icon for each notification action** — shown on the trailing side of the action title; use or edit an SF Symbol.

### Badging
- Badge: small filled oval with a number on the app icon = unread notification count; disappears when addressed, reappears on new ones. People can disable badges.
- **Use a badge only to show people how many unread notifications they have** — not for weather, dates/times, stock prices, game scores, etc.
- **Make sure badging isn't the only method you use to communicate essential information** — badging can be turned off; always make important info easy to find on app open.
- **Keep badges up to date** — update as soon as people open the corresponding notifications. Reducing the count to zero removes all related notifications from Notification Center.
- **Avoid creating a custom image or component that mimics the appearance or behavior of a badge.**

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS.
### watchOS
- Two stages: *short look* and *long look*; also Notification Center; double tap to respond on supported devices.
- Design Watch-relevant assets/actions. If an iPhone companion supports notifications, watchOS can provide default short/long look interfaces.

#### Short looks
- Appear when the wrist is raised, disappear when lowered.
- **Avoid using a short look as the only way to communicate important information** — shown only briefly; deliver critical info other ways too.
- **Keep privacy in mind** — discreet, basic info only; avoid potentially sensitive info in the title.

#### Long looks
- More detail; scroll by vertical swipe or Digital Crown; dismiss by tapping or lowering the wrist.
- Custom long look: *static* (message + static text/images) or *dynamic* (full notification content, more appearance options). You can customize the content area but not the overall structure: system *sash* at top, Dismiss button at bottom below all custom buttons.
- **Consider using a rich, custom long-look notification to let people get the information they need without launching your app** — SwiftUI Animations (engaging, interruptible), or SpriteKit / SceneKit.
- **At the minimum, provide a static interface; prefer providing a dynamic interface too** — static is the fallback when dynamic is unavailable (no network, iPhone companion unreachable); create and package static resources in advance.
- **Choose a background appearance for the sash** — sash shows app icon and name; customize color or use blurred (light, translucent; good with a photo at the top of the content area).
- **Choose a background color for the content area** — default transparent; to match system notifications use white with 18% opacity; or a custom (brand) color.
- **Provide up to four custom actions below the content area** — system picks which to show by notification type; Dismiss always at bottom. With an iPhone companion, the system shares its registered actionable notification types to configure your buttons.

#### Double tap
- Double tap selects the first nondestructive action.
- **Keep double tap in mind when choosing the order of custom actions you present as responses to a notification** — put the most frequently used first (e.g. parking extension: 5 minutes, 15 minutes, an hour — most common first).

## Specs
- Notification actions: up to 4 buttons (all platforms); watchOS long look: up to 4 custom actions + system Dismiss.
- watchOS long-look content background to match system: white at 18% opacity.

## APIs
`Asking permission to use notifications` (UserNotifications), `hiddenPreviewsBodyPlaceholder` (UserNotifications), `UNNotificationSound` (UserNotifications), `Handling notifications and notification-related actions` (UserNotifications), `Animations` (SwiftUI), `SpriteKit` (spritekit), `SceneKit` (scenekit), `User Notifications UI` (usernotificationsui), `User Notifications` (UserNotifications)

## Related
`managing-notifications, alerts, sf-symbols`
