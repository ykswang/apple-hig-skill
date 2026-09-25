# Eyes

> Source: https://developer.apple.com/design/human-interface-guidelines/eyes · In visionOS, people look at a virtual object to identify it as a target they can interact with.

## When to use / core idea
- Looking at an interactive element triggers the system *hover effect* (highlight), confirming it can be activated with an indirect gesture like tap (see `gestures`).
- The system may auto-expand a component on look: a tab bar resizes to reveal text labels (an individual tab highlights first so it can be selected before labels appear); a button may reveal a tooltip.
- Privacy: visionOS doesn't tell apps where people look before they tap; system components report taps automatically.
- *Focus effects* (keyboard/game controller navigation) are unrelated to hover effects — see `focus-and-selection`.

## Rules
### Best practices
- **Always give people multiple ways to interact with your app** — support the accessibility features people use to personalize interaction. See `accessibility`.
- **Design for visual comfort** — keep needed objects within field of view; the system places the first window/volume in front of people in the Shared Space or a Full Space; in a Full Space you can request head-pose info to place 3D content. Avoid requiring multiple quick eye adjustments over a large area or through multiple depth levels.
- **Place content at a comfortable viewing distance** — for reading/extended engagement, aim for at least one meter away; avoid placing content very close unless viewed/used only briefly.
- **Prefer using standard UI components** — they respond consistently to gaze; custom cues are hard to learn and remember.

### Making items easy to see
- **Minimize visual distractions** — visual noise hinders finding objects; movement (especially peripheral) draws involuntary looks — e.g., revealing content near a button being looked at pulls gaze away.
- **Make it easy for people to look at an item by providing enough space around it** — eyes make small, quick adjustments; use a margin of at least 16 pt around each item's bounds, or keep item centers at least 60 pt apart.
- **Avoid using a repeating pattern or texture that fills the field of view** — eyes can lock onto different elements, making them appear at different depths; use patterns in smaller areas.

### Encouraging interaction
- **Consider using subtle visual cues to encourage people to look at the item they're most likely to want** — place near center of field of view, or use gentle motion, increased contrast, color or scale variation. Prefer noticeable, not flashy or harsh.
- **In general, give an interactive item a rounded shape** — eyes are drawn to corners; more rounded = easier to target (circular button over square).
- **If you create an interactive component that consists of more than one element, be sure to provide an overall containing shape that visionOS can highlight** — e.g., image + label acting as one component need a custom region covering both.

### Custom hover effects
- Can apply to system or custom UI elements and RealityKit entities; replace or augment standard effect.
- You define two states (with and without effect); the system applies the effect out of your process, so you don't know when it's applied or the element's state, and it can't run code that depends on knowing people are looking (e.g., can show a different symbol for favorited photos, but can't perform favoriting on look).
- **Prefer using a custom hover effect to emphasize or enhance a special moment in your experience** — too many, or using them when standard effects suffice, dilutes impact, distracts, and can cause visual discomfort.
- **Choose the right delay:**
  - **No delay (default)** — subtle effects or ones inviting interaction (e.g., a knob appearing on a slider).
  - **Short delay** — lets people look and quickly interact without waiting (e.g., tab bar expansion).
  - **Long delay** — effect shows additional info (e.g., tooltip below a button), since most people don't need it every time.
- **Aim to keep one or more of the element's primary views unchanged in both states of a custom hover effect** — provides stability; changing all views disorients.
- **Thoroughly test custom hover effects** — ideally while wearing Apple Vision Pro.

## Platform considerations
Not supported: iOS, iPadOS, macOS, tvOS, watchOS (visionOS only).

## Specs
- Minimum spacing between interactive items: 16 pt margin around bounds, or centers ≥ 60 pt apart.
- Comfortable viewing distance for sustained content: ≥ 1 meter.
- Hover effect delays: none (default), short, long.

## APIs
`Adopting best practices for privacy and user preferences` (visionOS)

## Related
`gestures, focus-and-selection, spatial-layout, layout, immersive-experiences, accessibility`
