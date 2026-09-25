# Offering help

> Source: https://developer.apple.com/design/human-interface-guidelines/offering-help · The most effective experiences are approachable and intuitive, but you can provide contextual help when necessary.

## When to use / core idea
- Match help type to task complexity: inline view for simple 1–2 step tasks; tutorial for complex/multistep goals.
- *Tips* (TipKit): small, transient views teaching new/less obvious features or faster ways to do tasks. Types: popover tip (preserves content flow), inline tip (keeps surrounding info visible) — annotation-style (points at a UI element) or hint-style (not tied to specific UI).
- *Tooltips* (macOS, visionOS; "help tags" in user docs): transient descriptions of a component on pointer hover (Mac, including iPhone/iPad apps on Mac) or gaze/hover (visionOS).
- See also `onboarding`, `feedback`, `writing`, Help menu in `the-menu-bar`.

## Rules
### Best practices
- **Let your app's tasks inform the types of help people might need** — relate help directly to the current action/task and make it easy to dismiss or avoid.
- **Use relevant and consistent language and images in your help content** — match context (e.g. don't show game-controller imagery to a Siri Remote user); use platform-consistent terms (don't say "click" on iPhone or "tap a menu item" on Mac).
- **Make sure all help content is inclusive** — see `inclusion`.
- **Avoid bloating your help content by explaining how standard components or patterns work** — describe what the element does in your app; for unique controls or nonstandard input use (e.g. Siri Remote rotated 90 degrees), orient people quickly, preferring animation/graphics over lengthy description.

### Creating tips
- **Use the most appropriate tip type for your app's user interface** — popover to preserve content flow; inline to keep surrounding info visible; annotation-style inline when pointing to a specific element; hint-style when not tied to specific UI.
- **Use tips for simple features** — easy to describe, few simple steps; more than three actions is probably too complicated for a tip.
- **Make tips short, actionable, and engaging** — direct, action-oriented language on what it does and how to use it; one or two sentences; no promotional content (advertises, sells, or off-context) or content about a different feature/flow.
- **Define rules to help ensure your tips reach the intended audience** — parameter- or event-based eligibility rules; don't show tips for already-used features; with multiple tips set a reasonable display frequency (e.g. once every 24 hours).
- **If there's an image or symbol that people associate with the feature, consider including it in the tip, and prefer the filled variant** — e.g. filled star for favorites. If the tip connects directly to the feature's image in the UI, avoid repeating that image in the tip.
- **Use buttons to direct people to information or options** — e.g. button to the feature's settings or to additional resources such as a setup flow.

## Platform considerations
No additional considerations: iOS, iPadOS, tvOS, watchOS.
### macOS, visionOS (tooltips)
- **Describe only the control that people indicate interest in** — not nearby controls or larger tasks.
- **Explain the action or task the control initiates** — begin with a verb, e.g. "Restore default settings", "Add or remove a language from the list".
- **In general, avoid repeating a control's name in its tooltip** — wastes space, rarely adds value.
- **Be brief** — limit to a maximum of 60 to 75 characters (localization changes length); consider sentence fragments and omitting articles; if much text is needed, simplify the UI.
- **Use sentence case** — more casual/approachable; omit ending punctuation on complete sentences unless required for your app's style consistency.
- **Consider offering context-sensitive tooltips** — e.g. different text for a control's different states.

## Specs
- Tip: 1–2 sentences; feature should need ≤ 3 actions; example cadence once every 24 hours.
- Tooltip: max 60–75 characters.

## APIs
`TipKit`, `help(_:)` (SwiftUI), `NSHelpManager` (AppKit)

## Related
`onboarding, feedback, writing, the-menu-bar, inclusion, entering-data`
