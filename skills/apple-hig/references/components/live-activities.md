# Live Activities

> Source: https://developer.apple.com/design/human-interface-guidelines/live-activities · Lets people track the progress of an activity, event, or task at a glance.

## When to use / core idea
- Glanceable tracking across devices; goes beyond push notifications with frequent content/status updates over a few hours plus interaction (e.g. delivery ETA, live soccer info, workout metrics with pause/cancel).
- For tasks/events with a defined beginning and end, not exceeding eight hours. For one-off info use `notifications`; for static results use `snippets`.
- Start on iPhone or iPad and appear automatically in system locations:

| Platform or system experience | Location |
| --- | --- |
| iPhone and iPad | Lock Screen, Home Screen, in the Dynamic Island and StandBy on iPhone |
| Mac | The menu bar |
| Apple Watch | Smart Stack |
| CarPlay | CarPlay Dashboard |

## Rules
### Anatomy
- Dynamic Island is a unified home for alerts and ongoing-activity indicators. The system picks a presentation (or combination) per device/location, so you **must support: Compact, Minimal, Expanded, Lock Screen**. These also generate defaults for other contexts (compact's two elements combine into one view on Apple Watch and CarPlay).
- **Compact** — used in the Dynamic Island when only one Live Activity is active; two elements, leading and trailing the TrueDepth camera; shows up-to-date info.
- **Minimal** — when multiple are active, two appear in the Dynamic Island: one attached, one detached (circular or oval depending on content size). Tap opens the app; touch and hold shows expanded.
- **Expanded** — shown when people touch and hold a compact or minimal presentation.
- **Lock Screen** — banner at the bottom of the Lock Screen; use a layout similar to expanded. On devices without Dynamic Island, alerts show it briefly as a banner over the Home Screen or other apps.
- **StandBy** (iPhone) — appears as minimal; tap transitions to the Lock Screen presentation scaled 2x to fill the screen; a custom Lock Screen background color is extended to the whole screen.

### Best practices
- **Offer Live Activities for tasks and events that have a defined beginning and end** — short to medium duration, not exceeding eight hours.
- **Focus on important information that people need to see at a glance** — prioritize concisely; tap opens the app for detail.
- **Don't use a Live Activity to display ads or promotions** — only info related to the event/task.
- **Avoid displaying sensitive information** — visible on Lock Screen/Always-On; show an innocuous summary and reveal in-app, or redact views and let people configure showing sensitive data.
- **Create a Live Activity that matches your app's visual aesthetic and personality in both dark and light appearances.**
- **If you include a logo mark, display it without a container** — don't use the entire app icon.
- **Don't add elements to your app that draw attention to the Dynamic Island** — your Live Activity shows there when the app isn't in use; other items can appear there when your app is open.
- **Ensure text is easy to read** — large, heavier-weight text (medium weight or higher); use small text sparingly; key info legible at a glance.

### Creating Live Activity layouts
- **Adapt to different screen sizes and presentations** — layouts and assets for various devices and scale factors; use Specs values.
- **Adjust element size and placement for efficient use of space** — use only the space needed; fit elements together.
- **Use familiar layouts for custom views and layouts** — Apple Design Resources templates with default system margins and recommended text sizes (fits e.g. Apple Watch Smart Stack).
- **Use consistent margins and concentric placement** — even margins between rounded shapes and the Live Activity edges/corners; don't poke into the rounded outline. For a rounded rectangle near a corner: inner radius = outer radius − margin; use a SwiftUI container (`ContainerRelativeShape`). Keep content compact and snug within a concentric margin.
- **When separating a block of content, place it in an inset container shape or use a thick line** — don't draw content all the way to the Dynamic Island edge.
- Tip: blur nonrounded content in your drawing tool to find alignment with the rounded perimeter.
- **Dynamically change the height of your Live Activity on the Lock Screen or in the expanded presentation** — shrink when less info, grow as more arrives (e.g. rideshare: compact while locating driver, taller with pickup time/driver details).

### Choosing colors
- **Carefully consider using a custom background color and opacity** — not customizable for compact, minimal, expanded; allowed for Lock Screen. With custom background color/image, ensure sufficient contrast, especially tint colors on Always-On displays with reduced luminance.
- **Use color to express the character and identity of your app** — Dynamic Island background is black opaque; consider bold colors for text/objects for recognition, distinction, and relating elements.
- **Tint your Live Activity's key line color so that it matches your content** — on dark backgrounds (e.g. Dark Mode) a key line surrounds the Dynamic Island; keep it consistent with other element colors.

### Adding transitions and animating content updates
- Besides extend/contract transitions, system and custom animations have a **maximum duration of two seconds**. No animations on Always-On displays with reduced luminance.
- **Use animations to reinforce the information you're communicating and to bring attention to updates** — move elements; default content-replace transition; custom transitions with scale, opacity, movement (e.g. numeric content transitions for scores; fade timer at zero).
- **Animate layout changes** — e.g. StandBy expansion or new info; preserve existing layout by animating elements to new positions rather than removing and re-adding them.
- **Try to avoid overlapping elements** — sometimes animate out and back in at a new position; in lists, animate only the moving element and fade the others.

### Offering interactivity
- **Make sure tapping the Live Activity opens your app at the right location** — directly to related details/actions.
- **Focus on simple, direct actions** — controls take space; include only essential, directly related functionality people activate once or pause/resume (music playback, workouts, live audio recording). Prefer limiting interactivity to a single element.
- **Consider letting people respond to event or progress updates** — e.g. rideshare button to contact the driver.

### Starting, updating, and ending a Live Activity
- **Start Live Activities at appropriate times, and make it easy for people to turn them off in your app** — expected after food order, rideshare request, favorite team's match start; unexpected ones may be unwanted. Offer off controls in the corresponding app view (e.g. unfollow a game/team); otherwise people may disable Live Activities in Settings entirely.
- **Offer an App Shortcut that starts your Live Activity** — e.g. via the Action button on iPhone (see `app-shortcuts`).
- **Update a Live Activity only when new content is available.**
- **Alert people only for essential updates that require their attention** — alerts light the screen, play the notification sound by default, show expanded (or a banner without Dynamic Island). Don't alert too often or for noncrucial updates; don't send push notifications alongside Live Activities for the same updates.
- **Let people track multiple events efficiently with a single Live Activity** — prefer one with a dynamic layout rotating through events (e.g. points, substitutions, fouls across matches).
- **Always end a Live Activity immediately when the task or event ends, and consider setting a custom dismissal time** — ended activities are removed immediately from the Dynamic Island and CarPlay; remain up to four hours on Lock Screen, Mac menu bar, watchOS Smart Stack. Use a dismissal time proportional to duration; in most cases 15 to 30 minutes (e.g. rideshare: 30 minutes for summary and tip).

### Presentation
- Support all locations, devices, and appearances with layouts suited to each.
- **Start with the iPhone design, then refine it for other contexts** — standard designs per presentation first, then custom layouts for StandBy, CarPlay, Apple Watch as appropriate.

#### Compact presentation
- **Focus on the most important information** — dynamic, essential, easy to understand (e.g. two team logos + score).
- **Ensure unified information and design of the compact presentations in the Dynamic Island** — leading and trailing read as one piece of info; consistent color and typography.
- **Keep content as narrow as possible and ensure it's snug against the TrueDepth camera** — don't obscure status bar info; no padding between content and camera; balance similar-size leading/trailing views (shortened units or less precise data).
- **Link to relevant app content** — both leading and trailing elements link to the same screen.

#### Minimal presentation
- **Ensure that your Live Activity is recognizable in the minimal presentation** — show updated info rather than just a logo if possible (e.g. Timer shows remaining time).

#### Expanded presentation
- **Maintain the relative placement of elements to create a coherent layout between presentations** — expanded is an enlarged compact/minimal; expand predictably.
- **Wrap content tightly around the TrueDepth camera** — avoid excess room around it.

#### Lock Screen presentation
- **Don't replicate notification layouts** — create a unique layout for the Live Activity's info.
- **Choose colors that work well on a personalized Lock Screen** — use custom background/tint colors and opacity sparingly.
- **Make sure your design, assets, and colors look great and offer enough contrast in Dark Mode and on an Always-On display** — default: light background in light appearance, dark in dark. Custom background: one color working in both or one per appearance; verify on an Always-On device with reduced luminance (system adapts colors).
- **Verify the generated color of the dismiss button** — auto-generated from background/foreground colors; adjust with `activitySystemActionForegroundColor(_:)`.
- **Use standard margins to align your design with notifications** — standard Lock Screen margin is **14 points**; tighter margins may suit graphics or buttons, but avoid crowding edges (`padding(_:_:)`).

#### StandBy presentation
- **Update your layout for StandBy** — assets look good at larger scale; consider a custom layout using the extra space.
- **Consider using the default background color in StandBy** — blends with the device bezel, softer look, lets the system scale slightly larger (no TrueDepth camera margins needed).
- **Use standard margins and avoid extending graphic elements to the edge of the screen** — otherwise content is cut off as it extends.
- **Verify your design in Night Mode** — system applies a red tint; ensure enough contrast.

### CarPlay
- System combines compact leading + trailing into one layout on CarPlay Dashboard. Design applies to both CarPlay and Apple Watch; Apple Watch can be interactive, but CarPlay deactivates interactive elements.
- **Consider creating a custom layout if your Live Activity would benefit from larger text or additional information** — declare support for the `ActivityFamily.small` supplemental activity family.
- **Carefully consider including buttons or toggles in your custom layout** — deactivated in CarPlay; if likely used while driving, prefer timely content over buttons/toggles.

## Platform considerations
No additional considerations: iOS, iPadOS. Not supported: tvOS, visionOS.
### macOS
- Active Live Activities appear in the menu bar of a paired Mac using compact, minimal, and expanded presentations; clicking launches iPhone Mirroring to show your app.
### watchOS
- Appears at the top of the Smart Stack on a paired Apple Watch when started on iPhone; default view combines compact leading and trailing elements.
- Tap opens your watchOS app if you have one; otherwise a full-screen view with a button to open the app on the paired iPhone.
- **Consider creating a custom watchOS layout** — can show more info and add a button or toggle.
- **Carefully consider including buttons or toggles in your custom layout** — the custom watchOS layout also applies in CarPlay (interactive elements deactivated); if likely used while driving, don't include buttons or toggles.
- **Focus on essential information and significant updates** — progress (delivery ETA), interactive elements (stopwatch/timer controls), significant updates (score changes).

## Specs
- Max animation duration: 2 s. Max recommended activity length: 8 hours. Post-end persistence: up to 4 hours (Lock Screen, Mac menu bar, Smart Stack); suggested custom dismissal 15–30 minutes. Lock Screen standard margin: 14 pt. StandBy scale: 2x. Dynamic Island corner radius: 44 pt (matches TrueDepth camera shape).

### CarPlay
System may scale to fit the vehicle screen.

| Live Activity size (pt) |
| --- |
| 240x78 |
| 240x100 |
| 170x78 |

Test in the CarPlay simulator with Smart Display Zoom configurations (Settings > Display in CarPlay):

| Configuration | Resolution (pt) |
| --- | --- |
| Widescreen | 1920x720 |
| Portrait | 900x1200 |
| Standard | 800x480 |

### iOS (pt)
| Screen dimensions (portrait) | Compact leading | Compact trailing | Minimal (width given as a range) | Expanded (height given as a range) | Lock Screen (height given as a range) |
| --- | --- | --- | --- | --- | --- |
| 430x932 | 62.33x36.67 | 62.33x36.67 | 36.67–45x36.67 | 408x84–160 | 408x84–160 |
| 393x852 | 52.33x36.67 | 52.33x36.67 | 36.67–45x36.67 | 371x84–160 | 371x84–160 |

Dynamic Island width (pt):

| Device | Compact or minimal | Expanded |
| --- | --- | --- |
| iPhone 17 Pro Max | 250 | 408 |
| iPhone 17 Pro | 230 | 371 |
| iPhone Air | 250 | 408 |
| iPhone 17 | 230 | 371 |
| iPhone 16 Pro Max | 250 | 408 |
| iPhone 16 Pro | 230 | 371 |
| iPhone 16 Plus | 250 | 408 |
| iPhone 16 | 230 | 371 |
| iPhone 15 Pro Max | 250 | 408 |
| iPhone 15 Pro | 230 | 371 |
| iPhone 15 Plus | 250 | 408 |
| iPhone 15 | 230 | 371 |
| iPhone 14 Pro Max | 250 | 408 |
| iPhone 14 Pro | 230 | 371 |

### iPadOS (pt)
| Screen dimensions (portrait) | Lock Screen (height given as a range) |
| --- | --- |
| 1366x1024 | 500x84–160 |
| 1194x834 | 425x84–160 |
| 1012x834 | 425x84–160 |
| 1080x810 | 425x84–160 |
| 1024x768 | 425x84–160 |

### macOS
Use the iOS dimensions.

### watchOS
Same dimensions as watchOS widgets.

| Apple Watch size | Size of a Live Activity in the Smart Stack (pt) |
| --- | --- |
| 40mm | 152x69.5 |
| 41mm | 165x72.5 |
| 44mm | 173x76.5 |
| 45mm | 184x80.5 |
| 49mm | 191x81.5 |

## APIs
ActivityKit, WidgetKit, SwiftUI, `ContainerRelativeShape` (SwiftUI), `activitySystemActionForegroundColor(_:)` (SwiftUI), `padding(_:_:)` (SwiftUI), `ActivityFamily.small` (WidgetKit)

## Related
`app-shortcuts, dark-mode, always-on, notifications`
