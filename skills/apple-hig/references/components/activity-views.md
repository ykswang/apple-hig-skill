# Activity views

> Source: https://developer.apple.com/design/human-interface-guidelines/activity-views · An activity view — often called a *share sheet* — presents a range of tasks people can perform in the current context.

## When to use / core idea
- Presents sharing activities (e.g., messaging), actions (Copy, Print), and quick access to frequently used apps. Revealed by choosing an Action/Share button while viewing a page or document, or after selecting an item. Appears as a sheet or popover depending on device and orientation.
- Apps can provide app-specific activities (e.g., Photos: Copy Photo, Add to Album, Adjust Location). By default the system lists app-specific actions before cross-app/system actions (Add to Files, AirPlay). People can edit the list and add actions.
- *App extensions* (code people install and use outside your app) provide custom share and action activities usable in other apps. macOS has no activity view, but supports share and action extensions.

## Rules
### Best practices
- **Avoid creating duplicate versions of common actions already available in the activity view** — e.g., a duplicate Print is confusing. For similar app-specific functionality, give it a custom title (e.g., "Print Transaction").
- **Consider using a symbol to represent your custom activity** — SF Symbols; a custom interface icon should be centered in an area about **70x70 pixels**.
- **Write a succinct, descriptive title for each custom action** — long titles wrap and may truncate. Prefer a single verb or brief verb phrase. Avoid company or product names in action titles. (Share activities, by contrast, show their title — typically a company name — below the icon.)
- **Make sure activities are appropriate for the current context** — you can't reorder system tasks, but can exclude inapplicable ones (e.g., Print) and choose which custom tasks show at a given time.
- **Use the Share button to display an activity view** — people expect it; avoid providing an alternative way to do the same thing.

### Share and action extensions
- Share extensions share info from the current context with apps, social accounts, services. Action extensions initiate content-specific tasks (add bookmark, copy link, edit inline image, translate selected text) without leaving context.
- iOS/iPadOS: both appear in the share sheet from an Action button. macOS: share extensions via a toolbar Share button or Share in a context menu; action extensions by hovering over certain embedded content (e.g., an image in a Mail compose window), a toolbar button, or a Finder quick action.
- **If necessary, create a custom interface that feels familiar** — for share extensions prefer the system-provided composition view; for action extensions include your app name. If presenting an interface, include elements of your app's UI to show the relationship.
- **Streamline and limit interaction** — a few steps; e.g., post an image with a single tap/click.
- **Avoid placing a modal view above your extension** — the system already shows extensions modally; an alert may be necessary, but avoid additional modal views.
- **If necessary, provide an image that communicates the purpose of your extension** — share extensions automatically use your app icon; for action extensions prefer a symbol or an interface icon that clearly identifies the task.
- **Use your main app to denote the progress of a lengthy operation** — the activity view dismisses immediately on completion; continue long tasks in the background with status viewable in the main app. A notification can report a problem, but don't notify simply because the task completes.

## Platform considerations
No additional considerations: iOS, iPadOS, visionOS. Not supported: macOS, tvOS, watchOS (macOS supports share/action extensions only).

## Specs
- Custom activity interface icon: centered in an area of about 70x70 pixels.

## APIs
`UIActivityViewController` (UIKit), `UIActivity` (UIKit), App Extension Support (Foundation)

## Related
sheets, popovers, sf-symbols, icons, buttons
