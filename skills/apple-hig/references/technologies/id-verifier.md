# ID Verifier

> Source: https://developer.apple.com/design/human-interface-guidelines/id-verifier · ID Verifier lets your iPhone app read mobile IDs in person without external hardware.

## When to use / core idea
- iOS 17+: iPhone reads ISO18013-5 compliant mobile IDs for in-person verification (e.g., venue staff verifying age).
- Customers present only the minimum data needed, without handing over an ID card or showing their device; Apple provides certificate issuance, management, and validation.
- Two request types:
  - **Display Only request** — shows data (e.g., name or age alongside portrait) in system UI on the requester's iPhone for visual confirmation; data is not transmitted to your app.
  - **Data Transfer request** — only when you have a legal verification requirement and must store or process data (address, date of birth); requires an additional entitlement.

## Rules
### Best practices
- **Ask only for the data you need** — asking for more erodes trust; for minimum-age checks use an age-threshold request, avoid requesting current age or birth date.
- **If your app qualifies for Apple Business Register, register for ID Verifier to ensure that people can view essential information about your organization when you make a request** — provides official organization name and logo displayed on customers' devices in the verification UI.
- **Provide a button that initiates the verification process** — label "Verify Age" for a simple age check (e.g., event/venue entry) or "Verify Identity" for more detailed identity data (e.g., matching name and birth date at rental car pickup). Avoid symbols specifying a communication type (NFC, QR codes). Never include the Apple logo in any button label.
- **In a Display Only request, help the person using your app provide feedback on the visual confirmation they perform** — e.g., "Matches Person" / "Doesn't Match Person" buttons so the app receives an approved/rejected value.

## Platform considerations
No additional considerations: iOS. Not supported in iPadOS, macOS, tvOS, visionOS, or watchOS.

## APIs
`MobileDriversLicenseDisplayRequest`, `MobileDriversLicenseDataRequest`, `MobileDriversLicenseRawDataRequest`, `MobileDriversLicenseDataRequest.Element.ageAtLeast(_:)` (ProximityReader)

## Related
wallet, tap-to-pay-on-iphone, privacy
