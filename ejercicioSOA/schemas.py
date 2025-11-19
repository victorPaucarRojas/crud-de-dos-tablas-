from pydantic import BaseModel
from typing import Optional

# Esquemas para Producto
class ProductoBase(BaseModel):
    nombre: str
    cantidad: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    cantidad: Optional[int] = None

class Producto(ProductoBase):
    id: int

    class Config:
        from_attributes = True

# Esquemas para Usuario
class UsuarioBase(BaseModel):
    nombre: str
    email: str

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class Usuario(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
