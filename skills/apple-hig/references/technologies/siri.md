# Siri

> Source: https://developer.apple.com/design/human-interface-guidelines/siri · People use Siri to find, know, or do things every day — by voice, swiping down from the Dynamic Island, or in the Siri app.

## When to use / core idea
- Siri AI (on supported devices, powered by Apple Intelligence) lets people invoke app actions from anywhere, act on onscreen content ("Add this photo to my Landscapes album" → "And email it to Josh"), and reach deep features fast ("Make this black and white").
- The system has no awareness of an app by default; expose features/content via App Intents: actions = *intents*, content = *entities*. These surface in Siri, Spotlight, Shortcuts.
- Prefer app *schemas* (preset templates in domains like email, music, photos) to get built-in natural-language handling and deeper context.
- If functionality falls outside schema domains, use App Shortcuts to expose custom actions (see `app-shortcuts`).
- Customize schema responses by defining optional intent/entity properties (e.g., a playback-control snippet while audio plays). Optional properties may not always appear, since some response contexts aren't visual.

### Sharing contextual information
- Annotate views/onscreen content with app entities so Siri understands references to onscreen items (buttons, graphics).
- Donate entities to the on-device Spotlight index so content is findable in Spotlight and Siri.
- Donate actions people take as intents (recent activity, items of interest) so Siri can anticipate and surface them at appropriate times.

## Rules
### Best practices
- **Identify your app's most popular actions, and when and where they occur** — contexts (hands-free, particular device) help prioritize which actions/content to expose and shape the Siri experience.
- **Use familiar terms for your content and actions** — pick the name people most likely recognize (track vs. song vs. podcast).
- **Offer relevant content** — instead of giving Spotlight all content, consider personally relevant items (recent searches, favorites, bookmarks, wishlist). Email/messaging may justifiably treat the entire catalog as relevant.
- **Don't advertise** — no ads, marketing, or in-app purchase pitches in content Siri delivers.
- **Only provide a custom response if built-in responses don't meet your app's needs.**

### Custom response properties
- **Write response dialogue that's clear and descriptive** — convey what happens; customize default follow-up dialogue ("Which soup?" not "Which one?").
- **Keep responses as succinct as possible** — people hear them repeatedly; use conversation context to drop details; avoid unnecessary words and attempts at humor.
- **Provide responses that Siri can deliver audibly and visually** — Siri picks the method (onscreen on iPhone, spoken on AirPods); voice response must stand alone without visual elements.
- **Design inclusive interactions** — avoid unnecessary specific pronouns ("Who should I send it to?" not "What's his or her name?"). See `writing`, `inclusion`.
- **Ask an open-ended question when the full list of options is too long** — e.g., "What kind of shoes are you interested in?"
- **Keep responses device-independent whenever possible** — requests can start on one device and act on another; if you must reference a device, ensure accuracy in context.
- **Omit your app name from responses** — system already provides verbal and visual attribution.
- **Use appropriate language and respect parental controls** — no offensive language; families restrict explicit content by rating; Siri may respond aloud and others may hear.
- **Help people understand errors and failures** — enhance default errors to be situation-specific ("Sorry, we're out of chicken noodle soup" vs. "Sorry, we can't complete your order").

### Editorial guidelines
- **Refer to Siri by name** — never *she*, *him*, *her*; ideally just *Siri*.
- **Be aware that the system reserves important actions and phrases for Siri** — never impersonate Siri, reproduce Siri functionality, or appear to come from Apple. Don't use reserved phrases like "Call 911" or "Hey Siri."
- **In a localized context, translate only the word *Hey* in "Hey Siri"** — *Siri* (trademark) is never translated.

## Specs
Acceptable "Hey Siri" translations:

| Locale code | "Hey Siri" translation | Locale code | "Hey Siri" translation |
| --- | --- | --- | --- |
| ar_AE | يا Siri | fr_CA | Dis Siri |
| ar_SA | يا Siri | fr_CH | Dis Siri |
| da_DK | Hej Siri | fr_FR | Dis Siri |
| de_AT | Hey Siri | it_CH | Ehi Siri |
| de_CH | Hey Siri | it_IT | Ehi Siri |
| de_DE | Hey Siri | ja_JP | Hey Siri |
| en_AU | Hey Siri | ko_KR | Siri야 |
| en_CA | Hey Siri | ms_MY | Hai Siri |
| en_GB | Hey Siri | nb_NO | Hei Siri |
| en_IE | Hey Siri | nl_BE | Hé, Siri |
| en_IN | Hey Siri | nl_NL | Hé Siri |
| en_NZ | Hey Siri | no_NO | Hei Siri |
| en_SG | Hey Siri | pt_BR | E aí Siri |
| en_US | Hey Siri | ru_RU | привет Siri |
| en_ZA | Hey Siri | sv_SE | Hej Siri |
| es_CL | Oye Siri | th_TH | หวัดดี Siri |
| es_ES | Oye Siri | tr_TR | Hey Siri |
| es_MX | Oye Siri | zh_CN | 嘿Siri |
| es_US | Oye Siri | zh_HK | 喂 Siri |
| fi_FI | Hei Siri | zh_TW | 嘿 Siri |
| fr_BE | Dis Siri |  |  |

## APIs
`App Intents` (App Intents), `Getting started with the App Intents framework` (App Intents), `schemas` (App Intents), `Apple Intelligence and Siri AI` (App Intents), `Making actions and content discoverable by Apple Intelligence` (App Intents), `Providing contextual cues to Apple Intelligence and Siri` (App Intents), `Defining app entities for your custom data types` (App Intents), `Making app entities available in Spotlight` (App Intents), `Donating your app’s data and actions to the system` (App Intents), `app schema domains` (App Intents), `App Shortcuts` (App Intents), `Displaying static and interactive snippets` (App Intents), `App schema domains` (App Intents)

## Related
`app-shortcuts, snippets, writing, inclusion`
