from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/processamento", tags=["processamento"])


@router.get('/viniferas',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de processamento de viníferas')
def viniferas():
    return 'Processamento - Viníferas'

@router.get('/americanas-hibridas',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de processamento de americanas e híbridas')
def americanas_hibridas():
    return 'Processamento - Americanas e Híbridas'

@router.get('/uvas-mesa',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de processamento de uvas de mesa')
def uvas_mesa():
    return 'Processamento - Viníferas'

@router.get('/sem-classificacao',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de processamento sem classificação')
def sem_classificacao():
    return 'Processamento - Sem classificação'
