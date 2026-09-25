# Apple Pencil and Scribble

> Source: https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble · Apple Pencil makes drawing, handwriting, and marking effortless and natural, and also works well as a pointer and UI interaction tool.

## When to use / core idea
- iPad-only tool with pixel-level precision for notes, sketching, painting, document markup.
- Scribble: write with Apple Pencil in any text field via fast, private, on-device handwriting recognition; integrated into iPadOS and available to all apps by default; no tapping or mode switch first.
- Apple Pencil Pro adds squeeze and barrel roll. Hover, double tap depend on model.
- Use PencilKit for low-latency drawing canvases, tool picker, and ink palette.

## Rules
### Best practices
- **Support behaviors people intuitively expect when using a marking instrument** — anticipate real-world actions, e.g., writing in document/book margins.
- **Let people choose when to switch between Apple Pencil and finger input** — make controls respond to Apple Pencil too; otherwise controls seem unresponsive (malfunction/low battery impression). Scribble only supports Apple Pencil input.
- **Let people make a mark the moment Apple Pencil touches the screen** — never require tapping a button or entering a special mode first.
- **Help people express themselves by responding to the way they use Apple Pencil** — may sense tilt (altitude), force (pressure), orientation (azimuth), and barrel roll; vary stroke thickness/intensity. Keep pressure response simple — map to continuous properties like ink opacity or brush size.
- **Provide visual feedback to indicate a direct connection with content** — manipulate touched content directly and immediately; avoid seemingly disconnected actions or affecting content elsewhere on screen.
- **Design a great left- and right-handed experience** — avoid control placement either hand may obscure; if possible obscuring, consider letting people reposition controls.

### Hover
- **Use hover to help people predict what will happen when Apple Pencil touches the screen** — e.g., preview mark dimensions and color. Avoid continuously modifying the preview with height; it doesn't clarify and is distracting.
- **Avoid using hover to initiate an action** — hover is imprecise; never trigger actions (especially destructive ones) just because the pencil is near the screen.
- **Prefer showing a preview value that's near the middle in a range of dynamic values** — max-pressure preview can occlude the marking area; min-pressure can be invisible/inaccurate.
- **Consider using hover to support relevant interactions close to where people are marking** — e.g., show a contextual menu of tool sizes on squeeze or modifier-key press, near the marking point.
- **Prefer showing hover previews for Apple Pencil, not for a pointing device** — same feedback for both can confuse; restrict to Apple Pencil if sensible.

### Double tap
- **Respect people's settings for the double-tap gesture when they make sense in your app** — default: toggle current tool ↔ eraser; options: toggle current ↔ previous tool, show/hide color picker, or nothing. If system settings don't fit, you may still use it to change interaction mode (e.g., mesh tool raise/lower toggle in a 3D app).
- **Give people a way to specify custom double-tap behavior if necessary** — provide a control to choose the custom mode; make the current mode clear; make it discoverable but don't turn it on by default.
- **Avoid using the double-tap gesture to perform an action that modifies content** — accidental double taps happen; prefer easily undone actions; especially avoid potentially destructive actions causing data loss.

### Squeeze (Apple Pencil Pro)
- People may configure squeeze to run an App Shortcut instead of app-specific actions.
- Available only while the paired iPad screen is on and the pencil isn't touching it; people may not be visually aware of the onscreen result.
- **Treat squeeze as a single, quick gesture that performs a discrete — not continuous — action** — holding or rapid repeated squeezes are tiring; respond to one squeeze and show the result promptly.
- **If you use squeeze to reveal app UI, like a contextual menu, display it close to Apple Pencil Pro** — near the tip.
- **Define squeeze actions that are nondestructive and easy to undo** — accidental squeezes happen; avoid data-loss actions.

### Barrel roll (Apple Pencil Pro)
- Rolling while marking changes the mark type (e.g., rotating highlighter angle in Notes).
- **Use barrel roll only to modify marking behavior, not to enable navigation or display other controls.**

### Scribble
- **Make text entry feel fluid and effortless** — Scribble works by default in standard text components (text fields, text views, search fields, editable web fields) except password fields. For custom text fields, don't require tapping/selecting before writing.
- **Make Scribble available everywhere people might want to enter text** — e.g., Reminders lets people write a new reminder in blank space below the last item (`UIIndirectScribbleInteraction`).
- **Avoid distracting people while they write** — avoid showing autocompletion while writing; hide placeholder text the moment writing begins.
- **While people are writing in a text field, make sure it remains stationary** — if a field must move/resize on focus (e.g., search field), consider delaying until writing pauses.
- **Prevent autoscrolling text while people are writing and editing in a text field** — people avoid writing over it or select the wrong range.
- **Give people enough space to write** — when pencil input is likely, enlarge the field before writing begins or when writing pauses; avoid resizing during writing (`UIScribbleInteraction`).

### Custom drawing
- **Help people draw on top of existing content** — PencilKit canvas colors adapt to Dark Mode by default; when drawing over a PDF or photo, prevent dynamic color adjustment so markup stays sharp and visible.
- **Consider displaying custom undo and redo buttons when your app runs in a compact environment** — tool picker includes undo/redo only in regular environments; in compact, put them in a toolbar. Consider also supporting the standard 3-finger undo/redo gesture. See `undo-and-redo`.

## Platform considerations
Not supported: iOS, macOS, tvOS, visionOS, watchOS (iPadOS only).

## APIs
`Adopting hover support for Apple Pencil` (UIKit), `UIIndirectScribbleInteraction` (UIKit), `UIScribbleInteraction` (UIKit), `PencilKit` (PencilKit), `PaperKit` (paperkit)

## Related
`entering-data, undo-and-redo, app-shortcuts, pointing-devices, text-fields`
