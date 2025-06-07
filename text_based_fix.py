#!/usr/bin/env python3
"""
Text-based approach to fix notebooks using pattern replacement
"""
import re

def fix_notebook_text(content):
    """Fix notebook by removing outputs from markdown cells using regex"""
    
    # Pattern to match markdown cells with outputs field
    # This regex looks for markdown cells and removes the outputs field
    pattern = r'(\{\s*"cell_type":\s*"markdown"[^}]*)"outputs":\s*\[[^\]]*\],?\s*'
    
    # Replace the pattern to remove outputs field from markdown cells
    fixed_content = re.sub(pattern, r'\1', content)
    
    return fixed_content

# Test the pattern
test_cell = '''  {
   "cell_type": "markdown",
   "metadata": {},
   "source": "# Test",
   "outputs": []
  }'''

print("Test input:")
print(test_cell)
print("\nTest output:")
print(fix_notebook_text(test_cell))

# This approach could be used to fix the actual notebooks