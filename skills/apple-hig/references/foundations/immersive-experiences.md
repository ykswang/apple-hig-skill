# Immersive experiences

> Source: https://developer.apple.com/design/human-interface-guidelines/immersive-experiences · In visionOS, you can design apps and games that extend beyond windows and volumes, immersing people in your content.

## When to use / core idea
- visionOS only. Apps launch in the **Shared Space** (runs alongside other experiences, switchable like on a Mac) or a **Full Space** (runs alone, hides others). Apps can move between them fluidly at any time.
- In a Full Space you can show unbounded 3D content in addition to windows and volumes.
- Reserve immersion for meaningful moments; default to Shared Space or `mixed`.

### Immersion and passthrough
- *Passthrough* = real-time video from external cameras keeping people connected to surroundings.
- Digital Crown at any time: press and hold to recenter content; double-click to briefly hide all content and show passthrough.
- System comfort behaviors: in `mixed`, content in front of someone dims briefly if they get too close to a physical object. In `progressive` and `full`, a boundary extends about **1.5 m** from the initial head position; nearing it fades the experience and increases passthrough; beyond it, visuals are replaced by the app's icon, restored on return or recenter via Digital Crown.

### Immersion styles (`ImmersionStyle`, default `automatic`)
- **Dimmed passthrough** — subtly dim or tint passthrough/other content to focus attention on your app in the Shared Space (without hiding other apps) or in a Full Space. Tinted black by default; custom tint color possible (`SurroundingsEffect`).
- **`mixed`** (Full Space) — unbounded 3D blended with passthrough; can request nearby physical object and room layout info (ARKit). No boundary; content near physical objects becomes semi-opaque.
- **`progressive`** (Full Space) — custom environment partially replacing passthrough; define a custom immersion range; portrait or landscape orientation. Digital Crown adjusts immersion within the default **120–360°** range or your custom range. ~1.5 m boundary.
- **`full`** (Full Space) — **360°** custom environment completely replacing passthrough. ~1.5 m boundary.

## Rules
### Best practices
- **Offer multiple ways to use your app or game** — freedom of experience choice; support accessibility features (see `accessibility`).
- **Prefer launching your app or game in the Shared Space or using the `mixed` immersion style** — lets people use other software alongside; for `full`/`progressive` apps, launching in `mixed` or a Shared Space window lets people choose when to increase immersion.
- **Reserve immersion for meaningful moments and content** — not every task needs immersion, nor full immersion; e.g., Photos browses albums in a Shared Space window and temporarily goes to a Full Space to examine one photo.
- **Help people engage with key moments in your app or game, regardless of the level of immersion** — cues: dimming, tinting, motion, scale, Spatial Audio. Start subtle; strengthen only with good reason.
- **Prefer subtle tint colors for passthrough** — visionOS 2+; coordinates surroundings with content and makes hands look like they belong. Avoid bright or dramatic tints.

### Promoting comfort
- **Be mindful of people's visual comfort** — prefer placing 3D content within the field of view; display motion comfortably (see `motion`).
- **Choose a style of immersion that supports the movements people might make while they're in your app or game** — minor movement (shifting weight, turning around, sit/stand) is fine; excessive movement may cause interruptions. Avoid `progressive`/`full` (or transition back to `mixed`) if people might need to move beyond the 1.5 m boundary.
- **Avoid encouraging people to move while they're in a progressive or fully immersive experience** — some can't or won't move; e.g., let people bring a virtual object closer instead of walking to it.
- **If you use the `mixed` immersion style, avoid obscuring passthrough too much** — if virtual objects could substantially obscure passthrough, use `full` or `progressive` instead.
- **Adopt ARKit if you want to blend custom content with someone's surroundings** — e.g., integrate with surroundings or use hand positions; sensitive data requires permission (see `privacy`; `SceneReconstructionProvider`).

### Transitioning between immersive styles
- **Design smooth, predictable transitions when changing immersion** — gentle, visually trackable; avoid sudden, jarring transitions.
- **Let people choose when to enter or exit a more immersive experience** — provide a clear enter/exit action (e.g., Keynote's prominent Exit button in its Rehearsal environment). Avoid requiring system controls to reduce immersion.
- **Indicate the purpose of an exit control** — clarify whether it returns to a less immersive context or quits entirely; if exiting quits, consider offering pause or a place to save progress first.

### Displaying virtual hands
- In a Full Space, an app can ask permission to hide a person's hands and show virtual hands.
- **Prefer virtual hands that match familiar characteristics** — match positions and gestures of the viewer's hands.
- **Use caution if you create virtual hands that are larger than the viewer's hands** — can block content, feel clumsy, look out of proportion or too close to the face.
- **If there's an interruption in hand-tracking data, fade out virtual hands and reveal the viewer's own hands** — never leave frozen, unresponsive virtual hands; fade back in when tracking returns.

### Creating an environment
- In a Full Space you can replace passthrough with a custom environment partially or completely surrounding the person.
- **Minimize distracting content** — avoid much movement or high-contrast details during a primary task (e.g., video). To draw attention, use highest-quality textures/shapes in important areas and lower-quality assets plus dimming elsewhere.
- **Help people distinguish interactive objects in your environment** — proximity signals interactivity: far objects rarely get touched; near ones invite interaction.
- **Keep animation subtle** — small gentle movements (drifting clouds); always avoid too much movement near field-of-view edges.
- **Create an expansive environment, regardless of the place it depicts** — small/restrictive spaces feel claustrophobic.
- **Use Spatial Audio to create atmosphere** — avoid too much repetition or looping; lower or stop the soundscape when people play other audio (e.g., a movie).
- **In general, avoid using a flat 360-degree image to create your environment** — gives little sense of scale; prefer object meshes with lighting and shaders for subtle animation (clouds, leaves, reflections).
- **Help people feel grounded** — always provide a ground plane mesh; also helps if you must use a flat 360° image.
- **Minimize asset redundancy** — repeating the same assets/models feels less realistic.

## Platform considerations
Not supported: iOS, iPadOS, macOS, tvOS, watchOS.

## Specs
- Boundary for `progressive` and `full`: ~1.5 m from initial head position. `mixed`: no boundary.
- `progressive` default immersion range: 120–360° (custom range allowed). `full`: 360°.
- Passthrough tint: black by default; custom tint in visionOS 2+.

## APIs
`ImmersionStyle` (`automatic`, `mixed`, `progressive`, `full`), Immersive spaces, `SurroundingsEffect`, `CoordinateSpaceProtocol` (SwiftUI); ARKit, `SceneReconstructionProvider` (ARKit)

## Related
spatial-layout, motion, digital-crown, playing-audio, accessibility, privacy
