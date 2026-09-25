# Remotes

> Source: https://developer.apple.com/design/human-interface-guidelines/remotes · The Siri Remote is the primary input method for Apple TV, helping people feel connected to onscreen content from across the room.

## When to use / core idea
- Siri Remote combines specific buttons with a clickpad + touch surface supporting swipe and press to navigate apps, browse channels/content, play/pause media, and make selections.
- Works together with the tvOS focus system (see `focus-and-selection`).

## Rules
### Best practices
- **Prefer using standard gestures to perform standard actions** — outside active gameplay, people expect standard remote behavior in every app; redefining/repurposing confuses.
- **Be consistent with the tvOS focus experience** — combine gestures with focus in familiar ways, e.g., always move focus in the same direction as the gesture.
- **Provide clear feedback that shows people what happens when they make gestures in your app** — e.g., resting a thumb on the remote shows where to swipe down to reveal an info area.
- **Define new gestures only when it makes sense in your app** — e.g., in gameplay; elsewhere people expect standard gestures.
- **Differentiate between press and tap, and avoid responding to an inadvertent tap** — press is intentional (choose button, confirm selection, initiate gameplay action); tap is fine for navigation or showing more info. Inadvertent taps happen when resting a thumb, picking up, moving, or handing over the remote — often avoid responding to taps during live video playback.
- **Consider using the position of a tap to aid with navigation or gameplay** — remote distinguishes up, down, left, right taps; respond only if contextually sensible, intuitive, and discoverable.
- **In almost all cases, open the parent of the current screen when people press the Back button** — top level: parent is the Apple TV Home Screen; within an app, the parent comes from the app hierarchy (not necessarily the previous screen). Exception — active gameplay: Back opens an in-game pause menu (from which another interaction returns to the game's main menu); Back while the pause menu is open closes it and resumes. Press and hold Back goes to the Home Screen from anywhere.
- **Respond correctly to the Play/Pause button during media playback** — play, pause, or resume.

### Gestures
- **Swipe** — scrolls through many items with momentum (fast then slowing, based on swipe strength). Swiping up/down on the edge of the remote speeds through items very quickly.
- **Press** — activates a control or selects an item; pressing before swiping activates scrubbing mode.

### Compatible remotes
- Some compatible remotes have live TV/channel buttons (e.g., open an electronic program guide (EPG), browse guide, change channels). See `live-viewing-apps` › EPG experience.
- **If your live-viewing app provides an EPG, respond to a remote's EPG-browsing buttons in ways people expect** — "guide"/"browse" opens your EPG; "page up"/"page down" navigates within it; don't respond to these buttons in other ways while browsing the EPG. Siri Remote and compatible remotes also allow tapping the upper/lower touch surface areas to browse. Without an EPG, the system routes these presses to the device's default guide app.
- **While your content plays, respond to a compatible remote's "page up" or "page down" button by changing the channel.**

## Platform considerations
Not supported: iOS, iPadOS, macOS, visionOS, watchOS (tvOS only).

## Specs
| Button or area | Expected behavior in an app | Expected behavior in a game |
| --- | --- | --- |
| Touch surface (swipe) | Navigates. Changes focus. | Performs directional pad behavior. |
| Touch surface (press) | Activates a control or an item. Navigates deeper. | Performs primary button behavior. |
| Back | Returns to previous screen. Exits to Apple TV Home Screen. | Pauses/resumes gameplay. Returns to previous screen, exits to main game menu, or exits to Apple TV Home Screen. |
| Play/Pause | Activates media playback. Pauses/resumes media playback. | Performs secondary button behavior. Skips intro video. |

## APIs
`Providing Channel Navigation` (tvservices)

## Related
`focus-and-selection, gestures, live-viewing-apps, game-controls, designing-for-tvos`
