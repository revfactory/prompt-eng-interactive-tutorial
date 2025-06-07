#!/usr/bin/env python3
"""
Complete solution to fix Jupyter notebook schema issues
This script removes 'outputs': [] from markdown cells while keeping them for code cells
"""

import json
import os
import sys

def fix_notebook(filepath):
    """Fix a single notebook by removing outputs from markdown cells"""
    try:
        # Read the notebook
        with open(filepath, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Count and fix markdown cells with outputs
        fixed_count = 0
        total_markdown = 0
        total_code = 0
        
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown':
                total_markdown += 1
                if 'outputs' in cell:
                    del cell['outputs']
                    fixed_count += 1
            elif cell['cell_type'] == 'code':
                total_code += 1
                # Keep outputs for code cells (don't modify)
        
        # Write back the fixed notebook
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, ensure_ascii=False, indent=1)
        
        return fixed_count, total_markdown, total_code
        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return 0, 0, 0

def main():
    """Fix all specified notebooks"""
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
    
    print("Fixing Jupyter notebook schema issues...")
    print("=" * 50)
    
    total_fixed = 0
    total_notebooks = 0
    
    for notebook in notebooks:
        filepath = os.path.join(base_dir, notebook)
        
        if not os.path.exists(filepath):
            print(f"✗ {notebook}: File not found")
            continue
        
        print(f"Processing {notebook}...")
        fixed_count, markdown_count, code_count = fix_notebook(filepath)
        
        if fixed_count >= 0:  # Success
            print(f"  ✓ Fixed {fixed_count} markdown cells (total: {markdown_count} markdown, {code_count} code)")
            total_fixed += fixed_count
            total_notebooks += 1
        else:
            print(f"  ✗ Failed to fix {notebook}")
    
    print("=" * 50)
    print(f"Summary: Fixed {total_fixed} markdown cells across {total_notebooks} notebooks")
    
    # Verification step
    print("\nVerification - checking first notebook structure:")
    if notebooks and os.path.exists(os.path.join(base_dir, notebooks[0])):
        verify_notebook(os.path.join(base_dir, notebooks[0]))

def verify_notebook(filepath):
    """Verify that a notebook was fixed correctly"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        print(f"Checking {os.path.basename(filepath)}:")
        for i, cell in enumerate(notebook['cells'][:5]):  # Check first 5 cells
            cell_type = cell['cell_type']
            has_outputs = 'outputs' in cell
            status = "✓" if (cell_type == 'code' and has_outputs) or (cell_type == 'markdown' and not has_outputs) else "✗"
            print(f"  {status} Cell {i}: {cell_type} - outputs field present: {has_outputs}")
            
    except Exception as e:
        print(f"Error verifying {filepath}: {e}")

if __name__ == "__main__":
    main()