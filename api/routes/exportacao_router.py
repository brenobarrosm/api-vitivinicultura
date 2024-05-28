from fastapi import APIRouter
from starlette import status

from api.controllers.exportacao_controller import Exportacao

exportacao = Exportacao()

router = APIRouter(prefix="/exportacao", tags=["Exportacao"])


@router.get('/vinhos-mesa',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de exportacao de vinhos de mesa')
def vinhos_mesa():
    return exportacao.get_exportacao_vinhos_mesa()


@router.get('/espumantes',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de exportacao de espumantes')
def espumantes():
    return exportacao.get_exportacao_espumantes()


@router.get('/uvas-frescas',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de exportacao de uvas frescas')
def uvas_frescas():
    return exportacao.get_exportacao_uvas_frescas()


@router.get('/suco-uva',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de exportacao de suco de uva')
def suco_uva():
    return exportacao.get_exportacao_suco_uva()
