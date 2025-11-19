from sqlalchemy import Column, Integer, String, UniqueConstraint
from database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True)
    cantidad = Column(Integer)

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
