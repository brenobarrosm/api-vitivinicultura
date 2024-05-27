import json
from fastapi.responses import JSONResponse


class Comercializacao:

    def __init__(self):
        self.json_file = json.load(open('datasets/json/Comercio.json'))

    def get_comercializacao(self):
        return self.json_file
