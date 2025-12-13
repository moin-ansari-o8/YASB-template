# Media Widget Documentation

## Overview
The Media Widget is a customizable component for **YASB** (Yet Another Status Bar) that displays currently playing media information with controls, thumbnails, and an interactive popup menu. It supports various media players and browsers through Windows Media Session integration.

---

## Configuration Options

### Basic Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `label` | string | `"{artist}{s}{title}"` | The main label format for the media widget. Supports placeholders like `{title}`, `{artist}`, and `{s}` for separator. |
| `label_alt` | string | `"{title}"` | The alternative label format for the media widget. |
| `separator` | string | `" - "` | The dynamic separator `{s}` that will be automatically stripped from the label if it's at the end or start. Useful when parts of the label are not present at the source. |
| `class_name` | string | `""` | Custom CSS class name for the widget (optional). |
| `hide_empty` | boolean | `true` | Whether to hide the widget when there is no media information. |

### Display Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `show_thumbnail` | boolean | `true` | Whether to show the media thumbnail. |
| `thumbnail_alpha` | integer | `50` | The alpha transparency value for the thumbnail (0-100). |
| `thumbnail_padding` | integer | `8` | The padding around the thumbnail in pixels. |
| `thumbnail_corner_radius` | integer | `0` | The corner radius for the thumbnail. Set to 0 for square corners. |
| `symmetric_corner_radius` | boolean | `false` | Whether to use symmetric corner radius for the thumbnail. |
| `thumbnail_edge_fade` | boolean | `false` | Whether to apply an edge fade effect to the thumbnail for smoother transitions. |

### Controls Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `controls_only` | boolean | `false` | Whether to show only the media controls (hide label). |
| `controls_left` | boolean | `true` | Whether to position the controls on the left side. |
| `controls_hide` | boolean | `false` | Whether to hide the media controls buttons. |

### Label Sizing Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `max_field_size` | dict | - | Maximum field sizes for labels. |
| `max_field_size.label` | integer | `20` | Maximum size for the main label. If exceeded, it will be truncated. |
| `max_field_size.label_alt` | integer | `30` | Maximum size for the alternative label. If exceeded, it will be truncated. |
| `max_field_size.truncate_whole_label` | boolean | `false` | Whether to truncate the whole label or individual fields (`{title}`, `{artist}`) if it exceeds the maximum size. |

### Icon Configuration

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `icons` | dict | - | Icons for media controls. |
| `icons.prev_track` | string | `"\uf048"` | Icon for the previous track button. |
| `icons.next_track` | string | `"\uf051"` | Icon for the next track button. |
| `icons.play` | string | `"\uf04b"` | Icon for the play button. |
| `icons.pause` | string | `"\uf04c"` | Icon for the pause button. |

### Visual Effects

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `animation` | dict | `{'enabled': true, 'type': 'fadeInOut', 'duration': 200}` | Animation settings for the widget. |
| `container_shadow` | dict | See below | Container shadow options. |
| `label_shadow` | dict | See below | Label shadow options. |

### Advanced Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `media_menu` | dict | See below | Media menu popup configuration. |
| `media_menu_icons` | dict | See below | Media menu icons for popup. |
| `scrolling_label` | dict | See below | Widget label scrolling options. |
| `callbacks` | dict | See below | Callbacks for mouse events on the widget. |

---
## Example Configuration

Here's a comprehensive configuration example for the Media Widget:

```yaml
media:
  type: "yasb.media.MediaWidget"
  options:
    label: "{title}{s}{artist}"
    label_alt: "{title}"
    separator: " - "
    hide_empty: true
    callbacks:
      on_left: "toggle_label"
      on_middle: "do_nothing"
      on_right: "do_nothing"
    max_field_size:
      label: 20
      label_alt: 30
    show_thumbnail: true
    controls_only: false
    controls_left: true
    controls_hide: false
    thumbnail_alpha: 80
    thumbnail_padding: 8
    thumbnail_corner_radius: 16
    icons:
      prev_track: "\ue892"
      next_track: "\ue893"
      play: "\ue768"
      pause: "\ue769"
    media_menu:
      blur: false
      round_corners: true
      round_corners_type: "normal"
      border_color: "system"
      alignment: "right"
      direction: "down"
      offset_top: 6
      offset_left: 0
      thumbnail_corner_radius: 8
      thumbnail_size: 120
      max_title_size: 60
      max_artist_size: 20
      show_source: true
    media_menu_icons:
      play: "\ue768"
      pause: "\ue769"
      prev_track: "\ue892"
      next_track: "\ue893"
    scrolling_label:
      enabled: false
      update_interval_ms: 33
      style: "left"  # can be "left", "right", "bounce", "bounce-ease"
      separator: " | "
      label_padding: 0
      always_scroll: false
      # Easing curve params: https://www.desmos.com/calculator/j7eamemxzi
      ease_slope: 20
      ease_pos: 0.8
      ease_min: 0.5
    label_shadow:
      enabled: true
      color: "black"
      radius: 3
      offset: [ 1, 1 ]
```

---

## Detailed Option Descriptions

### Shadow Options

#### Container Shadow
Applies a shadow effect to the widget container.

```yaml
container_shadow:
  enabled: false          # Whether to enable the container shadow
  color: "black"          # The color of the shadow (HEX value or color name)
  radius: 3               # The blur radius of the shadow
  offset: [1, 1]          # The shadow offset in pixels [x, y]
```

#### Label Shadow
Applies a shadow effect to the widget label.

```yaml
label_shadow:
  enabled: false          # Whether to enable the label shadow
  color: "black"          # The color of the shadow (HEX value or color name)
  radius: 3               # The blur radius of the shadow
  offset: [1, 1]          # The shadow offset in pixels [x, y]
```

---

## Media Menu Configuration

The media menu is an interactive popup that displays detailed media information and controls.

### Media Menu Options

```yaml
media_menu:
  blur: false                          # Whether to apply a blur effect to the popup background
  round_corners: true                  # Whether to round the corners of the popup
  round_corners_type: "normal"         # The type of corner rounding ("normal" or "symmetric")
  border_color: "system"               # The border color (HEX, None, or "system")
  alignment: "right"                   # Popup alignment relative to widget ("left", "center", or "right")
  direction: "down"                    # Direction in which the popup opens ("up" or "down")
  offset_top: 6                        # Vertical offset of the popup from the widget (pixels)
  offset_left: 0                       # Horizontal offset of the popup from the widget (pixels)
  thumbnail_corner_radius: 8           # Corner radius for the thumbnail in the popup
  thumbnail_size: 120                  # Size of the thumbnail in the popup (pixels)
  max_title_size: 60                   # Maximum character length for the title
  max_artist_size: 20                  # Maximum character length for the artist name
  show_source: true                    # Whether to show the media source (e.g., Spotify, Firefox)
  show_volume_slider: false            # Whether to show the per-application volume slider
```

### Media Menu Icon Options

Customize the icons displayed in the media menu popup:

```yaml
media_menu_icons:
  play: "\ue768"       # Icon for the play button in the popup
  pause: "\ue769"      # Icon for the pause button in the popup
  prev_track: "\ue892" # Icon for the previous track button in the popup
  next_track: "\ue893" # Icon for the next track button in the popup
  mute: "\ue994"       # Icon for the mute button in the popup
  unmute: "\ue74f"     # Icon for the unmute button in the popup
```

---

## Scrolling Label Configuration

The scrolling label feature allows for animated text scrolling when content exceeds the available space.

### Scrolling Label Options

```yaml
scrolling_label:
  enabled: false                # Whether to enable the scrolling label
  update_interval_ms: 33       # Update interval in milliseconds (min: 4, max: 1000)
  style: "left"                 # Scrolling style: "left", "right", "bounce", or "bounce-ease"
  separator: " | "              # Separator between repeating text (for "left"/"right" styles)
  label_padding: 1              # Padding around the label in characters (for "bounce" styles)
  always_scroll: false          # Whether to always scroll regardless of text length (for "left"/"right" styles)
  ease_slope: 20                # Easing slope for the bounce effect
  ease_pos: 0.8                 # Easing curve position for the bounce effect
  ease_min: 0.5                 # Minimum value for the bounce effect easing curve
```

### Scrolling Label Notes

- The scrolling label uses `max_field_size` to limit its size.
- When scrolling is enabled, the `thumbnail_padding` option is disabled. Use `.media-widget .label { margin: ... }` in CSS instead.
- **Easing curve parameters**: [View on Desmos](https://www.desmos.com/calculator/j7eamemxzi)

### Scrolling Styles

- **`left`**: Text scrolls continuously from right to left
- **`right`**: Text scrolls continuously from left to right
- **`bounce`**: Text bounces back and forth with linear motion
- **`bounce-ease`**: Text bounces back and forth with easing curves for smooth acceleration/deceleration

---

## Callbacks

Callbacks define actions triggered by mouse events on the widget.

### Available Callbacks

| Callback | Description |
|----------|-------------|
| `toggle_label` | Toggles between the main label and alternative label |
| `do_nothing` | A placeholder callback that does nothing when triggered |
| `toggle_play_pause` | Toggles between play and pause states |
| `toggle_media_menu` | Toggles the visibility of the media menu popup |

### Callback Configuration

```yaml
callbacks:
  on_left: "toggle_label"       # Left-click action
  on_middle: "do_nothing"       # Middle-click action
  on_right: "toggle_media_menu" # Right-click action
```

---

## CSS Styling

### Available Widget CSS Classes

```css
.media-widget {}
.media-widget .widget-container {}
.media-widget .label {}
.media-widget .label.alt {}
.media-widget .btn.play {}
.media-widget .btn.prev {}
.media-widget .btn.next {}
.media-widget .btn.disabled {}
```

### Available Media Menu CSS Classes

```css
.media-menu {}
.media-menu .title {}
.media-menu .artist {}
.media-menu .source {}
.media-menu .btn.play {}
.media-menu .btn.pause {}
.media-menu .btn.prev {}
.media-menu .btn.next {}
.media-menu .btn.disabled {}
.media-menu .thumbnail {}
.media-menu .playback-time {}
.media-menu .progress-slider {}
.media-menu .progress-slider::groove {}
.media-menu .progress-slider::sub-page {}
.media-menu .progress-slider::handle {}
.media-menu .progress-slider::handle:hover {}
.media-menu .app-volume-container {}
.media-menu .app-volume-container .volume-slider {}
.media-menu .app-volume-container .volume-slider::groove {}
.media-menu .app-volume-container .volume-slider::sub-page {}
.media-menu .app-volume-container .volume-slider::handle {}
.media-menu .app-volume-container .volume-slider::handle:hover {}
.media-menu .app-volume-container .mute-button {}
.media-menu .app-volume-container .unmute-button {}
```

---

## Example Widget Styles

### Basic Widget Styling

```css
.media-widget {
    padding: 0;
    margin: 0;
}

.media-widget .label {
    color: #d2d6e2;
    padding: 0px;
    padding-right: 4px;
    font-size: 12px;
}

.media-widget .btn {
    color: #9498a8;
    padding: 0 4px;
    margin: 0;
    font-family: "Segoe Fluent Icons";
    font-weight: 400;
}

.media-widget .btn:hover {
    color: #babfd3;
}

.media-widget .btn.play {
    font-size: 16px;
}

.media-widget .btn.disabled:hover,
.media-widget .btn.disabled {
    color: #4e525c;
    font-size: 12px;
    background-color: rgba(0, 0, 0, 0);
}
```

---

## Example Media Menu Styles

### Basic Popup Styling

```css
.media-menu {
    min-width: 440px;
    max-width: 440px;
    background-color: rgba(31, 39, 49, 0.5);
}
```

### Text Styling

```css
.media-menu .title,
.media-menu .artist,
.media-menu .source {
    font-size: 14px;
    font-weight: 600;
    margin-left: 10px;
    font-family: 'Segoe UI';
}

.media-menu .artist {
    font-size: 13px;
    color: #6c7086;
    margin-top: 0px;
}

.media-menu .source {
    font-size: 11px;
    color: #000;
    border-radius: 3px;
    background-color: #bac2de;
    padding: 2px 4px;
    font-weight: 600;
    font-family: 'Segoe UI';
    margin-top: 10px;
}
```

### Source-Specific Styling

The source class name is generated from the media player name by replacing spaces with dashes and converting to lowercase. For example, "Windows Media" becomes "windows-media".

```css
/* Music Players */
.media-menu .source.aimp {
    background-color: #6f42c1;
    color: #ffffff;
}

.media-menu .source.apple-music {
    background-color: #fa2b56;
    color: #ffffff;
}

.media-menu .source.foobar2000 {
    background-color: #444444;
    color: #ffffff;
}

.media-menu .source.media-player {
    background-color: #0078d4;
    color: #ffffff;
}

.media-menu .source.murglar {
    background-color: #8a8a8a;
    color: #ffffff;
}

.media-menu .source.musicbee {
    background-color: #ffcc00;
    color: #000000;
}

.media-menu .source.nsmusics {
    background-color: #e64a19;
    color: #ffffff;
}

.media-menu .source.qobuz {
    background-color: #003a6f;
    color: #ffffff;
}

.media-menu .source.spotify {
    background-color: #1db954;
    color: #ffffff;
}

.media-menu .source.tidal {
    background-color: #000000;
    color: #ffffff;
}

.media-menu .source.winamp {
    background-color: #f1a11b;
    color: #000000;
}

.media-menu .source.youtube-music {
    background-color: #c51f1f;
    color: #ffffff;
}

/* Web Browsers */
.media-menu .source.brave {
    background-color: #fb542b;
    color: #ffffff;
}

.media-menu .source.chrome {
    background-color: #4285f4;
    color: #ffffff;
}

.media-menu .source.edge {
    background-color: #0078d4;
    color: #ffffff;
}

.media-menu .source.firefox {
    background-color: #ff7139;
    color: #ffffff;
}

.media-menu .source.opera {
    background-color: #ff1b2d;
    color: #ffffff;
}

.media-menu .source.youtube {
    background-color: #ff0000;
    color: #ffffff;
}

.media-menu .source.zen {
    background-color: #2ecc71;
    color: #000000;
}
```

### Control Button Styling

```css
.media-menu .btn {
    font-family: "Segoe Fluent Icons";
    font-size: 14px;
    font-weight: 400;
    margin: 10px 2px 0px 2px;
    min-width: 40px;
    max-width: 40px;
    min-height: 40px;
    max-height: 40px;
    border-radius: 20px;
}

.media-menu .btn.prev {
    margin-left: 10px;
}

.media-menu .btn:hover {
    color: white;
    background-color: rgba(255, 255, 255, 0.1);
}

.media-menu .btn.play {
    background-color: rgba(255, 255, 255, 0.1);
    font-size: 20px;
}

.media-menu .btn.disabled:hover,
.media-menu .btn.disabled {
    color: #4e525c;
    background-color: rgba(0, 0, 0, 0);
}
```

### Progress Bar Styling

```css
.media-menu .playback-time {
    font-size: 13px;
    font-family: 'Segoe UI';
    color: #7f849c;
    margin-top: 20px;
    min-width: 100px;
}

.media-menu .progress-slider {
    height: 10px;
    margin: 5px 4px;
    border-radius: 3px;
}

.media-menu .progress-slider::groove {
    background: transparent;
    height: 2px;
    border-radius: 3px;
    background: rgba(255, 255, 255, 0.1);
}

.media-menu .progress-slider::groove:hover {
    background: transparent;
    height: 6px;
    border-radius: 3px;
    background: rgba(255, 255, 255, 0.2);
}

.media-menu .progress-slider::sub-page {
    background: white;
    border-radius: 3px;
    height: 4px;
}
```

### Volume Control Styling

```css
.media-menu .app-volume-container {
    background-color: rgba(255, 255, 255, 0.05); 
    padding: 8px 6px;
    border-radius: 16px;
    margin-left: 10px; 
}

.media-menu .app-volume-container .volume-slider::groove {
    background: rgba(255, 255, 255, 0.1);
    width: 2px;
    border-radius: 3px;
}

.media-menu .app-volume-container .volume-slider::add-page {
    background: white;
    border-radius: 3px;
}

.media-menu .app-volume-container .volume-slider::groove:hover {
    background: rgba(255, 255, 255, 0.1);
    width: 6px;    
    border-radius: 3px;
}

.media-menu .app-volume-container .volume-slider::sub-page {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 3px;
}

.media-menu .app-volume-container .mute-button,
.media-menu .app-volume-container .unmute-button {
    font-size: 16px;
    color: #ffffff;
    font-family: "Segoe Fluent Icons";
    margin-top: 4px; 
}

.media-menu .app-volume-container .unmute-button {
    color: #a0a0a0;
}
```

---

## Label Placeholders

The following placeholders can be used in `label` and `label_alt` options:

| Placeholder | Description |
|-------------|-------------|
| `{title}` | The title of the currently playing media |
| `{artist}` | The artist of the currently playing media |
| `{s}` | Dynamic separator (defined in `separator` option) |

The `{s}` separator is automatically stripped if it appears at the beginning or end of the label, which is useful when some media sources don't provide certain fields (e.g., no artist information).

---

## Supported Media Sources

The Media Widget integrates with Windows Media Session and supports the following applications:

### Music Players
- AIMP
- Apple Music
- foobar2000
- MusicBee
- Murglar
- nsMusics
- Qobuz
- Spotify
- TIDAL
- Winamp
- Windows Media Player
- YouTube Music

### Web Browsers
- Brave
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Opera
- Yandex Browser (Zen)

And any other application that integrates with Windows Media Session.

---

## Tips and Best Practices

1. **Label Formatting**: Use the `{s}` separator placeholder to avoid extra separators when fields are missing.
   ```yaml
   label: "{artist}{s}{title}"  # Good: no separator if artist is missing
   label: "{artist} - {title}"   # Bad: shows " - " even if artist is missing
   ```

2. **Thumbnail Performance**: If experiencing performance issues, consider:
   - Reducing `thumbnail_alpha` value
   - Decreasing `thumbnail_size` in media menu
   - Disabling `thumbnail_edge_fade`

3. **Scrolling Labels**: When using scrolling labels:
   - Set appropriate `max_field_size` values to trigger scrolling
   - Use CSS margins instead of `thumbnail_padding`
   - Lower `update_interval_ms` for smoother animation (at cost of performance)

4. **Custom Styling**: Use `class_name` to create multiple themed versions of the widget in your bar.

5. **Media Menu**: Position the menu strategically using `alignment` and `direction` to avoid screen edges.

---

## Troubleshooting

### Widget not showing media information
- Ensure the media player supports Windows Media Session
- Check that `hide_empty` is set appropriately
- Verify the media is actually playing

### Thumbnail not appearing
- Confirm `show_thumbnail` is set to `true`
- Some media sources may not provide thumbnail artwork
- Check `thumbnail_alpha` is not set to 0

### Controls not working
- Verify the media player supports the specific control action
- Check that `controls_hide` is not set to `true`
- Some sources may disable certain controls

### Scrolling label issues
- Ensure `max_field_size` is smaller than the actual content
- Verify `update_interval_ms` is within valid range (4-1000)
- Check that scrolling is `enabled`

---

**Last Updated**: December 2025  
**Widget Type**: `yasb.media.MediaWidget`  
**Requires**: Windows Media Session support