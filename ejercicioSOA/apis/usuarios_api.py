from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas
from services import usuarios_service
from database import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"]
)

@router.post("/", response_model=schemas.Usuario, status_code=status.HTTP_201_CREATED)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return usuarios_service.create_usuario(db=db, usuario=usuario)

@router.get("/", response_model=List[schemas.Usuario])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios = usuarios_service.get_usuarios(db, skip=skip, limit=limit)
    return usuarios

@router.get("/{usuario_id}", response_model=schemas.Usuario)
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = usuarios_service.get_usuario(db, usuario_id=usuario_id)
    return db_usuario

@router.put("/{usuario_id}", response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario = usuarios_service.update_usuario(db=db, usuario_id=usuario_id, usuario=usuario)
    return db_usuario

@router.delete("/{usuario_id}", status_code=status.HTTP_200_OK)
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuarios_service.delete_usuario(db=db, usuario_id=usuario_id)
    return {"mensaje": "Usuario eliminado exitosamente"}
