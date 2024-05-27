import json


class Processamento:

    def __init__(self):
        self.processamento_americanas_json = json.load(open('datasets/json/Processamento_Americanas.json'))
        self.processamento_americanas_json = json.load(open('datasets/json/Processamento_Mesa.json'))
        self.processamento_americanas_json = json.load(open('datasets/json/Processamento_Americanas.json'))
        self.processamento_americanas_json = json.load(open('datasets/json/Processamento_Americanas.json'))

    def get_comercializacao(self):
        pass
