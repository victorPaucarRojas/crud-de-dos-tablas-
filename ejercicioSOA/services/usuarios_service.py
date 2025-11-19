from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories import usuarios_repository
import schemas

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = usuarios_repository.get_usuario_by_email(db, email=usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    return usuarios_repository.create_usuario(db=db, usuario=usuario)

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return usuarios_repository.get_usuarios(db=db, skip=skip, limit=limit)

def get_usuario(db: Session, usuario_id: int):
    db_usuario = usuarios_repository.get_usuario(db=db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioUpdate):
    # Asegura que el usuario a actualizar existe
    db_usuario = get_usuario(db, usuario_id=usuario_id)
    
    # Si se va a cambiar el email, asegura que no esté ya en uso por otro usuario
    if usuario.email:
        usuario_existente = usuarios_repository.get_usuario_by_email(db, email=usuario.email)
        if usuario_existente and usuario_existente.id != usuario_id:
            raise HTTPException(status_code=400, detail="El nuevo email ya está registrado por otro usuario")

    return usuarios_repository.update_usuario(db=db, usuario_id=usuario_id, usuario=usuario)

def delete_usuario(db: Session, usuario_id: int):
    # Asegura que el usuario a eliminar existe
    db_usuario = get_usuario(db, usuario_id=usuario_id)
    return usuarios_repository.delete_usuario(db=db, usuario_id=usuario_id)
