# Sheets

> Source: https://developer.apple.com/design/human-interface-guidelines/sheets · A sheet helps people perform a scoped task that's closely related to their current context.

## When to use / core idea
- Request specific information or present a simple task completed before returning to the parent view (e.g., attaching a file, choosing a save location).
- Alternatives: full-screen modal (iOS/iPadOS), new window or full screen (macOS), Full Space (visionOS) for complex/prolonged flows; panel (macOS) or split view (visionOS) for supplementary nonmodal content; popover for small transient content; alert/action sheet for info or choices.

## Anatomy
- Always *modal* in macOS, tvOS, visionOS, watchOS — blocks interaction with the parent until dismissed.
- iOS/iPadOS: modal or *nonmodal*; nonmodal lets people affect the parent without dismissing (e.g., Notes format sheet).
- Common buttons:
  - **Cancel** (or Close) — dismisses without saving; common in most sheets.
  - **Done** — dismisses after completing a task or explicitly saving.
  - **Back** — previous step in a multi-step flow or parent in a hierarchy; not for dismissing.

## Rules
### Best practices
- **For complex or prolonged user flows, consider alternatives to sheets** — iOS/iPadOS full-screen modal for videos, photos, camera, multistep editing (`UIModalPresentationStyle.fullScreen`); macOS: new window (e.g., document editing) or full screen (media); visionOS: transition to a Full Space.
- **Display only one sheet at a time from the main interface** — closing should return to the parent; if an action in a sheet spawns another, close the first before showing the new one; you may reshow the first after the second is dismissed.
- **Use a nonmodal view when you want to present supplementary items that affect the main task in the parent view** — visionOS split view, macOS panel, iOS/iPadOS nonmodal sheet.
- **Provide an alternative to the Done button** — always pair Done with Cancel (dismiss without confirming/saving) or Back (previous step). Done alone implies completion is the only exit — restrictive/misleading.
- Avoid showing all three buttons — Cancel, Done, and Back — together.

## Platform considerations
No additional considerations: tvOS.

### iOS, iPadOS
- Single-view sheets: Cancel on the leading edge of the top toolbar; Done (when present) on the trailing edge.
- Multi-step flows: first step — Cancel leading, (inactive) Done trailing; subsequent steps — Back leading, (inactive) Done trailing; final step — Back leading, Done trailing.
- Resizable sheets expand when people scroll contents or drag the *grabber* (small horizontal indicator at top edge). They rest at *detents*: **large** = fully expanded height; **medium** ≈ half of fully expanded height; custom detents allowed. Large is supported automatically; adding medium allows both; specifying only medium prevents full-height expansion (`detents`).
- **In an iPhone app, consider supporting the medium detent to allow progressive disclosure of the sheet's content** — e.g., share sheet shows most relevant items at medium; scroll/expand for more. Skip medium when full height is more useful (Messages/Mail compose sheets are full height only).
- **Include a grabber in a resizable sheet** — signals resizability; tap cycles detents; works with VoiceOver (`prefersGrabberVisible`).
- **Support swiping to dismiss a sheet** — people expect vertical swipe; if there are unsaved changes when a swipe begins, confirm with an action sheet.
- **Prefer using the page or form sheet presentation styles in an iPadOS app** — default sizes, content centered over a dimmed background (`UIModalPresentationStyle`).

### macOS
- Cardlike view with rounded corners floating over its parent window; parent is dimmed and non-interactive until dismissal, but people expect to use other app windows meanwhile.
- **Present a sheet in a reasonable default size** — people don't generally expect to resize sheets; but supporting resize is a good idea when expanding contents helps.
- **Let people interact with other app windows without first dismissing a sheet** — on open, bring the parent window to the front (plus its modeless document-related panels if a document window); other windows must still be bringable forward.
- **Use a panel instead of a sheet if people need to repeatedly provide input and observe results** — e.g., find and replace with individually initiated replacements.

### visionOS
- Floats in front of its parent window, dims it, and becomes the interaction target.
- **Avoid displaying a sheet that emerges from the bottom edge of a window** — prefer centering it in people's field of view.
- **Present a sheet in a default size that helps people retain their context** — avoid covering most or all of the window; consider allowing resize.

### watchOS
- Full-screen view sliding over current content; semitransparent, with a background material that blurs and desaturates covered content.
- **Use a sheet only when your modal task requires a custom title or custom content presentation** — for important info or a set of choices, consider an alert or action sheet.
- **Keep sheet interactions brief and occasional** — temporary interruption for an important task only; don't use a sheet to navigate app content.
- **If you change the default label, prefer using SF Symbols to represent the action** — avoid labels suggesting hierarchical navigation (e.g., a custom Back button) or text in the top-leading corner that looks like a page/app title (people won't know how to dismiss). Default Cancel button is correct.

## Specs
- System detents: **large** (full height), **medium** (≈ half of full height).

## APIs
`sheet(item:onDismiss:content:)` (SwiftUI), `UISheetPresentationController` (UIKit) incl. `detents`, `prefersGrabberVisible`, `UIModalPresentationStyle` / `.fullScreen` (UIKit), `presentAsSheet(_:)` (AppKit).

## Related
`modality, action-sheets, popovers, panels, alerts, split-views, going-full-screen, immersive-experiences, spatial-layout, icons, sf-symbols`
