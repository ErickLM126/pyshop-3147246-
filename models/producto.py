from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    descripcion = Column(String(1000))
    precio = Column(Integer)
    stock = Column(Integer)
    id_categoria = Column(Integer, ForeignKey("categorias_productos.id"))
