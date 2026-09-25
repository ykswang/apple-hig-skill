# Apple Pay

> Source: https://developer.apple.com/design/human-interface-guidelines/apple-pay · Apple Pay is a secure, easy way to pay for physical goods and services, donations, and subscriptions in apps and in any browser.

## When to use / core idea
- Use for physical goods (groceries, clothing, appliances), services (club memberships, hotel reservations, event tickets), donations, and subscriptions. Use **Apple In-App Purchase** instead for virtual goods (premium content) and digital-content subscriptions.
- Flow: Apple Pay button in purchase flow → payment sheet (card, amount incl. tax/fees, shipping options, contact info, other details) → authorize with Face ID, Touch ID, Optic ID, or double-click on Apple Watch. In browsers also via nearby iPhone/Apple Watch or scanning a code with iPhone/iPad.
- Apple Pay mark (graphic) = "we accept Apple Pay"; Apple Pay button = initiates payment. Never swap roles.

## Rules
### Offering Apple Pay
- **Offer Apple Pay on all devices and browsers that support it** — don't present it as an option on unsupported devices.
- **Make Apple Pay the primary payment option when credentials are available** — if you use APIs to check for an active Wallet card, Apple Pay must be primary (not necessarily sole) everywhere you use them; don't separate it into a different step or flow (e.g. pre-select it).
- **Use Apple Pay buttons only to initiate payment or, when appropriate, the Apple Pay setup process** — no other uses. Tapping without Apple Pay set up offers setup.
- **If you use a custom button to start Apple Pay, it must not display "Apple Pay" or the Apple Pay logo** — then show the Apple Pay mark or mention Apple Pay in text on the same page.
- **Use the Apple Pay mark graphic only to communicate that you accept Apple Pay** — never as or positioned like a button; when the mark shows Apple Pay as selected method, a separate custom button matching your design can initiate payment.
- **Don't hide an Apple Pay button or make it appear unavailable** — if it can't be used yet (size/color not selected), point out the problem gracefully after the tap/click.
- **Inform search engines that Apple Pay is accepted on your website** — list it as a payment option in semantic product markup.
- All websites offering Apple Pay must include a privacy statement and follow the Acceptable use guidelines for Apple Pay on the web.

### Streamlining checkout
- **Provide a cohesive checkout experience** — use your branding throughout; avoid opening different pages/windows (on web, new windows can suggest a handoff to another site).
- **If Apple Pay is available, assume people want to use it** — consider showing its button first, larger than other options, or separated by a line.
- **Accelerate single-item purchases with Apple Pay buttons on product detail pages** — purchase only that item, excluding cart contents; if the item is in the cart, remove it after purchase.
- **Accelerate multi-item purchases with express checkout** — immediately shows payment sheet for the whole cart with a single shipping method and destination.
- **Support coupons and promotional codes in the payment sheet** — especially for express checkout.
- **Collect necessary information, like color and size options, before people reach the Apple Pay button** — if missing at checkout, highlight or show warning text and auto-navigate to the problematic field.
- **Collect optional information before checkout begins** — payment sheet can't take optional data (gift messages, delivery instructions); collect before or after purchase.
- **Gather multiple shipping methods and destinations before showing the payment sheet** — sheet supports one method and destination per order.
- **For in-store pickup, help people choose a pickup location before displaying the payment sheet** — then show its address on the sheet (read-only pickup address).
- **Prefer checkout information from Apple Pay** — assume it's complete and current; consider fetching latest even if you have stored info.
- **Avoid requiring account creation before purchase** — ask on the order confirmation page; prepopulate from checkout info.
- **Report transaction results in the payment sheet** — failures (e.g. bad address) get actionable error messages.
- **Display an order confirmation or thank-you page** — thanks, ship timing, how to check status. Listing Apple Pay optional; if shown, after the last four digits or as separate note: "1234 (Apple Pay)" or "Paid with Apple Pay."

### Customizing the payment sheet
- **Only present and request essential information** — e.g. email but no shipping address for an electronically delivered gift card.
- **Display the active coupon or promotional code, or let people enter one** — show pre-entered codes on the sheet; consider in-sheet entry, especially for express checkout.
- **Let people choose the shipping method in the payment sheet** — per option: clear description, cost, optionally estimated delivery/pickup date or range; use calendar and time-zone support for accuracy regardless of location (`PKDateComponentsRange`).
- **For in-store pickup, consider letting people choose a pickup window** — via shipping method date/time ranges.
- **Use line items to explain additional charges, discounts, pending costs, add-on donations, recurring payments, and future payments** — label + cost (recurring can add frequency). Don't use line items to itemize products.
- **Keep line items short** — specific, glanceable, single line where possible.
- **Provide a business name after the word *Pay* on the same line as the total** — same name as on bank/card statement: "Pay [Business_Name]".
- **If you're not the end merchant, identify both businesses** — e.g. "Pay [End_Merchant_Business_Name (via Your_Business_Name)]" for marketplaces, apps, App Clips, websites acting as intermediaries.
- **Clearly disclose when people may incur additional costs after payment authorization** — e.g. distance/time-based rides, tips; where regulations allow, explain in sheet with subtotal marked **Amount Pending**; preauthorized amounts must be accurately reflected.
- **Handle data entry and payment errors gracefully.**
- **Defer to the payment sheet for progress information during payment** — no extra spinners/progress indicators.

### Displaying a website icon
- Websites supporting Apple Pay provide an icon used during payment authorization (notably Handoff to a connected device) and, for subscriptions, in Wallet. Sizes in Specs.

### Handling problems — data validation errors
- Validate when the sheet appears, when certain field values change, and after authentication. System error messages highlight fields; supply customized messages for the detail view.
- Privacy: before authorization only card type and a redacted shipping address are accessible. Display errors when authorization fails, but validate available info and report problems before authorization where possible.
- **Avoid forcing compliance with your business logic** — ignore irrelevant data, infer missing data (e.g. accept Zip+4 by ignoring extra digits; accept phone numbers with/without dashes and country code).
- **Accurately report problems to the system** — custom error message + correct status code (`PKPaymentError`, Apple Pay Status Codes).
- **Explain the problem clearly and succinctly when data is invalid or incorrectly formatted** — reference the field and what's expected: "Zip code doesn't match city", not "Address is invalid"; "Shipping not available for this state". Noun phrases, sentence-style capitalization, no ending punctuation, ≤128 characters.

### Handling problems — payment processing
- **Handle interruptions correctly** — on cancellation/timeout that dismisses the sheet, you must cancel any in-progress payment; people restart via the Apple Pay button.

### Supporting subscriptions
- Recurring payments: fixed (monthly movie subscription) or, where regulations allow, variable (weekly groceries); initial authorization may include discounts and fees.
- **Clarify subscription details before showing the payment sheet** — billing frequency and terms; frequency can also appear on the sheet.
- **Include line items that reiterate billing frequency, discounts, and additional upfront fees** — if no payment at authorization, clearly disclose when billing occurs.
- **Clearly communicate trial period terms** — line items for trial amount (including $0 if free), regular amount after trial, and date regular billing begins.
- **Clarify the current payment amount in the total line.**
- **Only show the payment sheet when a subscription change results in additional fees** — no authorization if cost decreases or stays the same.
- Billing agreement field: a concise plain-language summary, not a substitute for formal terms; don't duplicate info; when in doubt leave blank.

### Supporting donations
- Only approved nonprofits can accept donations.
- **Use a line item to identify a donation** — e.g. "Donation $50.00".
- **Streamline checkout by offering predefined donation amounts** — e.g. $25, $50, $100, plus an Other Amount option.

### Using Apple Pay buttons
- API-generated buttons give Apple-approved captions/fonts/colors/styles, proportional scaling, automatic localization, corner radius customization, built-in VoiceOver alt text.
- **Always use the Apple-provided API to display Apple Pay buttons** — don't create custom Apple Pay button designs or replicate them.
- Use the Apple Pay mark wherever you highlight payment options.

#### Button types (choose to match your flow's terminology)
| Button | Use for |
|---|---|
| Buy with Apple Pay | Purchase areas like product detail or shopping cart pages |
| Pay with Apple Pay | Paying bills/invoices (utilities, plumbing, car repair) |
| Check Out with Apple Pay | Carts where other payment buttons start with *Check Out* |
| Continue with Apple Pay | Carts where other payment buttons start with *Continue* |
| Book with Apple Pay | Booking flights, trips, experiences |
| Donate with Apple Pay | Approved nonprofits accepting donations |
| Subscribe with Apple Pay | Subscriptions (gym membership, meal kit) |
| Reload / Add Money / Top Up with Apple Pay | Adding money to a card/account/payment system (transit, prepaid phone) — match the term your app uses |
| Order with Apple Pay | Ordering meals, flowers, etc. |
| Rent with Apple Pay | Renting cars, scooters, etc. |
| Support / Contribute with Apple Pay | Giving money to projects, causes, organizations — match the term your app uses |
| Tip with Apple Pay | Tipping for goods or services |
| Apple Pay (plain) | Stylistic need for smaller minimum width or no call to action; system may substitute it for a type unsupported on the running OS |

- In some contexts the system shows the default card image on payment buttons, signaling Apple Pay is ready.
- **Set Up Apple Pay** button: when the device supports Apple Pay but it isn't set up; shows acceptance and offers explicit setup. Display in Settings, a user profile, or an interstitial page.

#### Button styles
- *Automatic*: system appearance decides (`PKPaymentButtonStyle.automatic`, `ApplePayButtonStyle`).
- *Black*: on white/light backgrounds with sufficient contrast; not on black/dark backgrounds.
- *White with outline*: on white/light backgrounds without sufficient contrast; not on dark or saturated backgrounds.
- *White*: on dark backgrounds with sufficient contrast (not on light backgrounds).

#### Button size and position
- **Prominently display the Apple Pay button** — no smaller than other payment buttons; don't make people scroll to see it.
- **Position the Apple Pay button correctly in relation to an Add to Cart button** — side-by-side: Apple Pay to the right; stacked: Apple Pay above.
- **Adjust the corner radius to match other buttons** — default rounded; can be square or capsule (`cornerRadius`).
- **Maintain the minimum button size and margins around the button** — titles vary by locale. If the size can't fit the translated title, the system substitutes the plain Apple Pay button; no automatic replacement for Set Up Apple Pay.

#### Apple Pay mark
- Shows Apple Pay as an available option alongside other payment options; not a button.
- **Use only the artwork provided by Apple, with no alterations other than height** — height ≥ other payment brand marks in the flow; don't change width, corner radius, aspect ratio; no trademark symbol or added content; don't remove the border; no shadows, glows, reflections; don't flip, rotate, animate.
- **Maintain a minimum clear space around the mark of 1/10 of its height** — don't share its border with another graphic or button.
- Download mark and full guidelines from Apple Pay Marketing Guidelines.

### Referring to Apple Pay
- Use exactly as in the Apple Trademark List; never plural or possessive; follow Guidelines for Using Apple Trademarks.
- **Capitalize Apple Pay as in the Apple Trademark List** — two words, uppercase *A* and *P*, rest lowercase; all caps only to conform to an established all-caps typographic style.
- **Never use the Apple logo to represent the name *Apple* in text** — in the US use ® the first time Apple Pay appears in body text; no ® when it's a selection option during checkout.
  - ✅ "Purchase with Apple Pay", "Purchase with Apple Pay®"; ❌ "ApplePay", "[Apple logo] Pay", "APPLE PAY" (unless all-caps style).
- **Coordinate the font face and size with your app or website** — don't mimic Apple typography.
- **Don't translate *Apple Pay* or any other Apple trademark** — always English.
- **In a payment selection context, text-only Apple Pay is allowed only when all payment options are text-only** — if any option has an icon/logo, use the Apple Pay mark.
- **When promoting Apple Pay in an app, follow App Store guidelines** (App Store marketing guidelines).

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, visionOS, watchOS. Not supported in tvOS.

## Specs
Website icon:

| @2x | @3x |
|---|---|
| 60x60 pt (120x120 px @2x) | 60x60 pt (180x180 px @3x) |

Apple Pay button minimums:

| Button | Minimum width | Minimum height | Minimum margins |
|---|---|---|---|
| Apple Pay | 100pt (100px @1x, 200px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of button height |
| Book / Buy / Check Out / Donate / Set Up / Subscribe with Apple Pay | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of button height |

- Apple Pay mark clear space: 1/10 of its height.
- Validation error messages: ≤128 characters.

## APIs
`Apple Pay` (PassKit), `Apple Pay on the Web` (applepayontheweb), `PKPaymentAuthorizationController` (PassKit), `applePayCapabilities` (applepayontheweb), `Offering Apple Pay in Your App` (PassKit), `Checking for Apple Pay availability` (applepayontheweb), `Displaying a Read-Only Pickup Address` (PassKit), `PKDateComponentsRange` (PassKit), `paymentSummaryItems` (PassKit), `PKPaymentAuthorizationViewControllerDelegate` (PassKit), `PKPaymentError` (PassKit), `Apple Pay Status Codes` (applepayontheweb), `oncancel` (applepayontheweb), `PKPaymentButtonType` (PassKit), `PKPaymentButtonStyle` (PassKit), `WKInterfacePaymentButton` (watchkit), `PKPaymentButtonStyle.automatic` (PassKit), `ApplePayButtonStyle` (applepayontheweb), `cornerRadius` (PassKit)

## Related
apple-in-app-purchase, app-clips, wallet, buttons
