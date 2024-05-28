import json


class Processamento:

    def __init__(self):
        self.processamento_americanas_json = json.load(open('datasets/json/Processamento_Americanas.json'))
        self.processamento_mesa_json = json.load(open('datasets/json/Processamento_Mesa.json'))
        self.processamento_sem_classificacao_json = json.load(open('datasets/json/Processamento_SemClassificacao.json'))
        self.processamento_viniferas_json = json.load(open('datasets/json/Processamento_Viniferas.json'))

    def get_processamento_americanas(self):
        return self.processamento_americanas_json

    def get_processamento_mesa(self):
        return self.processamento_mesa_json

    def get_processamento_sem_classificacao(self):
        return self.processamento_sem_classificacao_json

    def get_processamento_viniferas(self):
        return self.processamento_viniferas_json
