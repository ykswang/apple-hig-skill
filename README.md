# apple-design

An Agent Skill that packages Apple's
[Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) so Claude (or any other
AI agent) can design, build, and review UI for Apple platforms the way Apple recommends.

All 173 pages of the HIG are included, current as of **September 2026**. That covers Liquid Glass, iPhone Duo, and
Apple In-App Purchase. The 158 pages with real content are each distilled into their own reference file.

## What's in the repo

```
skills/apple-hig/            ← the skill; this folder is what you install
├── SKILL.md                 entry point: workflow, design principles, cross-cutting rules
│                            (hit targets, contrast, type sizes, Liquid Glass…), task → file routing, review checklist
└── references/
    ├── INDEX.md             one-line summary of every page, in the same order as the HIG sidebar
    ├── getting-started/     design principles + each platform (iOS, iPadOS, macOS, watchOS, tvOS, visionOS, games, iPhone Duo)
    ├── foundations/         color, typography, layout, materials, SF Symbols, icons, accessibility, privacy, …
    ├── patterns/            loading, onboarding, searching, settings, modality, drag and drop, undo, …
    ├── components/          every system component: buttons, menus, toolbars, tab bars, sheets, alerts, widgets, …
    ├── inputs/              gestures, keyboards, pointers, eyes, Apple Pencil, Digital Crown, …
    └── technologies/        Apple Pay, Sign in with Apple, Wallet, Siri, CarPlay, HealthKit, …
tools/                       ← only needed to refresh the skill
├── crawl.py                 downloads the whole HIG through Apple's DocC JSON API and renders it to Markdown
├── diff_crawl.py            compares a new download with the committed baseline and lists changed pages
├── hig-manifest.json        the baseline: a content hash for every page the skill was built from
├── DISTILL_SPEC.md          rules for turning a HIG page into a reference file
├── build_index.py           regenerates references/INDEX.md
└── verify.py                checks that reference files exist and kept every number from the source
```

Every reference file has the same layout: when to use it → rules → platform considerations → specs → APIs →
related pages. Rules keep Apple's own strength words (*Never / Avoid / Prefer / Consider*), and all numbers and spec
tables are copied exactly from the source.

## Install

After cloning, run the commands below from the repository root.

### Claude Code

Claude Code picks up skills from `~/.claude/skills/` (every project) or `<project>/.claude/skills/` (one project).

**For all projects (symlink, recommended).** A `git pull` then updates the skill in place:

```bash
mkdir -p ~/.claude/skills
ln -s "$PWD/skills/apple-hig" ~/.claude/skills/apple-hig
```

**For one project.** Copy the folder in, so the skill is committed with that project and works for everyone on
your team:

```bash
mkdir -p /path/to/your-project/.claude/skills
cp -R skills/apple-hig /path/to/your-project/.claude/skills/
```

Start a new Claude Code session to load the skill. Claude uses it by itself when a task involves Apple platform UI.
You can also ask for it directly: *"Use the apple-hig skill to review this SwiftUI view."*

### Claude apps (claude.ai / desktop)

Zip the skill folder and upload it where your Claude app lets you add custom skills:

```bash
cd skills && zip -r ../apple-hig.zip apple-hig && cd ..
```

### Other AI agents

Give the agent `skills/apple-hig/SKILL.md` as instructions and let it read files under `skills/apple-hig/references/`.
The files are plain Markdown with relative links. `SKILL.md` tells the agent which files to open for which task, so
it only loads what it needs.

## Refreshing the skill when Apple updates the HIG

Apple mostly updates the HIG at WWDC (June) and at the fall hardware launches (September), plus smaller updates in
between. Each HIG page ends with a *Change log* that shows what changed and when.

**Requirements:** Python 3.9+ (standard library only), a network connection, and an AI agent (Claude Code
recommended) for the rewriting step.

### 1. Download the current HIG

```bash
python3 tools/crawl.py /tmp/hig
```

This writes every page to `/tmp/hig/raw/<slug>.md` and a page list with content hashes to `/tmp/hig/pages.json`.
It takes about a minute.

### 2. Find what changed

```bash
python3 tools/diff_crawl.py /tmp/hig
```

Example output:

```
NEW      references/patterns/new-thing.md  <- /design/human-interface-guidelines/new-thing
CHANGED  references/components/buttons.md  <- /design/human-interface-guidelines/buttons
CHANGED  (index page: update INDEX.md / SKILL.md routing)  <- /design/human-interface-guidelines/components
REMOVED  references/components/toggles.md  <- /design/human-interface-guidelines/toggles
new=1 changed=2 removed=1 unchanged=169
```

If it reports `new=0 changed=0 removed=0`, the skill is already up to date and you can stop here.

### 3. Rewrite the new and changed pages

Each `NEW` or `CHANGED` page has to be rewritten from its new source. In Claude Code, open this repo and paste the
following prompt, filling in the page list from step 2:

```
Read tools/DISTILL_SPEC.md and follow it exactly.
For each page below, read /tmp/hig/raw/<slug>.md in full and (re)write the reference file at
skills/apple-hig/references/<section>/<slug>.md. Replace the whole file; don't patch the old version.
Only use API names that appear as links in the raw page.
Pages: components/buttons, patterns/new-thing
```

When many pages changed (usually after WWDC), ask Claude to split them across parallel subagents, 15–25 pages each.

Then handle the rest by hand:

- **`REMOVED` pages:** delete the reference file, and remove any mention of it from `SKILL.md` and from other
  files' *Related* lines (`grep -rn "<slug>" skills/`).
- **`index page` lines:** a section was reorganized. Check whether `SKILL.md`'s routing table still makes sense.
- **Foundations pages** (`accessibility`, `typography`, `color`, `materials`, `layout`, `privacy`, …): `SKILL.md`
  copies some of their numbers and rules (hit-target table, contrast table, default type sizes, Liquid Glass rules).
  If any of these pages changed, compare those sections of `SKILL.md` with the new reference files and update them.
- If the platform or feature list changed, update the "content current through …" line near the top of `SKILL.md`
  and the skill's `description`.

### 4. Rebuild the index and verify

```bash
python3 tools/build_index.py /tmp/hig skills/apple-hig
python3 tools/verify.py /tmp/hig skills/apple-hig
```

`build_index.py` fails if a page has no reference file. `verify.py` lists every page where a number from the source
is missing, or where the reference has noticeably fewer rules than the source has bold rule sentences. Some of these
are false alarms: times such as `9:41` in example screenshots, or bold labels that aren't rules. Check each one it
lists and fix any real gaps.

### 5. Save the new baseline and commit

```bash
python3 tools/diff_crawl.py /tmp/hig --update
git add skills tools
git commit -m "Refresh apple-hig from HIG as of <month year>"
```

`--update` overwrites `tools/hig-manifest.json`, so the next refresh compares against this download. Run it only
after the reference files are updated. If you run it earlier, the next diff won't show the pages you skipped.

If you installed with a symlink, other machines pick up the changes with `git pull`. Copied installs need copying
again.

## Known notes

- The current HIG *Layout* page no longer has per-device screen-size tables. Per-device sizes now appear only on the
  *Widgets* and *Live Activities* pages.
- A few table values look like typos in Apple's source (for example "18x18x pt" on *Complications*, and some
  leading/tracking values on *Typography*). They are copied as written, not corrected.
- The *APIs* section of each reference file only lists developer documentation that the source page links to.
- HIG content © Apple Inc. This repository contains condensed notes for use as AI context. The authoritative
  version is always [developer.apple.com/design/human-interface-guidelines](https://developer.apple.com/design/human-interface-guidelines).
