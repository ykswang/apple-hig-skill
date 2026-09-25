# CareKit

> Source: https://developer.apple.com/design/human-interface-guidelines/carekit · CareKit apps help people manage care plans for chronic illness (e.g. diabetes), recover from injury or surgery, or reach health and wellness goals.

## When to use / core idea
- CareKit 2.0 = **CareKit UI** (prebuilt customizable views) + **CareKit Store** (on-device database of patients, care plans, tasks, contacts), with automatic sync between database and UI.
- Pair with HealthKit (health data), Core Motion (motion), camera/photos, and ResearchKit (surveys, tasks, charts, informed consent) as appropriate.
- Build by choosing view styles and supplying CareKit Store data; use each view category only for its intended purpose.

## Rules
### Data and privacy
- **Provide a coherent privacy policy** — a URL to a clearly stated policy is required at App Store submission, viewable from the App Store page.
- Get permission before accessing data via iOS features; protect data whether user-entered or obtained from device/system.

### HealthKit integration
- HealthKit is the central health/fitness repository on iOS and watchOS; can share data with designated caregivers with permission.
- **Request access to health data only when you need it** — e.g. ask for weight when people log weight, not at launch. Permissions can change, so request every time you need access.
- **Clarify your app's intent by adding descriptive messages to the standard permission screen** — a few succinct sentences on why and how people benefit; avoid custom screens replicating the system permission screen.
- **Manage health data sharing solely through the system's privacy settings** — people manage it in Settings > Privacy; don't build in-app screens that affect health data flow.

### Motion data
- With permission and if useful for treatment: detect standing still, walking, running, cycling, driving; when walking/running, step count, pace, flights of stairs ascended/descended. Can include custom physical-therapy data (flexibility, range of motion, ambulatory capability via ResearchKit tasks).

### Photos
- With permission, access camera/photos to share progress pictures with a care team (e.g. periodic photos of an injury).

### ResearchKit integration
- Can incorporate ResearchKit surveys, tasks, charts, and its informed consent module to request permission to collect/share data.

### CareKit views
| Category | Purpose |
|---|---|
| Tasks | Present tasks (medication, physical therapy); log symptoms and other data. |
| Charts | Graphical data showing treatment progress. |
| Contact views | Contact info; phone, message, email; link to a map of the contact's location. |

- Anatomy: header (text, symbol, disclosure indicator, optional bottom separator) + optional vertical content stack of subviews. CareKit UI manages layout constraints when adding subviews.

### Tasks
Task information:

| Information | Required | Description | Example value |
|---|---|---|---|
| Title | Yes | Word/short phrase introducing the task | *Ibuprofen* |
| Schedule | Yes | Schedule on which the task must be completed | *Four times a day* |
| Instructions | No | Detailed instructions, recommendations, warnings | *Take 1 tablet every 4–6 hours (not to exceed 4 tablets daily).* |
| Group ID | No | Identifier to group similar tasks | *medication*, *exercise* |

Five task styles (CareKit 2.0): simple, instructions, log, checklist, grid.
- **Use the simple style for a one-step task** — header with title, subtitle, button; optional custom completion image, else button fills with checkmark. No content stack — use another style for additional content.
- **Use the instructions style when you need to add informative text to a simple task** — e.g. "Take on an empty stomach", "Take at bedtime".
- **Use the log style to help people log events** — e.g. tap when nauseated; auto-displays a timestamp per logged event.
- **Use the checklist style to display a list of actions or steps in a multistep task** — e.g. three daily dose times; each item has description + done button; optional instructional text below.
- **Use the grid style to display a grid of buttons in a multistep task** — more compact than checklist; succinct title per button (use checklist if more description needed); optional instructional text below; exposes underlying collection view for custom UI.
- **Consider using color to reinforce the meaning of task items** — e.g. one color for medications, another for physical activities; always avoid color as the only way to convey information.
- **Combine accuracy with simplicity when describing a task and its steps** — use a medication's marketing name, not chemical description; minimize words when context clarifies (e.g. omit repeated "take").
- **Consider supplementing multistep or complex tasks with videos or images** — helps avoid mistakes.

### Charts
- Show current and historical data; update automatically. Three styles (CareKit 2.0): bar, scatter, line; supply title, subtitle, axis markers (e.g. days of week), data set.
- **Consider highlighting narratives and trends to illustrate progress** — e.g. medication count vs. pain level; encourages adherence.
- **Label chart elements clearly and succinctly** — short labels, no repetition (e.g. *BPM* in axis label, not on every point).
- **Use distinct colors** — avoid different shades of the same color for different meanings; ensure sufficient contrast.
- **Consider providing a legend to add clarity** — when color meanings aren't immediately clear.
- **Clearly denote units of time** — seconds…years; in value labels, axis label, or elsewhere on the chart.
- **Consolidate large data sets for greater readability** — group and organize data.
- **If necessary, offset data to keep charts proportional** — restructure so small points aren't lost next to very large ones.

### Contact views
- Two styles (CareKit 2.0): simple (glyph, name, practice type, disclosure) and detailed (adds info plus call, message, email, directions buttons).
- **Consider using color to categorize care team members.**

### Notifications
- Used for medication/task reminders; badge for unread caregiver messages; also appear on Apple Watch.
- **Minimize notifications** — use sparingly; consider coalescing multiple items into one notification.
- **Consider providing a detail view** — lets people act without opening the app, e.g. mark pending tasks complete.

### Symbols and branding
- CareKit built-in symbols (phone, messaging, envelope in contact views; clock in log tasks). Most styles work best with CareKit symbols; exception: grid-style task can show custom UI.
- For custom symbols in grid views (e.g. pill for medication, person walking for exercise), consider SF Symbols — coordinates with CareKit visual language and supports custom symbols.
- **Design a relevant care symbol** — related to your app or health/wellness; avoid purely decorative symbols or corporate logos.
- **Incorporate refined, unobtrusive branding** — no advertising; express brand subtly via color and communication style.

## Platform considerations
No additional considerations: iOS, iPadOS. Not supported in macOS, tvOS, visionOS, watchOS.

## APIs
CareKit (CareKit UI, CareKit Store), `HKHealthStore.requestAuthorization(toShare:read:completion:)` (HealthKit), Core Motion, `UIImagePickerController` (UIKit), CareKit Chart Interfaces, ResearchKit

## Related
healthkit, researchkit, notifications, sf-symbols, color, accessibility, charts, privacy
