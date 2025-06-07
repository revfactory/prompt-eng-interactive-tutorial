#!/usr/bin/env python3
"""
Script to fix Jupyter notebooks by removing 'outputs' field from markdown cells.
Only code cells should have 'outputs' field.
"""

import json
import os
import sys

def fix_notebook(notebook_path):
    """Fix a single notebook by removing outputs from markdown cells."""
    try:
        # Read the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Process each cell
        changes_made = False
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'markdown' and 'outputs' in cell:
                # Remove outputs field from markdown cells
                del cell['outputs']
                changes_made = True
                print(f"Removed outputs from markdown cell in {notebook_path}")
        
        # Write back the fixed notebook if changes were made
        if changes_made:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=1, ensure_ascii=False)
            print(f"Fixed notebook: {notebook_path}")
            return True
        else:
            print(f"No changes needed for: {notebook_path}")
            return False
            
    except Exception as e:
        print(f"Error processing {notebook_path}: {e}")
        return False

def main():
    """Main function to fix all notebooks in Anthropic 1P directory."""
    base_dir = "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P"
    
    notebooks = [
        "00_Tutorial_How-To.ipynb",
        "01_Basic_Prompt_Structure.ipynb",
        "02_Being_Clear_and_Direct.ipynb",
        "03_Assigning_Roles_Role_Prompting.ipynb",
        "04_Separating_Data_and_Instructions.ipynb",
        "05_Formatting_Output_and_Speaking_for_Claude.ipynb",
        "06_Precognition_Thinking_Step_by_Step.ipynb"
    ]
    
    total_fixed = 0
    for notebook in notebooks:
        notebook_path = os.path.join(base_dir, notebook)
        if os.path.exists(notebook_path):
            if fix_notebook(notebook_path):
                total_fixed += 1
        else:
            print(f"Warning: {notebook_path} does not exist")
    
    print(f"\nCompleted: {total_fixed} notebooks were fixed")

if __name__ == "__main__":
    main()