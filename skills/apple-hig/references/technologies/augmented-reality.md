# Augmented reality

> Source: https://developer.apple.com/design/human-interface-guidelines/augmented-reality · AR delivers immersive, engaging experiences that seamlessly blend virtual objects with the real world.

## When to use / core idea
- Uses the live camera feed to superimpose 3D virtual objects; people reorient the device to explore, interact via gestures/movement, and join multiuser sessions (ARKit).
- Guidance below targets iOS/iPadOS; visionOS ARKit usage is covered under Platform considerations.
- **Offer AR features only on capable devices** — if AR is the app's primary purpose, make the app available only on ARKit-capable devices; if AR features are optional or need specific capabilities, don't show an error on unsupported devices — just don't offer the feature.

## Rules
### Best practices
- **Let people use the entire display** — maximize screen for the physical world and virtual objects; avoid cluttering controls/info.
- **Strive for convincing illusions when placing realistic objects** — detailed 3D assets, lifelike textures; use ARKit info to scale properly, place on detected surfaces, reflect environmental lighting, simulate camera grain, cast top-down diffuse shadows on real surfaces, update visuals as the camera moves. Update scenes 60 times per second so objects don't jump or flicker.
- **Consider how virtual objects with reflective surfaces show the environment** — reflections are camera-based approximations; prefer small or coarse reflective surfaces.
- **Use audio and haptics to enhance the immersive experience** — sound/bump to confirm contact with surfaces or objects; background music.
- **Minimize text in the environment** — only information needed.
- **If additional information or controls are necessary, consider displaying them in screen space** — *screen space* content stays fixed in a consistent location (in the virtual world or, less commonly, on the device screen) while AR moves with the device.
- **Consider using indirect controls when you need to provide persistent controls** — *indirect controls* are 2D controls in screen space; place so people needn't change grip; consider translucency to avoid blocking the scene (e.g. Measure app mixes translucent and opaque controls).
- **Anticipate that people will use your app in a wide variety of real-world environments** — little room, no large flat surfaces; communicate requirements up front; consider different feature sets per environment.
- **Be mindful of people's comfort** — holding a device at a distance/angle is fatiguing; place objects to reduce need to move closer; in games keep levels short with brief downtime.
- **If your app encourages people to move, introduce motion gradually** — let people adapt before e.g. dodging projectiles.
- **Be mindful of people's safety** — immersed people may not notice surroundings; avoid encouraging rapid, sweeping, large, or sudden movements.

### Providing coaching
- ARKit needs device movement to evaluate surroundings/detect surfaces; consider the built-in coaching view (`ARCoachingOverlayView`) for initialization and *relocalization* after interruptions.
- **Hide unnecessary app UI while people are using a coaching view** — it appears automatically when initialization/relocalization starts.
- **If necessary, offer a custom coaching experience** — system view can be configured (e.g. horizontal or vertical plane detection); if designing custom, use the system coaching view as reference.

### Helping people place objects
- **Show people when to locate a surface and place an object** — coaching view helps find horizontal/vertical flat surfaces; after detection show a custom placement indicator aligned with the detected surface's plane.
- **When people place an object, immediately integrate it into the AR environment** — don't wait for more accurate data; subtly refine position when detection completes (e.g. gently nudge objects placed beyond the surface back onto it; `ARTrackedRaycast`).
- **Consider guiding people toward offscreen virtual objects** — visual or audible cues, e.g. indicator along the left edge for an object offscreen left.
- **Avoid trying to precisely align objects with the edges of detected surfaces** — boundaries are approximations that change.
- **Incorporate plane classification information to inform object placement** — e.g. furniture only on "floor", game board only on "table".

### Designing object interactions
- **Let people use direct manipulation to interact with objects when possible** — more immersive than screen-space indirect controls; but when people move around while using the app, indirect controls can work better.
- **Let people directly interact with virtual objects using standard, familiar gestures** — e.g. single-finger drag to move, two-finger rotation to spin.
- **In general, keep interactions simple** — touch is 2D, AR is 3D; simplify (illustrated approaches: constrain movement to the 2D surface plane; constrain rotation to a single axis).
- **Respond to gestures within reasonable proximity of interactive virtual objects** — for small, thin, or distant objects, assume a nearby gesture targets that object.
- **Let people initiate object scaling when it makes sense in your app** — yes for imaginary environments; no when representing real-world size (e.g. furniture shopping). Never use scaling to adjust perceived distance — an enlarged distant object still looks far away.
- **Be wary of potentially conflicting gestures** — e.g. two-finger pinch vs. two-finger rotation; test that they're interpreted properly.
- **Strive for virtual object movement consistent with the physics of your app's AR environment** — keep moving objects visible and attached to real surfaces; avoid jumping or vanishing/reappearing during resize, rotate, move.
- **Explore even more engaging methods of interaction** — motion and proximity, e.g. a character turns its head as a person approaches.

### Offering a multiuser experience
- Each participant maps independently; ARKit merges maps automatically (`isCollaborationEnabled`).
- **Consider allowing people occlusion** — let people in the camera feed occlude virtual objects behind them.
- **When possible, let new participants enter a multiuser AR experience** — unless all must join first, use implicit map merging so newcomers join quickly.

### Reacting to real-world objects
- Provide 2D reference images or 3D reference objects; ARKit reports when/where they're detected (e.g. ships emerging from a movie poster, virtual guide at a sculpture).
- **When a detected image first disappears, consider delaying the removal of attached virtual objects** — ARKit doesn't track position/orientation changes of each detected image; wait up to one second before fading out/removing to prevent flicker.
- **Limit the number of reference images in use at one time** — best with 100 or fewer; for more, swap active sets by context (e.g. museum app uses location to load only that area's images).
- **Limit the number of reference images requiring an accurate position** — tracking costs more; use a tracked image when the image may move or when attached content is small relative to the image.

### Communicating with people
- **If you must display instructional text, use approachable terminology** — avoid technical terms like ARKit, world detection, tracking.

| Do | Don't |
|---|---|
| Unable to find a surface. Try moving to the side or repositioning your phone. | Unable to find a plane. Adjust tracking. |
| Tap a location to place the *[name of object to be placed]*. | Tap a plane to anchor an object. |
| Try turning on more lights and moving around. | Insufficient features. |
| Try moving your phone more slowly. | Excessive motion detected. |

- **In a three-dimensional context, prefer 3D hints** — e.g. 3D rotation indicator around an object over 2D text overlay; avoid textual overlay hints in 3D unless people aren't responding to contextual hints.
- **Make important text readable** — critical labels, annotations, instructions in screen space; text in 3D space must face people and use the same type size regardless of distance to the labeled object.
- **If necessary, provide a way to get more information** — a visual indicator fitting your app shows people they can tap for more (e.g. label ending in ">").

### Handling interruptions
- During interruptions (app switch, phone call) ARKit can't track; placed objects may appear in wrong positions afterward. Relocalization tries to restore them.
- **Consider using the system-provided coaching view to help people relocalize** — guide people back to the previous position and orientation.
- **Consider hiding previously placed virtual objects during relocalization** — avoid flicker; redisplay in new positions.
- **Minimize interruptions if your app supports both AR and non-AR experiences** — embed non-AR tasks within AR (e.g. change upholstery without leaving AR).
- **Allow people to cancel relocalization** — it can continue indefinitely; if coaching fails, provide a reset button or other way to restart.
- **Indicate when the front-facing camera is unable to track a face for more than about half a second** — use a visual indicator; minimal text.

### Suggesting problem resolutions
- **Let people reset the experience if it doesn't meet their expectations** — don't force waiting or struggling with placement.
- **Suggest possible fixes if problems occur** — causes: insufficient light, overly reflective surface, surface lacking detail, too much camera motion; use straightforward, friendly language.

| Problem | Possible suggestion |
|---|---|
| Insufficient features detected. | Try turning on more lights and moving around. |
| Excessive motion detected. | Try moving your phone slower. |
| Surface detection takes too long. | Try moving around, turning on more lights, and making sure your phone is pointed at a sufficiently textured surface. |

### Icons and badges
- AR glyph (downloadable from Apple Design Resources) may appear in controls that launch ARKit experiences (e.g. "View in AR" button).
- **Use the AR glyph as intended** — strictly for initiating ARKit experiences; never alter it (only size and color may change), use it for other purposes, or with non-ARKit AR.
- **Maintain minimum clear space** (glyph) — 10% of glyph height; nothing may infringe or occlude.
- Badges mark items viewable in AR via ARKit in collections (e.g. collectibles previewable at home).
- **Use the AR badges as intended and don't alter them** — collapsed (glyph-only) and expanded (glyph + "AR") forms; only for ARKit-viewable objects; never alter, recolor, repurpose, or use with non-ARKit AR.
- **Prefer the AR badge to the glyph-only badge** — glyph-only for constrained spaces; both work well at default size.
- **Use badging only when your app contains a mixture of AR-viewable and non-AR objects** — if all are viewable, badging is redundant.
- **Keep badge placement consistent and clear** — one corner of the object's photo, always the same corner; large enough to see, not occluding important detail.
- **Maintain minimum clear space** (badge) — 10% of badge height; nothing may infringe or occlude.

## Platform considerations
No additional considerations: iOS, iPadOS. Not supported in macOS, tvOS, watchOS.
### visionOS
- With the wearer's permission, ARKit can detect surfaces, use hand and finger positions to inform custom gestures, and incorporate nearby physical objects into immersive experiences.

## Specs
- Scene update rate: 60 times per second.
- Detected image disappears: wait up to 1 second before removing attached objects.
- Reference images: 100 or fewer active at once.
- Face-tracking loss indicator: after about 0.5 second.
- AR glyph / AR badge minimum clear space: 10% of glyph/badge height.

## APIs
ARKit, `ARCoachingOverlayView` (ARKit), `ARTrackedRaycast` (ARKit), `ARWorldTrackingConfiguration.isCollaborationEnabled` (ARKit), Occluding virtual content with people (ARKit), Detecting Images in an AR Experience (ARKit)

## Related
gestures, playing-haptics, playing-audio, immersive-experiences, privacy
