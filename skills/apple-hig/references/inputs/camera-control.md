# Camera Control

> Source: https://developer.apple.com/design/human-interface-guidelines/camera-control · The Camera Control provides direct access to your app's camera experience.

## When to use / core idea
- On iPhone 16 and iPhone 16 Pro models, quickly opens your app's camera experience. A light press shows an overlay extending from the device bezel; a light double-press shows available controls; sliding a finger on the Camera Control adjusts the selected control's value.
- Control types: *slider* (range of values, e.g., contrast amount) and *picker* (discrete options, e.g., grid on/off).
- System provides optional standard controls for zoom (zoom factor) and exposure (exposure bias), in addition to your custom controls.

## Rules
- **Use SF Symbols to represent control functionality** — custom symbols aren't supported; choose a symbol that clearly denotes behavior (e.g., `bolt.fill` flash, `camera.filters` filters). Symbols don't represent current state. See the Camera & Photos section of the SF Symbols app.
- **Keep names of controls short** — labels follow Dynamic Type; long names can obscure the viewfinder.
- **Include units or symbols with slider control values to provide context** — e.g., EV, %, or a custom string (`localizedValueFormat`).
- **Define prominent values for a slider control** — most frequently chosen or evenly spaced values (e.g., major zoom increments); the system lands on them more easily (`prominentValues`).
- **Make space for the overlay in the viewfinder** — overlay and labels occupy the area adjacent to the Camera Control in portrait and landscape; keep your UI outside those areas; maximize viewfinder size and let the overlay appear/disappear over it.
- **Minimize distractions in the viewfinder** — large preview with minimal distraction; avoid duplicating controls (sliders, toggles) in your UI and the overlay while the overlay shows.
- **Enable or disable controls depending on the camera mode** — e.g., disable video controls when taking photos. Multiple controls are supported but you can't add or remove controls at runtime.
- **Consider how to arrange your controls** — commonly used controls toward the middle, lesser-used on either side. System remembers the last control used in your app when the overlay reopens.
- **Allow people to use the Camera Control to launch your experience from anywhere** — create a locked camera capture extension so it can launch your camera from the locked device, Home Screen, or other apps (see `controls` › Camera experiences on a locked device).

## Platform considerations
Not supported: iPadOS, macOS, watchOS, tvOS, visionOS (iOS only).

## APIs
`localizedValueFormat` (AVFoundation), `prominentValues` (AVFoundation), `Enhancing your app experience with the Camera Control` (AVFoundation), `AVCaptureControl` (AVFoundation), `LockedCameraCapture` (lockedcameracapture)

## Related
`sf-symbols, controls`
