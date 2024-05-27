from fastapi import FastAPI

from src.routes import comercializacao_router
from src.routes import exportacao_router
from src.routes import importacao_router
from src.routes import processamento_router
from src.routes import producao_router


class AppRouters:

    def __init__(self):
        self.app = None

    def start_router(self, app: FastAPI) -> None:
        self.app = app
        self.__include_routes()

    def __include_routes(self):
        self.app.include_router(router=comercializacao_router.router)
        self.app.include_router(router=exportacao_router.router)
        self.app.include_router(router=importacao_router.router)
        self.app.include_router(router=processamento_router.router)
        self.app.include_router(router=producao_router.router)


app_routers = AppRouters()
