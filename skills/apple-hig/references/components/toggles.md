# Toggles

> Source: https://developer.apple.com/design/human-interface-guidelines/toggles · Lets people choose between a pair of opposing states (e.g. on/off), using a different appearance for each state.

## When to use / core idea
- Styles include switch and checkbox; platforms use them differently. All platforms also support buttons that behave like toggles (different appearance per state; `ToggleStyle`).
- Only for managing the state of something; for other actions (e.g. choosing from a list) use a different component such as `pop-up-buttons`.
- macOS also has radio buttons (mutually exclusive choices).

## Rules
### Best practices
- **Use a toggle to help people choose between two opposing values that affect the state of content or a view** — for other action types use e.g. a pop-up button.
- **Clearly identify the setting, view, or content the toggle affects** — context usually suffices; sometimes (often macOS) supply a label describing the state. A toggle-like button generally uses an interface icon conveying its purpose and updates its appearance (typically the background) per state.
- **Make sure the visual differences in a toggle's state are obvious** — add/remove color fill, show/hide background shape, change inner details (checkmark, dot). Avoid relying solely on color to communicate state.

## Platform considerations
No additional considerations: tvOS, visionOS, watchOS.
### iOS, iPadOS
- **Use the switch toggle style only in a list row** — no label needed; row content provides context.
- **Change the default color of a switch only if necessary** — default green works in most cases; you might use the app's accent color; ensure enough contrast with the uncolored (off) appearance.
- **Outside of a list, use a button that behaves like a toggle, not a switch** — e.g. Phone's filter button adds a blue highlight when active, removes it when inactive.
- **Avoid supplying a label that explains the button's purpose** — the interface icon plus alternate background appearances communicate it (`changesSelectionAsPrimaryAction`).
### macOS
- Supports switch and checkbox styles, plus radio buttons with similar behaviors.
- **Use switches, checkboxes, and radio buttons in the window body, not the window frame** — in particular avoid them in a toolbar or status bar.

#### Switches
- **Prefer a switch for settings that you want to emphasize** — more visual weight than a checkbox; suits controlling more functionality, e.g. turning a group of settings on/off (`switch` ToggleStyle).
- **Within a grouped form, consider using a mini switch to control the setting in a single row** — mini switch height matches buttons/other controls → consistent row heights. For hierarchy in a grouped form: regular switch for primary setting, mini switches for subordinates (`GroupedFormStyle`, `ControlSize`).
- **In general, don't replace a checkbox with a switch** — if already using a checkbox, keep it.

#### Checkboxes
- Anatomy: small square button — empty = off, checkmark = on, dash = mixed. Typically a title on its trailing side; in an editable checklist it can appear without title or other content.
- **Use a checkbox instead of a switch if you need to present a hierarchy of settings** — align (generally along leading edge) and indent to show dependencies, e.g. a checkbox governing subordinate checkboxes.
- **Consider using radio buttons if you need to present a set of more than two mutually exclusive options** — each option gets a unique label.
- **Consider using a label to introduce a group of checkboxes if their relationship isn't clear** — describe the set; align label baseline with the first checkbox.
- **Accurately reflect a checkbox's state in its appearance** — on, off, or mixed; a global checkbox over subordinates shows mixed when they differ (e.g. text style master + bold/italic/underline) (`allowsMixedState`).

#### Radio buttons
- Anatomy: small circular button followed by a label; typically in groups of two to five; mutually exclusive. Selected = filled circle, deselected = empty circle. Mixed state (dash) is rarely useful — use a checkbox if you need to show mixed.
- **Prefer a set of radio buttons to present mutually exclusive options** — for multiple selections use checkboxes.
- **Avoid listing too many radio buttons in a set** — more than about five options → consider a pop-up button.
- **To present a single setting that can be on or off, prefer a checkbox** — checkmark state is clearer at a glance; in rare cases where a checkbox doesn't convey opposing states, use a pair of radio buttons, each labeled with the state it controls.
- **Use consistent spacing when you display radio buttons horizontally** — measure the space for the longest label and use it consistently.

## APIs
`Toggle` (SwiftUI), `ToggleStyle` / `switch` (SwiftUI), `GroupedFormStyle` (SwiftUI), `ControlSize` (SwiftUI), `UISwitch` (UIKit), `changesSelectionAsPrimaryAction` (UIKit), `NSButton.ButtonType.toggle` (AppKit), `NSSwitch` (AppKit), `allowsMixedState` (AppKit)

## Related
`layout, pop-up-buttons, buttons`
