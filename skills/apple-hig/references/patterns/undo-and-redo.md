# Undo and redo

> Source: https://developer.apple.com/design/human-interface-guidelines/undo-and-redo · Easy ways to reverse many types of actions, helping people explore and experiment safely as they learn a new interface or task.

## When to use / core idea
- People expect undo/redo to reverse recent actions and often undo repeatedly until something changes, possibly forgetting which action is targeted → unintended changes. Help people predict outcomes and highlight results.
- Standard invocation: macOS Edit menu; keyboard shortcuts on Mac or iPad; shake iPhone; three-finger swipe (iOS, iPadOS).

## Rules
### Best practices
- **Help people predict the results of undo and redo as much as possible** — e.g. describe the result in the iPhone shake-to-undo alert (with option to undo or cancel); label menu items with the result, e.g. "Undo Typing", "Redo Bold".
- **Show the results of an undo or redo** — if the affected content is offscreen, highlight/reveal it (e.g. scroll to a restored paragraph) so people don't think it had no effect and repeat it.
- **Let people undo multiple times** — avoid unnecessary limits; people expect to undo every action since a logical step like opening or saving a document.
- **Consider giving people the option to revert multiple changes at once** — e.g. batch incremental adjustments to a single property; or undo all changes since opening/saving.
- **Provide undo and redo buttons only when necessary** — people expect system-supported methods; if dedicated buttons are important, use the standard system-provided symbols and put them in a toolbar.

## Platform considerations
No additional considerations: visionOS. Not supported: tvOS, watchOS.
### iOS, iPadOS
- **Avoid redefining standard gestures for undo and redo** — e.g. three-finger swipe, shaking iPhone; redefining confuses and makes the experience unpredictable.
- **Briefly and precisely describe the operation to be undone or redone** — the alert title automatically prefixes "Undo " or "Redo " (with trailing space); supply a word or two after it, e.g. "Undo Name", "Redo Address Change".
### macOS
- **Place undo and redo commands in the Edit menu and support the standard keyboard shortcuts** — at the top of the Edit menu; Command–Z = undo, Shift–Command–Z = redo.

## APIs
`UndoManager` (Foundation)

## Related
`feedback, pointing-devices, keyboards, the-menu-bar, toolbars`
