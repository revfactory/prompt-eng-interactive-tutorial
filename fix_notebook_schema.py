#!/usr/bin/env python3
"""
Fix Jupyter notebook schema violations by removing 'outputs': [] from markdown cells.
This script implements the same logic as the original /tmp/fix_notebook_05.py.
"""

import json
import shutil
from pathlib import Path

def fix_notebook_schema():
    """Fix the specific notebook file."""
    
    # Target notebook file
    notebook_path = Path("Anthropic 1P/05_Formatting_Output_and_Speaking_for_Claude.ipynb")
    
    print(f"Fixing notebook: {notebook_path}")
    
    # Create backup
    backup_path = notebook_path.with_suffix('.ipynb.backup')
    shutil.copy2(notebook_path, backup_path)
    print(f"Backup created: {backup_path}")
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    print(f"Total cells: {len(notebook.get('cells', []))}")
    
    # Track changes
    changes_made = 0
    
    # Process each cell
    for i, cell in enumerate(notebook.get('cells', [])):
        if cell.get('cell_type') == 'markdown':
            if 'outputs' in cell:
                print(f"Removing 'outputs' field from markdown cell {i}")
                del cell['outputs']
                changes_made += 1
    
    # Write the corrected notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"✅ Fixed {changes_made} markdown cells")
    print(f"✅ Notebook schema violations corrected!")
    return changes_made

if __name__ == "__main__":
    try:
        changes = fix_notebook_schema()
        print(f"\nSUCCESS: {changes} changes made to fix schema violations")
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)