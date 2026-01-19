# YASB Theme Switching System

## Overview
Your YASB configuration now supports easy theme switching! Currently includes:
- **golden-light** - Warm golden/yellow tones with off-white (current theme)
- **snow-light** - Cool white/snow tones with light blue-gray accents

## How to Switch Themes

### Method 1: Using the switch script (Recommended)
```bash
python switch_theme.py golden-light
# or
python switch_theme.py snow-light
```

### Method 2: Manual switching
1. Open `themes.yaml`
2. Change the `cur_theme` value at the top:
   ```yaml
   cur_theme: "snow-light"  # Change to your desired theme
   ```
3. Run the apply script:
   ```bash
   python apply_theme.py
   ```
4. Reload YASB to see the changes

## Files in the Theme System

- **themes.yaml** - Contains theme definitions and `cur_theme` setting
- **config.yaml** - Main YASB configuration file
- **theme-variables.css** - Auto-generated CSS variables (don't edit manually)
- **styles.css** - Main stylesheet using CSS variables
- **apply_theme.py** - Generates theme-variables.css from config.yaml
- **switch_theme.py** - Convenience script to switch themes
- **styles.css.backup** - Your original styles before theme system
- **styles.css.pre-variables** - Backup before converting to variables

## Creating New Themes
themes
1. Open `config.yaml`
2. Add a new theme section under `themes:`:
   ```yaml
   themes:
     my-custom-theme:
       primary: "#your-color"
       primary_dim: "#your-color"
       # ... etc
   ```
3. Copy the color structure from `golden-light` or `snow-light`
4. Switch to your new theme using the methods above

## Color Variables Reference

| Variable | Purpose |
|----------|---------|
| `primary` | Main accent color (icons, active elements) |
| `primary_dim` | Dimmed accent (inactive states) |
| `primary_hover` | Hover state for accents |
| `text_primary` | Main text color |
| `text_secondary` | Secondary text (labels, muted) |
| `text_tertiary` | Tertiary text (placeholders) |
| `bg_primary` | Main bar background |
| `bg_secondary` | Popup/dialog backgrounds |
| `bg_tertiary` | Card backgrounds |
| `bg_hover` | Hover background states |
| `bg_button_hover` | Button hover background |
| `border_primary` | Main border color |
| `border_secondary` | Secondary border color |
| `accent_warm` | Special accent (power menu, etc.) |

## Troubleshooting

- **Theme not applying?** Make sure to reload YASB after running `apply_theme.py`
- **Colors look wrong?** Check that `theme-variables.css` was regenerated
- **Want to go back?** Restore from `styles.css.backup` or `styles.css.pre-variables`
