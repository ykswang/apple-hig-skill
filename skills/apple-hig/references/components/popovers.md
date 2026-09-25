# Popovers

> Source: https://developer.apple.com/design/human-interface-guidelines/popovers · A popover is a transient view that appears above other content when people click or tap a control or interactive area.

## When to use / core idea
- Exposes a small amount of information/functionality temporarily, freeing space vs. sidebars or panels.
- Use an **alert** for warnings; a **sheet** (full-screen modal) in compact iOS/iPadOS views.

## Rules
### Best practices
- **Use a popover to expose a small amount of information or functionality** — limit to a few related tasks (e.g., calendar event popover: change date/time or calendar, then disappears).
- **Consider using popovers when you want more room for content** — temporary content in a popover streamlines the interface vs. space-hungry sidebars/panels.
- **Position popovers appropriately** — arrow points as directly as possible to the revealing element; ideally don't cover that element or essential content needed while using it.
- **Use a Close button for confirmation and guidance only** — Close/Cancel/Done only if it adds clarity (e.g., exit with or without saving). Otherwise popover closes on click/tap outside or on selecting an item. If multiple selections are possible, keep it open until explicitly dismissed or clicked/tapped outside.
- **Always save work when automatically closing a nonmodal popover** — outside clicks may be accidental; discard work only on an explicit Cancel.
- **Show one popover at a time** — never a cascade/hierarchy of popovers; close the open one before showing another.
- **Don't show another view over a popover** — nothing on top except an alert.
- **When possible, let people close one popover and open another with a single click or tap** — especially when several bar buttons each open a popover.
- **Avoid making a popover too big** — only big enough for contents and pointing to its origin; system may adjust size to fit.
- **Provide a smooth transition when changing the size of a popover** — animate condensed ↔ expanded so it doesn't look like a replacement.
- **Avoid using the word *popover* in help documentation** — refer to the task/selection ("Select the Show button").
- **Avoid using a popover to show a warning** — easily missed or closed; use an alert.

## Platform considerations
No additional considerations: visionOS. Not supported: tvOS, watchOS.

### iOS, iPadOS
- **Avoid displaying popovers in compact views** — adapt layout to size class; reserve popovers for wide views; in compact views use a full-screen modal like a sheet (see modality).

### macOS
- Popovers can be detachable: dragging turns it into a separate panel that stays visible while people use other content.
- **Consider letting people detach a popover** — to keep it visible while viewing other info.
- **Make minimal appearance changes to a detached popover** — panel resembling the popover preserves context.

## APIs
`popover(isPresented:attachmentAnchor:arrowEdge:content:)` (SwiftUI), `UIPopoverPresentationController` (UIKit), `NSPopover` (AppKit).

## Related
`sheets, action-sheets, alerts, modality, panels, sidebars`
