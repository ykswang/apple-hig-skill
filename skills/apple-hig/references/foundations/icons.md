# Icons

> Source: https://developer.apple.com/design/human-interface-guidelines/icons · An effective icon is a graphic asset that expresses a single concept in ways people instantly understand.

## When to use / core idea
- *Interface icons* (a.k.a. *glyphs*) use streamlined shapes and touches of color to communicate items, actions, modes — unlike `app-icons`, which use rich shading/texture/highlights.
- Design your own or use SF Symbols (as-is or customized). Both use black and clear to define shape; the system can recolor the black areas.
- Prefer the standard SF Symbols below for common actions in menus, toolbars, buttons.

## Rules
### Best practices
- **Create a recognizable, highly simplified design** — too much detail confuses; use familiar metaphors directly tied to the action/content.
- **Maintain visual consistency across all interface icons in your app** — custom or mixed with system icons: consistent size, level of detail, stroke thickness (weight), perspective. Adjust dimensions for visual weight (e.g., a lighter icon may need to extend taller to balance).
- **In general, match the weights of interface icons and adjacent text** — unless you want to emphasize one.
- **If necessary, add padding to a custom interface icon to achieve optical alignment** — asymmetric icons (e.g., download arrow, heavier at bottom) look off when geometrically centered. Nudge until optically centered, then bake the adjustment as padding in the asset so geometric centering of the asset yields optical centering. Adjustments are tiny but impactful.
- **Provide a selected-state version of an interface icon only if necessary** — not needed for standard components (toolbars, tab bars, buttons); system renders selected state automatically.
- **Use inclusive images** — prefer gender-neutral human figures; avoid culture- or language-specific imagery.
- **Include text in your design only when it's essential for conveying meaning** — e.g., a character for text formatting. Localize any characters; for a passage of text use an abstract representation and provide a flipped version for right-to-left contexts.
- **If you create a custom interface icon, use a vector format like PDF or SVG** — system scales vectors for high-res displays. PNG (for app icons/images with shading, texture, highlights) doesn't scale, so you'd need multiple versions. Alternatively create a custom SF Symbol with a scale matching adjacent text emphasis.
- **Provide alternative text labels for custom interface icons** — invisible accessibility descriptions for VoiceOver.
- **Avoid using replicas of Apple hardware products** — they date quickly; if needed, use only Apple Design Resources images or SF Symbols for Apple products.

### Standard icons (SF Symbols for common actions)

#### Editing
| Action | Symbol name |
| --- | --- |
| Cut | `scissors` |
| Copy | `document.on.document` |
| Paste | `document.on.clipboard` |
| Done, Save | `checkmark` |
| Cancel, Close | `xmark` |
| Delete | `trash` |
| Undo | `arrow.uturn.backward` |
| Redo | `arrow.uturn.forward` |
| Compose | `square.and.pencil` |
| Duplicate | `plus.square.on.square` |
| Rename | `pencil` |
| Move to, Folder | `folder` |
| Attach | `paperclip` |
| Add | `plus` |
| More | `ellipsis` |

#### Selection
| Action | Symbol name |
| --- | --- |
| Select | `checkmark.circle` |
| Deselect, Close | `xmark` |
| Delete | `trash` |

#### Text formatting
| Action | Symbol name |
| --- | --- |
| Superscript | `textformat.superscript` |
| Subscript | `textformat.subscript` |
| Bold | `bold` |
| Italic | `italic` |
| Underline | `underline` |
| Align Left | `text.alignleft` |
| Center | `text.aligncenter` |
| Justified | `text.justify` |
| Align Right | `text.alignright` |

#### Search
| Action | Symbol name |
| --- | --- |
| Search | `magnifyingglass` |
| Find, Find and Replace, Find Next, Find Previous, Use Selection for Find | `text.page.badge.magnifyingglass` |
| Filter | `line.3.horizontal.decrease` |

#### Sharing and exporting
| Action | Symbol name |
| --- | --- |
| Share, Export | `square.and.arrow.up` |
| Print | `printer` |

#### Users and accounts
| Action | Symbol name |
| --- | --- |
| Account, User, Profile | `person.crop.circle` |

#### Ratings
| Action | Symbol name |
| --- | --- |
| Dislike | `hand.thumbsdown` |
| Like | `hand.thumbsup` |

#### Layer ordering
| Action | Symbol name |
| --- | --- |
| Bring to Front | `square.3.layers.3d.top.filled` |
| Send to Back | `square.3.layers.3d.bottom.filled` |
| Bring Forward | `square.2.layers.3d.top.filled` |
| Send Backward | `square.2.layers.3d.bottom.filled` |

#### Other
| Action | Symbol name |
| --- | --- |
| Alarm | `alarm` |
| Archive | `archivebox` |
| Calendar | `calendar` |

## Platform considerations
No additional considerations: iOS, iPadOS, tvOS, visionOS, watchOS.

### macOS — Document icons
- For custom document types; traditional look = paper with top-right corner folded down, distinguishing documents from apps even at small sizes.
- If you supply none, macOS composites your app icon and the file extension onto the canvas (e.g., Preview's JPG icon). You can create a set for multiple file types (e.g., Xcode: projects, AR objects, Swift files).
- Supply any combination of **background fill**, **center image**, and **text**; the system layers, positions, masks, and composites them onto the folded-corner shape.
- **Design simple images that clearly communicate the document type** — uncomplicated shapes, reduced palette of distinct colors; icon can be as small as **16x16 px**.
- **Designing a single, expressive image for the background fill can be a great way to help people understand and recognize a document type** — e.g., Xcode, TextEdit use rich backgrounds with no center image.
- **Consider reducing complexity in the small versions of your document icon** — e.g., fewer, thicker pixel-aligned grid lines at intermediate sizes; remove them at 16x16 px.
- **Avoid placing important content in the top-right corner of your background fill** — system masks the image and draws the white folded corner over it.
- **If a familiar object can convey a document's type or its connection with your app, consider creating a center image that depicts it** — simple, unambiguous, clear at every size; center image = half the document icon canvas (e.g., 16x16 px for a 32x32 px icon).
- **Define a margin that measures about 10% of the image canvas and keep most of the image within it** — image should occupy about 80% of the canvas; parts may extend into the margin for optical alignment (e.g., 256x256 px canvas → ~205x205 px content).
- **Specify a succinct term if it helps people understand your document type** — system shows the extension at the bottom edge by default; supply a descriptive term for unfamiliar extensions (e.g., *scene* instead of *scn*). Text auto-scales to fit and is all-caps by default; keep it short.

## Specs
### Document icon background fill sizes
- 512x512 px @1x, 1024x1024 px @2x
- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x

### Document icon center image sizes (half the canvas)
- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x

### Other values
- Center image margin ≈ 10% of canvas; content ≈ 80% (256 px → ~205x205 px). Smallest document icon: 16x16 px.
- Custom interface icon format: PDF or SVG (vector); PNG requires multiple resolutions.

## APIs
SF Symbols (custom symbols), accessibility labels (VoiceOver)

## Related
app-icons, sf-symbols, inclusion, right-to-left, voiceover, menus, toolbars, buttons
