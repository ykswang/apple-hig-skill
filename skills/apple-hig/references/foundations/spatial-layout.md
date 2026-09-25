# Spatial layout

> Source: https://developer.apple.com/design/human-interface-guidelines/spatial-layout · Spatial layout techniques help you use the infinite canvas of Apple Vision Pro and present content in engaging, comfortable ways.

## When to use / core idea
- visionOS only: placement of windows, volumes, and 3D content in a person's space — field of view, depth, scale.
- For laying out content inside a window/volume see layout (visionOS); for windows/volumes see windows; for full immersion see immersive-experiences.
- Volume = component that displays 3D content, like a window without a visible frame. For content with more depth, create 3D objects with RealityKit.

## Rules

### Field of view
- *Field of view* = space visible without moving the head; varies with Light Seal configuration and peripheral acuity. The system doesn't provide information about a person's field of view.
- **Center important content within the field of view** — visionOS launches apps directly in front of people by default. In immersive experiences keep important content centered; avoid distracting motion or bright, high-contrast objects in the periphery.
- **Avoid anchoring content to the wearer's head** — head-locked content feels stuck, confining, uncomfortable, especially if it obscures much passthrough. Anchor content in people's space so they can look around naturally.

### Depth
- The system automatically applies color temperature, reflections, and shadow to convey depth of virtual content; effects update as objects or people move.
- Small amounts of depth throughout the interface, even in standard windows, look more natural; SwiftUI adds depth effects to views in 2D windows automatically.
- **Provide visual cues that accurately communicate the depth of your content** — missing or conflicting cues cause visual discomfort.
- **Use depth to communicate hierarchy** — depth makes objects stand out; people notice depth changes (e.g., a window recedes along the z-axis when a sheet appears, bringing the sheet forward).
- **In general, avoid adding depth to text** — text hovering above its background is hard to read and can cause vision discomfort.
- **Make sure depth adds value** — use it to clarify and delight, not everywhere. Good for separating large, important elements (tab bar, toolbar from a window); poor on small objects (e.g., raising a button's symbol off its background reduces legibility). Limit how often depth varies — refocusing on each depth change too often or quickly is tiring.

### Scale
- *Dynamic scale*: window scale increases as it moves away and decreases as it approaches, so it appears the same size at all distances — keeps content legible and interactive.
- *Fixed scale*: object keeps the same scale, appearing smaller farther away along the z-axis, like physical objects.
- visionOS defines a point as an angle (other platforms: a number of pixels that varies with display resolution).
- **Consider using fixed scale when you want a virtual object to look exactly like a physical object** — e.g., life-size product. Prefer applying fixed scale sparingly, reserving it for noninteractive objects that need it; interactive content must scale to remain usable.

### Best practices
- **Avoid displaying too many windows** — they obscure surroundings, overwhelm, constrict, cause discomfort, and make relocating the app cumbersome.
- **Prioritize standard, indirect gestures** — *indirect* gestures don't require the hand in the field of view and work on any object people look at, at any distance; *direct* gestures (touching the virtual object) are tiring, especially at or above line of sight. If supported, consider reserving direct gestures for nearby objects inviting close inspection or manipulation for short periods.
- **Rely on the Digital Crown to help people recenter windows in their field of view** — pressing it recenters content; apps need do nothing to support this.
- **Include enough space around interactive components to make them easy for people to look at** — the hover effect confirms targeting; spacing keeps looking comfortable and prevents hover crowding. Place multiple regular-size buttons with centers at least 60 pt apart, leaving 16 pt or more between them. Don't let controls overlap other interactive elements or views.
- **Let people use your app with minimal or no physical movement** — unless movement is essential, support staying stationary.
- **Use the floor to help you place a large immersive experience** — place content extending up from the floor on a flat horizontal plane aligned with the floor.

## Platform considerations
Not supported: iOS, iPadOS, macOS, tvOS, watchOS (visionOS only).

## Specs
- Regular-size buttons: centers ≥ 60 pt apart, gap ≥ 16 pt.
- Point in visionOS = an angle (not pixels).
- Reference field-of-view rings: 30°, 60°, 90°.

## APIs
RealityKit, Adding 3D content to your app (visionOS), Presenting windows and spaces (visionOS), Positioning and sizing windows (visionOS)

## Related
eyes, layout, immersive-experiences, windows, gestures, digital-crown, buttons, motion, images
