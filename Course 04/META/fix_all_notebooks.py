#!/usr/bin/env python3
"""
Comprehensive notebook fixer - fixes common syntax errors across all notebooks
"""
import json
import os
from pathlib import Path
import re

def fix_notebook(notebook_path):
    """Fix common issues in a notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        fixed = False
        
        for i, cell in enumerate(nb['cells']):
            if cell['cell_type'] != 'code':
                continue
            
            source_str = ''.join(cell['source'])
            original_source = cell['source'].copy()
            
            # Pattern 1: Fix broken imports (missing closing parenthesis)
            if 'from sklearn' in source_str:
                lines = cell['source']
                new_lines = []
                for j, line in enumerate(lines):
                    # Check for broken import with open parenthesis but no closing
                    if 'from sklearn' in line and '(' in line:
                        # Count parentheses
                        open_count = line.count('(')
                        close_count = line.count(')')
                        if open_count > close_count:
                            # This is broken - try to fix
                            if line.rstrip().endswith(','):
                                # Remove trailing comma and add closing
                                fixed_line = line.rstrip()[:-1] + ')\n'
                            else:
                                # Add closing parenthesis
                                fixed_line = line.rstrip() + ')\n'
                            new_lines.append(fixed_line)
                            fixed = True
                            continue
                    new_lines.append(line)
                
                if fixed:
                    cell['source'] = new_lines
            
            # Pattern 2: Fix concatenated code (common patterns)
            source_str = ''.join(cell['source'])
            
            # Check for obvious concatenation patterns
            patterns_to_fix = [
                (r'print\("\\n" \+ "=" \* 60\)print', r'print("\\n" + "=" * 60)\nprint'),
                (r'\)print\(', r')\nprint('),
                (r'\)plt\.', r')\nplt.'),
                (r'\)scaler\.', r')\nscaler.'),
                (r'\)X_train', r')\nX_train'),
                (r'\)y_train', r')\ny_train'),
                (r'cluster1 = np\.random\.normal\(\[2, 2\]', r'\ncluster1 = np.random.normal([2, 2]'),
                (r'cluster2 = np\.random\.normal\(\[6, 6\]', r'\ncluster2 = np.random.normal([6, 6]'),
                (r'cluster3 = np\.random\.normal\(\[2, 6\]', r'\ncluster3 = np.random.normal([2, 6]'),
                (r'iris = load_iris\(\)X =', r'iris = load_iris()\nX ='),
                (r'X = iris\.datay =', r'X = iris.data\ny ='),
                (r'scaler = StandardScaler\(\)X_train_scaled', r'scaler = StandardScaler()\nX_train_scaled'),
                (r'np\.random\.seed\(42\)X,', r'np.random.seed(42)\nX,'),
                (r'np\.random\.seed\(42\)cluster', r'np.random.seed(42)\ncluster'),
            ]
            
            for pattern, replacement in patterns_to_fix:
                if re.search(pattern, source_str):
                    # This cell likely has concatenation issues
                    # But we'll be conservative - only fix if it's clearly broken
                    if source_str.count('\n') < len(source_str) / 100:  # Very few newlines
                        # Try to split on common boundaries
                        source_str = re.sub(pattern, replacement, source_str)
                        fixed = True
            
            # Pattern 3: Fix missing comment prefixes (cells that should be comments)
            if len(cell['source']) == 1:
                line = cell['source'][0].strip()
                # If it's a short line that looks like a comment but isn't
                if (len(line) < 100 and 
                    not line.startswith('#') and 
                    not line.startswith('"""') and
                    not line.startswith("'''") and
                    '=' not in line and
                    '(' not in line and
                    not any(keyword in line for keyword in ['import', 'from', 'def', 'class', 'if', 'for', 'while'])):
                    # Might be a comment that lost its prefix
                    if any(word in line.lower() for word in ['generate', 'create', 'split', 'scale', 'visualize', 'compare', 'find', 'plot']):
                        cell['source'] = [f'# {line}\n']
                        fixed = True
        
        if fixed:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"  Error: {e}")
        return False
    
    return False

def main():
    """Scan and fix all notebooks"""
    base_dir = Path('.')
    notebooks = list(base_dir.rglob('*.ipynb'))
    
    print(f"Found {len(notebooks)} notebooks")
    print("Scanning for common issues...\n")
    
    fixed_count = 0
    for nb_path in notebooks:
        # Skip if it's a checkpoint or in __pycache__
        if '.ipynb_checkpoints' in str(nb_path) or '__pycache__' in str(nb_path):
            continue
        
        print(f"Checking: {nb_path.relative_to(base_dir)}")
        if fix_notebook(nb_path):
            print(f"  ✓ Fixed issues")
            fixed_count += 1
        else:
            print(f"  - No issues found")
    
    print(f"\n✓ Fixed {fixed_count} notebooks")
    print("Done!")

if __name__ == '__main__':
    main()

