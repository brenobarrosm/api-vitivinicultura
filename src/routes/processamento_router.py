from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/processamento")


@router.get('',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de processamento')
def exportacao():
    return 'Processamento'
