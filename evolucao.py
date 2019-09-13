import json
import io
from itens_evolucao import Evolucao, Mesorregiao, Microrregiao, Municipio

class GeradorEvolucao:
    regioes  = ["MESORREGIOES","MICRORREGIOES","MUNICIPIOS"]
    nome_regioes  = ["NOME_MESORREGIAO","NOME_MICRORREGIAO","NOME_MUNICIPIO"]

    json_referencia = {}
    nome_atributos = []
    evolucao = {}
    anos = []
    sigla = ''

    @classmethod
    def __get_referencia(cls):
        atributos = []

        for nome in cls.nome_atributos:
            atributos.append({"NOME" : nome,  "VALORES": [None] * len(cls.anos)})

        with open("./modelos_json/modelo_evolucao_limpo.json", 'r', encoding='utf8') as f:
            cls.evolucao = json.load(f)

        for regiao in cls.regioes:
            r = cls.evolucao[regiao]
            for item in r:
                item["ATRIBUTOS"] = atributos
        f.close()
        return cls.evolucao

    @classmethod
    def obj_dict(cls, obj):
        return obj.__dict__

    @classmethod
    def __preencher_evolucao(cls):
        cont = 1
        s = ' '
        for ano in cls.anos:
            print(ano)
            print('====')
            ano_index = cls.anos.index(ano)
            index = cls.anos.index(ano)
            with io.open('out/' + cls.sigla + '_' + str(ano) + '_geral.json', 'r', encoding='utf8') as f:
                json_atual = json.load(f)

            for regiao in cls.regioes:
                regiao_atual = json_atual[regiao]
                #print(regiao_atual)
                #print('----')
                for item in regiao_atual:
                    index_regiao = cls.regioes.index(regiao)
                    nome_regiao = cls.nome_regioes[index_regiao]
                    nome_item_atual = item[nome_regiao]
                    id_item_regiao_atual = item["ID"]
                    item_evolucao =  cls.__getByValue(cls.evolucao[regiao], nome_regiao, nome_item_atual)
                    #print(' ----- ' + nome_regiao + ' ' + nome_item_atual)
                    print(item_evolucao["ATRIBUTOS"])
                    for atributo_geral_atual in cls.nome_atributos:
                        index_atributo_geral_atual = cls.nome_atributos.index(atributo_geral_atual)
                        string = str('regiao:') + str(regiao) + str('item evolucao:') + str(list(item_evolucao.values())[1]) + str(',item geral:') + str(nome_item_atual) + '-' + atributo_geral_atual + '-' + str(ano)
                        item_evolucao["ATRIBUTOS"][index_atributo_geral_atual]["VALORES"][ano_index] = ''
                        #print(cls.evolucao[regiao][id_item_regiao_atual])
                        #print("+ " + item_evolucao[nome_regiao])
                        #print(item_evolucao["ATRIBUTOS"][index_atributo_geral_atual]["VALORES"])
                        m = Mesorregiao(id_item_regiao_atual,nome_item_atual,cls.nome_atributos, len(cls.anos))
                        m.set_atributo(index_atributo_geral_atual,3)
                        print(json.dumps(m, default=cls.obj_dict, ensure_ascii=False))
                        return
                        #print(str(cont) + '-' + str(item_de_evolucao["ID"]), end=", ")

    @classmethod
    def __getByValue(cls, dic, nome_regiao, valor):
        for item in dic:
            if item[nome_regiao] == valor:
                return item

    @classmethod
    def gerar_evolucao(cls,sigla,anos,nome_atributos):
        cls.nome_atributos = nome_atributos
        cls.anos = anos
        cls.sigla = sigla

        cls.json_referencia = cls.__get_referencia()
        cls.__preencher_evolucao()
        #print(cls.json_referencia)
        return cls.evolucao

