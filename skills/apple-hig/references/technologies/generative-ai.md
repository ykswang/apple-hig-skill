# Generative AI

> Source: https://developer.apple.com/design/human-interface-guidelines/generative-ai · Generative AI lets you enhance an app or game with dynamic content and intelligent features that unlock creativity, connection, and productivity.

## When to use / core idea
- Uses ML models to create/transform text, images, and other content (edit text, imaginative stories/images, AI-generated game dialog).
- Offer it only where it provides clear, specific value (time savings, better communication, enhanced creativity); not right for every situation.
- Outputs are nondeterministic: small input changes (or the same input repeated) can yield very different results, and requests/responses can't always be anticipated.
- Broader ML UX patterns (limitations, multiple options, explicit/implicit feedback) live in `machine-learning`.

## Rules
### Best practices
- **Design your experience responsibly** — responsible AI considers direct and indirect impacts on people, systems, society; easy to prototype, hard to make robust for all real-world situations. Orient design around inclusive, careful, privacy-protecting experiences.
- **Keep people in control** — honor in-scope requests with clear expected output; handle sensitive content carefully; let people dismiss unwanted content and revert or retry transformations/actions; clearly identify when and where AI is used.
- **Ensure an inclusive experience for all** — models favor common data, causing bias/stereotypes. When generating images/descriptions of people, ask for needed information rather than solely inferring personal or cultural traits; seek clarity before assumptions (e.g. gender identities, relationship types); test with a diverse set of people.
- **Design engaging and useful generative features** — only when and where they add clear, specific value.
- **Ensure a great experience even when generative features aren't available or people opt not to use them** — AI may be essential or merely complementary (e.g. Genmoji vs. regular emoji; notification summaries vs. reading notifications). When possible, consider a non-AI fallback.

### Transparency
- **Communicate where your app uses AI** — sets expectations and enables knowing choice. Never trick people into thinking they're interacting with or viewing content authored by a human when it's AI. Align disclosure with regional regulations.
- **Set clear expectations about what your AI-powered feature can and can't do** — e.g. brief tutorial on introduction; curated suggestions for open-ended inputs (search bar, generation prompt); state known limitations up front, show how to get good results, explain why inferior results occur.

### Privacy
- **Choose a model type that fits your feature's needs and protects people's privacy** — on-device: private, fast, offline; server-based: when more processing power or larger context is needed. Always weigh privacy alongside capability and performance. For server processing: process locally as much as possible, minimize what's shared; tell people data may go to a server, show what's shared, explain what may be stored off-device or used for training.
- **Ask permission before using personal information and usage data** — (personal details, messages, photos, usage). Then use the minimum data and always offer a clear opt-out. Explicit permission for sensitive data used for model improvement or storage. Understand third parties' privacy approach when sharing. Outputs may inadvertently contain sensitive info. Apps for kids have stricter rules.
- **Clearly disclose how your app and its model use and store personal information** — explain benefits concisely, specifically, understandably; state whether personal info is used for training and improvement.

### Models and datasets
- **Thoughtfully evaluate model capabilities** — general-knowledge vs. task-specific models; get hands-on with models/data early. Some models may be unavailable due to device compatibility, network access, battery level (e.g. Foundation Models requires a compatible device with Apple Intelligence turned on).
- **Be intentional when choosing or creating a dataset** — diverse subject-matter representation; know data provenance and collection; have licenses for data you don't own; offer appropriate choices when using people's data; allow time to test and mitigate bias and misinformation.

### Inputs
- **Guide people on how to use your generative feature** — e.g. diverse predefined example inputs hinting at what's possible.
- **Raise awareness about and minimize the chance of hallucinations** — clearly communicate AI content may contain errors (dates, facts about people); carefully scope requests; avoid requesting factual info unless the model has verified, up-to-date information; avoid AI content where a hallucination could misinform and harm someone.
- **Consider consequences and get permission before performing irreversible or potentially problematic tasks** — avoid automating destructive actions (deleting photos) and hard-to-undo actions (purchases on someone's behalf); generally ask for confirmation before significant actions on someone's behalf. Follow model-specific usage policies and government/regulatory AI policy per locale.

### Outputs
- **Make it easy for people to refine or revert generated results, and acknowledge when their corrections take effect** — surface Edit, Undo, Retry, Adjust near generated content; give a clear signal when adjustments/personalization take effect.
- **Help people improve requests when blocked or undesirable results occur** — coach for next time (e.g. Image Playground: "Unable to use that description."); consider offering example requests that lead to better results.
- **Reduce unexpected and harmful outcomes with thoughtful design and thorough testing** — identify risks, devise policies, evaluate. Test out-of-scope, unrelated, and poorly represented requests; poorly phrased, vague, ambiguous ones; personal, sensitive, controversial topics; attempts to elicit harmful or incorrect results. Use findings to improve the model, prevention, and responses.
- **Strive to avoid replicating copyrighted content** — build on models with protections; curate inputs (e.g. pre-approved prompts); instruct the model to avoid mimicking certain content/styles.
- **Factor processing time into your design** — *latency* = time to produce output. Non-generative models (ARKit body tracking, Vision) are low-latency/real-time; generative models are slower → design a loading experience or generate in the background while people use another part of the app.
- **Consider giving specific, reassuring feedback during generation** — "Finding substitutions for ingredients" / "Summarizing key themes from your notes" instead of "Processing…". On failure, describe what happened in plain language and offer a clear next step.
- **Consider offering alternate versions of results** — single result or multiple meaningfully different ones (e.g. Image Playground offers several images to pick from).

### Continuous improvement
- **Consider ways to improve your model over time** — some updates (e.g. blocked-word lists) can ship frequently, independent of app releases; plan big improvements with app updates. Plan fine-tuning, retesting, prompt engineering when moving to a newer base model; retrain/fine-tune own models; thoroughly test all updates.
- **Let people share feedback on outputs** — take it seriously, resolve quickly; always voluntary; place affordance clearly without interrupting; consider quick thumbs-up/thumbs-down plus an option for detailed feedback.
- **Design flexible, adaptable features** — e.g. separate the model from the UX so models can be swapped over time while keeping the same experience.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS, watchOS.

## APIs
Foundation Models, Core AI, Vision, ARKit body tracking (Capturing body motion in 3D), Image Playground

## Related
machine-learning, inclusion, accessibility, privacy, loading
