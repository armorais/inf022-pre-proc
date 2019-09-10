import xlrd
import json
import io
import pandas as pd
import numpy as np
from itens import Estado, Mesorregiao, Microrregiao, Municipio

# Arquivos utilizados
json_out_file = 'out.json'
xls_search_file = './2016/banana.xls'
json_search_file = 'bahia.json'

# Mapeamento das colunas do xls
NOME_REGIAO = {"coluna":0}
AREA_DESTINADA = {"nome":"Area destinada","coluna":1}
AREA_COLHIDA = {"nome":"Area colhida","coluna":2}
QUANTIDADE_PRODUZIDA = {"nome":"Quantidade produzida","coluna":3}
VALOR = {"nome":"Valor","coluna":5}

# Atributos a povoar o json de saída
atributos = [AREA_DESTINADA["nome"], AREA_COLHIDA["nome"], QUANTIDADE_PRODUZIDA["nome"], VALOR["nome"]]

# Estados a serem incluídos
estados = ['Bahia']

# Percentis a serem considerados
percentis_range = [20.0,40.0,60.0,80.0]
percentis = []

# Transforma um obj em um dicionário
def obj_dict(obj):
    return obj.__dict__

# Corrige erros nos nomes dos municípios encontrados no xls
def corrigir_nome(nome):
    if(nome == 'Santa Teresinha'):
        return 'Santa Terezinha'
    elif(nome == 'Iuiú'):
        return 'Iuiu'
    elif(nome == 'Araças'):
        return 'Araçás'
    return nome

# Busca um item em um fragmento do json de busca
def getByValue(dic, valor):
    for item in dic:
        if item["nome"] == valor:
            return item

# Abre o json de busca para leitura
with open(json_search_file, 'r', encoding='utf8') as f:
    json_estado = json.load(f)

# Abre o xls de busca para leitura
wb = xlrd.open_workbook(xls_search_file, formatting_info=True)

# Seleciona a primeira página do xls
sheet = wb.sheet_by_index(0)

# Salva o nome do produto (Categoria)
nome_produto = sheet.cell(5,0).value

# Instancia o objeto de referência para criação do json
j = Estado()

# flag utilizada para controlar quando transformar um linha em objeto
proc_flag = False

# Faz o processamento de cada linha
for i in range(sheet.nrows):
    cell = sheet.cell(i,0)
    inf = wb.xf_list[cell.xf_index]
    if(inf.alignment.indent_level == 0):
        if(not proc_flag and cell.value in estados):
            proc_flag = True
        else:
            proc_flag = False
    if(proc_flag):
        nome_regiao = sheet.cell(i,NOME_REGIAO["coluna"]).value
        area_destinada = sheet.cell(i,AREA_DESTINADA["coluna"]).value
        area_colhida = sheet.cell(i,AREA_COLHIDA["coluna"]).value
        quantidade_produzida = sheet.cell(i,QUANTIDADE_PRODUZIDA["coluna"]).value
        valor = sheet.cell(i,VALOR["coluna"]).value
        valores = [area_destinada,area_colhida,quantidade_produzida,valor]
        if(inf.alignment.indent_level == 3):
            nome_regiao = corrigir_nome(nome_regiao)
            mun = getByValue(json_estado["municipios"],nome_regiao)
            try:
                id = mun["id"]
            except TypeError:
                print(nome_regiao)
            id_micro = mun["microrregiao"]["id"]
            id_meso = mun["microrregiao"]["mesorregiao"]["id"]
            mun = Municipio(id,nome_regiao,nome_produto,atributos,valores,id_meso,id_micro)
            j.add_item("MUNICIPIOS",mun)
        elif(inf.alignment.indent_level == 2):
            micro = getByValue(json_estado["microrregioes"],nome_regiao)
            id = micro["id"]
            id_meso = micro["mesorregiao"]["id"]
            micro = Microrregiao(id,nome_regiao,nome_produto,atributos,valores,id_meso)
            j.add_item("MICRORREGIOES",micro)
        elif(inf.alignment.indent_level == 1):
            meso = getByValue(json_estado["mesorregioes"],nome_regiao)
            id = meso["id"]
            meso = Mesorregiao(id,nome_regiao,nome_produto,atributos,valores)
            j.add_item("MESORREGIOES",meso)

dataframe = pd.DataFrame.from_records(j.get_valores_list(), columns = atributos)

# Pega os percentis e adiciona em uma lista de dicionarios contendo {nome_atributo:percentil}
for coluna in range(len(atributos)):
    percentile = []
    for valor in range(len(percentis_range)):
        percentile.append(np.percentile(dataframe[atributos[coluna]],percentis_range[valor],0))
    percentis.append({atributos[coluna]:percentile})

# Seta os percentis
j.set_percentis(percentis)

# Transforma o objeto em json
s = json.dumps(j.get_itens(), default=obj_dict, ensure_ascii=False)

# Salva o json de saída
try:
    with io.open(json_out_file, 'w', encoding='utf8') as f:
        f.write("%s" % s)
        f.close()

    print("Json criado.")
except FileNotFoundError:
    print("Json nao criado, arquivo nao encontrado")