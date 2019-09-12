import json
import io

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
            referencia = json.load(f)

        for regiao in cls.regioes:
            r = referencia[regiao]
            for item in r:
                item["ATRIBUTOS"] = atributos
        f.close()
        return referencia

    @classmethod
    def __preencher_evolucao(cls):
        for ano in cls.anos:
            ano_index = cls.anos.index(ano)
            index = cls.anos.index(ano)
            with io.open('out/' + cls.sigla + '_' + str(ano) + '_geral.json', 'r', encoding='utf8') as f:
                json_atual = json.load(f)

            for regiao in cls.regioes:
                regiao_atual = json_atual[regiao]
                for item in regiao_atual:
                    index_regiao = cls.regioes.index(regiao)
                    nome_regiao = cls.nome_regioes[index_regiao]
                    nome_item_atual = item[nome_regiao]
                    item_evolucao_atributos =  cls.__getByValue(cls.json_referencia[regiao], nome_regiao, nome_item_atual)

                    for atributo_geral_atual in cls.nome_atributos:
                        index_atributo_geral_atual = cls.nome_atributos.index(atributo_geral_atual)
                        item_evolucao_atributos[index_atributo_geral_atual]["VALORES"][ano_index] = item["VALORES"][index_atributo_geral_atual]

    @classmethod
    def __getByValue(cls, dic, nome_regiao, valor):
        for item in dic:
            if item[nome_regiao] == valor:
                return item["ATRIBUTOS"]

    @classmethod
    def gerar_evolucao(cls,sigla,anos,nome_atributos):
        cls.nome_atributos = nome_atributos
        cls.anos = anos
        cls.sigla = sigla

        cls.json_referencia = cls.__get_referencia()
        cls.__preencher_evolucao()
        #print(cls.json_referencia)
        return cls.json_referencia