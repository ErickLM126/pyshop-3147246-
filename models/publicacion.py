
from db import Base
from sqlalchemy import Date, Column, Integer, String, ForeignKey
from datetime import datetime

class Publicacion(Base):
    __tablename__ = "publicaciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_artista = Column(Integer, ForeignKey("artistas.id"))
    titulo = Column(String(255))
    contenido = Column(String(1000))
    fecha_publicacion = Column(Date, default=datetime.now)