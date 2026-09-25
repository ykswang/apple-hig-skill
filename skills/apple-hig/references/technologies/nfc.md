# NFC

> Source: https://developer.apple.com/design/human-interface-guidelines/nfc · Near-field communication (NFC) lets devices within a few centimeters of each other exchange information wirelessly.

## When to use / core idea
- iOS apps on supported devices can read electronic tags on real-world objects (connect a toy to a game, scan in-store signs for coupons, track inventory).
- Two modes: in-app tag reading (scanning sheet while app is active, single or multiple objects) and background tag reading (system-initiated).

## Rules
### In-app tag reading
- App displays a scanning sheet whenever people are about to scan.
- **Don't encourage people to make contact with physical objects** — device only needs close proximity; say *scan* and *hold near*, not *tap* or *touch*.
- **Use approachable terminology** — avoid *NFC*, *Core NFC*, *Near-field communication*, *tag*; use friendly conversational terms.

  | Use | Don't use |
  | --- | --- |
  | Scan the [*object name*]. | Scan the NFC tag. |
  | Hold your iPhone near the [*object name*] to learn more about it. | To use NFC scanning, tap your phone to the [*object*]. |

- **Provide succinct instructional text for the scanning sheet** — complete sentence, sentence case, ending punctuation; identify the object; revise for subsequent scans; keep short to avoid truncation.

  | First scan | Subsequent scans |
  | --- | --- |
  | Hold your iPhone near the [*object name*] to learn more about it. | Now hold your iPhone near another [*object name*]. |

### Background tag reading
- On supported devices, system looks for compatible tags whenever the screen is illuminated; on a match it shows a notification people tap to send tag data to the app.
- Unavailable when: an NFC scanning sheet is visible, Wallet or Apple Pay is in use, cameras are in use, device is in Airplane Mode, or device is locked after a restart.
- **Support both background and in-app tag reading** — you must still provide an in-app way to scan for devices without background reading.

## Platform considerations
No additional considerations: iOS, iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.

## APIs
`Core NFC`

## Related
notifications, writing
