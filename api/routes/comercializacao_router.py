from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse

from api.controllers.comercializacao_controller import Comercializacao

comercializacao = Comercializacao()

router = APIRouter(prefix="/comercializacao", tags=["comercialização"])

@router.get('',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de comercialização')
def comercializacao_router():
    return comercializacao.get_comercializacao()
