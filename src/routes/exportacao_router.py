from fastapi import APIRouter
from starlette import status
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/exportacao")


@router.get('',
            status_code=status.HTTP_200_OK,
            description='Retorna os dados de exportacao')
def exportacao():
    return 'Exportacao'
