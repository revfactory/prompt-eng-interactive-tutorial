import json

# Test fix on a single notebook to verify approach
test_notebook = "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P/00_Tutorial_How-To.ipynb"

# Read the notebook
with open(test_notebook, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

print(f"Original notebook has {len(notebook['cells'])} cells")

# Check current state
markdown_with_outputs = 0
code_with_outputs = 0

for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown' and 'outputs' in cell:
        markdown_with_outputs += 1
    elif cell['cell_type'] == 'code' and 'outputs' in cell:
        code_with_outputs += 1

print(f"Before fix: {markdown_with_outputs} markdown cells with outputs, {code_with_outputs} code cells with outputs")

# Apply fix
changes = 0
for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown' and 'outputs' in cell:
        del cell['outputs']
        changes += 1

print(f"Removed outputs from {changes} markdown cells")

# Write back
with open(test_notebook, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print("Test notebook fixed!")

# Verify fix
with open(test_notebook, 'r', encoding='utf-8') as f:
    verified_notebook = json.load(f)

markdown_with_outputs_after = 0
code_with_outputs_after = 0

for cell in verified_notebook['cells']:
    if cell['cell_type'] == 'markdown' and 'outputs' in cell:
        markdown_with_outputs_after += 1
    elif cell['cell_type'] == 'code' and 'outputs' in cell:
        code_with_outputs_after += 1

print(f"After fix: {markdown_with_outputs_after} markdown cells with outputs, {code_with_outputs_after} code cells with outputs")
print("Fix verification: " + ("SUCCESS" if markdown_with_outputs_after == 0 else "FAILED"))