# Panels

> Source: https://developer.apple.com/design/human-interface-guidelines/panels · In a macOS app, a panel typically floats above other open windows providing supplementary controls, options, or information related to the active window or current selection.

## When to use / core idea
- macOS only. Less prominent than the main window. Can use a dark, translucent HUD (heads-up display) style when appropriate.
- On other platforms, use a modal view for supplementary task/selection content (see modality).
- Inspector alternatives: a split view pane. For an Info window with fixed contents, use a regular window, not a panel.

## Rules
### Best practices
- **Use a panel to give people quick access to important controls or information related to the content they're working with** — e.g., settings affecting the selected item in the active document/window.
- **Consider using a panel to present inspector functionality** — an *inspector* shows details of the current selection and updates automatically as selection changes. An *Info* window keeps the same contents regardless of selection → use a regular window. A split-view pane may also host an inspector.
- **Prefer simple adjustment controls in a panel** — avoid controls requiring typing or selecting items to act on (multi-step); prefer sliders and steppers for direct control.
- **Write a brief title that describes the panel's purpose** — panels need a title bar for positioning; use a noun or noun phrase with title-style capitalization (e.g., "Fonts", "Colors", "Inspector").
- **Show and hide panels appropriately** — when the app becomes active, bring all its open panels to the front regardless of which window was active; when inactive, hide all panels.
- **Avoid including panels in the Window menu's documents list** — show/hide commands in the Window menu are fine, but panels aren't documents or standard windows.
- **In general, avoid making a panel's minimize button available** — panels appear only when needed and disappear when the app is inactive.
- **Refer to panels by title in your interface and in help documentation** — menus: "Show Fonts", "Show Colors", "Show Inspector" (no word *panel*). Help docs: use the title, or append *window* when clearer ("Fonts window", "Colors window"; "Inspector" stands alone).

### HUD-style panels
- Same function as a standard panel but darker and translucent; for highly visual/immersive apps (media editing, full-screen slide show), e.g., QuickTime Player inspector.
- **Prefer standard panels** — HUDs without logical reason distract/confuse and may not match the appearance setting. Use a HUD only:
  - In a media-oriented app presenting movies, photos, or slides;
  - When a standard panel would obscure essential content;
  - When you don't need controls — except the disclosure triangle, most system controls don't match HUD appearance.
- **Maintain one panel style when your app switches modes** — e.g., keep HUD style after exiting full-screen if used in full-screen.
- **Use color sparingly in HUDs** — small amounts of high-contrast color to highlight important info.
- **Keep HUDs small** — don't obscure the content being adjusted or compete with it for attention.

## Platform considerations
Not supported: iOS, iPadOS, tvOS, visionOS, watchOS.

## APIs
`NSPanel` (AppKit), `NSWindow.StyleMask.hudWindow` (AppKit).

## Related
`windows, modality, split-views, the-menu-bar, sliders, steppers`
