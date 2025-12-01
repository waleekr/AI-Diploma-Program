#!/usr/bin/env python3
"""
Fix cells that have all code on one line without newlines.
These cells have plotting code but missing line breaks.
"""

import json
import re
from pathlib import Path

def split_long_line(code):
    """Intelligently split a long line of code into multiple lines."""
    if not code or len(code) < 100:
        return code
    
    # Split points (where to insert newlines)
    # 1. After comments: # comment → newline
    code = re.sub(r'(# [^\n]+?)([a-z#_])', r'\1\n\2', code)
    
    # 2. Before plt. calls (but not at start)
    code = re.sub(r'([^#\n])(plt\.)', r'\1\n\2', code)
    
    # 3. Before fig, axes = 
    code = re.sub(r'([^#\n])(fig, axes)', r'\1\n\2', code)
    
    # 4. After closing parens followed by lowercase letter (new statement)
    code = re.sub(r'(\)\s*)([a-z#_])', r'\1\n\2', code)
    
    # 5. After print statements
    code = re.sub(r'(print\([^)]*\)\s*)([a-z#_])', r'\1\n\2', code)
    
    # 6. Before common keywords
    for keyword in ['for ', 'if ', 'def ', 'class ', 'print(']:
        code = re.sub(rf'([^#\n])({keyword})', r'\1\n\2', code)
    
    # 7. Split on common patterns
    # After savefig/close/show
    code = re.sub(r'(plt\.(savefig|close|show|tight_layout)\([^)]*\)\s*)([a-z#])', r'\1\n\3', code)
    
    # Clean up multiple newlines
    code = re.sub(r'\n{3,}', '\n\n', code)
    
    return code

def fix_missing_newlines(notebook_path):
    """Fix cells with missing newlines."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        changes_made = False
        
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
                
                # Check if it's a long single line that should be split
                lines = source.split('\n')
                non_empty_lines = [l for l in lines if l.strip()]
                
                # If very few lines but lots of code, likely missing newlines
                if len(non_empty_lines) <= 3 and len(source) > 200:
                    # Check if it contains plotting code (indicates it should be multiple lines)
                    if 'plt.' in source or 'fig,' in source or 'axes[' in source:
                        # Try to split it
                        fixed = split_long_line(source)
                        fixed_lines = [line for line in fixed.split('\n') if line.strip() or line == '']
                        
                        # Only apply if we actually created more lines
                        if len([l for l in fixed_lines if l.strip()]) > len(non_empty_lines):
                            # Format properly with newlines
                            formatted_lines = []
                            for line in fixed_lines:
                                if line.strip():
                                    formatted_lines.append(line.rstrip() + '\n')
                                else:
                                    formatted_lines.append('\n')
                            
                            # Remove trailing newline from last line
                            if formatted_lines and formatted_lines[-1].endswith('\n'):
                                formatted_lines[-1] = formatted_lines[-1].rstrip('\n')
                            
                            cell['source'] = formatted_lines
                            changes_made = True
        
        if changes_made:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
        
        return False
    
    except Exception as e:
        print(f"  Error: {e}")
        return None

def main():
    notebooks = list(Path('.').rglob('*.ipynb'))
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    print(f"Fixing missing newlines in {len(notebooks)} notebooks...")
    print("=" * 60)
    
    fixed_count = 0
    
    for nb_path in sorted(notebooks):
        rel_path = nb_path.relative_to(Path('.'))
        result = fix_missing_newlines(nb_path)
        
        if result is True:
            fixed_count += 1
            print(f"✅ Fixed: {rel_path}")
        elif result is None:
            print(f"❌ Error: {rel_path}")
    
    print("\n" + "=" * 60)
    print(f"Fixed {fixed_count} notebooks with missing newlines")

if __name__ == '__main__':
    main()

