from fastapi import FastAPI
import models
from database import engine
from apis import productos_api, usuarios_api

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mi Proyecto SOA con FastAPI",
    description="Una API para gestionar productos y usuarios con una arquitectura por capas.",
    version="1.0.0"
)

app.include_router(productos_api.router)
app.include_router(usuarios_api.router)

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de Productos y Usuarios"}
