# Game controls

> Source: https://developer.apple.com/design/human-interface-guidelines/game-controls · Precise, intuitive game controls enhance gameplay and can increase a player's immersion in the game.

## When to use / core idea
- Games can accept physical game controllers or default system input (touch, remote, mouse and keyboard).
- Also support the platform's default input because: all platforms except watchOS support controllers, but not every player has one; and players appreciate using the input they know best.
- iOS/iPadOS touch: virtual controls over game content (Touch Controller framework) plus direct touch on game elements.

## Rules
### Touch controls
- **Determine whether it makes sense to display virtual controls on top of game content** — virtual controls suit games with many actions or movement control; otherwise prefer direct interaction with in-game objects. Reduce overlapping controls by mapping actions to in-game gestures (e.g., tap objects to select instead of a selection button).
- **Place virtual buttons where they're easy to access** — respect device boundaries and safe areas; don't overlap the Home indicator or Dynamic Island on iPhone. Frequently used buttons near the thumb, avoiding the circular regions where players expect movement and camera input. Secondary controls (menus) at the top of the screen.
- **Make sure controls are large enough** — frequently used controls minimum 44x44 pt; less important controls (menus) minimum 28x28 pt.
- **Always include visible and tactile press states** — visual press effect (e.g., glow) visible even under the finger, combined with sound and haptics. See `playing-haptics`.
- **Use symbols that communicate the actions they perform** — e.g., weapon graphic for attack; avoid abstract shapes or controller-based names (A, X, R1) as artwork.
- **Show and hide virtual controls to reflect gameplay** — hide unavailable/irrelevant actions; e.g., hide movement controls until the player touches the screen (more visible while moving, less at rest).
- **Combine functionality into a single control** — redesign mechanics needing simultaneous/sequenced presses; use double tap and touch and hold for variations (touch and hold for powered-up attack); combine related actions (walk/sprint) into one control.
- **Map movement and camera controls to predictable behavior** — movement on left side, camera on right; maximize input areas. Movement: show a virtual thumbstick wherever the thumb lands rather than a static position. Camera: direct touch to pan instead of a virtual thumbstick.

### Physical controllers
- **Support the platform's default interaction method** — controllers are optional purchases; every iPhone/iPad has touch, every Mac keyboard + trackpad/mouse, every Apple TV a remote, every Apple Vision Pro eyes-and-hands gestures. Provide a fallback.
- **Tell people about game controller requirements** — tvOS and visionOS can require a controller (App Store shows a "Game Controller Required" badge). People may open the game without one; check for presence and gracefully prompt to connect (`GCRequiresControllerUserInteraction`).
- **Automatically detect whether a controller is paired** — detect and get its profile instead of manual setup.
- **Customize onscreen content to match the connected game controller** — framework uses placement-based standard element names, but real colors/symbols differ; use the connected controller's labeling scheme (`GCControllerElement`).
- **Map controller buttons to expected UI behavior** — outside gameplay, follow the table in Specs across all Apple platforms.
- **Support multiple connected controllers** — labels/glyphs match the controller actively in use; in multiplayer, use appropriate labels per player's controller; when referring to buttons on multiple controllers, consider listing them together.
- **Prefer using symbols, not text, to refer to game controller elements** — Game Controller framework provides SF Symbols for most elements across controller brands; helps inexperienced players.

### Keyboards
- **Prioritize single-key commands** — easier with simultaneous mouse/trackpad use; e.g., first letter of a menu item (I = Inventory, M = Map); main action on Space bar.
- **Test key binding comfort using an Apple keyboard** — e.g., remap Control (^) bindings from non-Apple keyboards to Command (⌘), which sits next to Space and is easy to reach while using W, A, S, D.
- **Take the proximity of keys into account** — with WASD navigation, put high-value commands on nearby keys; map related action groups to physically close keys (number keys for inventory categories).
- **Let players customize key bindings** — provide reasonable defaults plus customization.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS. Not supported: watchOS.

### visionOS
- **Match spatial game controller behavior to hand input** — supports spatial controllers such as PlayStation VR2 Sense controller: look at an object + press left/right trigger for indirect interaction; reach out + press left/right trigger for direct interaction. See `gestures` › visionOS.

## Specs
- Touch control minimum sizes: frequently used 44x44 pt; less important (menus) 28x28 pt.

| Button | Expected behavior for UI |
| --- | --- |
| A | Activates a control |
| B | Cancels an action or returns to previous screen |
| X | — |
| Y | — |
| Left shoulder | Navigates left to a different screen or section |
| Right shoulder | Navigates right to a different screen or section |
| Left trigger | — |
| Right trigger | — |
| Left/right thumbstick | Moves selection |
| Directional pad | Moves selection |
| Home/logo | Reserved for system controls |
| Menu | Opens game settings or pauses gameplay |

## APIs
Touch Controller framework; Game Controller framework (`GCController`, `GCControllerElement`, SF Symbols for elements); `GCRequiresControllerUserInteraction` (Info.plist).

## Related
`designing-for-games, gestures, keyboards, playing-haptics, sf-symbols, layout`
