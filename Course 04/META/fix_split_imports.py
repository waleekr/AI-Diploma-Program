#!/usr/bin/env python3
"""
Fix split import statements across all notebooks.
Some notebooks have import statements split across multiple cells, causing syntax errors.
"""

import json
import re
from pathlib import Path

def fix_split_imports(notebook_path):
    """Fix import statements that are split across cells."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        cells = nb['cells']
        new_cells = []
        i = 0
        changes_made = False
        
        while i < len(cells):
            source = ''.join(cells[i]['source']) if isinstance(cells[i]['source'], list) else cells[i]['source']
            
            # Check if this cell has an incomplete import (ends with comma or opening paren)
            incomplete_import_pattern = r'from\s+\S+\s+import\s*\([^)]*$'
            incomplete_import = re.search(incomplete_import_pattern, source)
            
            if incomplete_import and i + 1 < len(cells):
                # Try to find continuation in next cell
                next_source = ''.join(cells[i + 1]['source']) if isinstance(cells[i + 1]['source'], list) else cells[i + 1]['source']
                
                # Check if next cell starts with import continuation (indented, contains closing paren)
                if re.match(r'^\s+[\w_,\s]+\s*\)', next_source.strip()):
                    # Combine the import statements
                    # Extract the continuation from next cell
                    continuation_match = re.match(r'^(\s*[\w_,\s]+)\s*\)', next_source.strip())
                    if continuation_match:
                        continuation = continuation_match.group(1)
                        
                        # Combine: add continuation and closing paren to first cell
                        combined_source = source.rstrip() + '\n' + continuation + ')\n'
                        
                        # Update first cell
                        new_cells.append({
                            'cell_type': cells[i]['cell_type'],
                            'execution_count': cells[i].get('execution_count'),
                            'metadata': cells[i].get('metadata', {}),
                            'outputs': cells[i].get('outputs', []),
                            'source': combined_source.split('\n')
                        })
                        
                        # Remove import continuation from second cell
                        remaining_source = next_source[len(continuation):].lstrip()
                        remaining_source = remaining_source.lstrip(')').lstrip()
                        
                        # If remaining source is not empty, create new cell with it
                        if remaining_source.strip():
                            new_cells.append({
                                'cell_type': cells[i + 1]['cell_type'],
                                'execution_count': cells[i + 1].get('execution_count'),
                                'metadata': cells[i + 1].get('metadata', {}),
                                'outputs': cells[i + 1].get('outputs', []),
                                'source': remaining_source.split('\n')
                            })
                        
                        changes_made = True
                        i += 2
                        continue
            
            # Regular cell, keep as is
            new_cells.append(cells[i])
            i += 1
        
        if changes_made:
            nb['cells'] = new_cells
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return None

def main():
    """Check all notebooks for split imports."""
    notebooks = list(Path('.').rglob('*.ipynb'))
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    print(f"Checking {len(notebooks)} notebooks for split imports...")
    print("=" * 60)
    
    fixed_count = 0
    
    for notebook_path in sorted(notebooks):
        rel_path = notebook_path.relative_to(Path('.'))
        result = fix_split_imports(notebook_path)
        
        if result is True:
            fixed_count += 1
            print(f"✅ Fixed: {rel_path}")
        elif result is None:
            print(f"❌ Error: {rel_path}")
    
    print("\n" + "=" * 60)
    print(f"Fixed {fixed_count} notebooks with split imports")

if __name__ == '__main__':
    main()

