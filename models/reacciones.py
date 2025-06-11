from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Reaccion(Base):
    __tablename__ = "reacciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id"))
    id_usuario = Column(Integer, ForeignKey("artistas.id"))
    tipo_reaccion = Column(String(20))
    comentario = Column(String(1000))
    fecha_reaccion = Column(String(100))