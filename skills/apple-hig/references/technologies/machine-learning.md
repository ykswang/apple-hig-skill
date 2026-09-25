# Machine learning

> Source: https://developer.apple.com/design/human-interface-guidelines/machine-learning · Machine learning lets apps and games learn from data and usage patterns to improve existing experiences and create new ones.

## When to use / core idea
- Powers image recognition, recommendations, curated feeds, itineraries, personalized search. For model-driven intelligent experiences also see `generative-ai`.
- ML features depend on well-designed models as much as UI. Models take a long time to adjust — keep the intended experience in mind and be ready to change data/metrics use.
- You can't design reactions to a static set of scenarios; you teach the app how to interpret data and react.
- Process: define the **role** of ML in your app, then apply input/output patterns (feedback, calibration, mistakes, corrections, multiple options, confidence, attribution, limitations).

## Rules
### The role of machine learning in your app
- **Critical vs. complementary** — critical if the app can't work without it (Face ID); complementary if it can (QuickType). The more central the feature, the more people expect accurate, reliable results; people forgive secondary features more.
- **Private vs. public** — the more sensitive the data, the more serious inaccurate results are (health app wrongly recommending a doctor visit vs. music app suggesting a disliked artist). Sensitive-data features must prioritize accuracy/reliability; all apps must protect privacy at all times.
- **Proactive vs. reactive** — proactive provides unrequested results (Siri Suggestions); reactive responds to requests/actions (QuickType). People tolerate low quality less in proactive results; you may need additional data.
- **Visible vs. invisible** — visible features offer choices (Image Playground); invisible ones aren't obvious (News topic suggestions). Invisible features struggle to communicate reliability and receive feedback.
- **Dynamic vs. static** — dynamic improves as people interact (often uses calibration and implicit/explicit feedback); static improves offline, only with app updates.

### Explicit feedback
- Info people provide in response to a specific app request. Favoriting and social feedback are actually *implicit* feedback (people pursue their own goals).
- **Request explicit feedback only when necessary** — prefer implicit feedback.
- **Always make providing explicit feedback a voluntary task.**
- **Use simple, direct language to describe each explicit feedback option and its consequences** — avoid vague terms like *dislike* (no consequence, hard to translate); e.g., "Suggest less pop music", "Suggest more thrillers", "Mute politics for a week".
- **Add icons to an option description if it helps people understand it** — avoid an icon by itself.
- **Consider offering multiple options when requesting explicit feedback** — gives control; consider progressively more specific options.
- **Act immediately when you receive explicit feedback and persist the resulting changes** — e.g., hide unwanted content and ensure it doesn't appear elsewhere.
- **Consider using explicit feedback to help improve when and where you show results.**

### Implicit feedback
- Info arising from interaction; not required but improves UX without extra work.
- **Always secure people's information** — maintain strict privacy controls.
- **Help people control their information** — tell people how you get and share info; give ways to restrict its flow (cross-app effects can surprise and erode trust).
- **Don't let implicit feedback decrease people's opportunities to explore** — reinforcement helps short term, may hurt long term.
- **When possible, use multiple feedback signals to improve suggestions and mitigate mistakes** — viewing/sharing/adding a photo doesn't necessarily mean liking it.
- **Consider withholding private or sensitive suggestions** — devices/accounts are shared; avoid recommendations based on sensitive feedback.
- **Prioritize recent feedback** — tastes change (Face ID prioritizes recent input); fall back to historical if none.
- **Use feedback to update predictions on a cadence that matches the person's mental model of the feature** — typing suggestions update immediately; continuously updating song recommendations feels rushed.
- **Be prepared for changes in implicit feedback when you make changes to your app's UI** — e.g., moving a button changes usage.
- **Beware of confirmation bias** — implicit feedback is limited to what people can see/do; avoid relying solely on it.

### Calibration
- People provide info a feature needs to function (e.g., Face ID face scan). Only use when the feature can't function without it; otherwise gather via implicit/explicit feedback.
- **Always secure people's information.**
- **Be clear about why you need people's information** — emphasize what the feature does, not how it works.
- **Collect only the most essential information.**
- **Avoid asking people to participate in calibration more than once** — best early in the experience; evolve via feedback. Exception: calibrating with an object (e.g., each new baseball field).
- **Make calibration quick and easy** — get a few important pieces and infer the rest; avoid info people would have to look up; avoid difficult actions.
- **Make sure people know how to perform calibration successfully** — explicit goal and visible progress (Face ID tick marks).
- **Immediately provide assistance if progress stalls** — actionable recommendations; never imply something's wrong or people are at fault; never leave them without a clear next step.
- **Confirm success** — explicit completion and clear path to the feature.
- **Let people cancel calibration at any time** — no judgment; no messaging about the cancellation needed.
- **Give people a way to update or remove information they provided during calibration** — also outside the calibration experience.

### Mistakes
- Anticipate (avoid and mitigate), help people handle them (tools matching consequences), learn from them when it improves the app (unless it causes unpredictability). Patterns: limitations, corrections, attribution, confidence, explicit/implicit feedback.
- **Understand the significance of a mistake's consequences** — wrong keyboard suggestion vs. route causing a missed flight; match corrective tools to severity.
- **Make it easy for people to correct frequent or predictable mistakes.**
- **Continuously update your feature to reflect people's evolving interests and preferences and help avoid mistakes** — use implicit feedback and domain info (trends); ideally no work for people.
- **When possible, address mistakes without complicating the UI** — corrections/limitations integrate easily; attributions are harder and a wrong attribution magnifies the mistake.
- **Be especially careful to avoid mistakes in proactive features** — less patience; reduces sense of control.
- **As you work on reducing mistakes in one area, always consider the effect your work has on other areas and overall accuracy** — e.g., better dog recognition may hurt cats; mistakes evolve with models.

### Corrections
- **Give people familiar, easy ways to make corrections** — show steps the app took (Photos highlights auto-crop controls so people refine/undo with them).
- **Provide immediate value when people make a correction** — instantly show corrected content; persist updates.
- **Let people correct their corrections** — respond immediately and persist.
- **Always balance the benefits of a feature with the effort required to make a correction** — people abandon it if doing the task themselves seems easier.
- **Never rely on corrections to make up for low-quality results.**
- **Learn from corrections when it makes sense** — corrections are implicit feedback; ensure they'll lead to higher-quality results first.
- **When possible, use guided corrections instead of freeform corrections** — guided suggests alternatives (speech-to-text alternatives list); freeform needs more input (Photos crop). A combination is fine.

### Multiple options
- Gives control and sets realistic expectations. Contexts: suggested options (proactive, e.g., Apple Music For You), requested options (reactive, e.g., QuickType), corrections (e.g., Photos Auto-Crop).
- **Prefer diverse options** — balance accuracy with diversity (Maps: no-toll, scenic, highway routes).
- **In general, avoid providing too many options** — cognitive load; when possible list on one screen without scrolling.
- **List the most likely option first** — rank by confidence (if it correlates with quality) or context (time, location); consider selecting the first option by default.
- **Make options easy to distinguish and choose** — brief descriptions highlighting differences; group many options into scannable categories.
- **Learn from selections when it makes sense** — selections are implicit feedback; repeated incorrect results erode trust.

### Confidence
- Measure of certainty; not all models produce it — consider computing it if useful. Higher confidence doesn't necessarily mean higher quality: verify correlation (multiple thresholds, across app versions). If unsure how it correlates, don't convey confidence to people.
- **Know what your confidence values mean before you decide how to present them** — low-quality results presented prominently erode trust.
- **In general, translate confidence values into concepts that people already understand** — "Because you listen to pop music" beats "97% match".
- **In situations where attributions aren't helpful, consider ranking or ordering the results in a way that implies confidence levels** — if you must show confidence directly, use semantic categories ("high chance", "low chance").
- **In scenarios where people expect statistical or numerical information, display confidence values that help them interpret the results** — weather, sports stats, polling (intervals or percentages).
- **Whenever possible, help people make decisions by conveying confidence in terms of actionable suggestions** — "This is a good time to buy", "Consider waiting for a better price".
- **Consider changing how you present results based on different confidence thresholds** — Photos face recognition shows photos when high confidence, asks for confirmation when lower.
- **When you know that confidence values correspond to result quality, you generally want to avoid showing results when confidence is low** — set a threshold below which proactive/suggestion features show nothing.

### Attribution
- Expresses the basis for a result without explaining the model ("Because you've read mysteries"). Uses: encourage behavior change, minimize impact of mistakes, build a mental model, promote trust.
- **Consider using attributions to help people distinguish among results** — e.g., "New books by authors you've read."
- **Avoid being too specific or too general** — too specific feels like surveillance/extra work; too general feels impersonal/useless.
- **Keep attributions factual and based on objective analysis** — never imply understanding or judgment of emotions, preferences, beliefs: "Because you've read nonfiction", not "Because you love nonfiction".
- **In general, avoid technical or statistical jargon** — except when the result is statistical/technical (weather, sports, polling/elections, scientific data).

### Limitations
- Two types: things a feature can't do well, and can't do at all. Mismatched expectations make limitations seem like defects. Set expectations beforehand, show how to get best results during use, explain inferior results.
- **Help people establish realistic expectations** — rare but serious limitations: tell people before use (marketing or in-context); non-serious: use attributions.
- **Demonstrate how to get the best results** — placeholder text suggesting input (Photos search "Photos, People, Places…"); real-time feedback guiding improvement (Memoji lighting/distance); suggest alternatives instead of showing no results.
- **Explain how limitations can cause unsatisfactory results** — e.g., Memoji says it doesn't work well in the dark.
- **Consider telling people when limitations are resolved.**

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## APIs
`Create ML`, `Core ML`, Apple Intelligence and machine learning frameworks

## Related
generative-ai, privacy, icons, onboarding
