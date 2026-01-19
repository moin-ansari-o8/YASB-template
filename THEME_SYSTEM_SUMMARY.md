# YASB Theme System - Quick Start Guide

## ✅ System Successfully Implemented!

Your YASB configuration now has a complete theme switching system!

## 🎨 Available Themes

### golden-light (Current Default)
- Warm golden/yellow tones
- Off-white text (#d4c5b0)
- Perfect for cozy, warm ambiance

### snow-light
- Cool white/snow tones
- Bright white text (#f5f5f5)
- Clean, crisp winter feel

## 🚀 How to Switch Themes

### Easiest Method:
```bash
python switch_theme.py snow-light
```

Then reload YASB to see the changes!

### List Available Themes:
```bash
python switch_theme.py
```

## 📁 Files Created

| File | Purpose |
|------|---------|
| **themes.yaml** | Theme definitions + cur_theme selector |
| **config.yaml** | YASB configuration (theme data removed to avoid validation errors) |
| **theme-variables.css** | Auto-generated CSS variables (don't edit!) |
| **styles.css** | Updated to use CSS variables |
| **apply_theme.py** | Generates theme-variables.css from config |
| **switch_theme.py** | Convenience script to switch themes |
| **THEME_SWITCHING.md** | Detailed documentation |

## 🎨 Create Your Own Theme

1. Edit `themes.yaml`
2. Add a new theme under the `themes:` section:

```yaml
themes:
  my-theme:
    primary: "#your-color"
    primary_dim: "#your-color"
    primary_hover: "#your-color"
    text_primary: "#your-color"
    # ... copy structure from golden-light or snow-light
```

3. Switch to it:
```bash
python switch_theme.py my-theme
```

## 🔄 How It Works

1. Theme colors are defined in `config.yaml`
2. `cur_theme` parameter selects active theme
3. `apply_theme.py` reads the selected theme and generates `theme-variables.css`
4. `styles.css` uses CSS variables from `theme-variables.css`
5. Reload YASB to apply changes

## 💾 Backups Created

- `styles.css.backup` - Your original styles before the system
- `styles.css.pre-variables` - Backup before converting to CSS variables

## 📝 Notes

- Always reload YASB after switching themes
- Don't edit `theme-variables.css` manually (it's auto-generated)
- You can add unlimited custom themes to `config.yaml`
- All widgets will automatically use the theme colors

Enjoy your new theme system! 🎉
