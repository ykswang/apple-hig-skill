# Collaboration and sharing

> Source: https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing · Great collaboration and sharing experiences are simple and responsive, letting people engage with content while communicating effectively with others.

## When to use / core idea
- Use system interfaces (share sheet / sharing popover) and Messages integration: people start sharing/collaborating by dropping a document into a Messages conversation or picking a destination in the share sheet.
- After collaboration begins, the Collaboration button lets people communicate, perform custom actions, and manage details; Messages notifies people of mentions, changes, joins, leaves.
- Works with CloudKit, iCloud Drive, or a custom solution; custom collaboration infrastructure must also support universal links.
- For real-time shared activities across devices, use `shareplay`.

## Rules
### Best practices
- **Place the Share button in a convenient location, like a toolbar, to make it easy for people to start sharing or collaborating** — iOS 16 share sheet (and iPadOS 16 / macOS 13 sharing popover) includes file-sharing method and permission choices for new collaborations. In SwiftUI, a `ShareLink` opens the system share sheet.
- **If necessary, customize the share sheet or sharing popover to offer the types of file sharing your app supports** — CloudKit: pass both the file and the collaboration object so "send copy" is auto-detected; iCloud Drive: collaboration object supports "send copy" by default; custom: include a file (or plain-text representation) in the collaboration object.
- **Write succinct phrases that summarize the sharing permissions you support** — e.g. "Only invited people can edit", "Everyone can make changes"; the system uses the summary in a button revealing sharing options.
- **Provide a set of simple sharing options that streamline collaboration setup** — customize the view behind the permission-summary button (who can access, edit vs. read-only, whether collaborators can add participants); keep custom choices to a minimum and group them for at-a-glance understanding.
- **Prominently display the Collaboration button as soon as collaboration starts** — it reminds people content is shared and shows who's sharing; place it next to the Share button.
- **Provide custom actions in the collaboration popover only if needed** — popover has 3 sections: top = collaborators + Messages/FaceTime communication buttons; middle = your custom items; bottom = button to manage the shared file. Offer only the most essential items (e.g. Notes: recent-update summary + buttons for more info/activities).
- **If it makes sense in your app, customize the title of the modal view's collaboration-management button** — default title "Manage Shared File"; opens the management view (change settings, add/remove collaborators). CloudKit sharing provides this view; otherwise you create your own.
- **Consider posting collaboration event notifications in Messages** — choose the event type (content change, membership change, participant mention) and include a universal link to the relevant view in your app.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS. Not available in tvOS.
### visionOS
- By default the system supports screen sharing for an app in the Shared Space by streaming the current window to collaborators; if someone moves the app to a Full Space during sharing, the stream pauses for others until the app returns to the Shared Space (see `immersive-experiences`).
### watchOS
- In SwiftUI, use `ShareLink` to present the system share sheet.

## APIs
`ShareLink` (SwiftUI), `SWHighlightEvent` (Shared with You), Shared with You framework, CloudKit sharing

## Related
`activity-views, shareplay, immersive-experiences`
