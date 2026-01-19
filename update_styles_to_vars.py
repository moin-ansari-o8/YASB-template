#!/usr/bin/env python3
"""
Update styles.css to use CSS variables
"""

import re
import os

def update_styles():
    """Replace hardcoded colors with CSS variables"""
    styles_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    
    with open(styles_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Color mappings - map hex/rgba colors to CSS variables
    replacements = [
        # Primary colors
        (r'#b8956a\b', 'var(--primary)'),
        (r'#8b6f47\b', 'var(--primary-dim)'),
        (r'#c9a66b\b', 'var(--primary-hover)'),
        
        # Text colors
        (r'#d4c5b0\b', 'var(--text-primary)'),
        (r'rgba\(212,\s*197,\s*176,\s*[\d.]+\)', lambda m: f'rgba(212, 197, 176, {re.search(r"([\d.]+)\)", m.group()).group(1)})'),  # Keep alpha
        (r'rgb\(212,\s*197,\s*176\)', 'var(--text-primary)'),
        (r'#9b8b7e\b', 'var(--text-secondary)'),
        (r'#8b7355\b', 'var(--text-tertiary)'),
        
        # Background colors
        (r'rgba\(35,\s*28,\s*24,\s*0\.6\)', 'var(--bg-primary)'),
        (r'rgba\(35,\s*28,\s*24,\s*0\.8\d*\)', 'var(--bg-primary)'),  # 0.8, 0.85
        (r'rgba\(45,\s*36,\s*30,\s*0\.75\)', 'var(--bg-secondary)'),
        (r'rgba\(45,\s*36,\s*30,\s*0\.6\)', 'var(--bg-secondary)'),
        (r'rgba\(30,\s*24,\s*20,\s*0\.[457]\d*\)', 'var(--bg-tertiary)'),  # 0.4, 0.5, 0.7
        (r'rgba\(30,\s*24,\s*20,\s*0\.2\)', 'rgba(30, 24, 20, 0.2)'),  # Keep special alpha
        (r'rgba\(50,\s*40,\s*32,\s*0\.6\)', 'var(--bg-hover)'),
        (r'rgb\(65,\s*52,\s*42\)', 'var(--bg-button-hover)'),
        (r'#5a4a3a\b', 'var(--bg-button-hover)'),  # Used for hover states
        
        # Border colors
        (r'#3d3228\b', 'var(--border-primary)'),
        (r'#4a3f35\b', 'var(--border-secondary)'),
        
        # Special colors
        (r'#c17a5c\b', 'var(--accent-warm)'),
        (r'rgba\(193,\s*122,\s*92,', 'rgba(193, 122, 92,'),  # Keep rgba versions for alpha
        
        # Additional color variations that should use primary
        (r'rgba\(184,\s*149,\s*106,', 'rgba(184, 149, 106,'),  # Keep alpha channel
        (r'#6b5542\b', 'var(--primary-hover)'),  # Darker variant
        (r'rgba\(139,\s*111,\s*71,', 'rgba(139, 111, 71,'),  # Keep alpha channel
    ]
    
    # Apply replacements
    for pattern, replacement in replacements:
        if callable(replacement):
            content = re.sub(pattern, replacement, content)
        else:
            content = re.sub(pattern, replacement, content)
    
    # Write back
    backup_path = styles_path + '.pre-variables'
    if not os.path.exists(backup_path):
        # Create backup
        with open(backup_path, 'w', encoding='utf-8') as f:
            with open(styles_path, 'r', encoding='utf-8') as orig:
                f.write(orig.read())
        print(f"✓ Created backup: {os.path.basename(backup_path)}")
    
    with open(styles_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Updated styles.css to use CSS variables")
    print("✓ You can now switch themes by changing cur_theme in config.yaml")
    print("✓ Run 'python apply_theme.py' after changing the theme")

if __name__ == '__main__':
    try:
        update_styles()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
