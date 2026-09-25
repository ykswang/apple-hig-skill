---
name: apple-hig
description: Apple Human Interface Guidelines (HIG), complete and distilled — design principles, platform guidance (iOS, iPadOS, macOS, watchOS, tvOS, visionOS, games, iPhone Duo), foundations (color, typography, layout, Liquid Glass/materials, SF Symbols, app icons, accessibility, dark mode, motion, writing, privacy), every system component, interaction patterns, input methods, and Apple technology integrations (Apple Pay, Sign in with Apple, Wallet, widgets, Live Activities, Siri, CarPlay, HealthKit, etc.). Use whenever designing, building, or reviewing UI for any Apple platform — SwiftUI/UIKit/AppKit code, mockups, Figma/Sketch specs, or web UIs meant to feel native to Apple — or when the user asks "what does Apple recommend", mentions HIG, native iOS/macOS feel, App Store review readiness for UI, or asks about a specific component (tab bar, sheet, alert, toolbar, sidebar, menu, button, picker, etc.).
---

# Apple Human Interface Guidelines

Distilled from the official HIG (developer.apple.com/design/human-interface-guidelines), all 173 pages,
content current through September 2026 (includes Liquid Glass, iPhone Duo, Apple In-App Purchase).

## How to use this skill

1. **Identify the platform(s)** → read `references/getting-started/designing-for-<platform>.md` first.
   Platforms: `ios`, `ipados`, `macos`, `watchos`, `tvos`, `visionos`, `games`, `iphone-duo`.
2. **Find the relevant pages** in the routing table below, or search `references/INDEX.md`
   (one line per page with its purpose). Load only what the task needs — each file is self-contained.
3. **Apply the rules.** Reference files keep Apple's modal strength: *Never/Don't/Avoid* = hard rule;
   *Prefer/Generally* = strong default (deviate only with a stated reason); *Consider* = suggestion.
4. **Check platform considerations** at the bottom of each reference — iOS and macOS rules often differ.
5. **Review** the result against the checklist at the end of this file.

When the user's request conflicts with the HIG, say so, cite the page, and offer the compliant alternative.
When the HIG is silent, fall back to the design principles below and to system-component default behavior.

## Design principles (the foundation of all other guidance)

| Principle | Tagline | Guidance |
| --- | --- | --- |
| Purpose | Make something meaningful | Create value; keep focused on the most important features; find new ways to solve the problem instead of re-creating existing ones. |
| Agency | Let people do things their own way | Stay out of the way; give freedom to explore (no locked flows — make guided flows skippable); help people recover from mistakes (undo, return to prior state). |
| Responsibility | Act in people's best interest | Be transparent about what the product does and why (clear rationale for permissions/data); keep information safe — collect only what's needed. |
| Familiarity | Build on what people know | Use known real-world and software concepts; keep visuals and interactions consistent; provide clear feedback using system patterns. |
| Flexibility | Adapt to diverse contexts and needs | Design for everyone (accessibility from the start); preserve context across platforms/configurations; support many input methods; approach every platform with intention. |
| Simplicity | Be clear and direct | Include just what's necessary (simplicity ≠ minimalism); be concise; establish hierarchy with recognizable controls and consistent structure. |
| Craft | Care about every detail | Quality sets the tone; experiment and iterate, test in real-world settings; maintain your craft — keep current with platform capabilities. |
| Delight | Make it human | Identify the emotion to inspire; create defining moments; don't mistake delight for decoration; delight emerges from the whole. |

Full text: `references/getting-started/design-principles.md`.

## Cross-cutting rules (apply to almost every UI task)

### Prefer system components and behaviors
- Use standard system components (SwiftUI/UIKit/AppKit) before custom ones — they automatically get Liquid Glass,
  Dynamic Type, Dark Mode, accessibility, localization, and platform-correct behavior.
- Don't redefine the meaning of standard gestures, keyboard shortcuts, SF Symbols, or system colors.

### Liquid Glass & materials → `foundations/materials.md`
- Liquid Glass is the **functional layer** (tab bars, toolbars, sidebars, controls) floating above the **content layer**.
- **Don't use Liquid Glass in the content layer**; use standard materials for content-layer backgrounds.
- Use Liquid Glass effects sparingly on custom controls — only the most important functional elements.
- Use the *clear* variant only over visually rich backgrounds; otherwise *regular*.
- Apply color sparingly to glass and to symbols/text on it.

### Color → `foundations/color.md`, `foundations/dark-mode.md`
- Use semantic/dynamic system colors; **avoid hard-coding system color values**; don't redefine their semantics.
- Every color must work in light, dark, and increased-contrast modes. Don't ship an app-specific appearance setting.
- **Never rely on color alone** to convey state, interactivity, or essential information.
- Don't use the same color to mean different things.

### Accessibility → `foundations/accessibility.md`, `technologies/voiceover.md`
| Platform | Default control size | Minimum control size |
| --- | --- | --- |
| iOS, iPadOS | 44x44 pt | 28x28 pt |
| macOS | 28x28 pt | 20x20 pt |
| visionOS | 60x60 pt | 28x28 pt |
| watchOS | 44x44 pt | 28x28 pt |

| Text size | Text weight | Minimum contrast ratio |
| --- | --- | --- |
| Up to 17 pt | All | 4.5:1 |
| 18 pt | All | 3:1 |
| All | Bold | 3:1 |

- Support Dynamic Type, VoiceOver labels for every custom control/icon/symbol, Reduce Motion, Increase Contrast,
  Bold Text, and full keyboard access where the platform has it.

### Typography → `foundations/typography.md`
| Platform | Default size | Minimum size |
| --- | --- | --- |
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| tvOS | 29 pt | 23 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |
- Use the built-in text styles (Large Title … Caption 2) so text scales with Dynamic Type; avoid light weights;
  minimize the number of typefaces. System fonts: SF Pro / SF Compact / SF Mono / New York.
- Layout must adapt to all text sizes: minimize truncation, reflow at large sizes, scale meaningful icons with text.

### Layout → `foundations/layout.md` (per-device widget/Live Activity dimensions: `components/widgets.md`, `components/live-activities.md`)
- Respect safe areas (they keep content clear of hardware features like the Dynamic Island and of bars). macOS: avoid controls/critical info at the bottom of a window and content behind the camera housing.
- Lay out by **size class**, not device type or orientation; keep functionality identical across size classes.
- Order content by importance, align to aid scanning, group related items, use progressive disclosure,
  and visually differentiate controls from content.

### Icons & symbols → `foundations/sf-symbols.md`, `foundations/icons.md`, `foundations/app-icons.md`
- Prefer SF Symbols; match symbol weight to adjacent text; custom icons as vectors (PDF/SVG) with alt-text labels.
- Never depict replicas of Apple hardware.

### Motion → `foundations/motion.md`
- Motion must be purposeful, brief, and optional (honor Reduce Motion); avoid motion on frequent interactions; let people cancel it.

### Writing → `foundations/writing.md`
- Clear, concise, action-oriented labels; consistent capitalization style; clear error messages with a next step;
  clear next steps on empty screens; hints in text fields.

### Privacy → `foundations/privacy.md`
- Request access only to data you actually need; request permission only when the app clearly needs it — not at launch
  unless required to function; write purpose copy that clearly says how the data is used; process on-device where possible.

## Routing table: task → reference files

| Task | Read |
| --- | --- |
| App structure / top-level navigation | `components/tab-bars.md`, `components/sidebars.md`, `components/split-views.md`, `foundations/layout.md` |
| Toolbars, nav bars, actions in bars | `components/toolbars.md`, `components/buttons.md` |
| Buttons, menus, context actions | `components/buttons.md`, `components/menus.md`, `components/context-menus.md`, `components/pull-down-buttons.md`, `components/pop-up-buttons.md` |
| macOS menu bar, Dock menu, windows | `components/the-menu-bar.md`, `components/dock-menus.md`, `components/windows.md`, `components/panels.md` |
| Modal presentation | `patterns/modality.md`, `components/sheets.md`, `components/alerts.md`, `components/action-sheets.md`, `components/popovers.md` |
| Lists, tables, collections | `components/lists-and-tables.md`, `components/collections.md`, `components/outline-views.md`, `components/column-views.md` |
| Forms & data entry | `patterns/entering-data.md`, `components/text-fields.md`, `components/pickers.md`, `components/toggles.md`, `components/segmented-controls.md`, `components/sliders.md`, `components/steppers.md`, `components/virtual-keyboards.md` |
| Search | `patterns/searching.md`, `components/search-fields.md`, `components/token-fields.md` |
| Loading, progress, feedback | `patterns/loading.md`, `components/progress-indicators.md`, `patterns/feedback.md`, `patterns/playing-haptics.md` |
| Onboarding, launch, help | `patterns/launching.md`, `patterns/onboarding.md`, `patterns/offering-help.md` |
| Settings | `patterns/settings.md`, `components/toggles.md` |
| Accounts & sign-in | `patterns/managing-accounts.md`, `technologies/sign-in-with-apple.md` |
| Notifications | `components/notifications.md`, `patterns/managing-notifications.md` |
| Widgets, Live Activities, Controls, complications | `components/widgets.md`, `components/live-activities.md`, `components/controls.md`, `components/complications.md` |
| Siri, Shortcuts, Spotlight snippets | `technologies/siri.md`, `components/app-shortcuts.md`, `components/snippets.md` |
| Charts & data viz | `components/charts.md`, `patterns/charting-data.md`, `components/gauges.md` |
| Media | `patterns/playing-video.md`, `patterns/playing-audio.md`, `components/image-views.md`, `technologies/airplay.md` |
| Files & documents | `patterns/file-management.md`, `patterns/drag-and-drop.md`, `patterns/undo-and-redo.md`, `patterns/printing.md` |
| Sharing & collaboration | `patterns/collaboration-and-sharing.md`, `components/activity-views.md`, `technologies/shareplay.md` |
| Payments & purchases | `technologies/apple-pay.md`, `technologies/apple-in-app-purchase.md`, `technologies/wallet.md`, `technologies/tap-to-pay-on-iphone.md` |
| App icon | `foundations/app-icons.md` |
| Branding within an app | `foundations/branding.md`, `foundations/color.md` |
| Localization / RTL | `foundations/right-to-left.md`, `foundations/inclusion.md`, `foundations/writing.md` |
| visionOS / spatial | `getting-started/designing-for-visionos.md`, `foundations/spatial-layout.md`, `foundations/immersive-experiences.md`, `components/ornaments.md`, `inputs/eyes.md` |
| Games | `getting-started/designing-for-games.md`, `inputs/game-controls.md`, `technologies/game-center.md` |
| Keyboard, pointer, trackpad | `inputs/keyboards.md`, `inputs/pointing-devices.md`, `inputs/focus-and-selection.md` |
| Touch gestures | `inputs/gestures.md` |
| Apple Watch | `getting-started/designing-for-watchos.md`, `inputs/digital-crown.md`, `components/complications.md`, `components/watch-faces.md`, `patterns/workouts.md` |
| Apple TV | `getting-started/designing-for-tvos.md`, `inputs/remotes.md`, `inputs/focus-and-selection.md`, `components/top-shelf.md` |
| AI / ML features | `technologies/generative-ai.md`, `technologies/machine-learning.md` |

All paths are relative to `references/`. For anything not listed, search `references/INDEX.md`.

## Review checklist

Use when reviewing a design, mockup, or UI code. Report violations as: rule → page → fix.

- [ ] Platform conventions: navigation model and component choices match `designing-for-<platform>.md`.
- [ ] System components used where one exists; custom controls justified and behave like their system counterparts.
- [ ] Liquid Glass only in the functional layer; not stacked on content; color applied sparingly.
- [ ] Hit targets meet the platform default size (table above); adequate spacing between controls.
- [ ] Text uses text styles / Dynamic Type; layout survives the largest accessibility sizes without clipping.
- [ ] Contrast ≥ 4.5:1 for text ≤ 17 pt (3:1 for ≥ 18 pt or bold); works in Light, Dark, and Increase Contrast.
- [ ] No information conveyed by color alone; every icon-only control has an accessibility label.
- [ ] Safe areas respected; layout driven by size class; works in all orientations/window sizes the platform allows.
- [ ] Destructive actions use the destructive style, are never the primary/default button, come with a Cancel option,
      and are undoable when possible (no confirmation alerts for common, undoable actions).
- [ ] Modality used only when needed; every modal has an obvious way to dismiss/cancel.
- [ ] Permissions requested only when needed (not at launch unless essential) with clear purpose copy; no unnecessary data collection.
- [ ] Copy is concise, action-oriented, consistently capitalized; errors say what happened and how to fix it.
- [ ] Motion is purposeful and honors Reduce Motion.
- [ ] SF Symbols used consistently; symbol weight matches adjacent text.
