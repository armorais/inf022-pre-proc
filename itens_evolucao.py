class Evolucao:
    def __init__(self):
        self.itens = {"MESORREGIOES":[],"MICRORREGIOES":[],"MUNICIPIOS":[]}

    def add_item(self, chave, item):
        self.itens[chave].append(item)

class Atributo:
    def __init__(self, nome, num_anos):
        self.NOME = nome
        self.VALORES = [None] * num_anos

    def set_nome(self, nome):
        self.NOME = nome

    def get_nome(self):
        return self.NOME

    def set_valores(self, valores):
        self.VALORES = valores

    def get_valores(self):
        return self.VALORES

    def append_valor(self, valor):
        self.VALORES.append(valor)

class Regiao:
    def __init__(self, ID, LISTA_ATRIBUTOS, NUM_ANOS):
        self.ID = ID
        self.ATRIBUTOS = self.set_atributos(LISTA_ATRIBUTOS, NUM_ANOS)

    def set_atributos(self, LISTA_ATRIBUTOS, NUM_ANOS):
        atributos = []
        for nome in LISTA_ATRIBUTOS:
            atributos.append(Atributo(nome, NUM_ANOS))
        return atributos

    def get_atributo(self, index_atributo):
        return self.ATRIBUTOS[index_atributo]

    def set_atributo(self, index_atributo, valor):
        self.ATRIBUTOS[index_atributo]=valor

class Municipio(Regiao):
    def __init__(self, ID, NOME_MUNICIPIO, LISTA_ATRIBUTOS, ID_MESO, ID_MICRO, NUM_ANOS):
        super().__init__(ID, LISTA_ATRIBUTOS, NUM_ANOS)
        self.NOME_MUNICIPIO = NOME_MUNICIPIO
        self.ID_MICRO = ID_MICRO
        self.ID_MESO = ID_MESO

class Microrregiao(Regiao):
    def __init__(self, ID, NOME_MICRORREGIAO, LISTA_ATRIBUTOS, ID_MESO, NUM_ANOS):
        super().__init__(ID, LISTA_ATRIBUTOS, NUM_ANOS)
        self.NOME_MICRORREGIAO = NOME_MICRORREGIAO
        self.ID_MESO = ID_MESO

class Mesorregiao(Regiao):
    def __init__(self, ID, NOME_MESORREGIAO, LISTA_ATRIBUTOS, NUM_ANOS):
        super().__init__(ID, LISTA_ATRIBUTOS, NUM_ANOS)
        self.NOME_MESORREGIAO = NOME_MESORREGIAO