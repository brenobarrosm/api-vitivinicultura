from fastapi import APIRouter
from starlette import status

from api.controllers.processamento_controller import Processamento

processamento = Processamento()

router = APIRouter(prefix="/processamento", tags=["Processamento"])


@router.get('/viniferas',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de processamento de viníferas')
def viniferas():
    return processamento.get_processamento_viniferas()

@router.get('/americanas-hibridas',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de processamento de americanas e híbridas')
def americanas_hibridas():
    return processamento.get_processamento_americanas()

@router.get('/uvas-mesa',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de processamento de uvas de mesa')
def uvas_mesa():
    return processamento.get_processamento_mesa()

@router.get('/sem-classificacao',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de processamento sem classificação')
def sem_classificacao():
    return processamento.get_processamento_sem_classificacao()
