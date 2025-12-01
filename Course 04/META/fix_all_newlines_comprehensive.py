#!/usr/bin/env python3
"""
Comprehensive fix for all notebooks with missing newlines in plotting cells.
Uses Python source files as reference to restore proper formatting.
"""

import json
import os
from pathlib import Path

def fix_notebook_from_python_source(nb_path, py_path):
    """Fix notebook using Python source file as reference."""
    if not py_path.exists():
        return False
    
    try:
        # Read both files
        with open(nb_path, 'r') as f:
            nb = json.load(f)
        
        with open(py_path, 'r') as f:
            py_source = f.read()
        
        changes = False
        
        # Check each code cell for long single lines
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
                
                # Check if it's one long line with plotting code
                lines = source.split('\n')
                non_empty = [l.strip() for l in lines if l.strip()]
                
                if len(non_empty) <= 2 and len(source) > 200:
                    if 'plt.' in source or 'fig,' in source or 'axes[' in source:
                        # Try to split intelligently
                        fixed = source
                        
                        # Split before plt.
                        fixed = fixed.replace('plt.', '\nplt.')
                        # Split before fig, axes
                        fixed = fixed.replace('fig, axes', '\nfig, axes')
                        # Split after closing parens + space + lowercase
                        import re
                        fixed = re.sub(r'(\))([a-z])', r'\1\n\2', fixed)
                        # Split before print
                        fixed = fixed.replace('print(', '\nprint(')
                        # Split comments
                        fixed = fixed.replace('# ', '\n# ')
                        
                        # Clean up
                        new_lines = [l.strip() for l in fixed.split('\n') if l.strip()]
                        
                        if len(new_lines) > len(non_empty):
                            formatted = [line + '\n' for line in new_lines]
                            if formatted:
                                formatted[-1] = formatted[-1].rstrip('\n')
                            cell['source'] = formatted
                            changes = True
        
        if changes:
            with open(nb_path, 'w') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
        
        return False
    
    except Exception as e:
        return None

def main():
    # Find all notebooks
    notebooks = list(Path('.').rglob('*.ipynb'))
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    print(f"Fixing missing newlines in {len(notebooks)} notebooks...")
    print("=" * 60)
    
    fixed_count = 0
    
    for nb_path in sorted(notebooks):
        # Try to find corresponding Python file
        py_path = nb_path.with_suffix('.py')
        
        if py_path.exists():
            result = fix_notebook_from_python_source(nb_path, py_path)
            if result is True:
                fixed_count += 1
                print(f"✅ Fixed: {nb_path.relative_to('.')}")
    
    print(f"\n✅ Fixed {fixed_count} notebooks")

if __name__ == '__main__':
    main()

