import json


class Comercializacao:

    def __init__(self):
        self.comercializacao_json = json.load(open('datasets/json/Comercio.json'))

    def get_comercializacao(self):
        return self.comercializacao_json
