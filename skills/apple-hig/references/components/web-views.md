# Web views

> Source: https://developer.apple.com/design/human-interface-guidelines/web-views · A web view loads and displays rich web content, such as embedded HTML and websites, directly within your app.

## When to use / core idea
- Show web content inside the app without leaving its context (e.g., Mail renders HTML message content in a web view).
- For general browsing, send people to Safari rather than building a browser.

## Rules
### Best practices
- **Support forward and back navigation when appropriate** — not enabled by default; if people are likely to visit multiple pages, enable it and provide controls to trigger it.
- **Avoid using a web view to build a web browser** — brief website access in-context is fine; replicating Safari is unnecessary and discouraged.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, visionOS. Not supported: tvOS, watchOS.

## APIs
`WKWebView` (WebKit).

## Related
None listed on the page.

