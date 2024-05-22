from fastapi import FastAPI
from src.routes import app_routers

api = FastAPI(title='Vitivinicultura Embrapa')


def create_app() -> FastAPI:
    app_routers.start_router(api)
    return api


app = create_app()
