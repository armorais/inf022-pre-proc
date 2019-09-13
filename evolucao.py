import json
import io
from itens_evolucao import Mesorregiao, Microrregiao, Municipio

class GeradorEvolucao:
    regioes  = ["MESORREGIOES","MICRORREGIOES","MUNICIPIOS"]
    nome_regioes_obj  = ["NOME_MESORREGIAO","NOME_MICRORREGIAO","NOME_MUNICIPIO"]
    nome_atributos = []
    anos = []
    sigla = ''
    out = {"MESORREGIOES":{},"MICRORREGIOES":{},"MUNICIPIOS":{}}

    @classmethod
    def obj_dict(cls, obj):
        return obj.__dict__

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
                    nome_regiao = cls.nome_regioes_obj[index_regiao]
                    nome_item_atual = item[nome_regiao]
                    id_item_regiao_atual = item["ID"]
                    for atributo_geral_atual in cls.nome_atributos:
                        index_atributo_geral_atual = cls.nome_atributos.index(atributo_geral_atual)
                        m = cls.getByValue(regiao, id_item_regiao_atual)
                        if(m==None):
                            if(regiao=="MESORREGIOES"):
                                m = Mesorregiao(id_item_regiao_atual,nome_item_atual,cls.nome_atributos, len(cls.anos))
                            elif(regiao=="MICRORREGIOES"):
                                id_meso = item["ID_MESO"]
                                m = Microrregiao(id_item_regiao_atual,nome_item_atual,cls.nome_atributos,id_meso,len(cls.anos))
                            else:
                                id_meso = item["ID_MESO"]
                                id_micro = item["ID_MICRO"]
                                m = Municipio(id_item_regiao_atual,nome_item_atual,cls.nome_atributos,id_meso,id_micro ,len(cls.anos))

                        m.set_atributo(index_atributo_geral_atual,item["VALORES"][index_atributo_geral_atual],ano_index)
                        cls.out[regiao][id_item_regiao_atual] = m

        for regiao in cls.regioes:
            lista = []
            for item in cls.out[regiao].items():
                lista.append(item[1])
            cls.out[regiao] = lista

    @classmethod
    def getByValue(cls, nome_regiao, id_item):
        item = cls.out[nome_regiao].get(id_item,None)
        return item

    @classmethod
    def gerar_evolucao(cls,sigla,anos,nome_atributos):
        cls.nome_atributos = nome_atributos
        cls.anos = anos
        cls.sigla = sigla
        cls.__preencher_evolucao()
        return cls.out