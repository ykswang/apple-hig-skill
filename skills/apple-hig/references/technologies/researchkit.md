# ResearchKit

> Source: https://developer.apple.com/design/human-interface-guidelines/researchkit · A research app lets people everywhere participate in important medical research studies.

## When to use / core idea
- ResearchKit provides predesigned screens and transitions for custom research apps.
- Guidelines are informational only, not legal advice — consult an attorney on applicable laws.
- Flow: onboarding (introduction → eligibility → informed consent → data permission), then conducting research (surveys, active tasks), plus profile and dashboard screens.

## Rules
### Creating the onboarding experience
- Onboarding screens introduce the study, check eligibility, get consent, and request data access; rarely revisited, so clarity is essential.
- **Always display the onboarding screens in the correct order** — 1. Introduction → 2. Eligibility → 3. Informed consent → 4. Permission to access data.
- **Provide an introduction that informs and provides a call to action** — describe subject and purpose; let existing participants quickly log in and continue.
- **Determine eligibility as soon as possible** — ineligible people shouldn't reach consent; present only necessary requirements; simple language; easy data entry.
- **Make sure participants understand your study before you get their consent** — concise, friendly consent that can include legal/IRB/ethics board requirements; comply with App Store Guidelines consent requirements. Typically explains how the study works, ensures understanding of study and responsibilities, gets consent.
- **Break a long consent form into easily digestible sections** — one aspect per section (data gathering, data use, benefits, risks, time commitment, how to withdraw…); simple high-level overview with optional Learn More for detail. Participants must be able to view the entire form before agreeing.
- **If it makes sense, provide a quiz that tests the participant's understanding** — e.g., questions otherwise asked during in-person consent.
- **Get the participant's consent and, if appropriate, some contact information** — confirmation dialog, then signature and contact screens; most apps email a PDF of the consent form.
- **Get permission to access the participant's device or data, and to send notifications** — clearly explain why you need location, Health, or other data; don't request data not critical to the study; ask for notification permission if required.

### Conducting research
- Surveys and/or active tasks; participants may interact once or repeatedly.
- **Create surveys that keep participants engaged** — answer types include true/false, multiple choice, dates/times, sliding scales, open-ended text:
  - State number of questions and approximate duration.
  - One screen per question.
  - Show progress.
  - Keep as short as possible; several short surveys beat one long one.
  - For explanations, standard font for the question, slightly smaller font for explanatory text.
  - Tell participants when the survey is complete.
- **Make active tasks easy to understand** — activities like speaking into the mic, tapping, walking, memory tests:
  - Describe how to perform the task in clear, simple language.
  - Explain requirements (particular time or circumstances).
  - Make sure participants can tell when the task is complete.

### Managing personal information and providing encouragement
- Ideally both profile and dashboard screens are accessible at all times.
- **Use a profile to help participants manage personal data related to your study** — edit changing data (weight, sleep habits), remind of upcoming activities, easy way to leave the study, view consent document and privacy policy.
- **Use a dashboard to show progress and motivate participants to continue** — daily progress, weekly assessments, activity results, comparison with aggregated results from others, if appropriate.

## Platform considerations
No additional considerations: iOS, iPadOS. Not supported in macOS, tvOS, visionOS, or watchOS.

## APIs
`ResearchKit` (Research & Care; open source), `CareKit`, HealthKit privacy

## Related
healthkit, onboarding, privacy, notifications
