from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse
import json

json_file = json.load(open('datasets/json/Comercio.csv.json'))

router = APIRouter(prefix="/comercializacao")


@router.get('',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de comercialização')
def comercializacao():
    return 'Comercializacao'
