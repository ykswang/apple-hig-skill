# Sign in with Apple

> Source: https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple · Sign in with Apple provides a fast, private way to sign into apps and websites with a consistent, trusted experience and no extra accounts or passwords.

## When to use / core idea
- People use their existing Apple Account to sign in/up, skipping forms, email verification, and passwords. If you ask for name/email, people can share a unique random relay email that forwards to their personal address.
- Offer it in every version of your app/website on all platforms, including non-Apple platforms.
- Authenticates with Face ID, Touch ID, or Optic ID; two-factor built in. Apple doesn't use it to profile people or their app activity.

## Rules
### Offering Sign in with Apple
- **Ask people to sign in only in exchange for value** — briefly describe benefits (personalization, additional features, data sync).
- **Delay sign-in as long as possible** — let people explore first (e.g., browse streaming content before signing in to stream).
- **If you require an account, ask people to set it up before offering any sign-in options** — explain why first; after setup, offer Sign in with Apple and other methods.
- **Consider letting people link an existing account to Sign in with Apple** — before or after sign-in: suggest linking if the shared email matches an existing account; or show a linking suggestion in account settings for username/password users.
- **In a commerce app, wait until after people make a purchase before asking them to create an account** — with guest checkout, offer quick account creation after the transaction (e.g., on the Apple Pay order confirmation page); don't re-ask for name/email already provided in Apple Pay.
- **As soon as Sign in with Apple completes, welcome people to their new account** — don't delay with non-required info requests.
- **Indicate when people are currently signed in** — e.g., "Using Sign in with Apple" in settings/account UI.

### Collecting data
- Minimize data requests during account setup; explain why you need additional data and clearly display what you receive.
- **Clarify whether the additional data you request is required or just recommended** — legally/contractually required (terms of service agreement, country/region, birth date, real-identity law info): make clear it's needed to finish setup. Optional: say so and explain benefits.
- **Don't ask people to supply a password** — unless they've stopped using Sign in with Apple with your app/website.
- **Avoid asking for a personal email address when people supply a private relay address** — for email-based identification (customer service, retail): let people view their relay address in your app/site; direct them to Settings > Apple Account > Password & Security > Apps using Apple Account; or use other identifiers (order number, phone number from purchase).
- **Give people a chance to engage with your app before asking for optional data** — e.g., phone for real-time text updates, social network for games with friends; declining must not block account access or any features.
- **Be transparent about the data you collect** — e.g., welcome people using the shared name or email (shows where a relay address appears); if you don't display data people provided, they'll wonder why you asked.

### Displaying buttons
- **Prominently display a Sign in with Apple button** — no smaller than other sign-in buttons; avoid requiring scrolling to see it.

#### System-provided buttons
- Advantages: Apple-approved appearance; ideal proportions across styles; automatic title localization; configurable corner radius (iOS, macOS, web); system alt text for VoiceOver.
- Titles (iOS, macOS, tvOS, web): *Sign in with Apple*, *Sign up with Apple*, *Continue with Apple*. watchOS: *Sign in*. Choose the variant matching your terminology and use it consistently.
- Appearances (up to three, by platform) — choose per background:
  - **White** — all platforms and web; use on dark backgrounds with sufficient contrast (not on light backgrounds).
  - **White with outline** — iOS, macOS, web; use on white/light backgrounds lacking contrast with white fill; avoid on dark or saturated backgrounds (outline adds clutter) — use White there.
  - **Black** — all platforms and web; use on white/light backgrounds with sufficient contrast; don't use on black or dark backgrounds.
  - watchOS "black" button uses the system-defined dark gray fill (not fully black) to contrast with Apple Watch's pure black background.
- **Adjust the corner radius to match the appearance of other buttons in your app** — default rounded; in iOS, macOS, web can be square-cornered or capsule.
- **Maintain the minimum button size and margin around the button in iOS, macOS, and the web** — title length varies by locale (see Specs).

#### Creating a custom Sign in with Apple button
- Allowed for iOS, macOS, or web when needed (align logos across sign-in buttons, logo-only buttons, custom font/bezel/background).
- Always make it instantly identifiable as Sign in with Apple; App Review evaluates all custom buttons.
- Use only logo artwork from Apple Design Resources (PNG, SVG, PDF; black and white; logo-only and logo+text variants, with built-in padding); never create a custom Apple logo.
  - Use the logo file to position the logo in a button; never use the Apple logo as a button.
  - Match logo file height to button height.
  - Don't crop the logo file.
  - Don't add vertical padding.
- Don't change: **titles** (only *Sign in with Apple*, *Sign up with Apple*, *Continue with Apple*); **general shape** (logo+text always rectangular; logo-only circular or rectangular); **logo and title colors** (both black or both white; no custom colors).
- May change: title font (incl. weight/size); title case (all caps allowed); background (must stay overall black or white; subtle texture/gradient OK); corner radius (match other buttons); bezel and shadow (stroke, drop shadow).

##### Custom buttons with a logo and text
- **Choose the format of the logo file based on the height of your button** — SVG/PDF for any height; PNG only for 44 pt-tall buttons (iOS default and recommended). Logos in small, medium, large to match other sign-up buttons.
- **Prefer the system font for the title** — whatever the font, keep system proportions: font size = 43% of button height (button height = 233% of font size, rounded to nearest integer). Examples: 44 pt button / 19 pt font; 56 pt button / 24 pt font.
- **In general, preserve the capitalization style of the title** — capitalize first word (*Sign*/*Continue*) and *Apple*, rest lowercase; avoid changing unless your UI is all uppercase.
- **Keep the title and logo vertically aligned within the button** — vertically center the title, then add the logo with height matching the button (padding built in).
- **Inset the logo if necessary** — adjust leading space to align with other authentication logos.
- **Maintain a minimum margin between the title and the right edge of the button** — at least 8% of button width.
- **Maintain the minimum button size and margin around the button** — see Specs.

##### Custom logo-only buttons
- **Choose the format of the logo file based on the size of your button** — SVG/PDF any size; PNG only for 44x44 pt buttons.
- **Don't add horizontal padding to a logo-only image** — always 1:1 aspect ratio; padding already included.
- **Use a mask to change the default square shape of the logo-only image** — e.g., circle or rounded rect; never crop the artwork to reduce padding or use the bare logo; avoid extra padding.
- **Maintain a minimum margin around the button** — at least 1/10 of the button's height.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## Specs
Minimum sizes (system buttons in iOS, macOS, web; and custom logo+text buttons):

| Minimum width | Minimum height | Minimum margin |
| --- | --- | --- |
| 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button's height |

- Custom logo+text: title font size 43% of button height (height 233% of font size, rounded); e.g., 44 pt → 19 pt, 56 pt → 24 pt. Title-to-right-edge margin ≥ 8% of button width. PNG logos only at 44 pt height.
- Custom logo-only: 1:1 aspect ratio; PNG only at 44x44 pt; margin ≥ 1/10 of button height.

## APIs
`Authentication Services`, `ASAuthorizationAppleIDButton` + `cornerRadius` (AuthenticationServices; iOS, macOS, tvOS), `WKInterfaceAuthorizationAppleIDButton` (WatchKit), Sign in with Apple JS (web buttons)

## Related
buttons, apple-pay, privacy, onboarding, voiceover
