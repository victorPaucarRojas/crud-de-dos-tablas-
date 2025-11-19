from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories import productos_repository
import schemas

def create_producto(db: Session, producto: schemas.ProductoCreate):
    return productos_repository.create_producto(db=db, producto=producto)

def get_productos(db: Session, skip: int = 0, limit: int = 100):
    return productos_repository.get_productos(db=db, skip=skip, limit=limit)

def get_producto(db: Session, producto_id: int):
    db_producto = productos_repository.get_producto(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

def update_producto(db: Session, producto_id: int, producto: schemas.ProductoUpdate):
    db_producto = get_producto(db, producto_id=producto_id) # Re-usa get_producto para el check de existencia
    return productos_repository.update_producto(db=db, producto_id=producto_id, producto=producto)

def delete_producto(db: Session, producto_id: int):
    db_producto = get_producto(db, producto_id=producto_id) # Re-usa get_producto para el check de existencia
    return productos_repository.delete_producto(db=db, producto_id=producto_id)
