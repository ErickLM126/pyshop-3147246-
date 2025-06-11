from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Imagen(Base):
    __tablename__ = "imagenes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(500), nullable=False)
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id"), nullable=True)
    id_publicacion_tienda = Column(Integer, ForeignKey("publicaciones_tienda.id"))
