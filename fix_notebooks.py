#!/usr/bin/env python3
import json
import os

def fix_notebook(file_path):
    """Fix a Jupyter notebook by removing 'outputs' field from markdown cells."""
    try:
        # Read the notebook
        with open(file_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        modified_cells = 0
        
        # Process each cell
        for cell in notebook.get('cells', []):
            # If it's a markdown cell and has outputs field, remove it
            if cell.get('cell_type') == 'markdown' and 'outputs' in cell:
                del cell['outputs']
                modified_cells += 1
        
        # Write the corrected notebook back
        if modified_cells > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=1, ensure_ascii=False)
            print(f"Fixed {file_path}: {modified_cells} markdown cells corrected")
            return modified_cells
        else:
            print(f"No changes needed for {file_path}")
            return 0
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

def main():
    # Base directory
    base_dir = "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P"
    
    # Target files (chapters 0-6)
    target_files = [
        "00_Tutorial_How-To.ipynb",
        "01_Basic_Prompt_Structure.ipynb", 
        "02_Being_Clear_and_Direct.ipynb",
        "03_Assigning_Roles_Role_Prompting.ipynb",
        "04_Separating_Data_and_Instructions.ipynb",
        "05_Formatting_Output_and_Speaking_for_Claude.ipynb",
        "06_Precognition_Thinking_Step_by_Step.ipynb"
    ]
    
    total_fixed = 0
    files_modified = 0
    
    for filename in target_files:
        file_path = os.path.join(base_dir, filename)
        if os.path.exists(file_path):
            fixed_count = fix_notebook(file_path)
            if fixed_count > 0:
                files_modified += 1
                total_fixed += fixed_count
        else:
            print(f"File not found: {file_path}")
    
    print(f"\nSummary:")
    print(f"Files modified: {files_modified}")
    print(f"Total markdown cells fixed: {total_fixed}")

if __name__ == "__main__":
    main()