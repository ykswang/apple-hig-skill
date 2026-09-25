# Apple In-App Purchase

> Source: https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase · Lets people pay securely within your app for digital goods and services like premium content and subscriptions; items can also be promoted/offered through the App Store.

## When to use / core idea
- Use In-App Purchase for virtual goods: premium app content, subscriptions to digital content.
- Use **Apple Pay** instead for physical goods (groceries, clothing, appliances), services (club memberships, hotel reservations, event tickets), and donations.
- Four content types:
  - *Consumable* — depletes with use, can be repurchased (lives, gems).
  - *Non-consumable* — doesn't expire (premium features).
  - *Auto-renewable subscriptions* — renew automatically each period until canceled.
  - *Non-renewing subscriptions* — limited-time access (e.g. battle pass); repurchased to extend.
- Advanced Commerce API: for exceptionally large, frequently updated catalogs from multiple creators, or subscriptions with optional add-on content as a single purchase — lets you manage the catalog directly.
- What you can/can't sell: see App Review Guidelines.

## Rules
### Best practices
- **Let people experience your app before making a purchase** — if you offer auto-renewable subscriptions, consider limited free access.
- **Design an integrated shopping experience** — present products and transactions in your app's style; shouldn't feel like a different app.
- **Use simple, succinct product names and descriptions** — titles that don't truncate or wrap; plain, direct language.
- **Display the total billing price for each in-app purchase you offer, regardless of type.**
- **Display your store only when people can make payments** — if they can't (e.g. parental restrictions), consider hiding the store or showing UI explaining why it's unavailable (`canMakePayments`).
- **Use the default confirmation sheet** — system sheet prevents accidental purchases; don't modify or replicate it.

### Supporting Family Sharing
- Family Sharing shares auto-renewable subscriptions and non-consumables with up to five additional family members across their Apple devices.
- **Prominently mention Family Sharing where people learn about your content** — e.g. "Family" or "Shareable" in item/subscription name; mention on sign-up screen.
- **Help people understand the benefits of Family Sharing and how to participate** — when enabled, existing subscribers with sharing off (default) get an Apple notice inviting them to share; family members can be notified of shared content.
- **Aim to customize in-app messaging so it makes sense to both purchasers and family members** — e.g. "Your family subscription includes…" on first view.

### Providing help
- You can present custom help UI that assists, offers alternatives, and initiates the system refund flow (`beginRefundRequest(for:in:)`).
- **Provide help that customers can view before they request a refund** — besides a link to the system refund flow: resolve missing purchases, FAQs, feedback, contact support.
- **Use a simple title for the refund action, like "Refund" or "Request a Refund"** — system flow already makes clear the refund is from Apple.
- **Help people find the problematic purchase** — for each recent purchase show context: product image, name, description, original purchase date.
- **Consider offering alternative solutions** — e.g. immediate fulfillment or a conciliatory item; always make clear they can still request a refund.
- **Make it easy for people to request a refund** — help content must not be a barrier; avoid making people scroll or open another screen to reveal the refund button. Choosing it enters the system refund flow.
- **Avoid characterizing or providing guidance on Apple's refund policies** — don't speculate on outcomes; you may link to Apple's "Request a refund for apps or content that you bought from Apple" support article.

### Auto-renewable subscriptions
- **Call attention to subscription benefits during onboarding** — show value at first launch; strong call to action and clear summary of terms.
- **Offer a range of content choices, service levels, and durations.**
- **Consider letting people try your content for free before signing up** — freemium app, metered paywall, or free trial.
- **Prompt people to subscribe at relevant times, like when they near their monthly limit of free content** — also consider prompts at relevant points throughout the app so they can subscribe any time.
- **Encourage a new subscription only when someone isn't already a subscriber** — otherwise they may think it lapsed. If offered in multiple apps or on your website, provide sign-in so people don't pay twice.

### Making signup effortless
- **Provide clear, distinguishable subscription options** — short, self-explanatory names; price and duration for each. For introductory prices, list the intro price, offer duration, and standard price after the offer ends.
- **Simplify initial signup by asking only for necessary information** — defer extra info until after signup.
- **In your tvOS app, help people sign up or authenticate using another device** — send a code to another device instead of in-app input.
- **Give people more information in your app's sign-up screen** — besides Terms of Service and Privacy Policy links (in app and App Store metadata), the sign-up screen must include:
  - Subscription name, duration, and content/services provided each period.
  - Billing amount, correctly localized for territories and currencies.
  - A way for existing subscribers to sign in or restore purchases.
  - Pattern: billing totals in most prominent positions; per-period breakdowns subordinate for comparison; restore button.
- **Clearly describe how a free trial works** — people must know payment starts automatically when the trial ends; state trial duration and amount billed at the end.
- **Include a sign-up opportunity in your app's settings.**

### Supporting offer codes (iOS, iPadOS)
- Offer codes give new, existing, and lapsed subscribers free/discounted access via online/offline channels (email, events, printed on products).
- *One-time use code*: unique, generated in App Store Connect; redeemable via redemption URL, in-app (if supported), or App Store (prompts install). Consider for small distribution or restricted access.
- *Custom code*: your own (e.g. NEWYEAR, SPRINGSALE); redeemable via redemption URL or in-app only. Consider for large mass-distribution campaigns.
- **Clearly explain offer details** — straightforward, succinct description in marketing materials.
- **Follow guidelines for creating a custom code** — alphanumeric ASCII only; don't use special characters, including Chinese and Arabic characters.
- **Tell people how to redeem a custom code** — can't be redeemed in App Store account settings; point to redemption URL or in-app.
- **Consider supporting offer redemption within your app** — system provides the redemption screens; you only build UI that initiates it, e.g. a "Redeem Code" button on paywall, onboarding, or settings.
- **Supply an engaging and informative promotional image** — optional; defaults to the app icon.
- **Help people benefit from unlocked content as soon as they complete the redemption flow** — welcome new subscribers or tour new features for upgraded ones; be ready for people who subscribe before first opening the app (smooth account creation/sign-in).

### Helping people manage their subscriptions
- In-app management lets people upgrade, downgrade, cancel without leaving the app, and is a natural place for help and alternative offers.
- **Provide summaries of the customer's subscriptions** — especially the upcoming renewal date; consider showing in settings/account screen near the management option (`Product.SubscriptionInfo`).
- **Consider using the system-provided subscription-management UI** (`showManageSubscriptions(in:)`).
- **Encourage a subscriber to keep their subscription or resubscribe later** — on cancel attempt, remind what they'd lose, suggest another plan, or offer a discount; after cancellation consider a personalized discounted resubscribe offer.
- **Always make it easy for customers to cancel an auto-renewable subscription** — don't bury or obscure the manage action.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS.
### watchOS
- Sign-up screen must display the same subscription information as other versions of your app (see Making signup effortless).
- **Clearly describe the differences between versions of your app on different devices** — be straightforward about Watch advantages without implying the experience is identical.
- **Consider using a modal sheet to display the required information** — all required items in one scrolling view; default Close button returns to free content in one tap. If custom view instead, design a complete efficient flow with a Close or Cancel button.
- **Make subscription options easy to compare on a small screen** — compact duration and discount info. Two patterns:
  - One button per option (one-tap start); lock each button up with its description so relation is clear while scrolling.
  - List of options (one per row) followed by a single button whose title updates to reflect the chosen option; minimizes scrolling.

## Specs
- Family Sharing: up to 5 additional family members.
- Custom offer codes: alphanumeric ASCII characters only.

## APIs
In-App Purchase (StoreKit), `AppStore.canMakePayments` (StoreKit), `Transaction.beginRefundRequest(for:in:)` (StoreKit), `AppStore.presentOfferCodeRedeemSheet(from:options:)` (StoreKit), `offerCodeRedemption(options:isPresented:onCompletion:)` (SwiftUI), `Product.SubscriptionInfo` (StoreKit), `AppStore.showManageSubscriptions(in:)` (StoreKit), Retention Messaging API, Advanced Commerce API

## Related
apple-pay, onboarding, sheets, designing-for-watchos, designing-for-tvos
