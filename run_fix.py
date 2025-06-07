import json

# File path
file_path = "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P/02_Being_Clear_and_Direct.ipynb"

# Read the notebook
with open(file_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Fix the outputs issue
fixed_cells = 0
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'markdown' and 'outputs' in cell:
        del cell['outputs']
        fixed_cells += 1
        print(f"Fixed markdown cell {i}")

print(f"Fixed {fixed_cells} cells total")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print("Notebook has been fixed and saved!")