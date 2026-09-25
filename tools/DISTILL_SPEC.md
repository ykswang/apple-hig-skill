# Distillation spec: Apple HIG page → skill reference file

Goal: turn each raw HIG page (Markdown rendered from Apple's official DocC JSON) into a dense, actionable
reference that another AI (Claude or otherwise) can load on demand to design or review UI that follows
Apple's Human Interface Guidelines. The reader is an AI agent that will APPLY the rules, so optimize for
precision and scannability, not prose.

## Output format (English, Markdown)

```
# <Page title>

> Source: <canonical URL> · <one-sentence purpose of the component/topic from the abstract>

## When to use / core idea
2–5 bullets: what it is, when to choose it vs. alternatives (name the alternatives).

## Rules
- **<Imperative rule, preserving Apple's bold sentence meaning>** — <why / condition / example, compressed>.
...  (group with ### subheadings mirroring the page's own subsections, e.g. ### Best practices, ### Content, ### Behavior)

## Platform considerations
### iOS, iPadOS
- ...
### macOS
- ...
(only platforms the page actually discusses; if the page says "No additional considerations for X", write one line: `No additional considerations: X, Y.`)

## Specs
(Only if the page has concrete values: sizes, pt, px, ratios, counts, durations, colors, font sizes, tables.
Reproduce EVERY number and table faithfully — these are the most valuable part. Keep tables as Markdown tables.)

## APIs
One line, comma-separated developer API names with framework, e.g. `Toggle` (SwiftUI), `UISwitch` (UIKit), `NSSwitch` (AppKit).

## Related
Comma-separated slugs of related HIG pages, e.g. `pop-up-buttons, layout`.
```

## Fidelity rules (critical)
1. EVERY bold guideline sentence in the raw page must survive as a rule bullet (compressed wording OK, meaning must be exact).
   Do not merge two distinct rules into one if that loses a condition. Do not invent rules not in the source.
2. Keep all numbers, limits, thresholds, and platform-specific values exactly (e.g. "44x44 pt", "about five options", "4.5:1").
3. Keep "Avoid / Don't / Never / Prefer / Consider" strength as written — Apple's modal verbs signal priority.
   Map: "Always/Never/Don't/Avoid" = hard rule; "Prefer/Generally" = strong default; "Consider" = suggestion. Preserve the verb.
4. Non-bold explanatory paragraphs that contain real guidance (definitions, behaviors, component anatomy) → compress into
   bullets under the relevant heading. Drop marketing prose, image alt-text lines (`[Image: ...]`), video mentions, and the
   "Change log" section entirely.
5. Keep links only as related slugs or API names — no full URLs except the Source line.
6. Target length: roughly 35–55% of the raw page's character count. Very dense pages (tables/specs) may be longer. Never pad.
7. For pages that are platform overviews (designing-for-*), structure as: Device characteristics / Key traits, Best practices,
   and a Specs section with any listed resolutions/sizes.

## Process per page
1. Read the raw file fully (use the Read tool; files can be long — read in chunks if needed, never skim-truncate).
2. Write the reference file.
3. Self-check: scan the raw file for every `**...**` bold rule and every number; confirm each appears in your output.
