from fastapi import APIRouter
from starlette import status

from api.controllers.producao_controller import Producao

producao = Producao()

router = APIRouter(prefix="/producao", tags=["Produção"])


@router.get('',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de producao')
def exportacao():
    return producao.get_producao()
