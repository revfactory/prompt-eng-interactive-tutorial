#!/usr/bin/env python3
"""
Final fix for the Jupyter notebook outputs issue.
This script will definitively fix the invalid JSON structure.
"""

import json
import os
import sys

def main():
    """Main function to fix the notebook."""
    
    notebook_path = "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P/02_Being_Clear_and_Direct.ipynb"
    
    print(f"🔧 Fixing notebook: {notebook_path}")
    
    # Verify file exists
    if not os.path.exists(notebook_path):
        print(f"❌ Error: File not found at {notebook_path}")
        return False
    
    try:
        # Read the notebook
        print("📖 Reading notebook file...")
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        print(f"📊 Found {len(notebook.get('cells', []))} cells")
        
        # Track fixes
        fixed_markdown_cells = []
        added_outputs_to_code_cells = []
        
        # Process each cell
        for i, cell in enumerate(notebook.get('cells', [])):
            cell_type = cell.get('cell_type', 'unknown')
            
            if cell_type == 'markdown':
                if 'outputs' in cell:
                    # Remove invalid outputs field from markdown cell
                    del cell['outputs']
                    fixed_markdown_cells.append(i)
                    print(f"  ✅ Fixed markdown cell {i} - removed 'outputs' field")
            
            elif cell_type == 'code':
                if 'outputs' not in cell:
                    # Add missing outputs field to code cell
                    cell['outputs'] = []
                    added_outputs_to_code_cells.append(i)
                    print(f"  ✅ Fixed code cell {i} - added 'outputs' field")
        
        # Summary
        total_fixes = len(fixed_markdown_cells) + len(added_outputs_to_code_cells)
        
        if total_fixes == 0:
            print("✨ No issues found - notebook is already correctly formatted!")
            return True
        
        print(f"🔧 Applied {total_fixes} fixes:")
        if fixed_markdown_cells:
            print(f"   📝 Removed 'outputs' from markdown cells: {fixed_markdown_cells}")
        if added_outputs_to_code_cells:
            print(f"   💻 Added 'outputs' to code cells: {added_outputs_to_code_cells}")
        
        # Write the corrected notebook back
        print("💾 Saving corrected notebook...")
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, ensure_ascii=False, indent=1)
        
        print("✅ Successfully fixed and saved the notebook!")
        print(f"🎉 Fixed {len(fixed_markdown_cells)} markdown cells with invalid 'outputs' fields")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    print("\n" + "="*60)
    if success:
        print("🎉 NOTEBOOK FIX COMPLETED SUCCESSFULLY!")
        print("The Jupyter notebook now conforms to the correct schema:")
        print("- Markdown cells do NOT have 'outputs' fields")
        print("- Code cells DO have 'outputs' fields (even if empty)")
    else:
        print("❌ NOTEBOOK FIX FAILED!")
        print("Please check the error messages above.")
    print("="*60)
    
    sys.exit(0 if success else 1)