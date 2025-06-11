from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class PublicacionTienda(Base):
    __tablename__ = "publicaciones_tienda"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_artista_vendedor = Column(Integer, ForeignKey("artistas.id"))
    id_artista_comprador = Column(Integer, ForeignKey("artistas.id"))
    id_producto = Column(Integer, ForeignKey("productos.id"))
    nombre_producto = Column(String(255))
    descripcion = Column(String(1000))
    precio = Column(Integer)
    stock = Column(Integer)
    fecha_publicacion = Column(String(100))
    id_categoria = Column(Integer, ForeignKey("categorias_productos.id"))
