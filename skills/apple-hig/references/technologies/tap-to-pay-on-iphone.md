# Tap to Pay on iPhone

> Source: https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone · Tap to Pay on iPhone lets merchants accept contactless payments using an app on their iPhone, without external hardware.

## When to use / core idea
- For iOS payment apps; gives merchants a consistent, trusted payment experience. Works alongside existing payment hardware/accessories.
- Prerequisites: a supported payment service provider (PSP), the Tap to Pay on iPhone entitlement, and ProximityReader APIs (directly or via PSP SDK). If the PSP SDK supplies UI (e.g., tap result), follow its docs.
- For reading NFC tags generally, see `nfc`; for in-person ID reading, see `id-verifier`.

## Rules
### Enabling Tap to Pay on iPhone
- Merchant must accept terms and conditions before device configuration; use ProximityReader to check status and show acceptance flow only when needed.
- **Help merchants accept Tap to Pay on iPhone terms and conditions before they begin interacting with their customers** — e.g., acceptance buttons in in-app messaging or onboarding ("Enable Tap to Pay on iPhone", "Try a test transaction").
- **Present Tap to Pay on iPhone terms and conditions only to an administrative user** — nonadmins see a message that admin access is required. For enterprise/nonadmin primary users, admins can accept via web or another app (even on non-iPhone devices); contact your PSP.
- **If necessary, help merchants make sure their device is up to date** — if the PSP requires specific iOS versions, present terms only after the update.

### Educating merchants
- **Provide a tutorial that describes the supported payment types and shows how to use Tap to Pay on iPhone to accept each type** — offer via: Learn More in in-app messaging; automatically after terms acceptance; automatically for new users; a consistent findable place (help or settings).
- Build with Apple-approved assets from the marketing guidelines, or use `ProximityReaderDiscovery` for a pre-built, Apple-maintained, region-localized education experience.
- A custom tutorial must show how to: launch checkout for each payment type; help customers position a contactless card or digital wallet on the device; handle card PIN entry, including accessibility mode.
- At the tutorial's end, let merchants who haven't accepted terms do so.

### Checking out
- Be prepared to: offer other payment options as needed; respond quickly if checkout starts before the feature is enabled; allow checkout while configuration is in progress; present pre-payment actions affecting the total before checkout completes.
- **Provide Tap to Pay on iPhone as a checkout option whether the feature is enabled or not** — on tap, present terms if needed and auto-show the Tap to Pay screen when configuration completes.
- **Avoid making merchants wait to use Tap to Pay on iPhone** — configuration is needed initially per device and each time the app becomes frontmost; prepare at app start and immediately after each foreground transition.
- **Make sure the Tap to Pay on iPhone checkout option is available even if configuration is continuing in the background** — let merchants select it, then show a progress indicator ("Preparing Tap to Pay on iPhone"); usually indeterminate, but determinate if ProximityReader reports ongoing configuration progress.
- **If your app supports multiple payment-acceptance methods, make the Tap to Pay on iPhone button easy to find** — no scrolling; if it's the only method, open Tap to Pay automatically when checkout begins.
- **Make it easy for merchants to switch between Tap to Pay on iPhone and the hardware accessories you support** — consider setting up both at once (e.g., Bluetooth chip-and-PIN reader); let merchants choose the method in checkout without visiting settings.
- **For the label of the button that activates the feature, use "Tap to Pay on iPhone" or, if space is constrained, "Tap to Pay."** — exception: if it's your only acceptance method, reuse existing Charge/Checkout buttons. With icons for multiple methods, use SF Symbols `wave.3.right.circle` or `wave.3.right.circle.fill`. Always avoid the Apple logo in these buttons.
- **Important:** use the "Tap to Pay on iPhone" label only for payment actions.
- **Design your Tap to Pay on iPhone button to match the other buttons in your app** — required label, but color and shape can coordinate with your UI.
- **Determine the final amount that customers need to pay before merchants initiate the Tap to Pay on iPhone experience** — offer tipping or other total-affecting interactions first; aim to show the final amount on the Tap to Pay screen.
- **If you support pre-payment options in your checkout flow, display them before the Tap to Pay on iPhone screen** — e.g., payment-type selection after tapping the button and before opening the Tap to Pay screen.

### Displaying results
- Customers *tap* (bring card/wallet near the screen). On success (and PIN if required), system shows a checkmark and returns an encrypted payment object for your PSP; on failure, an error screen. Your app shows results or alternatives.
- **Start processing a transaction as soon as possible** — request the read result before the checkmark animation finishes.
- **Display a progress indicator while payment is authorizing before you show your transaction result screen** — authorization can take several seconds; show it ("Authorizing") after the Tap to Pay screen animation finishes.
- **Clearly display the result of a transaction, whether it's declined or successful** — declines: insufficient funds, suspected fraud, incorrect PIN. Where possible offer digital receipts (QR code, text message).
- **Help merchants complete the checkout flow when a payment can't complete with Tap to Pay on iPhone** — failures: unreadable card, unsupported network, amount not allowed, no online PIN. Options: new/reused checkout screen for alternate payment (cash); different method (external hardware, payment link); relaunch Tap to Pay for another card.
- Post-read scenarios (consult PSP): Strong Customer Authentication (SCA) regions — issuer may request a PIN after processing request, so show PIN entry instead of result; Offline PIN markets may need extra requirements; some PSPs offer PIN fallback collecting partial tap data to continue with another method (e.g., payment link).
- **If the system returns an error that the merchant must address, display a clear description of the problem and recommend an appropriate resolution** — e.g., alert recommending an iOS update if unsupported.
- **Make it easy for merchants to get help with issues they can't resolve** — link to help content (app/website) and a contact-support action.

### Additional interactions
- Merchants can read a card with no transaction amount (look up past transaction, store card for future payment, refunds, verify customer info).
- **Use a generic label in a button that opens the Tap to Pay on iPhone screen to read a payment card when there's no transaction amount** — no "Tap to Pay on iPhone"/"Tap to Pay"; use "Look Up", "Store Card", "Verify", "Refund".
- Other NFC Wallet items (loyalty, discount, points cards) can be read with a payment card or independently.
- **If your app supports an independent loyalty card transaction, distinguish this flow from a payment-acceptance flow that uses Tap to Pay on iPhone** — separate clearly labeled button (✓ "Loyalty Card"); avoid "Tap to Pay on iPhone", "Tap to Pay", or payment terms in its label (✗ "Tap to Pay on iPhone - Loyalty").

## Platform considerations
No additional considerations: iOS. Not supported in iPadOS, macOS, tvOS, visionOS, or watchOS.

## APIs
`ProximityReader`, `PaymentCardReader.prepare(using:)`, `PaymentCardReader.Event.updateProgress(_:)`, `PaymentCardReader.Event.readyForTap`, `PaymentCardReader.Options.returnReadResultImmediately`, `PaymentCardReaderSession.ReadError`, `ProximityReaderDiscovery` (ProximityReader); SF Symbols `wave.3.right.circle`, `wave.3.right.circle.fill`

## Related
apple-pay, progress-indicators, alerts, sf-symbols, buttons, onboarding, nfc, id-verifier
