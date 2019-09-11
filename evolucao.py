from jsonmerge import Merger
import json
import io

class GeradorEvolucao:
    @classmethod
    def __get_referencia(cls, sigla, ano):
        regioes  = ["MESORREGIOES","MICRORREGIOES","MUNICIPIOS"]

        with open("./out/" + sigla + "_" + str(ano) + "_geral.json", 'r', encoding='utf8') as f:
            referencia = json.load(f)
        for regiao in regioes:
            r = referencia[regiao]
            for item in r:
                valor_atual = item["VALORES"].copy()
                item["VALORES"] = []
                item["VALORES"].append(valor_atual)
        f.close()
        return referencia

    @classmethod
    def __merge(cls,referencia, sigla, anos):
        schema = {"properties": { "MESORREGIOES" : { "properties": { "VALORES" : { "mergeStrategy": "append"}}},
                                "MICRORREGIOES" : { "properties": { "VALORES" : { "mergeStrategy": "append"}}},
                                "MUNICIPIOS" : { "properties": { "VALORES" : { "mergeStrategy": "append"}}},}}
        merger = Merger(schema)
        jsons = []

        for ano in anos:
            jsons.append(cls.__get_referencia(sigla, ano))

        evolucao = merger.merge(jsons[0],jsons[1])
        print(evolucao)

        return evolucao

    @classmethod
    def gerar_evolucao(cls,sigla,anos):
        json_referencia = cls.__get_referencia(sigla, anos[0])
        return cls.__merge(json_referencia, sigla, anos)