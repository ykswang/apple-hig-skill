# Top Shelf

> Source: https://developer.apple.com/design/human-interface-guidelines/top-shelf · Apple TV Home Screen area that showcases your content richly while giving access to favorite apps in the Dock.

## When to use / core idea
- Full-screen Top Shelf: people swipe through multiple full-screen content views, play trailers/previews, get more info. Highlight new, featured, or recommended content and deep-link into your app/game.
- E.g. selecting Apple TV in the Dock: full-screen previews start playing, Dock slides away; people swipe between featured shows and choose Play or More Info.
- System layout templates are available (download from Apple Design Resources).

## Rules
### Best practices
- **Help people jump right into your content** — carousel actions and carousel details templates include two buttons by default: primary (begin playback) and More Info (open app to a details view).
- **Feature new content** — new releases/episodes, upcoming movies/shows; avoid promoting content already purchased, rented, or watched.
- **Personalize people's favorite content** — targeted recommendations; resume media playback or jump back into active gameplay.
- **Avoid showing advertisements or prices** — purchasable content is fine, but prefer focus on new/exciting content; consider showing prices only when people show interest.
- **Showcase compelling dynamic content that can help draw people in and encourage them to view more** — static images allowed if necessary, but prefer dynamic; prefer layered images.
- **If you don't provide the recommended full-screen content, supply at least one static image as a fallback** — shown when the app is in the Dock and in focus and full-screen content is unavailable; tvOS flips and blurs it to fit a 1920 px width at 16:9.
- **Avoid implying interactivity in a static image** — a static Top Shelf image isn't focusable.

### Dynamic layouts
- Forms: carousel of full-screen video/images with two buttons and optional details; row of focusable content; set of scrolling banners.

#### Carousel actions
- Full-screen video/images with unobtrusive controls; best for content people already know (user-generated photos, new content from a known franchise/show).
- **Provide a title** — succinct (show/movie or album title); optional brief subtitle (album date range; show name for an episode).

#### Carousel details
- Extends carousel actions with info (plot summary, cast list, metadata).
- **Provide a title that identifies the currently playing content** — appears near the top; above it you can add a succinct phrase or app attribution (e.g. "Featured on *My App*").

#### Sectioned content row
- Single labeled row of sectioned content (recently viewed, new, favorites); focusable, fast scrolling; label appears on focus; small Touch-surface movements animate the focused image; can show multiple labels.
- **Provide enough content to constitute a complete row** — at minimum enough images to span full screen width; include at least one label.
- **Be aware of additional scaling when combining image sizes** — mixed sizes scale up to match the tallest image; e.g. a 16:9 image scales to 500 px high in a row with poster or square images.

#### Scrolling inset banner
- Large images spanning almost the full width; auto-scroll on a preset timer until one is focused; loops back after the last. Focused banner: small circular Touch-surface gesture → system focus effect (animation, lighting, 3D for layered images); swipe pans to next/previous. For rich content like a popular new movie.
- **Provide three to eight images** — minimum three to feel effective; more than eight makes navigating to a specific image hard.
- **If you need text, add it to your image** — no labels under content; in layered images consider putting text on a dedicated top layer; also add the text to the image's accessibility label for VoiceOver.

## Platform considerations
Not supported: iOS, iPadOS, macOS, visionOS, watchOS.

## Specs
Static fallback image:

| Image size |
| --- |
| 2320x720 pt (2320x720 px @1x, 4640x1440 px @2x) |

Sectioned content row — Poster (2:3):

| Aspect | Image size |
| --- | --- |
| Actual size | 404x608 pt (404x608 px @1x, 808x1216 px @2x) |
| Focused/Safe zone size | 380x570 pt (380x570 px @1x, 760x1140 px @2x) |
| Unfocused size | 333x570 pt (333x570 px @1x, 666x1140 px @2x) |

Sectioned content row — Square (1:1):

| Aspect | Image size |
| --- | --- |
| Actual size | 608x608 pt (608x608 px @1x, 1216x1216 px @2x) |
| Focused/Safe zone size | 570x570 pt (570x570 px @1x, 1140x1140 px @2x) |
| Unfocused size | 500x500 pt (500x500 px @1x, 1000x1000 px @2x) |

Sectioned content row — 16:9:

| Aspect | Image size |
| --- | --- |
| Actual size | 908x512 pt (908x512 px @1x, 1816x1024 px @2x) |
| Focused/Safe zone size | 852x479 pt (852x479 px @1x, 1704x958 px @2x) |
| Unfocused size | 782x440 pt (782x440 px @1x, 1564x880 px @2x) |

Scrolling inset banner:

| Aspect | Image size |
| --- | --- |
| Actual size | 1940x692 pt (1940x692 px @1x, 3880x1384 px @2x) |
| Focused/Safe zone size | 1740x620 pt (1740x620 px @1x, 3480x1240 px @2x) |
| Unfocused size | 1740x560 pt (1740x560 px @1x, 3480x1120 px @2x) |

## APIs
None listed on the page.

## Related
`images, voiceover`
