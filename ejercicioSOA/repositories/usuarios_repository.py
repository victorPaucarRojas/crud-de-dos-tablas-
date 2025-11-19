from sqlalchemy.orm import Session
import models
import schemas
import security

def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

def get_usuario_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hashed_password = security.get_password_hash(usuario.password)
    db_usuario = models.Usuario(email=usuario.email, nombre=usuario.nombre, hashed_password=hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: schemas.UsuarioUpdate):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        update_data = usuario.model_dump(exclude_unset=True)
        if "password" in update_data:
            hashed_password = security.get_password_hash(update_data["password"])
            update_data["hashed_password"] = hashed_password
            del update_data["password"]
        
        for key, value in update_data.items():
            setattr(db_usuario, key, value)
        
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario
