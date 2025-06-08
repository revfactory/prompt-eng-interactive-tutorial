#!/usr/bin/env python3

# Auto-executing notebook fixer script
import json
import os

def fix_notebooks():
    base_dir = "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P"
    files = [
        "00_Tutorial_How-To.ipynb",
        "01_Basic_Prompt_Structure.ipynb", 
        "02_Being_Clear_and_Direct.ipynb",
        "03_Assigning_Roles_Role_Prompting.ipynb",
        "04_Separating_Data_and_Instructions.ipynb",
        "05_Formatting_Output_and_Speaking_for_Claude.ipynb",
        "06_Precognition_Thinking_Step_by_Step.ipynb"
    ]

    total_modified = 0
    total_fixed = 0
    results = []

    print("Fixing Jupyter notebook schema errors...")
    print("=" * 50)

    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    notebook = json.load(f)
                
                modified = False
                cells_fixed = 0
                
                for cell in notebook.get('cells', []):
                    if cell.get('cell_type') == 'markdown' and 'outputs' in cell:
                        del cell['outputs']
                        modified = True
                        cells_fixed += 1
                
                if modified:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(notebook, f, indent=1, ensure_ascii=False)
                    total_modified += 1
                    total_fixed += cells_fixed
                    result = f"✅ {filename}: Fixed {cells_fixed} markdown cells"
                    print(result)
                    results.append(result)
                else:
                    result = f"ℹ️  {filename}: No issues found"
                    print(result)
                    results.append(result)
            except Exception as e:
                result = f"❌ {filename}: Error - {e}"
                print(result)
                results.append(result)
        else:
            result = f"❌ {filename}: File not found"
            print(result)
            results.append(result)

    print("=" * 50)
    summary = f"Summary: {total_modified} files modified, {total_fixed} cells fixed"
    print(summary)
    
    # Write results to a file
    with open('/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/fix_results.txt', 'w') as f:
        f.write("Jupyter Notebook Schema Fix Results\n")
        f.write("=" * 40 + "\n\n")
        for result in results:
            f.write(result + "\n")
        f.write("\n" + summary + "\n")
    
    return total_modified, total_fixed

# Execute the fixes
if __name__ == "__main__":
    fix_notebooks()

# Also execute when imported
fix_notebooks()