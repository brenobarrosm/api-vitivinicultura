from fastapi import APIRouter
from starlette import status

from api.controllers.importacao_controller import Importacao

importacao = Importacao()

router = APIRouter(prefix="/importacao", tags=["Importacao"])


@router.get('/vinhos-mesa',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importacao de vinhos de mesa')
def vinhos_mesa():
    return importacao.get_importacao_vinhos_mesa()

@router.get('/espumantes',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importação de espumantes')
def espumantes():
    return importacao.get_importacao_espumantes()

@router.get('/uvas-frescas',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importação de uvas frescas')
def uvas_frescas():
    return importacao.get_importacao_uvas_frescas()

@router.get('/uvas-passas',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importação de uvas passas')
def uvas_passas():
    return importacao.get_importacao_passas()

@router.get('/suco-uva',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importação de suco de uva')
def suco_uva():
    return importacao.get_importacao_suco_uva()
