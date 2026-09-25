# Managing accounts

> Source: https://developer.apple.com/design/human-interface-guidelines/managing-accounts · When it doesn't create an unnecessary barrier, an account is a convenient way for people to access content and track personal details.

## When to use / core idea
- Ask people to create an account only if core functionality requires it; otherwise let them use the app/game without one.
- If an account is required, consider `sign-in-with-apple`; otherwise prefer passkeys (iOS, iPadOS, macOS, visionOS).
- If you let people create an account in-app, you must let them delete it (not just deactivate); comply with regional legal requirements (account deletion, right to be forgotten).

## Rules
### Best practices
- **Explain the benefits of creating an account and how to sign up** — brief, friendly description of reasons and benefits, shown in the sign-in view.
- **Delay sign-in for as long as possible** — forced early sign-in causes abandonment; e.g. shopping app allows browsing, requires sign-in only at purchase.
- **If you don't use Sign in with Apple in your iOS, iPadOS, macOS, or visionOS app, prefer using a passkey** — no passwords; people provide just a user name to create/sign in. If you must keep passwords, require two-factor authentication.
- **Always identify the authentication method you offer** — e.g. "Sign In with Face ID", not generic "Sign In".
- **Refer only to authentication methods that are available in the current context** — e.g. don't mention Face ID on a device without it; check device capabilities and use correct terminology.
- **In general, avoid offering an app-specific setting for opting in to biometric authentication** — biometrics are enabled at the system level; an in-app setting is redundant and confusing.
- **Avoid using the term *passcode* to refer to account authentication** — passcode means device unlock/Apple services; people may think you want them to reuse it.

### Deleting accounts
- Important: if law compels you to retain accounts/information (e.g. digital health records) or follow a specific deletion process, clearly describe what's retained and the process.
- **Provide a clear way to initiate account deletion within your app or game** — if deletion can't happen in-app, provide a direct, easy-to-find link to the deletion webpage (not buried in Privacy Policy/Terms of Service).
- Developer note: for accounts created with Sign in with Apple, revoke the associated tokens on deletion.
- **Provide a consistent account-deletion experience whether people perform it within your app or game or on the website** — don't make one flow longer or more complicated.
- **Consider letting people schedule account deletion to occur in the future** — lets them use remaining services or wait for subscription renewal; if you offer scheduling, also offer immediate deletion.
- **Tell people when account deletion will complete, and notify them when it's finished** — keep people informed since deletion can take a while.
- **If you support in-app purchases, help people understand how billing and cancellation work when they delete their account** — e.g. auto-renewable subscription billing continues through Apple until canceled regardless of account deletion; after deletion people need to cancel their subscription or request a refund. Also explain how to cancel subscriptions and manage purchases (see `in-app-purchase`). Support account deletion even if the subscription wasn't purchased through your app.

### TV provider accounts
- If your TV provider app requires sign-in, use TV Provider Authentication (system-level sign-in avoids per-app authentication).
- **Avoid displaying a sign-out option when people are signed in at the system level** — if you must include one, invoking it must direct people to Settings > TV Provider to sign out.
- **Never instruct people to sign out by adjusting privacy controls** — Settings > Privacy TV provider controls manage which apps can access the account; they aren't a sign-out mechanism.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, visionOS.
### tvOS
- People mostly use a remote, not a keyboard — ask for the minimum information necessary.
- **Prefer letting people use another device to sign up or authenticate** — with associated domains configured, Apple TV works with other devices to suggest credentials, including Sign in with Apple.
- **When people are signed in to a shared account, avoid asking them to choose their profile every time they become the current user** — tvOS 16+: share credentials with all users while storing each profile/data separately and automatically use the current user's profile.
- **Minimize data entry** — for more than a small amount of info, ask people to visit a website on another device; for email, show the email keyboard screen (includes recently entered addresses).
### watchOS
- Use iCloud synchronization for Keychain access so people can autofill user names/passwords and preserve app settings.

## APIs
Supporting passkeys (Authentication Services), Securing Logins with iCloud Keychain Verification Codes (Authentication Services), `LABiometryType` (LocalAuthentication), Token revocation (Sign in with Apple REST API), TV Provider Authentication, `kSecUseUserIndependentKeychain` (Security), User Management Entitlement `com.apple.developer.user-management`, Configuring an associated domain (Xcode)

## Related
onboarding, sign-in-with-apple, apple-in-app-purchase, entering-data
