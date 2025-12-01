"""
Convert all Python files (.py) to Jupyter Notebooks (.ipynb)
Converts examples, exercises, and solutions to interactive notebooks
"""

import json
import os
from pathlib import Path

def create_notebook_from_py(py_file_path):
    """Convert a Python file to a Jupyter notebook"""
    
    # Read Python file
    with open(py_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into sections based on comments and print statements
    lines = content.split('\n')
    
    # Create notebook structure
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Extract docstring for title
    docstring = ""
    if '"""' in content:
        docstring_start = content.find('"""') + 3
        docstring_end = content.find('"""', docstring_start)
        if docstring_end > docstring_start:
            docstring = content[docstring_start:docstring_end].strip()
    
    # Add title cell if docstring exists
    if docstring:
        title_lines = docstring.split('\n')
        title_md = "\n".join(["# " + line if line.strip() and not line.startswith('#') else line for line in title_lines[:10]])
        notebook["cells"].append({
            "cell_type": "markdown",
            "metadata": {},
            "source": title_md.split('\n')
        })
    
    # Add import cell
    imports = []
    code_section = []
    current_section = []
    in_markdown = False
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Skip empty lines at start
        if not line and not code_section and not imports:
            i += 1
            continue
            
        # Collect imports
        if line.startswith('import ') or line.startswith('from '):
            imports.append(line)
            i += 1
            continue
        
        # Check for section markers (comments with ### or ## or #)
        if line.strip().startswith('# ') and ('=' * 60 in line or 'Example' in line or 'Task' in line):
            # Save previous code section
            if code_section:
                notebook["cells"].append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": code_section
                })
                code_section = []
            
            # Create markdown header
            md_text = line.replace('# ', '').strip()
            if '=' in md_text:
                md_text = md_text.split('=')[0].strip()
            notebook["cells"].append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"## {md_text}"]
            })
            i += 1
            continue
        
        # Collect code
        if line:
            code_section.append(line)
        else:
            if code_section:  # Empty line - potential cell break
                # Check if next non-empty line is a comment/markdown
                next_non_empty = None
                for j in range(i+1, len(lines)):
                    if lines[j].strip():
                        next_non_empty = lines[j].strip()
                        break
                
                if next_non_empty and (next_non_empty.startswith('#') or next_non_empty.startswith('"')):
                    # Save current code cell
                    notebook["cells"].append({
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": code_section
                    })
                    code_section = []
        
        i += 1
    
    # Add remaining code
    if code_section:
        notebook["cells"].append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": code_section
        })
    
    # Add imports as first code cell if exists
    if imports:
        notebook["cells"].insert(1 if docstring else 0, {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": imports
        })
    
    return notebook


def convert_all_py_to_notebooks():
    """Convert all Python files in the course structure to notebooks"""
    
    base_dir = Path(".")
    units = ["unit1-data-processing", "unit2-regression", "unit3-classification", 
             "unit4-clustering", "unit5-model-selection"]
    
    folders = ["examples", "exercises", "solutions"]
    
    converted = 0
    errors = []
    
    for unit in units:
        unit_path = base_dir / unit
        if not unit_path.exists():
            continue
            
        for folder in folders:
            folder_path = unit_path / folder
            if not folder_path.exists():
                continue
            
            # Find all Python files
            py_files = list(folder_path.glob("*.py"))
            
            for py_file in py_files:
                try:
                    # Create notebook
                    notebook = create_notebook_from_py(py_file)
                    
                    # Save notebook
                    nb_file = folder_path / f"{py_file.stem}.ipynb"
                    with open(nb_file, 'w', encoding='utf-8') as f:
                        json.dump(notebook, f, indent=2, ensure_ascii=False)
                    
                    print(f"✅ Converted: {nb_file}")
                    converted += 1
                    
                except Exception as e:
                    error_msg = f"❌ Error converting {py_file}: {str(e)}"
                    print(error_msg)
                    errors.append(error_msg)
    
    print(f"\n{'='*60}")
    print(f"Conversion Complete!")
    print(f"Converted: {converted} files")
    if errors:
        print(f"Errors: {len(errors)}")
        for error in errors:
            print(f"  - {error}")
    print(f"{'='*60}")


if __name__ == "__main__":
    print("Converting Python files to Jupyter Notebooks...")
    print("=" * 60)
    convert_all_py_to_notebooks()

