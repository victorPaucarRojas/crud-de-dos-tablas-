from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas
from services import productos_service
from database import get_db

router = APIRouter(
    prefix="/productos",
    tags=["productos"]
)

@router.post("/", response_model=schemas.Producto, status_code=status.HTTP_201_CREATED)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return productos_service.create_producto(db=db, producto=producto)

@router.get("/", response_model=List[schemas.Producto])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    productos = productos_service.get_productos(db, skip=skip, limit=limit)
    return productos

@router.get("/{producto_id}", response_model=schemas.Producto)
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = productos_service.get_producto(db, producto_id=producto_id)
    return db_producto

@router.put("/{producto_id}", response_model=schemas.Producto)
def update_producto(producto_id: int, producto: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    db_producto = productos_service.update_producto(db=db, producto_id=producto_id, producto=producto)
    return db_producto

@router.delete("/{producto_id}", status_code=status.HTTP_200_OK)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    productos_service.delete_producto(db=db, producto_id=producto_id)
    return {"mensaje": "Producto eliminado exitosamente"}
