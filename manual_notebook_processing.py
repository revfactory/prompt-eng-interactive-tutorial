#!/usr/bin/env python3
"""
Manual processing of each notebook to fix the outputs issue
"""

import json
import os

def process_notebook(notebook_path, notebook_name):
    """Process a single notebook"""
    print(f"Processing {notebook_name}...")
    
    try:
        # Read the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Count changes
        changes = 0
        total_markdown = 0
        total_code = 0
        
        # Process each cell
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                total_markdown += 1
                if 'outputs' in cell:
                    del cell['outputs']
                    changes += 1
            elif cell.get('cell_type') == 'code':
                total_code += 1
                # Keep outputs for code cells
        
        # Write back the corrected notebook
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        
        print(f"  ✓ Fixed {changes} markdown cells (Total: {total_markdown} markdown, {total_code} code)")
        return changes > 0
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

# List of notebooks to fix
notebooks = [
    "00_Tutorial_How-To.ipynb",
    "01_Basic_Prompt_Structure.ipynb",
    "02_Being_Clear_and_Direct.ipynb", 
    "03_Assigning_Roles_Role_Prompting.ipynb",
    "04_Separating_Data_and_Instructions.ipynb",
    "05_Formatting_Output_and_Speaking_for_Claude.ipynb",
    "06_Precognition_Thinking_Step_by_Step.ipynb"
]

base_dir = "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P"

print("Starting notebook fixing process...")
print("=" * 50)

fixed_count = 0
for notebook in notebooks:
    notebook_path = os.path.join(base_dir, notebook)
    if os.path.exists(notebook_path):
        if process_notebook(notebook_path, notebook):
            fixed_count += 1
    else:
        print(f"  ✗ {notebook} not found")

print("=" * 50)
print(f"Completed: {fixed_count} notebooks were updated")

# Verify the first notebook
if notebooks:
    first_notebook = os.path.join(base_dir, notebooks[0])
    if os.path.exists(first_notebook):
        print(f"\nVerifying {notebooks[0]}:")
        with open(first_notebook, 'r') as f:
            nb = json.load(f)
        
        for i, cell in enumerate(nb['cells'][:3]):
            cell_type = cell['cell_type']
            has_outputs = 'outputs' in cell
            status = "✓" if (cell_type == 'code' and has_outputs) or (cell_type == 'markdown' and not has_outputs) else "✗"
            print(f"  {status} Cell {i}: {cell_type} - outputs: {has_outputs}")

print("\nNotebook fixing completed!")