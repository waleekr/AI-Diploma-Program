#!/usr/bin/env python3
"""
Fix all notebook visualization issues:
1. Combine plotting code split across multiple cells
2. Replace plt.close() with plt.show()
3. Ensure all figure creation and plotting happens in single cells
"""

import json
import os
from pathlib import Path

def fix_notebook_visuals(notebook_path):
    """Fix visualization issues in a single notebook."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        cells = nb['cells']
        new_cells = []
        i = 0
        changes_made = False
        
        while i < len(cells):
            source = ''.join(cells[i]['source'])
            
            # Check if this cell creates a figure
            creates_figure = ('fig, axes = plt.subplots' in source or 
                            ('plt.figure(' in source and 'figsize' in source))
            
            if creates_figure:
                # Try to combine with following cells that use axes
                combined = source
                j = i + 1
                combined_count = 0
                
                # Look ahead for cells that use axes or complete the plot
                while j < len(cells):
                    next_source = ''.join(cells[j]['source']).strip()
                    
                    # Skip empty cells
                    if not next_source or next_source == '':
                        j += 1
                        continue
                    
                    # Check if this cell uses axes or completes plotting
                    uses_axes = ('axes[' in next_source or 'axes[0]' in next_source or 
                                'axes[1]' in next_source or 'axes[0,0]' in next_source)
                    is_plotting = ('plt.plot' in next_source or 'plt.scatter' in next_source or
                                  'plt.bar' in next_source or 'plt.hist' in next_source or
                                  'plt.savefig' in next_source)
                    
                    if uses_axes or is_plotting:
                        combined += '\n\n' + next_source
                        combined_count += 1
                        j += 1
                        
                        # Stop if we see plt.savefig or plt.tight_layout followed by save/show
                        if 'plt.savefig' in next_source or ('plt.tight_layout()' in next_source and j < len(cells)):
                            # Check next cell for plt.savefig or plt.close
                            if j < len(cells):
                                next_next = ''.join(cells[j]['source']).strip()
                                if 'plt.savefig' in next_next:
                                    combined += '\n\n' + next_next
                                    combined_count += 1
                                    j += 1
                            break
                    else:
                        # Not a plotting cell, stop combining
                        break
                
                # Replace plt.close() with plt.show()
                combined = combined.replace('plt.close()', 'plt.show()')
                
                # Add the combined cell
                new_cells.append({
                    'cell_type': 'code',
                    'execution_count': None,
                    'metadata': cells[i].get('metadata', {}),
                    'outputs': [],
                    'source': combined.split('\n')
                })
                
                # Skip the cells we just combined
                if combined_count > 0:
                    changes_made = True
                i = j
                
            elif 'plt.close()' in source:
                # Replace plt.close() with plt.show()
                new_source = source.replace('plt.close()', 'plt.show()')
                new_cells.append({
                    'cell_type': cells[i]['cell_type'],
                    'execution_count': cells[i].get('execution_count'),
                    'metadata': cells[i].get('metadata', {}),
                    'outputs': cells[i].get('outputs', []),
                    'source': new_source.split('\n') if isinstance(new_source, str) else cells[i]['source']
                })
                changes_made = True
                i += 1
            else:
                # Regular cell, keep as is
                new_cells.append(cells[i])
                i += 1
        
        # Update notebook
        if changes_made:
            nb['cells'] = new_cells
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True, len(cells), len(new_cells)
        return False, len(cells), len(cells)
        
    except Exception as e:
        return None, 0, 0, str(e)

def main():
    """Fix all notebooks in the project."""
    # Find all notebook files
    root_dir = Path('.')
    notebooks = list(root_dir.rglob('*.ipynb'))
    
    # Filter out hidden/checkpoint files
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    print(f"Found {len(notebooks)} notebook files")
    print("=" * 60)
    
    fixed_count = 0
    error_count = 0
    
    for notebook_path in sorted(notebooks):
        rel_path = notebook_path.relative_to(root_dir)
        print(f"\nProcessing: {rel_path}")
        
        result = fix_notebook_visuals(notebook_path)
        
        if result[0] is None:
            error_count += 1
            print(f"  ❌ Error: {result[-1]}")
        elif result[0]:
            fixed_count += 1
            print(f"  ✅ Fixed! {result[1]} → {result[2]} cells")
        else:
            print(f"  ✓ No changes needed ({result[1]} cells)")
    
    print("\n" + "=" * 60)
    print(f"Summary:")
    print(f"  ✅ Fixed: {fixed_count} notebooks")
    print(f"  ✓ No changes: {len(notebooks) - fixed_count - error_count} notebooks")
    print(f"  ❌ Errors: {error_count} notebooks")
    print("=" * 60)

if __name__ == '__main__':
    main()

