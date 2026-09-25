# Game Center

> Source: https://developer.apple.com/design/human-interface-guidelines/game-center · Apple's social gaming network: players track progress and connect with friends across Apple platforms, and it boosts your game's discovery.

## When to use / core idea
- Lets players discover games friends play, invite friends, and see game activity across the system (Apple Games app, App Store, notifications).
- Integrate via GameKit: system full-featured UI, or present Game Center data in custom UI.
- At launch, check whether the player is signed in to Game Center; if not, initialize the player then — most seamless and maximizes discovery (Top Played chart, friend recommendations).
- Features: access point, achievements, leaderboards (classic/recurring, sets), challenges, multiplayer activities (real-time and turn-based, party codes).

## Rules
### Integrating the access point
- *Access point*: Apple-designed UI element for viewing Game Center profile/info without leaving the game. iOS/iPadOS/macOS → opens the **Game Overlay** (full screen on iPhone, vertical on trailing edge on iPad); visionOS/tvOS → opens the full-screen **dashboard** over the game.
- **Display the access point in menu screens** — consider main menu or settings; avoid during active gameplay, temporary splash screens, cinematics, or tutorials before the main menu.
- **Avoid placing controls near the access point** — fixed position at any of four screen corners; has collapsed and expanded versions — check overlap with important UI and adjust layout. (visionOS: locations vary by game type, e.g. immersive vs. volume-based.)
- **Consider pausing your game while the Game Overlay or dashboard is present.**

### Using custom UI
- Custom links can deep-link into the Game Overlay (iOS, iPadOS, macOS) or dashboard (visionOS, tvOS), e.g. leaderboards, Game Center profile.
- **Use the artwork Game Center provides in custom links** — official Apple Design Resources artwork; preserve appearance; don't adjust dimensions or visual effects.
- **Use the correct terminology in custom links:**

| Term | Incorrect terms | Localization |
|---|---|---|
| Game Center | GameKit, GameCenter, game center | Use system-provided translation of *Game Center* |
| Game Center Profile | Profile, Account, Player Info | System translation of *Game Center*; localize *Profile* |
| Achievements | Awards, Trophies, Medals | |
| Leaderboards | Rankings, Scores, Leaders | |
| Challenges | Competitions | |
| Add Friends | Add, Add Profiles, Include Friends | |

### Achievements
- Shown as collectible cards highlighting progress and artwork.
- **Align with Game Center achievement states** — four states: locked, in-progress, hidden, completed. System groups completed into Completed, all others into Locked.
- **Determine a display order** — upload order = display order (e.g. follow the most common path through the game).
- **Be succinct when describing achievements** — title and description max two lines each, truncated beyond. Title-style capitalization for titles; sentence-style for descriptions.
- **Give players a sense of progress** — progressive achievements show progress and system encouragement (e.g. "You're more than halfway to completing…").
- **Design rich, high-quality images that help players feel rewarded** — avoid reusing one asset for multiple achievements; missing asset → placeholder image.
- **Create artwork in the appropriate size and format** — circular mask applied; keep content centered (specs below).

### Leaderboards
- Players compare against friends and global players; notified when friends challenge them or pass their score. System UI or custom UI.
- **Choose a leaderboard type:**
  - *Classic* — best all-time score; always active, no end (e.g. most perfect rhythm score, most coins in a single dungeon run, longest time in an endless runner).
  - *Recurring* — resets on an interval you define (daily, weekly); more chances to lead (e.g. daily rotating puzzles, seasonal/holiday events, weekly boards per battle mode).
- **Take advantage of leaderboard sets for multiple leaderboards** — group by difficulty modes (Easy, Standard, Hard), activity types (Combat, Crafting, Farming), genres/themes (Disco, Pop, Rock).
- **Add leaderboard images** — unique image per leaderboard reflecting its gameplay. iOS/iPadOS/macOS: a single image; tvOS: a set of layered images that animate in focus (use Apple Design Resources tvOS template).
- Cropping: iOS/iPadOS/macOS crop artwork for leaderboards in a set; tvOS focus effect may crop layer edges — keep primary content comfortably visible.

### Challenges
- Built on leaderboards; time-limited competitions among friends turning single-player activities multiplayer.
- **Create engaging challenges** — short, skill-based, clearly measurable; 1–5 minutes; completable individually (e.g. fastest lap, most enemies in a round, daily puzzle with fewest mistakes).
- **Avoid creating challenges that track overall progress or personal best scores** — unfair to newcomers; track the most recent score after each attempt.
- **Make it easy to jump into your challenge** — accessible via invitation links, Game Overlay, Games app (iOS, iPadOS, macOS). Always deep-link to the exact mode/level; complete first-time onboarding first (e.g. tutorial), with UI saying the game will jump into the challenge afterward.
- **Create high-quality artwork that encourages players to engage** — shown in Game Overlay, Games app, invitation link previews; keep primary content away from where title/description overlay (system gradient at card bottom); localize any text via App Store Connect or Xcode.

### Multiplayer activities
- Real-time and turn-based; accessed via party codes, Game Overlay, dashboard, Games app.
- **Use party codes to invite players to multiplayer activities** — work with Game Center matchmaking/networking or your own; alphanumeric, typically eight characters (e.g. "2MP4-9CMF"). Allow joining late, leaving early, returning later; show the current party code in-game; allow manual code entry.
- **Support multiplayer activities through in-game UI** — default UI invites nearby/recent players, Game Center friends, contacts; or use custom UI.
- **Provide engaging activity artwork** — preview image appears in party codes, Games app, in-game UI.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, visionOS.
### tvOS
- **Display an optional image at the top of the dashboard** — simple, recognizable at a distance; consider game logo or wordmark; don't use your app icon.
### watchOS
- **Be aware of Game Center support on watchOS** — GameKit APIs available, but no system Game Center UI on watchOS; content appears on the connected iPhone.

## Specs
Achievement image — iOS, iPadOS, macOS, visionOS:

| Attribute | Value |
|---|---|
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Mask diameter | 512 pt (1024 px @2x) |

Achievement image — tvOS:

| Attribute | Value |
|---|---|
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 320x320 pt (640x640 px @2x) |
| Mask diameter | 200 pt (400 px @2x) |

Leaderboard image — iOS, iPadOS, macOS:

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 512x512 pt (1024x1024 px @2x) |
| Cropped area | 512x312 pt (1024x624 px @2x) |

Leaderboard image — tvOS:

| Attribute | Value |
|---|---|
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 659x371 pt (1318x742 px @2x) |
| Focused size | 618x348 pt (1236x696 px @2x) |
| Unfocused size | 548x309 pt (1096x618 px @2x) |

Challenge image and multiplayer activity image (identical specs):

| Attribute | Value |
|---|---|
| Format | JPEG, JPG, or PNG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |
| Image size | 1920x1080 pt (3840x2160 px @2x) |
| Cropped area | 1465x767 pt (2930x1534 px @2x) |

tvOS dashboard image:

| Attribute | Value |
|---|---|
| Image size | 600x180 pt (1200x360 px @2x) |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |

- Achievement card: title ≤2 lines, description ≤2 lines.
- Challenge duration: 1–5 minutes.
- Party code: typically 8 alphanumeric characters.

## APIs
GameKit, Adding an access point to your game (GameKit), Rewarding players with achievements, Encourage progress and competition with leaderboards, Creating engaging challenges from leaderboards, Creating activities for your game, Finding multiple players for a game (GameKit)

## Related
designing-for-games, game-controls, focus-and-selection, designing-for-tvos
