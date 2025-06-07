import json

# Direct implementation to fix notebook issues
notebooks_to_fix = [
    "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P/00_Tutorial_How-To.ipynb",
    "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P/01_Basic_Prompt_Structure.ipynb",
    "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P/02_Being_Clear_and_Direct.ipynb",
    "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P/03_Assigning_Roles_Role_Prompting.ipynb",
    "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P/04_Separating_Data_and_Instructions.ipynb",
    "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P/05_Formatting_Output_and_Speaking_for_Claude.ipynb",
    "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P/06_Precognition_Thinking_Step_by_Step.ipynb"
]

for notebook_path in notebooks_to_fix:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    changes = 0
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown' and 'outputs' in cell:
            del cell['outputs']
            changes += 1
    
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"Fixed {notebook_path.split('/')[-1]}: {changes} cells")