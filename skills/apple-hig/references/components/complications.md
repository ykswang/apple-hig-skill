# Complications

> Source: https://developer.apple.com/design/human-interface-guidelines/complications · Displays timely, relevant information on the watch face, viewable each time people raise their wrist.

## When to use / core idea
- People prefer apps with multiple, powerful complications — quick views of data without opening the app. Most watch faces show at least one complication; some four or more.
- watchOS 9+: complications (*accessories*) are organized into families (circular, corner, inline, rectangular) with recommended layouts; each watch face slot specifies its supported family. Earlier watchOS: legacy templates (nongraphic styles that don't take on the wearer's selected color).
- Developer: prefer WidgetKit for watchOS 9+; for earlier versions implement ClockKit `CLKComplicationDataSource`.

## Rules
### Best practices
- **Identify essential, dynamic content that people want to view at a glance** — up-to-date relevant info is valued more than app launching; static, meaningless complications are less likely to stay prominent.
- **Support all complication families when possible** — more families = more watch faces. If a family can't show useful info, provide an image representing your app (e.g. app icon) that still launches the app.
- **Consider creating multiple complications for each family** — enables shareable watch faces and app-centered faces (e.g. triathlon app: three circular complications — swim, bike, run — each deep-linking; plus a preconfigured shareable face with custom images/colors). See `watch-faces`.
- **Define a different deep link for each complication you support** — open the most relevant area; identical destinations seem less useful.
- **Keep privacy in mind** — Always-On display can expose info to others; help people hide sensitive info (see `always-on`).
- **Carefully consider when to update data** — data is a timeline of entries with display times (meeting app: an hour before; weather: at forecast time). Timeline updates per day and stored entries per app are limited; choose times that maximize usefulness.

### Visual design
- **Choose a ring or gauge style based on the data you need to display:**
  - Closed — value as percentage of a whole (battery).
  - Open — arbitrary min/max, not a percentage (speed).
  - Segmented — app-defined range; conveys rapid value changes (Noise).
- **Make sure images look good in tinted mode** — system applies a solid color to text, gauges, images and desaturates full-color images unless you supply tinted versions (`WidgetRenderingMode`; with legacy templates tinted mode applies only to graphic complications).
  - Avoid using color as the only way to communicate important information.
  - When necessary, provide an alternative tinted-mode version of a full-color image that doesn't desaturate well.
- **Recognize that people might prefer to use tinted mode for complications, instead of viewing them in full color** — system desaturates to grayscale and tints images, gauges, text with one color based on the wearer's selected color.
- **When creating complication content, generally use line widths of two points or greater** — thinner lines are hard to see, especially in motion; match weight to image size/complexity.
- **Provide a set of static placeholder images for each complication you support** — used when no content (e.g. first install, while checking for a localized placeholder) and in the complication selection carousel. Placeholder size may differ from the actual image size (`placeholder(in:)`).

### Circular
- Text, gauges, full-color images in circular areas on Infograph and Infograph Modular; extra-large layouts for the X-Large face (e.g. Contacts with photo — full-color images, text, gauges filling most of the face; some fields support multicolor text).
- Regular-size circular image can have accompanying text curved along the bezel (e.g. Infograph); text fills nearly 180 degrees of the bezel before truncating.
- System applies a circular mask to each regular image; for extra-large, to circular, open-gauge, and closed-gauge images.

### Corner
- Full-color images, text, gauges in watch face corners (e.g. Infograph); some templates support multicolor text. System applies a circular mask to each image.

### Inline
- Utilitarian small: rectangular area in a corner (e.g. Chronograph, Simple); image, interface icon, or circular graph.
- Utilitarian large: primarily text, optional interface icon on the leading side; spans the bottom of the face (e.g. Utility, Motion).

### Rectangular
- Full-color images, text, a gauge, optional title in a large rectangular region; some fields support multicolor text. Good for details of values changing over time — charts, graphs, diagrams (Heart Rate: 24-hour graph, high-contrast white/red for primary content, lower-contrast gray for graph lines/labels).
- watchOS 10+: rectangular layouts may appear in the Smart Stack. Optimize by: background color/content that communicates info or aids recognition; App Intents relevancy so it appears at appropriate times; a custom layout optimized for the Smart Stack (see `widgets`; `WidgetFamily.accessoryRectangular`).
- Both large-image layouts automatically include a 4 pt corner radius.

### Legacy templates
- **Circular small** — small image or a few characters of text, in a corner (e.g. Color face).
- **Modular small** — two stacked rows (icon + content), a circular graph, or a single larger item (e.g. bottom row of Modular face).
- **Modular large** — large canvas, up to three rows of content (e.g. center of Modular face).
- **Extra large** — larger text and images (X-Large faces).
- In stack measurements, the width value is the maximum size.

## Platform considerations
Not supported: iOS, iPadOS, macOS, tvOS, visionOS.

## Specs
Minimum line width: 2 pt.

### Circular — regular-size images
| Image | 40mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- |
| Image | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Closed gauge | 27x27 pt (54x54 px @2x) | 28.5x28.5 pt (57x57 px @2x) | 31x31 pt (62x62 px @2x) | 32x32 pt (64x64 px @2x) |
| Open gauge | 11x11 pt (22x22 px @2x) | 11.5x11.5 pt (23x23 px @2x) | 12x12 pt (24x24 px @2x) | 13x13 pt (26x26 px @2x) |
| Stack (not text) | 28x14 pt (56x28 px @2x) | 29.5x15 pt (59X30 px @2x) | 31x16 pt (62x32px @ 2x) | 33.5x16.5 pt (67x33 px @2x) |

Default SwiftUI text (regular circular): Rounded, Medium; 12 pt (40mm), 12.5 pt (41mm), 13 pt (44mm), 14.5 pt (45mm/49mm).

### Circular — extra-large images
| Image | 40mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- |
| Image | 120x120 pt (240x240 px @2x) | 127x127 pt (254x254 px @2x) | 132x132 pt (264x264 px @2x) | 143x143 pt (286x286 px @2x) |
| Open gauge | 31x31 pt (62x62 px @2x) | 33x33 pt (66x66 px @2x) | 33x33 pt (66x66 px @2x) | 37x37 pt (74x74 px @2x) |
| Closed gauge | 77x77 pt (154x154 px @2x) | 81.5x81.5 (163x163 px @2x) | 87x87 pt (174x174 px @2x) | 91.5x91.5 (183x183 px @2x) |
| Stack | 80x40 pt (160x80 px @2x) | 85x42 (170x84 px @2x) | 87x44 pt (174x88 px @2x) | 95x48 pt (190x96 px @2x ) |

Default SwiftUI text (extra-large circular): Rounded, Medium; 34.5 pt (40mm), 36.5 pt (41mm), 36.5 pt (44mm), 41 pt (45mm/49mm).

### Circular family — no-content placeholders
| Layout | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- | --- |
| Circular | – | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Bezel | – | 42x42 pt (84x84 px @2x) | 44.5x44.5 pt (89x89 px @2x) | 47x47 pt (94x94 px @2x) | 50x50 pt (100x100 px @2x) |
| Extra Large | – | 120x120 pt (240x240 px @2x) | 127x127 pt (254x254 px @2x) | 132x132 pt (264x264 px @2x) | 143x143 pt (286x286 px @2x) |

### Corner
| Image | 40mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- |
| Circular | 32x32 pt (64x64 px @2x) | 34x34 pt (68x68 px @2x) | 36x36 pt (72x72 px @2x) | 38x38 pt (76x76 px @2x ) |
| Gauge | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |
| Text | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |

Corner no-content placeholders:

| 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- |
| – | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22x22 pt (44x44 px @2x) | 24x24 pt (48x48 px @2x) |

Default SwiftUI text (corner): Rounded, Semibold; 10 pt (40mm), 10.5 pt (41mm), 11 pt (44mm), 12 pt (45mm/49mm).

### Inline — utilitarian small
| Content | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- | --- |
| Flat | 9-21x9 pt (18-42x18 px @2x) | 10-22x10 pt (20-44x20 px @2x) | 10.5-23.5x21 pt (21-47x21 @2x) | N/A | 12-26x12 pt (24-52x24 px @2x) |
| Ring | 14x14 pt (28x28 px @2x) | 14x14 pt (28x28 px @2x) | 15x15 pt (30x30 px @2x) | 16x16 pt (32x32 px @2x) | 16.5x16.5 pt (33x33 px @2x) |
| Square | 20x20 pt (40x40 px @2x) | 22x22 pt (44x44 px @2x) | 23.5x23.5 pt (47x47 px @2x) | 25x25 pt (50x50 px @2x) | 26x26 pt (52x52 px @2x) |

### Inline — utilitarian large
| Content | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- | --- |
| Flat | 9-21x9 pt (18-42x18 px @2x) | 10-22x10 pt (20-44x20 px @2x) | 10.5-23.5x10.5 pt (21-47x21 px @2x) | N/A | 12-26x12 pt (24-52x24 px @2x) |

### Rectangular
| Content | 40mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- |
| Large image with title * | 150x47 pt (300x94 px @2x) | 159x50 pt (318x100 px @2x) | 171x54 pt (342x108 px @2x) | 178.5x56 pt (357x112 px @2x) |
| Large image without title * | 162x69 pt (324x138 px @2x) | 171.5x73 pt (343x146 px @2x) | 184x78 pt (368x156 px @2x) | 193x82 pt (386x164 px @2x) |
| Standard body | 12x12 pt (24x24 px @2x) | 12.5x12.5 pt (25x25 px @2x) | 13.5x13.5 pt (27x27 px @2x) | 14.5x14.5 pt (29x29 px @2x) |
| Text gauge | 12x12 pt (24x24 px @2x) | 12.5x12.5 pt (25x25 px @2x) | 13.5x13.5 pt (27x27 px @2x) | 14.5x14.5 pt (29x29 px @2x) |

\* Both large-image layouts automatically include a 4 pt corner radius.

Default SwiftUI text (rectangular): Rounded, Medium; 16.5 pt (40mm), 17.5 pt (41mm), 18 pt (44mm), 19.5 pt (45mm/49mm).

### Legacy — circular small
| Image | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- | --- |
| Ring | 20x20 pt (40x40 px @2x) | 22x22 pt (44x44 px @2x) | 23.5x23.5 pt (47x47 px @2x) | 24x24 pt (48x48 px @2x) | 26x26 pt (52x52 px @2x) |
| Simple | 16x16 pt (32x32 px @2x) | 18x18 pt (36x36 px @2x) | 19x19 pt (38x38 px @2x) | 20x20 pt (40x40 px @2x) | 21.5x21.5 pt (43x43 px @2x) |
| Stack | 16x7 pt (32x14 px @2x) | 17x8 pt (34x16 px @2x) | 18x8.5 pt (36x17 px @2x) | 19x9 pt (38x18 px @2x) | 19x9.5 pt (38x19 px @2x) |
| Placeholder | 16x16 pt (32x32 px @2x) | 18x18x pt (36x36 px @2x) | 19x19 pt (38x38 px @2x) | 20x20 pt (40x40 px @2x) | 21.5x21.5 pt (43x43 px @2x) |

### Legacy — modular small
| Image | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- | --- |
| Ring | 18x18 pt (36x36 px @2x) | 19x19 pt (38x38 px @2x) | 20x20 pt (40x40 px @2x) | 21x21 pt (42x42 px @2x) | 22.5x22.5 pt (45x45 px @2x) |
| Simple | 26x26 pt (52x52 px @2x) | 29x29 pt (58x58 px @2x) | 30.5x30.5 pt (61x61 px @2x) | 32x32 pt (64x64 px @2x) | 34.5x34.5 pt (69x69 px @2x) |
| Stack | 26x14 pt (52x28 px @2x) | 29x15 pt (58x30 px @2x) | 30.5x16 pt (61x32 px @2x) | 32x17 pt (64x34 px @2x) | 34.5x18 pt (69x36 px @2x) |
| Placeholder | 26x26 pt (52x52 px @2x) | 29x29 pt (58x58 px @2x) | 30.5x30.5 pt (61x61 px @2x) | 32x32 pt (64x64 px @2x) | 34.5x34.5 pt (69x69 px @2x) |

### Legacy — modular large
| Content | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- | --- |
| Columns | 11-32x11 pt (22-64x22 px @2x) | 12-37x12 pt (24-74x24 px @2x) | 12.5-39x12.5 pt (25-78x25 px @2x) | 14-42x14 pt (28-84x28 px @2x) | 14.5-44x14.5 pt (29-88x29 px @2x) |
| Standard body | 11-32x11 pt (22-64x22 px @2x) | 12-37x12 pt (24-74x24 px @2x) | 12.5-39x12.5 pt (25-78x25 px @2x) | 14-42x14 pt (28-84x28 px @2x) | 14.5-44x14.5 pt (29-88x29 px @2x) |
| Table | 11-32x11 pt (22-64x22 px @2x) | 12-37x12 pt (24-74x24 px @2x) | 12.5-39x12.5 pt (25-78x25 px @2x) | 14-42x14 pt (28-84x28 px @2x) | 14.5-44x14.5 pt (29-88x29 px @2x) |

### Legacy — extra large
| Image | 38mm | 40mm/42mm | 41mm | 44mm | 45mm/49mm |
| --- | --- | --- | --- | --- | --- |
| Ring | 63x63 pt (126x126 px @2x) | 66.5x66.5 pt (133x133 px @2x) | 70.5x70.5 pt (141x141 px @2x) | 73x73 pt (146x146 px @2x) | 79x79 pt (158x158 px @2x) |
| Simple | 91x91 pt (182x182 px @2x) | 101.5x101.5 pt (203x203 px @2x) | 107.5x107.5 pt (215x215 px @2x) | 112x112 pt (224x224 px @2x) | 121x121 pt (242x242 px @2x ) |
| Stack | 78x42 pt (156x84 px @2x) | 87x45 pt (174x90 px @2x) | 92x47.5 pt (184x95 px @2x) | 96x51 pt (192x102 px @2x) | 103.5x53.5 pt (207x107 px @2x) |
| Placeholder | 91x91 pt (182x182 px @2x) | 101.5x101.5 pt (203x203 px @2x) | 107.5x107.5 pt (215x215 px @2x) | 112x112 pt (224x224 px @2x) | 121x121 pt (242x242 px @2x) |

## APIs
WidgetKit, `WidgetRenderingMode` (WidgetKit), `WidgetFamily.accessoryRectangular` (WidgetKit), `TimelineProvider.placeholder(in:)` (WidgetKit), `CLKComplicationDataSource` (ClockKit, pre-watchOS 9), App Intents (relevancy)

## Related
`watch-faces, widgets, always-on`
