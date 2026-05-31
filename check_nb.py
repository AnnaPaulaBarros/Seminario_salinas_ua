import json

path = r'c:\Users\annap\Downloads\Seminário 2\Seminário 2\coleta_de_dados_ua_M1_executed.ipynb'
with open(path, encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        outputs = cell.get('outputs', [])
        src = ''.join(cell.get('source', []))[:60]
        print(f"\n--- Celula {i+1}: {src}")
        for o in outputs:
            otype = o.get('output_type', '')
            if otype == 'error':
                print(f"  ERRO: {o.get('ename')}: {o.get('evalue')}")
            elif otype == 'stream':
                text = ''.join(o.get('text', []))[:300]
                print(f"  OUTPUT: {text}")
            elif otype == 'execute_result':
                data = o.get('data', {})
                text = ''.join(data.get('text/plain', []))[:200]
                print(f"  RESULT: {text}")
