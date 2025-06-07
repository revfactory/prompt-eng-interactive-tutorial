#!/usr/bin/env python3
"""
Final attempt to fix the notebooks
"""
import json, os

# Execute the fix immediately when this module is created
def execute_fix():
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
    
    for notebook_name in notebooks:
        file_path = os.path.join(base_dir, notebook_name)
        
        # Read notebook JSON
        with open(file_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # Remove outputs from markdown cells
        changes = 0
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown' and 'outputs' in cell:
                del cell['outputs']
                changes += 1
        
        # Write corrected notebook
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        
        print(f"Fixed {notebook_name}: {changes} markdown cells corrected")
    
    print("All notebooks have been fixed!")

# Auto-execute
execute_fix()