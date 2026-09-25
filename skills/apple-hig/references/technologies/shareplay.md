# SharePlay

> Source: https://developer.apple.com/design/human-interface-guidelines/shareplay · SharePlay lets people experience activities together from anywhere — watching a movie, playing a game, or sketching on a whiteboard.

## When to use / core idea
- An *activity* is a shareable experience your app offers; participants use their own devices; the system keeps it in sync and works alongside FaceTime or Messages.
- Starts from an in-app control, a FaceTime call, or a shared link. System asks each participant to open your app and invites those without it to download it.
- **Note:** for bought/subscribed content, each participant needs their own copy/subscription; the system prompts those without access.
- For asynchronous collaboration, pair with shared content collaboration (Shared with You).

## Rules
### Best practices
- **Use SharePlay for real-time experiences** — for asynchronous work, let people share or save the activity after the session (e.g., Freeform board then share a link).
- **Design an experience that best fits what people are doing together** — one shared view for watching/browsing; role-adapted views (e.g., per-player perspective in games) where richer.
- **Design activities that work across Apple platforms** — different devices, settings, and communication methods.
- **Make it easy to start a shared activity** — clear, recognizable entry like a button with the SharePlay symbol (e.g., "Start Activity"); also share sheet; in visionOS, the Share button next to the window bar.
- **Let people join an activity without friction** — get to shared content fast; avoid unrelated views. Guide sign-in/download/subscribe in a view that dismisses when done; offer provisional access to nonsubscribers or support Family Sharing; defer nonessential steps (join the match now, set up profile later).
- **Describe activities clearly and concisely** — e.g., movie title, short summary, poster; brief enough to avoid truncation.
- **Keep people oriented as an activity changes** — system coordinates media playback (one pauses, all pause); for other changes use in-app cues showing who's doing what (e.g., Freeform shows participant initials by contributions).
- **Use the term *SharePlay* correctly** — noun ("Join SharePlay") or verb in UI ("SharePlay Movie" button). Don't pair with an adjective (in visionOS avoid *virtual*, *spatial*); don't alter it (*SharePlayed*, *SharePlays*, *SharePlaying*).

## Platform considerations
No additional considerations: tvOS. Not supported in watchOS.

### iOS, iPadOS, macOS
- **Support Picture in Picture for shared video** — iPhone/iPad: PiP window; Mac: keeps playing in a window people bring forward.

### visionOS
- Standard windows are shareable via screen mirroring by default (Share button); adopt SharePlay to share volumetric windows and immersive content.
- System creates a *shared context* so everyone sees content in the same relative location; align windows/volumes across devices; position 3D objects, sounds, and interactions to strengthen togetherness.
- **Prefer starting your experience from a window** — windows are shareable via the Share button next to the window bar; activities starting in an immersive space need custom UI to start.
- **Resolve conflicts naturally** — if only one person can use a tool/object at a time, don't show UI letting someone else take control; let people speak/gesture for turns; consider a simple rule like last change wins.
- **Reserve unique views for moments that call for them** — generally keep views and immersion levels in sync. When someone enters their own immersive view, replace their spatial Persona with a contact photo and keep FaceTime Audio going.
- **Let people opt in to immersion changes when they're mid-task** — if a change would interrupt someone, prompt them to join when ready (e.g., Apple TV app: people busy in another window get a join prompt; others transition immediately).
- **Let participants customize their experience for personal comfort and accessibility needs** — volume, subtitles; keep per-participant.
- **Make it easy to leave and rejoin** — clear rejoin control; a windowed version lets people multitask while staying connected with FaceTime Audio.

#### Personas
- Remote Vision Pro users may appear as spatial Personas (eye contact, gestures, movement); without a Persona, a contact photo. iPhone, iPad, Mac, Apple TV participants appear as 2D video windows. Co-located Vision Pro users see shared content in the same physical place and each other via passthrough.
- **Support people who aren't represented by a spatial Persona** — other devices, Persona turned off, windowed FaceTime; if your experience relies on facial expressions/gestures, offer UI alternatives.

#### Spatial templates
- Arrange participants (seats with position and facing) around content; adopt the best-fitting system template or create a custom one.
  - **Side-by-side** — next to each other along a curve facing content; for watching; less nonverbal interaction, focus on content.
  - **Surround** — circle around content; for tabletop games/centralized experiences, esp. 3D or per-participant content; encourages verbal and nonverbal interaction.
  - **Conversational** — circle around a center point with content on the circle's edge; not everyone sees content equally; for being together while the app works in the background (e.g., music).
- **Divide a complex activity into stages** — a template per stage (team selection vs. play); mixing system and custom templates is preferable to one complex custom template.
- **Let people initiate template transitions** — tie changes to explicit actions (e.g., choosing a team).
- **Keep template transitions smooth** — avoid frequent transitions or excessive movement; fade out and back in when moving seats/roles; provide visual cues to reorient.

#### Custom templates
- Seats apply only to spatial Persona users in visionOS; people on other platforms participate without a seat.
- **Account for people who are physically together** — templates can move remote Personas but not physically present people; guide with visual cues like position markers.
- **Provide the best seat orientation for your content** — default faces content center; direction is fully controllable.
- **Support the maximum number of seats** — up to five spatial Personas; include five seats whenever possible; define every seat up front and keep seats after people leave. With participant limits (e.g., two-player), consider spectator seats.
- **Place seats at least a meter apart** — Personas too close are replaced with contact photos, breaking presence (handshakes/high fives still OK).
- **Define the order in which people take seats** — seats fill in join order; order for balance when partially occupied (left-to-right can feel unbalanced).
- **Keep roles independent of seats** — roles (player, spectator, team member) must work for people without seats; let people fill any open seat; reserve a specific spot only when a role truly requires it (e.g., game host at head of table).

## Specs
- visionOS: up to 5 spatial Personas per activity → 5 seats; seats ≥ 1 meter apart.

## APIs
`Adding shared content collaboration to your app` (sharedwithyou), `Presenting SharePlay activities from your app’s UI` (Group Activities), `Synchronizing data during a SharePlay activity` (Group Activities), `Implementing SharePlay for immersive spaces in visionOS` (visionOS), `Adding spatial Persona support to an activity` (Group Activities), `Configure your visionOS app for sharing with people nearby` (Group Activities), `Adopt the spatial template` (Group Activities), `Building a guessing game for visionOS` (Group Activities), `SpatialTemplateSeatElement` (Group Activities), `isSpatial` (Group Activities), `isNearbyWithLocalParticipant` (Group Activities), `Group Activities` (Group Activities)

## Related
immersive-experiences, activity-views, playing-video, collaboration-and-sharing, spatial-layout
