# Wallet

> Source: https://developer.apple.com/design/human-interface-guidelines/wallet · Wallet securely stores credit/debit cards, driver's license or state ID, transit cards, event tickets, keys, and more on iPhone and Apple Watch.

## When to use / core idea
- Integrate Wallet to create custom passes and present them when needed, verify identity (Verify with Wallet) for access to personal content, and show receipts/order tracking.
- Passes = digital event tickets, boarding passes, membership/reward cards, coupons.
- Order tracking = Wallet shows orders placed via your app/website (Apple Pay), updated as status changes; iOS 17+ lets people start tracking from your app/website.
- Identity verification (iOS 16+) = app or App Clip reads ID card info in Wallet without leaving context. For in-person mobile ID verification use `id-verifier`.
- Payments themselves: see `apple-pay`.

## Rules
### Passes
- **Offer to add new passes to Wallet** — when an action creates a pass (ticket purchase, reward sign-up), present system UI that adds with one tap. For frequent, predictable actions (flight check-in), add passes in the background after one-time authorization. Wallet notifies the person whenever a pass is added. To let people review first, show a custom view with an Add to Apple Wallet button.
- **Help people add a pass created outside your app** — if created on your website or another device, suggest adding it next time they open the app. If they decline, don't ask again.
- **Add related passes as a group** — e.g., all boarding passes for a multi-connection flight at once; bundle website-distributed groups (event tickets) for one download.
- **Display an Add to Apple Wallet button to let people add an existing pass not already in Wallet** — for passes declined earlier or removed; show it wherever corresponding pass info appears. An Add to Apple Wallet badge exists for emails/webpages.
- **Let people jump from your app to their pass in Wallet** — link labeled like "View in Wallet."
- **Tell the system when your passes expire** — Wallet auto-hides expired passes (with a button to revisit); set expiration date, relevant date, and voided properties correctly.
- **Always get permission before deleting passes from Wallet** — e.g., in-app setting for manual vs. automatic removal; show an alert before deleting if necessary.
- **Help the system suggest a pass when relevant** — provide when/where relevance so the system shows a Lock Screen link (gym card on entering the gym). For some pass types (event tickets) the system can start a Live Activity.
- **Keep passes up to date** — e.g., boarding pass auto-updates for delays and gate changes.
- **Use change messages only for updates to time-critical information** — they interrupt people (gate change yes; customer service number change no). Never use for marketing or noncritical communication. Change messages are per-field.

### Pass anatomy
- Content/structure = pass fields (what appears and how it's arranged) + semantic tags (describe content to system; enable surfacing at the right time and featured actions — quick links like venue directions or event guides).
- Poster event tickets and semantic boarding passes: semantic tags are required and enable automatic layout. Still include pass fields so passes display correctly on older iOS.
- Supplemental info can go in sheets linked from the pass front; the back holds rarely needed settings/info (legal text).
- Pass field areas:
  - Logo and logo text: brand icon and name; visible when pass is collapsed.
  - Header: critical info; visible when collapsed.
  - Primary: most important info.
  - Secondary and auxiliary: useful but less critical.
  - Footer: supplemental info such as pass category ("Family", "Annual").
  - Back: supplemental details shown in pass details in Wallet.
- Layout varies by pass style.

### Designing passes
- Design a clean, simple pass that feels at home in Wallet rather than replicating the physical counterpart. Pass Designer (Mac) designs/previews passes from templates or blank: boarding passes, coupons, event tickets, store cards, generic, poster generic.
- **Design a pass that looks great and works well on all devices** — Apple Watch shows less info and fewer images; don't put essential info in elements that may be unavailable; avoid padding images (watchOS crops white space from some images).
- **Keep the pass front uncluttered** — essential info (event date, account balance) in the header so it's visible when collapsed; rest of front for quick-access info; rarely needed details on the additional pass information sheet.
- **Make your pass instantly identifiable** — brand colors, images, icons, full-art backgrounds.
- **Ensure sufficient contrast between background and text colors** — label colors legible on both solid backgrounds and background images.
- **Use language that works on any device** — e.g., "Slide to view" works on iPhone, not Apple Watch.

### Pass styles
- **Boarding passes** — travel tickets (airline, train, bus, boat, generic transit); typically one trip with start/end. Use semantic tags for airline boarding passes; pass fields for all other transit.
- **Coupons** — coupons, special offers, discounts.
- **Event tickets** — sporting events, concerts, movies, plays; usually one event, or one pass for many (season ticket). Poster style supports full-art background. Non-poster event tickets use standard pass fields and can use a background image and thumbnail.
- **Store cards** — loyalty, discount, points, gift cards; usually display balance if the account carries one.
- **Poster generic passes** — full background image and distinct field layout; not category-bound; use when no other style fits.
- **Generic passes** — anything else (gym membership, coat-check ticket).

### Pass images
- Create pass images as PNG at @2x and @3x.
- **Reserve pass images for visual content** — embedded text isn't accessible and may not show on all devices; use text fields and semantic tags for text. Add barcodes via Pass Designer or APIs, not embedded in images.
- **Keep image file sizes small** — passes arrive via email/web; smallest files that still look great.
- **Provide a pass icon** — used on Lock Screen, in Mail, and on passes in Wallet; app icon or separate design.
- Logo: top-leading corner of pass-field passes; typically a horizontal text logo, optionally with a graphic. **Avoid inner drop shadows on logo artwork** — reduces legibility.
- Primary logo: top-leading corner, semantic passes only.
- Secondary logo: issuer/organizer logo in the bottom-trailing corner of poster event tickets.
- Icon: square; system applies rounded corners — don't round them yourself.
- Strip image: coupons and store cards; text may overlay — ensure contrast, keep areas behind text uncluttered, place important visuals toward bottom or trailing edge, avoid embedding text.
- Thumbnail: small image (e.g., movie poster) on event tickets and generic passes; square — use rounded corners on artwork, export as transparent PNG.
- Background: visual centerpiece. Poster passes: keep content in the safe area — a material strip covers the bottom edge on poster generic passes and poster event tickets; account for any barcode; verify in Pass Designer (`footerBackgroundColor`).
- Footer image: airline boarding passes only.

### Order tracking
- Wallet dashboard shows active and completed orders; details include items and shipping/pickup fulfillment. Wallet Orders schema supplies product descriptions, status, contact info, shipping/pickup details (ETA, addresses, tracking numbers, pickup instructions). Supply as much info as matches your process.
- **Make it easy for people to add an order to Wallet** — after an Apple Pay transaction, use `PKPaymentOrderDetails` (app) / `ApplePayPaymentOrderDetails` (web) to add automatically. iOS 17+: `AddOrderToWalletButton` shows the Track with Apple Wallet button on order confirmation/status/tracking pages or in emails. Re-adding an existing order opens it in Wallet.
- **Make information about an order available immediately after people place it** — provide what you have; use a status description like "Check back later for full order details."
- **Provide fulfillment information as soon as it's available, and keep the status up to date** — system updates and can notify. Statuses: Order Placed, Processing, Ready for Pickup, Picked Up, Out for Delivery, Delivered, Issue, Canceled.
- **Supply a high-resolution logo image that uses a nontransparent background** — PNG or JPEG, 300x300 px; shown in dashboard and detail view.
- **Supply distinct, high-resolution product images that use nontransparent backgrounds** — straightforward depiction on solid background (no "lifestyle" or busy backgrounds); PNG or JPEG, 300x300 px; shown in detail views, dashboard, notifications.
- **In general, keep text brief** — system may truncate.
- **Use clear, approachable language, and localize the text you provide** — shown price must match the final confirmed price.

### Displaying order and fulfillment details
- **Provide a link to an area where people manage their order** — universal link works without app installed.
- **Clearly describe each item so people can verify that their order contains everything they expect** — `LineItem` (price, name, image). Order lists all line items; a fulfillment lists only its own. Can attach a PDF receipt to an individual transaction.
- **Supply a prioritized list of your apps that might be installed on the device** — system links to highest-listed installed app; if none installed, links to the first app on the list.
- **Avoid sending duplicate notifications** — e.g., suppress Wallet order notifications when one of your associated apps is installed.
- **Make it easy for customers to contact the merchant** — minimum: link to merchant website/landing page; optionally Messages for Business link, phone, email, support page. Contact button shows a menu of these.
- **Help people track their order** — multi-item orders can have multiple fulfillments (each shipping or pickup). Supply where items are and when to expect them, plus ETA and:
  - Direct carrier-website tracking link (in addition to tracking number); show it on any intermediate tracking page.
  - Scannable barcode when required for pickup, available in Wallet.
  - Clear, detailed receive/pickup instructions.
- **Keep the fulfillment screen centered on order tracking** — prioritize tracking over promos for your app/services.
- **Choose shipping-fulfillment values that match the details you have about the shipping process** — known carrier → `carrier` property; else leave default "Track Shipment". With interim carrier details use `onTheWay`, `outForDelivery`, `delivered`; without them use `shipped`. Provide a tracking link when available.
- **Keep customers informed through relevant fulfillment status descriptions** — approachable, accurate, clearly related to the status; can use brand voice.
- **Be direct and thorough when describing an Issue or Canceled status** — say why and what people can do.

### Identity verification
- Apple doesn't create or see ID documents; your app receives only encrypted data not readable on device.
- Verify with Wallet button reveals a sheet describing the request; people agree to share or cancel.
- **Present a Wallet verification option only when the device supports it** — don't show the button if the device can't return the requested info; have a fallback view with another verification method.
- **Ask for identity information only at the precise moment you need it** — when completing the process/transaction requiring it; not before people are ready or at simple account creation.
- **Clearly and succinctly describe the reason you need the information you're requesting** — required purpose string (usage description) shown in the sheet. Brief, complete sentence; direct, specific, easy to understand; sentence case; no passive voice; end with a period.
- **Ask only for the data you actually need** — e.g., request an age threshold (`age(atLeast:)`) rather than current age or birth date.
- **Clearly indicate whether you will keep the data and — if you need to keep it — specify how long you'll do so** — specify duration via PassKit (period, indefinitely, or only for the current verification); system shows explanatory content (`PKIdentityIntentToStore`).
- **Choose the system-provided verification button that matches your use case and the visual design of your app** — see table. All labels have a multiline variant used automatically when horizontal space is constrained. Button always white letters on black; optional light-outline style for dark backgrounds; `cornerRadius` adjustable to match related buttons.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, visionOS. Not supported in tvOS.

### watchOS
- Passes appear in a scrolling carousel of cards; people can add your pass to Apple Watch even without a watch app.
- Tapping a pass reveals a scrolling details screen; sometimes a specific transaction can be tapped for more.
- Basic layout: row 1 = logo image + essential field area; row 2 = primary field area; row 3 = secondary and auxiliary fields. Overflow goes to the details screen.
- In every style, watchOS crops the strip image to the card's aspect ratio and may crop white space from other images.
- Per style layout:
  - Boarding: logo + departure/boarding time; origin/destination; passenger name + seat.
  - Coupon: logo + expiration date; strip image; row 3 unused.
  - Store: logo + unused area; strip image; member name + number.
  - Event: logo + event start date; event info; attendee name + seat location.
  - Generic: logo + expiration date; strip image; name + number.

## Specs
### Pass images (PNG, @2x and @3x)
| Image | Supported pass styles | Filename | Width | Height |
| --- | --- | --- | --- | --- |
| Logo | Non-semantic airline boarding passes, non-airline boarding pass styles, coupons, non-poster event tickets, generic passes, store cards | logo.png | min 50 pt, max 160 pt | 50 pt |
| Primary logo | Airline boarding passes, poster event tickets, poster generic passes | primaryLogo.png | min 30 pt, max 126 pt | 30 pt |
| Secondary logo | Poster event ticket | secondaryLogo.png | min 12 pt, max 135 pt | 12 pt |
| Icon | All | icon.png | 38 pt | 38 pt |
| Strip image | Coupon, store card | strip.png | 375 pt | 144 pt |
| Thumbnail | Event ticket, generic pass | thumbnail.png | min 60 pt, max 90 pt | 90 pt |
| Background (non-poster) | Event tickets | background.png | 343 pt | 503 pt |
| Background (poster) | Poster event tickets, poster generic passes | artwork.png | 358 pt | 448 pt |
| Footer | Airline boarding passes | footer.png | 268 pt | 15 pt |

### Order images
- Merchant logo: PNG or JPEG, 300x300 px, nontransparent background.
- Product image: PNG or JPEG, 300x300 px, nontransparent solid background.

### Purpose string examples
| To verify… | To support… | Example purpose string |
| --- | --- | --- |
| Identity | Opening an account for which proof of identity is legally required to prevent fraud | Federal law requires this information to verify your identity and also to help [App Name] prevent fraud. |
| Driving privilege | Renting a vehicle that requires legal driving privileges | Applicable state law requires [App Name] to verify your driving privileges. |

### Verification button labels
| Button type | Consider using when… |
| --- | --- |
| Verify Age with Apple Wallet | App can complete the transaction after verifying age (e.g., making a car available to lease). |
| Verify Identity with Apple Wallet | App can complete the transaction after verifying identity (e.g., car rental). |
| Continue with Apple Wallet | Verify with Wallet is one part of a process that also needs info it doesn't provide (e.g., Social Security number, phone number) — opening a financial account, background check. |
| Verify with Apple Wallet | App completes verification without additional steps, but "Verify Age," "Verify Identity," and "Continue" labels don't fit (e.g., signing up for a government service). |

## APIs
`addPasses(_:withCompletionHandler:)`, `PKPassLibrary.Capability.backgroundAddPasses`, `PKAddPassesViewController`, `PKAddPassButton` (PassKit); `Pass` (Wallet Passes: expirationDate, relevantDate, voided, footerBackgroundColor); Wallet Orders (`Order`, `Merchant`, `LineItem`, `ShippingFulfillment`); `PKPaymentOrderDetails` (PassKit), `ApplePayPaymentOrderDetails` (Apple Pay on the Web); `AddOrderToWalletButton` (FinanceKitUI); `VerifyIdentityWithWalletButton`, `PKIdentityButton.Label`, `PKIdentityButton.Style.blackOutline`, `PKIdentityButton.cornerRadius`, `PKIdentityElement.age(atLeast:)`, `PKIdentityIntentToStore` (PassKit); FinanceKit.

## Related
`apple-pay, id-verifier, live-activities`
