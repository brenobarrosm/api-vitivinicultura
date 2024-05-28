import json


class Exportacao:

    def __init__(self):
        self.exportacao_espumantes = json.load(open('datasets/json/Export_Espumantes.json'))
        self.exportacao_suco_uva = json.load(open('datasets/json/Export_SucoUva.json'))
        self.exportacao_uvas_frescas = json.load(open('datasets/json/Export_UvasFrescas.json'))
        self.exportacao_vinhos_mesa = json.load(open('datasets/json/Export_VinhosMesa.json'))

    def get_exportacao_espumantes(self):
        return self.exportacao_espumantes

    def get_exportacao_suco_uva(self):
        return self.exportacao_suco_uva

    def get_exportacao_uvas_frescas(self):
        return self.exportacao_uvas_frescas

    def get_exportacao_vinhos_mesa(self):
        return self.exportacao_vinhos_mesa
