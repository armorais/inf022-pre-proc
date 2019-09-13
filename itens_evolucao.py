class Atributo:
    def __init__(self, nome, num_anos):
        self.NOME = nome
        self.VALORES = [0] * num_anos

    def set_nome(self, nome):
        self.NOME = nome

    def get_nome(self):
        return self.NOME

    def set_valores(self, valores):
        self.VALORES = valores

    def get_valores(self):
        return self.VALORES

    def add_valor(self, valor, ano):
        self.VALORES[ano] = valor

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

    def set_atributo(self, index_atributo, valor, ano):
        self.ATRIBUTOS[index_atributo].add_valor(valor,ano)

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