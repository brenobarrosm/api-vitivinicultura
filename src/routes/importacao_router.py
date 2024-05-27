from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/importacao", tags=["importacao"])


@router.get('/vinhos-mesa',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importacao de vinhos de mesa')
def vinhos_mesa():
    return 'Importacao - Vinhos de Mesa'

@router.get('/espumantes',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importação de espumantes')
def espumantes():
    return 'Importacao - Espumantes'

@router.get('/uvas-frescas',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importação de uvas frescas')
def uvas_frescas():
    return 'Importacao - Uvas frescas'

@router.get('/uvas-passas',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importação de uvas passas')
def uvas_passas():
    return 'Importacao - Uvas passas'

@router.get('/suco-uva',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importação de suco de uva')
def suco_uva():
    return 'Importacao - Suco de uva'
