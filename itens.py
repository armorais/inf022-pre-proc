class Regiao:
  def __init__(self, ID, POPULACAO, VALOR, CATEGORIA, ATRIBUTOS, VALORES):
    self.ID = ID
    self.POPULACAO = POPULACAO
    self.VALOR = VALOR
    self.CATEGORIA = CATEGORIA
    self.ATRIBUTOS = ATRIBUTOS
    self.VALORES = VALORES

class Municipio(Regiao):
    def __init__(self, ID, NOME_MUNICIPIO ,POPULACAO, VALOR, CATEGORIA, ATRIBUTOS, VALORES, ID_MESO, ID_MICRO):
        super().__init__(ID, POPULACAO, VALOR, CATEGORIA, ATRIBUTOS, VALORES)
        self.NOME_MUNICIPIO = NOME_MUNICIPIO
        self.ID_MICRO = ID_MICRO
        self.ID_MESO = ID_MESO

class Microrregiao(Regiao):
    def __init__(self, ID, NOME_MICRORREGIAO ,POPULACAO, VALOR, CATEGORIA, ATRIBUTOS, VALORES, ID_MESO):
        super().__init__(ID, POPULACAO, VALOR, CATEGORIA, ATRIBUTOS, VALORES)
        self.NOME_MICRORREGIAO = NOME_MICRORREGIAO
        self.ID_MESO = ID_MESO

class Mesorregiao(Regiao):
    def __init__(self, ID, NOME_MESORREGIAO ,POPULACAO, VALOR, CATEGORIA, ATRIBUTOS, VALORES):
        super().__init__(ID, POPULACAO, VALOR, CATEGORIA, ATRIBUTOS, VALORES)
        self.NOME_MESORREGIAO = NOME_MESORREGIAO

class JsonRegioes:

    def __init__(self):
        self.MIN_Valor = []
        self.MAX_Valor = []
        self.itens = {"MIN_Valor":[],"MAX_Valor":[],"MESORREGIOES":[],"MICRORREGIOES":[],"MUNICIPIOS":[]}

    def add_item(self, chave, item):
        self.itens[chave].append(item)
        if(len(self.MIN_Valor) == 0):
            self.MIN_Valor = item.VALORES.copy()
            self.MAX_Valor = item.VALORES.copy()
        elif(chave == "MUNICIPIOS"):
            for i in range(4):
                if(item.VALORES[i] < self.MIN_Valor[i]):
                    self.MIN_Valor[i] = item.VALORES[i]
                if(item.VALORES[i] > self.MAX_Valor[i]):
                    self.MAX_Valor[i] = item.VALORES[i]

    def get_itens(self):
        self.set_max_valor()
        self.set_min_valor()
        return self.itens

    def get_max_valor(self):
        return self.MAX_Valor

    def set_max_valor(self):
        self.itens["MAX_Valor"] = self.MAX_Valor

    def get_min_valor(self):
        return self.MIN_Valor

    def set_min_valor(self):
        self.itens["MIN_Valor"] = self.MIN_Valor