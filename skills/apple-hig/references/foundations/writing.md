# Writing

> Source: https://developer.apple.com/design/human-interface-guidelines/writing · The words you choose within your app are an essential part of its user experience.

## When to use / core idea
- Applies to all UI copy: onboarding, alerts, button labels, empty states, errors, settings, text-field hints, accessibility descriptions.
- Establish a consistent voice; vary tone by situation.
- Companion pages: inclusion (welcoming language), accessibility/voiceover, buttons (label content), alerts, notifications.

## Rules

### Getting started
- **Determine your app's voice** — consider audience and familiar vocabulary, and how you want people to feel (banking: trust, stability; game: excitement, fun). Keep a list of common terms for consistency.
- **Match your tone to the context** — consider what people are doing physically and in-app (reached an exercise goal vs. hit a payment error). E.g., Apple Watch Fall Detection is straightforward ("It looks like you've taken a hard fall"), Activity is light and congratulatory ("…longest daily Move streak, 35 days!").
- **Be clear** — easily understood words; remove unnecessary words; use fewer words when possible; when in doubt, read aloud.
- **Write for everyone** — simple, plain language; write with accessibility and localization in mind; avoid jargon and gendered terminology.

### Best practices
- **Consider each screen's purpose** — put the most important information first; format for readability; for more than one idea, consider splitting across screens and plan the flow.
- **Be action oriented** — active voice and clear labels. Buttons and links: almost always use a verb. Avoid being too cute or clever ("Send" beats "Let's do it!"). Avoid "Click here" for links; use descriptive text ("Learn more about UX Writing") — especially important for screen reader users.
- **Build language patterns** — consistency builds familiarity and makes writing easier.
- **Adopt capitalization rules that align with your app's style, then apply them consistently** — some components have specific rules (button labels). Title case = more formal; sentence case = more casual. Pick one style per UI element type and apply it app-wide (e.g., title case for all alerts, sentence case for all headlines).
- **Give clear guidance and use consistent language throughout processes with multiple steps** — start with language like "Get Started"; advance with labels hinting at the next step, or "Continue"/"Next", consistently; end with "Done".
- **Use possessive pronouns sparingly** — "Favorites" beats "Your Favorites". If used, be consistent and don't switch perspectives. Avoid *we* altogether — unclear who it means, especially in errors ("Unable to load content" beats "We're having trouble loading this content").
- **Write for how people use each device** — stay consistent across devices but adapt where helpful; describe gestures correctly (don't say "click" on iPhone/iPad where you mean "tap"). iPhone and Apple Watch allow personalization but small screens require brevity; TVs are in shared spaces (consider who you're addressing) and big screens also require brevity because text must be large to read from a distance.
- **Provide clear next steps on any blank screens** — empty states (completed to-do list, empty bookmarks folder) can welcome and educate and show voice, but must be useful and in context. Guide next actions and provide a button or link when possible. Empty states are usually temporary — don't show crucial information there.
- **Write clear error messages** — best to help people avoid errors. Show errors as close to the problem as possible, avoid blame, say how to fix ("Choose a password with at least 8 characters" beats "That password is too short"). Avoid interjections like "oops!"/"uh-oh" (insincere). If language alone can't address an error likely to affect many people, rethink the interaction.
- **Choose the right delivery method** — weigh urgency, importance, context, whether immediate action is required, and how much supporting info is needed; pick notification, alert, or action sheet and an appropriate tone.
- **Keep settings labels clear and simple** — label practically; add an explanation if needed, describing what happens when on (people infer the opposite), e.g., "Apple Watch can detect when you're washing your hands and start a 20-second timer." To direct people to a setting, provide a direct link or button instead of describing its location.
- **Show hints in text fields** — label all fields clearly; use hint/placeholder text for format, as an example ("name@example.com") or description ("Your name"). Show errors right next to the field and instruct instead of scold ("Use only letters for your name" beats "Don't use numbers or symbols"). Avoid robotic unhelpful errors like "Invalid name".

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## APIs
Localization (Xcode)

## Related
inclusion, accessibility, voiceover, color, buttons, notifications, alerts, action-sheets, settings, text-fields, onboarding
