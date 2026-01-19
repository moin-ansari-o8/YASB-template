#!/usr/bin/env python3
"""
Theme Switcher for YASB
Reads the current theme from config.yaml and generates theme-variables.css
"""

import re
import os

def load_config():
    """Load the YASB configuration file and extract theme data"""
    config_path = os.path.join(os.path.dirname(__file__), 'themes.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract cur_theme
    theme_match = re.search(r'cur_theme:\s*["\']([^"\']+)["\']', content)
    cur_theme = theme_match.group(1).strip() if theme_match else 'golden-light'
    
    print(f"Loading theme: {cur_theme}")
    
    # Find the theme section - look for the theme name followed by a colon
    # Match theme section with proper indentation
    theme_section_pattern = rf'  {re.escape(cur_theme)}:\s*\n((?:    [^\n]+\n?)+)'
    theme_match = re.search(theme_section_pattern, content)
    
    if not theme_match:
        print(f"Warning: Theme '{cur_theme}' not found in config.yaml")
        print(f"Searching for pattern: {theme_section_pattern}")
        return None, None
    
    theme_data = {}
    theme_lines = theme_match.group(1).strip().split('\n')
    
    for line in theme_lines:
        # Skip empty lines and comment-only lines
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
            
        if ':' in line:
            # Split only on the first colon
            parts = line.split(':', 1)
            if len(parts) == 2:
                key = parts[0].strip()
                value = parts[1].strip()
                
                # Handle quoted values properly (they may contain # as hex colors)
                if value.startswith('"') or value.startswith("'"):
                    # Find the closing quote
                    quote_char = value[0]
                    end_quote = value.find(quote_char, 1)
                    if end_quote > 0:
                        value = value[1:end_quote]
                else:
                    # No quotes - check for inline comment after a space
                    # But preserve hex colors like #abc123
                    if '  #' in value or '\t#' in value:
                        value = value.split('  #')[0].split('\t#')[0].strip()
                    value = value.strip('"\'')
                
                if value:
                    theme_data[key] = value
    
    print(f"Loaded {len(theme_data)} color variables")
    return cur_theme, theme_data

def generate_theme_css(cur_theme, theme_data):
    """Generate CSS variables from the selected theme"""
    if not theme_data:
        print("Error: Could not load theme data")
        return
    
    # Generate CSS with custom properties
    css_content = f"""/* Auto-generated theme file - DO NOT EDIT MANUALLY */
/* Current theme: {cur_theme} */
/* To switch themes, change 'cur_theme' in config.yaml and run: python apply_theme.py */

:root {{
    /* Primary colors */
    --primary: {theme_data.get('primary', '#b8956a')};
    --primary-dim: {theme_data.get('primary_dim', '#8b6f47')};
    --primary-hover: {theme_data.get('primary_hover', '#c9a66b')};
    
    /* Text colors */
    --text-primary: {theme_data.get('text_primary', '#d4c5b0')};
    --text-secondary: {theme_data.get('text_secondary', '#9b8b7e')};
    --text-tertiary: {theme_data.get('text_tertiary', '#8b7355')};
    
    /* Background colors */
    --bg-primary: {theme_data.get('bg_primary', 'rgba(35, 28, 24, 0.6)')};
    --bg-secondary: {theme_data.get('bg_secondary', 'rgba(45, 36, 30, 0.75)')};
    --bg-tertiary: {theme_data.get('bg_tertiary', 'rgba(30, 24, 20, 0.5)')};
    --bg-hover: {theme_data.get('bg_hover', 'rgba(50, 40, 32, 0.6)')};
    --bg-button-hover: {theme_data.get('bg_button_hover', 'rgb(65, 52, 42)')};
    
    /* Border colors */
    --border-primary: {theme_data.get('border_primary', '#3d3228')};
    --border-secondary: {theme_data.get('border_secondary', '#4a3f35')};
    
    /* Special colors */
    --accent-warm: {theme_data.get('accent_warm', '#c17a5c')};
}}
"""
    
    # Write to theme-variables.css
    output_path = os.path.join(os.path.dirname(__file__), 'theme-variables.css')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print(f"[OK] Theme '{cur_theme}' applied successfully!")
    print(f"[OK] Generated: theme-variables.css")
    print(f"[OK] Reload YASB to see changes")

if __name__ == '__main__':
    try:
        cur_theme, theme_data = load_config()
        if theme_data:
            generate_theme_css(cur_theme, theme_data)
        else:
            print("Failed to load theme configuration")
            exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
