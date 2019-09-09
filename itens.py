class Regiao:
  def __init__(self, ID, CATEGORIA, ATRIBUTOS, VALORES):
    self.ID = ID
    self.CATEGORIA = CATEGORIA
    self.ATRIBUTOS = ATRIBUTOS
    self.VALORES = VALORES

class Municipio(Regiao):
    def __init__(self, ID, NOME_MUNICIPIO, CATEGORIA, ATRIBUTOS, VALORES, ID_MESO, ID_MICRO):
        super().__init__(ID, CATEGORIA, ATRIBUTOS, VALORES)
        self.NOME_MUNICIPIO = NOME_MUNICIPIO
        self.ID_MICRO = ID_MICRO
        self.ID_MESO = ID_MESO

class Microrregiao(Regiao):
    def __init__(self, ID, NOME_MICRORREGIAO, CATEGORIA, ATRIBUTOS, VALORES, ID_MESO):
        super().__init__(ID, CATEGORIA, ATRIBUTOS, VALORES)
        self.NOME_MICRORREGIAO = NOME_MICRORREGIAO
        self.ID_MESO = ID_MESO

class Mesorregiao(Regiao):
    def __init__(self, ID, NOME_MESORREGIAO, CATEGORIA, ATRIBUTOS, VALORES):
        super().__init__(ID, CATEGORIA, ATRIBUTOS, VALORES)
        self.NOME_MESORREGIAO = NOME_MESORREGIAO

class Metadados:
    def __init__(self):
        self.MIN_Valores = []
        self.MAX_Valores = []
        self.PERCENTIS = []

class Estado:
    def __init__(self):
        self.MIN_Valores = []
        self.MAX_Valores = []
        self.itens = {"METADADOS":Metadados(),"MESORREGIOES":[],"MICRORREGIOES":[],"MUNICIPIOS":[]}

    def add_item(self, chave, item):
        self.itens[chave].append(item)
        if(len(self.MIN_Valores) == 0):
            self.MIN_Valores = item.VALORES.copy()
            self.MAX_Valores = item.VALORES.copy()
        elif(chave == "MUNICIPIOS"):
            for i in range(4):
                if(item.VALORES[i] < self.MIN_Valores[i]):
                    self.MIN_Valores[i] = item.VALORES[i]
                if(item.VALORES[i] > self.MAX_Valores[i]):
                    self.MAX_Valores[i] = item.VALORES[i]

    def get_itens(self):
        self.set_max_valores()
        self.set_min_valores()
        return self.itens

    def set_max_valores(self):
        self.itens["METADADOS"].MAX_Valores = self.MAX_Valores

    def set_min_valores(self):
        self.itens["METADADOS"].MIN_Valores = self.MIN_Valores