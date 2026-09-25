# Drag and drop

> Source: https://developer.apple.com/design/human-interface-guidelines/drag-and-drop · Lets people move or duplicate selected photos, text, and other content by dragging the selection from one location to another.

## When to use / core idea
- People select content at a *source* and drop it at a *destination* — same container (e.g. a text view), different containers (e.g. two sides of a split view), or different apps.
- *Move*: content ends up only in destination; *copy*: exists in both. General rule: same container = move; different container = copy; between apps = always copy.
- Interactions by platform: visionOS — pinch and hold a virtual object while dragging in any direction including the z-axis; iOS/iPadOS — touch gestures, pointing device, full keyboard access; Universal Control — drag between Mac and iPad; Mac — pointing device, full keyboard access, VoiceOver.

## Rules
### Best practices
- **As much as possible, support drag and drop throughout your app** — people try it everywhere; system components (text fields, text views) have built-in support.
- **Offer alternative ways to accomplish drag-and-drop actions** — e.g. menu commands to copy and move items; in iOS/iPadOS use accessibility APIs to identify sources/destinations for assistive technologies.
- **Determine when dragging and dropping content within your app results in a move or a copy** — move when source and destination containers are the same, copy when different; before changing defaults, prefer the behavior least likely to cause frustration or data loss.
- **Support multi-item drag and drop when it makes sense** — iOS, iPadOS, macOS, visionOS: select multiple items and drag as a group; macOS: select items from several apps and drag together; iPadOS: add items to the group mid-drag.
- **Prefer letting people undo a drag-and-drop operation** — consider asking for confirmation before a drop that can't be undone (e.g. Finder when dropping into a write-only folder); where undo isn't possible, consider a way to reverse results (e.g. Photos lets people cancel sharing after dropping into a shared photo stream).
- **Consider offering multiple versions of dragged content, ordered from highest to lowest fidelity** — destination picks the best it accepts; e.g. line drawing: PDF vector → lossless PNG with transparency → lossy JPEG without transparency; or native chart object → image of chart.
- **Consider supporting spring loading** — activating controls (buttons, segmented controls) by dragging content over them (e.g. Calendar event over day/week/month/year segments). Mac with Magic Trackpad: activates on force-click while holding content; iPad: activates on hover while holding content.

### Providing feedback
- Provide clear, continuous feedback throughout the drag.
- **Display a drag image as soon as people drag a selection about three points** — a translucent representation works well (distinguishes from original, shows destinations beneath); display it until drop.
- **If it adds clarity, modify the drag image to help people predict the result of a drag-and-drop operation** — e.g. expand a photo to its default size in the document; use drag *flocking* to visually group multiple items, ungroup on drop. Avoid a drag image that constantly and radically changes.
- **Show people whether a destination can accept dragged content** — show insertion point/highlight only when accepted; otherwise no feedback or an explicit "not allowed" image (e.g. SF Symbol `circle.slash`). Show cues only while content is over the destination and remove when dragged away; with multiple possible destinations, cue one at a time.
- **When people drop an item on an invalid destination, or when dropping fails, provide visual feedback** — e.g. item moves back to its source (if visible) or scales up and fades out ("evaporates").

### Accepting drops
- **Scroll the contents of a destination when necessary** — auto-scroll a large scrolling container as the item moves over it; stop when the drag leaves the container. System text views/fields do this by default.
- **When there's a choice, pick the richest version of dropped content your app can accept** — e.g. use the native chart object if supported, otherwise the image.
- **Extract only the relevant portion of dropped content if necessary** — e.g. contact dropped on Mail recipient field shows only name and email, not address.
- **When a physical keyboard is attached, check for the Option key at drop time** — holding Option forces a same-container drag to copy; releasing Option before the drop results in a move.
- **Provide feedback when dropped content needs time to transfer** — e.g. progress indicator; in collections/lists/tables, a placeholder at the drop location. The system can show an alert for time-consuming inter-app transfers.
- **Provide feedback when dropped content initiates a task or action** — e.g. dropping on a print control: show the task began and keep people informed of progress.
- **Apply appropriate styling to dropped text** — if source and destination support the same styles, keep original font, typeface, size, other attributes; otherwise apply the destination's style.
- **After a drop, maintain the content's selection state in the destination, updating it in the source as needed** — dropped content stays selected; same-container move removes it from the original location; same-container copy: deselect the content remaining at the original location; drag to a different container: deselect in the source.

## Platform considerations
Not supported: tvOS, watchOS.
### iOS, iPadOS
- **Let people perform multiple simultaneous drag activities** — in iPadOS people add items sequentially to an in-progress drag (e.g. gathering Home Screen app icons); let people add items mid-drag with flocking feedback and accept multiple simultaneous drops.
### macOS
- **Consider letting people drag content from your app into the Finder** — present it in a format your app can open later (e.g. Calendar event → `.ics` file). When necessary, output a *clipping* (temporary container for dragged content, e.g. text dragged to Finder, later draggable into text fields); clippings are unrelated to the Clipboard.
- **Let people drag selected content from an inactive window without first making the window active** — a *background selection* (appears differently from active-window selection) can be dragged to the active window without bringing the inactive window forward.
- **When possible, let people drag individual items from an inactive window without affecting an existing background selection** — e.g. drag an unselected file from an inactive Finder window without deselecting others.
- **Consider displaying a badge during multi-item drag operations** — small filled oval with the item count; update it if the destination accepts only a subset.
- **Consider changing the pointer appearance to indicate what will happen when people drop content** — besides *copy*, use *drag link*, *disappearing item*, *operation not allowed* as appropriate (see `pointing-devices`).
- **As much as possible, let people select and drag content with a single motion** — unless selecting multiple items, don't require a pause between selecting and dragging.
### visionOS
- **When possible, launch your app to handle content that people drop into empty space** — associate a user activity with draggable content so your app opens a window/scene to handle it (e.g. URL → Safari; Quick Look–supported content → Quick Look).

## APIs
`accessibilityDragSourceDescriptors`, `accessibilityDropPointDescriptors` (NSObject accessibility), Drag and drop (UIKit), Drag and Drop (AppKit), File Provider, `NSUserActivity` (Foundation)

## Related
`pointing-devices, undo-and-redo, keyboards, sf-symbols`
