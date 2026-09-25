# Motion

> Source: https://developer.apple.com/design/human-interface-guidelines/motion · Fluid motion conveys status, provides feedback and instruction, and enriches the visual experience of an app or game.

## When to use / core idea
- Prefer system components: they include motion automatically and adapt it to accessibility settings and input methods (e.g., Liquid Glass responds to direct touch with greater emphasis, more subdued with a trackpad).
- Follow these rules only when designing custom motion.
- Motion must never be the sole channel for important information — pair with haptics (playing-haptics) and audio (playing-audio).

## Rules

### Best practices
- **Add motion purposefully, supporting the experience without overshadowing it** — don't add motion for its own sake; gratuitous or excessive animation distracts and can cause disconnection or physical discomfort.
- **Make motion optional** — never use it as the only way to communicate important information; supplement with haptics and audio.

### Providing feedback
- **Strive for realistic feedback motion that follows people's gestures and expectations** — in nongame apps, nonsensical motion disorients (e.g., a view revealed by sliding down from the top shouldn't dismiss by sliding sideways).
- **Aim for brevity and precision in feedback animations** — brief, precise feedback feels lightweight and communicates better than prominent animation (e.g., succinct animation tied to a successful game action; visionOS Photos panorama expanding quickly and smoothly on tap).
- **In apps, generally avoid adding motion to UI interactions that occur frequently** — the system already animates standard elements subtly; don't make people watch unnecessary motion on every interaction with a custom element.
- **Let people cancel motion** — as much as possible, don't make people wait for an animation to complete before acting, especially for animations they'll see more than once.
- **Consider using animated symbols where it makes sense** — SF Symbols 5 or later supports animating SF Symbols and custom symbols (see sf-symbols Animations).

### Leveraging platform capabilities
- **Make sure your game's motion looks great by default on each platform you support** — a consistent 30–60 fps typically looks smooth; use each device's graphics capabilities to set good defaults so people needn't change settings first.
- **Let people customize the visual experience of your game to optimize performance or battery life** — e.g., consider letting people switch power modes when the system detects an external power source.

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS.

### visionOS
- Motion combines with depth to give essential feedback when people look at interactive elements; since motion is a large part of visionOS, avoid distraction, confusion, or discomfort.
- **As much as possible, avoid displaying motion at the edges of a person's field of view** — peripheral motion distracts and can make people feel they or their surroundings are moving. If you must show peripheral motion in an immersive experience, keep the object's brightness similar to the rest of the visible content.
- **Help people remain comfortable when showing the movement of large virtual objects** — objects filling much of the field of view / occluding passthrough can be perceived as part of the surroundings; increase translucency or lower contrast to make motion less noticeable.
  - Note: discomfort can occur even when the person moves the large object (e.g., a window); adjust translucency/contrast and consider keeping window size fairly small.
- **Consider using fades when you need to relocate an object** — if the movement communicates nothing useful, fade out, move, fade back in.
- **In general, avoid letting people rotate a virtual world** — rotation upsets sense of stability even when user-controlled and subtle; instead consider instantaneous directional changes during a quick fade-out.
- **Consider giving people a stationary frame of reference** — contain visual movement within a non-moving area; if the entire surroundings appear to move (e.g., auto-moving the player through space) people can feel unwell.
- **Avoid showing objects that oscillate in a sustained way** — especially around 0.2 Hz, to which people are very sensitive; if needed, keep amplitude low and consider making content translucent.

### watchOS
- SwiftUI is the streamlined way to add motion; to animate layout/appearance changes or animated image sequences with WatchKit, use `WKInterfaceImage`.
- All layout- and appearance-based animations include built-in easing at start and end; you can't turn off or customize easing.

## Specs
- Game frame rate: consistent 30–60 fps.
- visionOS: avoid sustained oscillation near 0.2 Hz.
- Animated symbols: SF Symbols 5 or later.

## APIs
Animating views and transitions (SwiftUI), `WKInterfaceImage` (WatchKit)

## Related
feedback, accessibility, spatial-layout, immersive-experiences, materials, playing-haptics, playing-audio, sf-symbols
