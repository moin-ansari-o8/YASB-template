#!/usr/bin/env python3
"""
Theme Switcher - Convenience script to switch between YASB themes
Usage: python switch_theme.py <theme_name>
Example: python switch_theme.py snow-light
"""

import re
import os
import sys

def list_available_themes():
    """List all available themes from themes.yaml"""
    config_path = os.path.join(os.path.dirname(__file__), 'themes.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the themes section
    themes_section_match = re.search(r'^themes:\s*\n((?:  [a-z-]+:.*\n(?:    .*\n)*)+)', content, re.MULTILINE)
    if not themes_section_match:
        return []
    
    # Find theme names (lines that start with 2 spaces and end with colon)
    theme_pattern = r'^  ([a-z-]+):\s*$'
    themes = re.findall(theme_pattern, themes_section_match.group(1), re.MULTILINE)
    return themes

def get_current_theme():
    """Get the currently active theme"""
    config_path = os.path.join(os.path.dirname(__file__), 'themes.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    theme_match = re.search(r'cur_theme:\s*["\']([^"\']+)["\']', content)
    return theme_match.group(1) if theme_match else None

def switch_theme(theme_name):
    """Switch to the specified theme"""
    config_path = os.path.join(os.path.dirname(__file__), 'themes.yaml')
    
    # Read config
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if theme exists
    available_themes = list_available_themes()
    if theme_name not in available_themes:
        print(f"[ERROR] Theme '{theme_name}' not found!")
        print(f"Available themes: {', '.join(available_themes)}")
        return False
    
    # Update cur_theme value
    new_content = re.sub(
        r'(cur_theme:\s*["\'])([^"\']+)(["\'])',
        rf'\1{theme_name}\3',
        content
    )
    
    # Write back
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"[OK] Switched to theme: {theme_name}")
    
    # Run apply_theme.py
    import subprocess
    result = subprocess.run([sys.executable, 'apply_theme.py'], 
                          capture_output=True, text=True, cwd=os.path.dirname(__file__))
    
    if result.returncode == 0:
        print(result.stdout)
        print("\n[SUCCESS] Theme applied successfully!")
        print("[INFO] Reload YASB to see the changes")
        return True
    else:
        print(f"[ERROR] Error applying theme:")
        print(result.stderr)
        return False

def main():
    if len(sys.argv) < 2:
        current = get_current_theme()
        available = list_available_themes()
        
        print("YASB Theme Switcher")
        print("=" * 50)
        print(f"Current theme: {current}")
        print(f"\nAvailable themes:")
        for theme in available:
            marker = " ← current" if theme == current else ""
            print(f"  - {theme}{marker}")
        print("\nUsage: python switch_theme.py <theme_name>")
        print(f"Example: python switch_theme.py {[t for t in available if t != current][0]}")
        return
    
    theme_name = sys.argv[1]
    switch_theme(theme_name)

if __name__ == '__main__':
    main()
