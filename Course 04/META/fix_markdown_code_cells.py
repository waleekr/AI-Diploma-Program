"""
Fix markdown cells that contain Python code
Convert them to proper code cells or split into markdown + code cells
"""

import json
import glob
import re
import os
from pathlib import Path


def has_code_patterns(source):
    """Check if text contains patterns that indicate it's Python code"""
    if isinstance(source, list):
        source_str = ''.join(source)
    else:
        source_str = source
    
    # Check if it's already a proper markdown code block
    if source_str.strip().startswith('```'):
        return False  # Properly formatted code block in markdown is OK
    
    # Python code indicators
    code_indicators = [
        r'\bimport\s+', r'\bfrom\s+\w+\s+import',
        r'\bdef\s+\w+\s*\(', r'\bclass\s+\w+',
        r'print\s*\(', r'plt\.', r'df\.', r'np\.', r'pd\.',
        r'\w+\s*=\s*\w+', r'\w+\s*=\s*\[', r'\w+\s*=\s*\{',
        r'\w+\(.*\)', r'if\s+.*:', r'for\s+\w+\s+in', r'while\s+',
        r'return\s+', r'yield\s+', r'async\s+', r'await\s+',
        r'X_', r'y_', r'X_train', r'y_train', r'X_test', r'y_test'
    ]
    
    source_lower = source_str.lower()
    for pattern in code_indicators:
        if re.search(pattern, source_str, re.IGNORECASE):
            return True
    return False


def extract_description_and_code(source):
    """Extract description text and code from a markdown cell"""
    if isinstance(source, list):
        source_str = ''.join(source)
    else:
        source_str = source
    
    # Strong patterns that definitely indicate start of code (order matters - check specific first)
    # Use word boundaries to avoid matching inside words
    code_start_markers = [
        (r'\bnp\.random', 'np.random'),
        (r'\bpd\.', 'pd.'),
        (r'\bplt\.', 'plt.'),
        (r'\bdf\.', 'df.'),
        (r'\bdf_\w+\[', 'dataframe access'),  # df_clean['column']
        (r'\bX_\w+\s*=', 'X_ variable assignment'),
        (r'\by_\w+\s*=', 'y_ variable assignment'),
        (r'\bimport\s+', 'import'),
        (r'\bfrom\s+\w+\s+import', 'from import'),
        (r'\bdef\s+\w+\s*\(', 'def'),
        (r'\bclass\s+\w+', 'class'),
        (r'\bprint\s*\(', 'print'),
        (r'\bif\s+', 'if statement'),
        (r'\bfor\s+', 'for loop'),
        (r'\b\w+\.fillna\(', 'fillna method'),
        (r'\b\w+\.\w+\(', 'method call'),  # object.method()
        # Look for variable assignments with proper word boundaries
        (r'\b[a-z_][a-z0-9_]*\s*=\s*(np\.|pd\.|\[|\{|make_|train_test_split|StandardScaler)', 'assignment with module'),
        (r'\b[a-z_][a-z0-9_]*\s*=\s*[a-z_][a-z0-9_]*\s*\(', 'assignment with function call'),
        # DataFrame/variable access patterns
        (r'\b[a-z_][a-z0-9_]*\[\'', 'variable access'),  # variable['key'] - with word boundary
        (r'\b[a-z_][a-z0-9_]*\s*=\s*[^=]', 'assignment'),
    ]
    
    # Find the first strong code marker
    first_code_pos = None
    first_pattern_name = None
    
    for pattern, name in code_start_markers:
        match = re.search(pattern, source_str)
        if match:
            pos = match.start()
            if first_code_pos is None or pos < first_code_pos:
                first_code_pos = pos
                first_pattern_name = name
    
    if first_code_pos is None:
        # No clear code found, return all as description
        return source_str, ""
    
    # Split at the code start position
    description = source_str[:first_code_pos].strip()
    code = source_str[first_code_pos:].strip()
    
    # Clean up description - remove trailing # symbols or comment markers
    description = re.sub(r'#+\s*$', '', description).strip()
    
    # If description ends with a # comment marker followed by Arabic/text, keep it as part of description
    # but if code starts with # comment, it's part of code
    if code.startswith('#'):
        # Check if it's a meaningful comment or just Arabic text
        comment_match = re.match(r'#\s*([^#\n]+)', code)
        if comment_match:
            comment_text = comment_match.group(1)
            # If comment is substantial and before actual code, consider it description
            if len(comment_text.strip()) > 5 and not has_code_patterns(comment_text):
                # Move the comment to description
                description = (description + "\n" + code[:comment_match.end()]).strip()
                code = code[comment_match.end():].strip()
    
    return description, code


def should_split_cell(description, code):
    """Determine if cell should be split into markdown + code"""
    if not description or len(description.strip()) == 0:
        return False
    
    # Remove Arabic comment markers from description for length calculation
    desc_clean = re.sub(r'#\s*[^\n]*', '', description).strip()
    
    if not desc_clean or len(desc_clean.strip()) == 0:
        # Only has comments, don't split
        return False
    
    # If description is just a single short line, might be better as a comment
    desc_lines = [l.strip() for l in desc_clean.split('\n') if l.strip()]
    
    # Split if description is substantial (multiple lines or longer text)
    if len(desc_lines) > 1:
        return True
    
    # Split if single line is longer than 30 chars (substantial description)
    if len(desc_lines) == 1 and len(desc_lines[0]) > 30:
        return True
    
    # Otherwise, keep as comment in code cell
    return False


def fix_notebook(notebook_path):
    """Fix markdown cells containing code in a notebook"""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    new_cells = []
    fixes_applied = 0
    
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            source = cell['source']
            
            # Check if this markdown cell contains code
            if has_code_patterns(source):
                description, code = extract_description_and_code(source)
                
                if code:  # There's actual code to convert
                    if should_split_cell(description, code):
                        # Split into two cells: markdown description + code
                        if description:
                            # Create markdown cell with description
                            new_cells.append({
                                "cell_type": "markdown",
                                "metadata": {},
                                "source": description.split('\n') if isinstance(description, str) else description
                            })
                        
                        # Create code cell with Python code
                        code_source = code.split('\n') if isinstance(code, str) else code
                        new_cells.append({
                            "cell_type": "code",
                            "execution_count": None,
                            "metadata": {},
                            "outputs": [],
                            "source": code_source
                        })
                        
                        fixes_applied += 1
                    else:
                        # Convert to single code cell with description as comment
                        code_lines = []
                        if description:
                            # Add description as comment(s)
                            for desc_line in description.split('\n'):
                                if desc_line.strip():
                                    code_lines.append(f"# {desc_line.strip()}")
                                else:
                                    code_lines.append("")
                        
                        # Add code
                        code_lines.extend(code.split('\n') if isinstance(code, str) else code)
                        
                        new_cells.append({
                            "cell_type": "code",
                            "execution_count": None,
                            "metadata": {},
                            "outputs": [],
                            "source": code_lines
                        })
                        
                        fixes_applied += 1
                else:
                    # No code found, keep as markdown
                    new_cells.append(cell)
            else:
                # Legitimate markdown cell, keep it
                new_cells.append(cell)
        else:
            # Code or other cell type, keep as is
            new_cells.append(cell)
    
    if fixes_applied > 0:
        nb['cells'] = new_cells
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    
    return fixes_applied


def main():
    """Fix all notebooks with markdown cells containing code"""
    
    # List of notebooks with issues (from the plan)
    notebooks_to_fix = [
        # Unit 1
        "unit1-data-processing/examples/05_polynomial_regression.ipynb",
        "unit1-data-processing/exercises/exercise_01.ipynb",
        "unit1-data-processing/exercises/exercise_02.ipynb",
        "unit1-data-processing/solutions/exercise_01_solution.ipynb",
        "unit1-data-processing/solutions/exercise_02_solution.ipynb",
        # Unit 2
        "unit2-regression/examples/02_cross_validation.ipynb",
        "unit2-regression/exercises/exercise_01.ipynb",
        "unit2-regression/solutions/exercise_01_solution.ipynb",
        # Unit 3
        "unit3-classification/examples/02_decision_trees.ipynb",
        "unit3-classification/exercises/exercise_01.ipynb",
        # Unit 4
        "unit4-clustering/examples/01_kmeans_clustering.ipynb",
        "unit4-clustering/examples/02_hierarchical_clustering.ipynb",
        "unit4-clustering/examples/03_pca.ipynb",
        "unit4-clustering/exercises/exercise_01.ipynb",
        # Unit 5
        "unit5-model-selection/examples/01_grid_search.ipynb",
        "unit5-model-selection/examples/02_boosting.ipynb",
        "unit5-model-selection/exercises/exercise_01.ipynb",
    ]
    
    print("Fixing markdown cells containing Python code...")
    print("=" * 70)
    
    total_fixes = 0
    notebooks_fixed = 0
    
    for nb_path in notebooks_to_fix:
        if os.path.exists(nb_path):
            fixes = fix_notebook(nb_path)
            if fixes > 0:
                notebooks_fixed += 1
                total_fixes += fixes
                print(f"✅ {nb_path}: Fixed {fixes} cell(s)")
            else:
                print(f"ℹ️  {nb_path}: No fixes needed")
        else:
            print(f"⚠️  {nb_path}: File not found")
    
    print("=" * 70)
    print(f"✅ Fixed {total_fixes} cells across {notebooks_fixed} notebooks")


if __name__ == "__main__":
    main()

