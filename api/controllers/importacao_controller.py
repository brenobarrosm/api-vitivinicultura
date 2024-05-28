import json


class Importacao:

    def __init__(self):
        self.importacao_espumantes = json.load(open('datasets/json/Import_Espumantes.json'))
        self.importacao_passas = json.load(open('datasets/json/Import_Passas.json'))
        self.importacao_suco_uva = json.load(open('datasets/json/Import_SucoUva.json'))
        self.importacao_uvas_frescas = json.load(open('datasets/json/Import_UvasFrescas.json'))
        self.importacao_vinhos_mesa = json.load(open('datasets/json/Import_VinhosMesa.json'))

    def get_importacao_espumantes(self):
        return self.importacao_espumantes

    def get_importacao_passas(self):
        return self.importacao_passas

    def get_importacao_suco_uva(self):
        return self.importacao_suco_uva

    def get_importacao_uvas_frescas(self):
        return self.importacao_uvas_frescas

    def get_importacao_vinhos_mesa(self):
        return self.importacao_vinhos_mesa
