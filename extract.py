import json
with open('c:/Users/thris/OneDrive/Desktop/tsa_proj.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('extracted_code.py', 'w', encoding='utf-8') as f:
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            f.write("# Cell\n")
            f.write("".join(cell.get('source', [])))
            f.write("\n\n")
