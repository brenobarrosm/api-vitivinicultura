from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/producao", tags=["produção"])


@router.get('',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de producao')
def exportacao():
    return 'Producao'
