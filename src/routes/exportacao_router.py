from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/exportacao", tags=["exportacao"])


@router.get('/vinhos-mesa',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de exportacao de vinhos de mesa')
def vinhos_mesa():
    return 'Exportacao - Vinhos de Mesa'


@router.get('/espumantes',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de exportacao de espumantes')
def espumantes():
    return 'Exportacao - Espumantes'


@router.get('/uvas-frescas',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de exportacao de uvas frescas')
def uvas_frescas():
    return 'Exportacao - Uvas frescas'


@router.get('/suc-uva',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de exportacao de suco de uva')
def uvas_frescas():
    return 'Exportacao - Suco de uva'
