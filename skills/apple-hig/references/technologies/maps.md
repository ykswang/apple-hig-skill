# Maps

> Source: https://developer.apple.com/design/human-interface-guidelines/maps · A map displays outdoor or indoor geographical data in your app or on your website.

## When to use / core idea
- Familiar interface with much of the Maps app's functionality: zoom, pan, rotate; annotations, overlays, routing.
- Views: standard (graphical), satellite, or hybrid.
- Place cards show rich place info (hours, phone, address) in or outside a map; indoor maps serve venues (malls, stadiums, airports).

## Rules
### Best practices
- **In general, make your map interactive** — noninteractive elements obscuring the map break expectations.
- **Pick a map emphasis style that suits the needs of your app** — *default*: fully saturated; good for standard maps without many custom elements and for visual alignment with the Maps app. *Muted*: desaturated; lets information-rich content stand out.
- **Help people find places in your map** — consider search plus category filters (e.g., mall: clothing, housewares, electronics, jewelry, toys).
- **Clearly identify elements that people select** — distinct styling like outline and color variation.
- **Cluster overlapping points of interest to improve map legibility** — one pin for nearby POIs; clusters expand progressively on zoom.
- **Help people see the Apple logo and legal link** — temporary covering is fine, not permanent:
  - Adequate padding from map boundaries and custom controls (e.g., 7 pt on the sides, 10 pt above and below).
  - Avoid moving the logo/link with your interface; they should appear fixed to the map.
  - If custom UI moves relative to the map, base placement on its lowest position (e.g., 10 pt above the lowest resting position of a bottom card).
  - Note: logo and link aren't shown on maps smaller than 200x100 pixels.

### Custom information
- **Use annotations that match the visual style of your app** — default marker: red tint, white pin icon. Change tint to your color scheme; icon can be a string or image (e.g., logo). Icon strings can contain any characters incl. Unicode, but keep to two to three characters.
- **If you want to display custom information that's related to standard map features, consider making them independently selectable** — Apple-provided features (POIs, territories, physical features) are treated separately from your annotations; configure custom appearance/info on selection.
- **Use overlays to define map areas with a specific relationship to your content** — *Above roads* (default): above roads, below buildings/trees/other features; people see what's below while understanding it's a defined space. *Above labels*: above roads and labels, hiding everything beneath; for fully abstracted content or hiding irrelevant areas.
- **Make sure there's enough contrast between custom controls and the map** — consider a thin stroke or light drop shadow, or blend modes on the map area.

### Place cards
- Display a place card in the map when someone selects a place you specify (e.g., bookstores on a signing tour), or for other places (POIs, territories, physical features) for nearby context. Websites can embed a custom map showing a place card by default for one place (Maps Embed API).
- Styles:
  - *automatic* — system chooses based on map view size.
  - *callout* — popover next to the place; *full* (large, detailed) or *compact* (concise); unspecified defaults to *automatic* callout based on view size.
  - *caption* — "Open in Apple Maps" link.
  - *sheet* — place card in a sheet.
- Full callout appears as a popover in iPadOS and macOS, as a sheet in iOS.
- **Consider your map presentation when choosing a style** — full callout is richest; for a small map with many annotations consider compact callout.
- **Make sure your place card looks great on different devices and window sizes** — for full callout you can set a minimum width to prevent text overflow on small devices.
- **Avoid duplicating information** — if your app already shows the info, compact callout or caption may complement better.
- **Keep the location on your map visible when displaying a place card** — set an offset and point the card to the selected location.

#### Adding place cards outside of a map
- E.g., a list of places (search results, store locator) that opens a place card on selection.
- **Important:** if the place card isn't shown directly within a map view, you must include a map in the place card.
- **Use location-related cues in surrounding content to help communicate that people can open a place card** — place names/addresses with a details button, or a map pin icon with the place name for compactness.

### Indoor maps
- Custom interactive venue maps with overlays (rooms, kiosks), labels, icons, routes.
- **Adjust map detail based on the zoom level** — show large areas (rooms, buildings) at all zoom levels; progressively add detail (airport: terminals/gates zoomed out; stores/restrooms zoomed in).
- **Use distinctive styling to differentiate the features of your map** — color plus icons for area/store/service types.
- **Offer a floor picker if your venue includes multiple levels** — keep floor numbers concise; usually a list of numbers rather than names suffices.
- **Include surrounding areas to provide context** — adjacent streets, playgrounds; if noninteractive, dim them and use a distinct color.
- **Consider supporting navigation between your venue and nearby transit points** — bus stops, train stations, parking lots, garages; maybe a quick switch to Apple Maps.
- **Limit scrolling outside of your venue** — keep at least part of the indoor map onscreen; adjust allowed scrolling by zoom level.
- **Design an indoor map that feels like a natural extension of your app** — don't replicate Apple Maps' appearance; match overlays, icons, text to your app style (see Indoor Mapping Data Format, IMDF).

## Platform considerations
No additional considerations: iOS, iPadOS, macOS, tvOS, visionOS.
### watchOS
- Maps are static snapshots: place the element at design time, show the region at runtime; not interactive — tapping opens Maps on Apple Watch. Up to five annotations.
- **Fit the map interface element to the screen** — entire element visible without scrolling.
- **Show the smallest region that encompasses the points of interest** — content doesn't scroll; all key content must be visible.

## Specs
- Apple logo / legal link padding (example): 7 pt left/right, 10 pt above/below; 10 pt above lowest resting position of a movable bottom card.
- Logo and legal link hidden on maps smaller than 200x100 pixels.
- Annotation icon string: two to three characters. Default marker: red tint, white pin.
- watchOS: up to five annotations per map.

## APIs
`MapKit`, `MapKit JS`, `MKStandardMapConfiguration.EmphasisStyle`, `MKAnnotationView`, `MKMapFeatureOptions`, `MKOverlayLevel`, `mapItemDetailSelectionAccessory(_:)` (MapKit for SwiftUI), `mapFeatureSelectionAccessory(_:)` (SwiftUI), `MKMapViewDelegate.mapView(_:selectionAccessoryFor:)`, `MapItemDetailSelectionAccessoryStyle`, `MKSelectionAccessory.MapItemDetailPresentationStyle`, `MKSelectionAccessory.mapItemDetail(_:)`, `MKAnnotationView.accessoryOffset`, `offset(_:)` (SwiftUI), `mapItemDetailSheet(item:displaysMap:)` (SwiftUI), `MKMapItemDetailViewController.init(mapItem:displaysMap:)`, `selectionAccessory` / `selectableMapFeatureSelectionAccessory` / `selectionAccessoryOffset` / `PlaceSelectionAccessoryStyle` / `PlaceDetail` (MapKit JS), `WKInterfaceMap` (WatchKit)

## Related
sheets, popovers, search-fields, color
