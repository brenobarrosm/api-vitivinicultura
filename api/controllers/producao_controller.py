import json


class Producao:

    def __init__(self):
        self.producao_json = json.load(open('datasets/json/Producao.json'))

    def get_producao(self):
        return self.producao_json