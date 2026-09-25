# Privacy

> Source: https://developer.apple.com/design/human-interface-guidelines/privacy · Be transparent about the privacy-related data and resources you require and protect the data people allow you to access.

## When to use / core idea
- Applies to any app collecting personal data, requesting permissions, tracking, handling authentication, or storing sensitive info.
- App Store submissions must declare privacy practices and privacy-relevant data collected (managed in App Store Connect); shown on the product page ("Data Used to Track You", "Data Linked to You").
- Permission flow = system alert with your purpose string; optional pre-alert custom screen; location button as a lightweight alternative for one-time location.
- Related: sign-in-with-apple, managing-accounts, onboarding, entering-data.

## Rules

### Best practices
- **Request access only to data that you actually need** — asking for more than a feature needs, or before people show interest in the feature, erodes trust. Make requests as specific as possible for precise control.
- **Be transparent about how your app collects and uses people's data** — always respect choices like Hide My Email and Mail Privacy Protection; understand your app-tracking obligations.
- **Process data on the device where possible** — e.g., Apple Neural Engine and custom CreateML models in iOS avoid lengthy, risky server round trips.
- **Adopt system-defined privacy protections and follow security best practices** — e.g., iOS 15+ CloudKit provides encryption and key management for more data types (strings, numbers, dates).

### Requesting permission
- Must request permission for: personal data (location, health, financial, contact, other PII); user-generated content (emails, messages, calendar, contacts, gameplay info, Apple Music activity, HomeKit data, audio/video/photo); protected resources (Bluetooth peripherals, home automation, Wi-Fi connections, local networks); device capabilities (camera, microphone); in visionOS Full Space, ARKit data (hand tracking, plane estimation, image anchoring, world tracking); the advertising identifier (app tracking).
- System shows a standard alert with your description; people can review and change choices in Settings > Privacy.
- **Request permission only when your app clearly needs access to the data or resource** — ideally wait until people use a feature requiring it (e.g., location button after they show interest).
- **Avoid requesting permission at launch unless the data or resource is required for your app to function** — OK when the reason is obvious (navigation app needs location; visionOS game bouncing objects off walls needs surroundings data).
- **Write copy that clearly describes how your app uses the ability, data, or resource you're requesting** — the *purpose string* / *usage description string* appears after the app name, before the grant/deny buttons. Brief, complete sentence; straightforward, specific, easy to understand; sentence case; avoid passive voice; end with a period.

| | Example purpose string | Notes |
| --- | --- | --- |
| Correct | The app records during the night to detect snoring sounds. | Active sentence clearly describing how and why data is collected. |
| Incorrect | Microphone access is needed for a better experience. | Passive, vague, undefined justification. |
| Incorrect | Turn on microphone access. | Imperative, no justification. |

- Alert button examples: location — Allow Once / Allow While Using App / Don't Allow (with Precise On map); photos — Select Photos / Allow Access to All Photos / Don't Allow; contacts — Don't Allow / Allow.

### Pre-alert screens, windows, or views
- Ideally context explains the request; if essential, show a custom screen before the system alert (applies to camera, microphone, location, contact, calendar, tracking).
- **Include only one button and make it clear that it opens the system alert** — a second button that doesn't open the alert feels manipulative; don't title it "Allow" (similar meaning/weight to the alert's allow button leads to accidental grants). Use "Continue" or "Next".
- **Don't include additional actions in your custom screen or window, unless needed to obtain a legal consent** — e.g., no close or cancel option that leaves without viewing the system alert.

### Tracking requests
- To track as soon as the app launches, you must display the system alert before collecting any tracking data. A custom screen describing tracking benefits can make sense in some cases.
- **Never precede the system-provided alert with a custom screen or window that could confuse or mislead people** — exploiting quick-dismiss behavior leads to App Store rejection.
- Prohibited pre-tracking designs (cause rejection): offering incentives (e.g., "$100 credit"), a screen that looks like a request (imitation "Allow Tracking" button), displaying an image of the alert, annotating the screen behind the alert (e.g., arrow + "Choose Allow").
- Allowed: a consent screen before or after the App Tracking Transparency alert to comply with local privacy laws (App Review Guidelines 5.1.1 (iv)).

### Location button (iOS, iPadOS, watchOS)
- Core Location button grants temporary authorization at the moment a task needs it; appearance can match your UI but is always instantly recognizable.
- First tap shows a standard alert explaining the limited access and the location indicator; afterward each tap grants one-time permission without reconfirmation (each one-time authorization expires when people stop using the app).
- No authorization status → tap = *Allow Once*. If people previously chose *While Using the App*, tapping doesn't change status.
- **Consider using the location button to give people a lightweight way to share their location for specific app features** — attach location to a message/post, find a store, identify a building/plant/animal. If people often grant *Allow Once*, the button avoids repeated alerts.
- **Consider customizing the location button to harmonize with your UI** — you can: choose a system-provided title (e.g., "Current Location", "Share My Current Location"); choose filled or outlined glyph; select background color and title/glyph color; adjust corner radius. Other visual attributes aren't customizable.
- System warns about low-contrast colors or too much translucency; you must fix those and ensure text fits without truncation at all accessibility text sizes and in all localizations.
- If the system identifies consistent problems with a customized button, tapping it won't grant location access (it can still do other app actions, but people may lose trust).

### Protecting data
- Use system security technologies for local storage, authorization, and network transport.
- **Avoid relying solely on passwords for authentication** — use passkeys where possible; if keeping passwords, require two-factor authentication; protect kept-logged-in apps with Face ID, Optic ID, or Touch ID.
- **Store sensitive information in a keychain.**
- **Never store passwords or other secure content in plain-text files** — even with restricted file permissions; use the encrypted keychain.
- **Avoid inventing custom authentication schemes** — prefer passkeys, Sign in with Apple, or Password AutoFill.

## Platform considerations
No additional considerations: iOS, iPadOS, tvOS, watchOS.

### macOS
- **Sign your app with a valid Developer ID** — when distributing outside the store; identifies you as an Apple developer and confirms the app is safe.
- **Protect people's data with app sandboxing** — required for all Mac App Store apps.
- **Avoid making assumptions about who is signed in** — fast user switching means multiple people may be active.

### visionOS
- ARKit algorithms (persistence, world mapping, segmentation, matting, environment lighting) always run; apps benefit automatically in the Shared Space, but ARKit sends no data to Shared Space apps — ARKit APIs require a Full Space.
- Plane Estimation, Scene Reconstruction, Image Anchoring, and Hand Tracking require permission.
- Input is private by design: system hover effects on SwiftUI/RealityKit interactive components give feedback without exposing gaze before a tap.
- Cameras: back camera provides blank input (compatibility only); front camera feeds spatial Personas only after permission. Remove camera-dependent features from ported iOS/iPadOS apps or replace them with an import-content option.

## APIs
`LocationButton` (SwiftUI / CoreLocationUI), `CLLocationButton` (CoreLocationUI), App Tracking Transparency, Requesting access to protected resources (UIKit), Requesting authorization to use location services (CoreLocation), Keychain services (Security), Local Authentication, passkeys / Securing Logins with iCloud Keychain Verification Codes (AuthenticationServices), Password AutoFill, CloudKit, CreateML, Configuring the macOS App Sandbox (Xcode), Setting up access to ARKit data (visionOS), Making your existing app compatible with visionOS

## Related
entering-data, onboarding, sign-in-with-apple, managing-accounts, eyes, gestures, shareplay, alerts
