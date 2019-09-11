import io
import json

regioes  = ["MESORREGIOES","MICRORREGIOES","MUNICIPIOS"]

with open("./modelo_geral.json", 'r', encoding='utf8') as f:
    referencia = json.load(f)
for regiao in regioes:
    r = referencia[regiao]
    for item in r:
        item["VALORES"] = []
        item["CATEGORIA"] = []
        item["ATRIBUTOS"] = []
f.close()

try:
    with io.open("./modelo_geral_limpo.json", 'w', encoding='utf8') as f:
        f.write("%s" % json.dumps(referencia, ensure_ascii=False))
        f.close()

    print("Json de evolucao criado.")
except FileNotFoundError:
    print("Json nao criado, arquivo nao encontrado")