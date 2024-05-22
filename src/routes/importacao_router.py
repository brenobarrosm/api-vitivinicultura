from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/importacao")


@router.get('',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de importacao')
def exportacao():
    return 'Importacao'
