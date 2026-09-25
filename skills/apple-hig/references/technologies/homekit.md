# HomeKit

> Source: https://developer.apple.com/design/human-interface-guidelines/homekit · HomeKit lets people securely control connected accessories in their homes using Siri or the Home app on iPhone, iPad, Apple Watch, and Mac.

## When to use / core idea
- In iOS the Home app also manages/configures accessories. Your iOS, tvOS, or watchOS app can integrate with HomeKit to: help set up, name, and organize accessories; allow fine-grained configuration and control; expose custom accessory features; show how to create hands-free automations; provide support.
- Always use HomeKit's object model and terminology to reinforce understanding. MFi licensees: see MFi portal for packaging naming/messaging.

## Rules
### Terminology and layout
- Hierarchy: **home** is the root containing rooms, accessories, zones; with multiple homes, each is the root of its own hierarchy.
- **Acknowledge the hierarchical model that HomeKit uses** — even if your UI doesn't organize by rooms/zones, reference the model during setup/control; people need locations for Siri/HomePod commands ("Siri, turn on the lights upstairs", "It's dark in here").
- **Make it easy for people to find an accessory's related HomeKit details** — don't bury zone/room in a hard-to-discover settings screen; consider showing them in an accessory detail view.
- **Recognize that people can have more than one home** — even if you don't support multiple homes, consider showing the relevant home in the accessory detail view.
- **Don't present duplicate home settings** — don't ask people to set up their home again or show a duplicate settings view; always defer to Home app settings.

#### Vocabulary
- **Home**: physical home, office, or other relevant location; a person may have several.
- **Room**: a name with meaning (Bedroom, Office); no size/location attributes. Enables "turn on all the lights except the bedroom."
- **Accessory**: physical connected device (fan, lamp, lock, camera). **Category**: accessory type (thermostat, fan, light); usually set by manufacturer, app can help assign — a switch connected to a fan/lamp gets the category of what it controls.
- **Service**: a controllable feature (light switch); accessories can have several (garage light + door; top/bottom outlet). Never say "service" in UI — use descriptive names ("garage door opener", "ceiling fan light"). Siri uses the service name, not the accessory name.
- **Characteristic**: controllable attribute of a service (speed, brightness). Never say "characteristic" in UI — use the attribute term.
- **Service group**: services controlled as a unit (e.g., three lamps → "reading lamps").
- **Action**: changing a characteristic; initiated by people or automation. **Scene**: group of actions across services/accessories ("Movie Time", "Good Morning").
- **Tip:** the API says *action set*; in UI always say *scene*.
- **Automation**: accessories react to location change, time of day, another accessory's state, or a sensor (e.g., lights on at sunset/arrival).
- **Zone**: area with multiple rooms (upstairs/downstairs); optional; enables "turn off all the lights downstairs."

### Setup
- **Use the system-provided setup flow to give people a familiar experience** — faster: name, join network, pair, assign room/service categories, designate favorites in a few steps.
- **Provide context to explain why you need access to people's Home data** — purpose string, e.g., "Lets you control this accessory with the Apple Home app and Siri across your Apple devices."
- **Don't require people to create an account or supply personal information** — defer to HomeKit; make any extra-service account (e.g., cloud) optional and offer it only after initial HomeKit setup.
- **Honor people's setup choices** — don't force setup of other platforms during HomeKit setup.
- **Carefully consider how and when to provide a custom accessory setup experience** — always begin with the system flow; after basic functionality works, offer a custom post-setup experience highlighting unique features (e.g., light scenes from photo colors).

#### Help people choose useful names
- **Suggest service names that suit your accessory** — recommend alternatives to suboptimal Siri names; never suggest company names or model numbers.
- **Check that the names people provide follow HomeKit naming rules** — when renaming (system flow checks originals); if broken, briefly explain and suggest alternatives. Rules: only alphanumeric, space, and apostrophe characters; start and end with an alphabetic or numeric character; no emojis. ✓ "Reading lamp", ✗ "📚 lamp", ✓ "2nd garage door", ✗ "#2 garage door".
- **Help people avoid creating names that include location information** — "kitchen light" causes unpredictable voice results; detect and offer to remove room/zone from the name and assign the accessory to that room/zone instead.

### Siri interactions
- **Present example voice commands to demonstrate using Siri to control accessories during setup** — right after setup, consider example phrases using the chosen service name.
- **After setup, consider teaching people about more complex Siri commands** — e.g., in a scene detail view: *You can say "Hey Siri, set 'Movie Time.'"*
- Siri recognizes names of homes, rooms, zones, services, scenes, plus category and characteristic (e.g., "brighter"/"dim" → brightness service).
- **Recommend that people create zones and service groups, if they make sense for your accessory** — e.g., zone "upstairs", service group "media center".
- **Offer shortcuts only for accessory-specific functionality that HomeKit doesn't support** — don't duplicate HomeKit; consider complementary ones (e.g., "Order AC filters").
- **If your app supports both HomeKit and shortcuts, help people understand the difference between these types of voice control** — clearly indicate what shortcuts do; never encourage a shortcut for a scene or action HomeKit already supports.

### Custom functionality
- **Be clear about what people can do in your app and when they might want to use the Home app** — e.g., lights-only app: guide creation of a scene with your accessory's actions, then suggest opening the Home app to add shades/TV.
- **Defer to HomeKit if your database differs from the HomeKit database** — automatically reflect changes from Home app/other apps; if people must resolve conflicts, present visually (e.g., old and new names side by side).
- **Ask permission to update the HomeKit database when people make changes in your app** — never overwrite HomeKit settings without explicit direction.

#### Cameras
- Apps can show stills or streaming video from HomeKit IP cameras.
- **Don't block camera images** — supplementing (e.g., activity alert) is fine; avoid covering portions of the image.
- **Show a microphone button only if the camera supports bidirectional audio.**

### Using HomeKit icons
- Use the HomeKit icon in setup or instructional communications. Use the Apple Home app icon when referencing the app or in a button that opens its App Store product page.
- **Use only Apple-provided icons** — don't create or mimic; download from Apple Design Resources.
- Styles: **black** icon on white/light backgrounds when other technology icons are black; **white** icon on black/dark backgrounds when others are white; **custom color** when other technology icons use that same color.
- **Position the HomeKit icon consistently with other technology icons** — if others are inside shapes, treat HomeKit the same.
- **Use the HomeKit icon noninteractively** — don't use the icon or name *HomeKit* in custom interactive elements/buttons. (Apple Home app icon may open the App Store page.)
- **Don't use the HomeKit icon within text or as a replacement for the word HomeKit** — icon may lead the line before text ("[icon] Lights set with HomeKit"), never inline after "with" or at line end.
- **Pair the icon with the name *HomeKit* correctly** — name below or beside the icon if other technologies are shown that way; use the layout's font.

### Referring to HomeKit
- **Emphasize your app over HomeKit** — HomeKit/Apple Home references less prominent than your app name/identity.
- **Adhere to Apple's trademark guidelines** — no Apple trademarks in app name or images; use names exactly per the Apple Trademark List:
  - Singular only; never possessive.
  - Don't translate Apple, Apple Home, HomeKit, or other trademarks.
  - No category descriptors (say iPad, not tablet).
  - Don't imply sponsorship, partnership, or endorsement.
  - Attribute trademarks with correct credit lines where legal info appears.
  - Refer to Apple devices/OSs only in technical specs or compatibility descriptions. ✓ "…from your iPhone or iPad." ✗ "…from your iOS devices."

#### Referencing HomeKit and the Home app
- **Use correct capitalization when using the term *HomeKit*** — one word, uppercase H and K; *Apple Home* two words, uppercase A and H. All caps only if the layout uses all-uppercase designations.
- **Don't use the name *HomeKit* as a descriptor** — use *works with*, *use*, *supports*, *compatible*. ✓ "[Brand] lightbulbs work with HomeKit." ✓ "HomeKit-enabled thermostat." ✓ "You can use HomeKit with [App Name]." ✗ "HomeKit lightbulbs."
- **Don't suggest that HomeKit is performing an action or function** — ✓ "Back door is unlocked with HomeKit." ✗ "HomeKit unlocked the back door."
- **Use the name *Apple* with the name *HomeKit*, if desired** — ✓ "Compatible with Apple HomeKit."
- **Use the name *HomeKit* for setup, configuration, and instructions, if desired** — ✓ "Open HomeKit settings."
- **Use the app name *Apple Home* whenever referring specifically to the app** — full name on first body-copy mention; later "the Home app". ✓ "Open the Apple Home app." ✗ "Open Home."

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## Specs
Siri phrase → what Siri understands:

| Phrase | Siri understands |
| --- | --- |
| "Turn on the floor lamp" | Service (*floor lamp*) |
| "Show me the entryway camera" | Service (*entryway camera*) |
| "Turn on the light" | Accessory category (*light*) |
| "Turn off the living room light" | Room (*living room*); Accessory category (*light*) |
| "Make the living room a little bit brighter" | Room (*living room*); Accessory category (implied); Brightness characteristic (*brighter*) |
| "Turn on the recessed lights" | Service group (*recessed lights*) |
| "Turn off the lights upstairs" | Accessory category (*lights*); Zone (*upstairs*) |
| "Dim the lights in the bedroom and nursery" | Accessory category (*lights*); Brightness characteristic (*dim*); Rooms (*bedroom*, *nursery*) |
| "Run Good night" | Scene (*Good night*) |
| "Is someone in the living room?" | Accessory category (implied); Occupancy detection characteristic (implied) |
| "Is my security system tripped?" | Accessory category (*security system*) |
| "Did I leave the garage door open?" | Accessory category (*garage door*); Open characteristic (*open*) |
| "Did I forget to turn off the lights in the Tahoe House?" | Accessory category (*lights*); Home (*Tahoe House*) |
| "It's dark in here" | Current home (*here*); Current room (via HomePod); Accessory category (implied) |

## APIs
`HomeKit`, `HMAccessorySetupManager.performAccessorySetup(using:completionHandler:)` (HomeKit)

## Related
siri, app-shortcuts, privacy
