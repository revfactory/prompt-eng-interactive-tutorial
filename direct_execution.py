#!/usr/bin/env python3
import json
import os

# Immediate execution of the fix for all notebooks
base = "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P"

# Fix each notebook by loading, modifying, and saving
notebooks = ["00_Tutorial_How-To.ipynb", "01_Basic_Prompt_Structure.ipynb", "02_Being_Clear_and_Direct.ipynb", "03_Assigning_Roles_Role_Prompting.ipynb", "04_Separating_Data_and_Instructions.ipynb", "05_Formatting_Output_and_Speaking_for_Claude.ipynb", "06_Precognition_Thinking_Step_by_Step.ipynb"]

total_changes = 0
for name in notebooks:
    path = os.path.join(base, name)
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    changes = 0
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown' and 'outputs' in cell:
            del cell['outputs']
            changes += 1
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f"Fixed {name}: {changes} markdown cells")
    total_changes += changes

print(f"Total: {total_changes} markdown cells fixed across {len(notebooks)} notebooks")

# Quick verification of the first notebook
with open(os.path.join(base, notebooks[0]), 'r') as f:
    test_nb = json.load(f)

print(f"\nVerification of {notebooks[0]}:")
for i, cell in enumerate(test_nb['cells'][:3]):
    has_outputs = 'outputs' in cell
    cell_type = cell['cell_type']
    expected = cell_type == 'code'  # Only code cells should have outputs
    status = "✓" if has_outputs == expected else "✗"
    print(f"  {status} Cell {i} ({cell_type}): outputs present = {has_outputs}")

print("\nNotebook fixing process completed!")

# Import and run this when module is imported
if __name__ != "__main__":
    # This will run when the module is imported
    import sys
    print("Auto-executing notebook fix...")
    sys.modules[__name__].__dict__.update(locals())