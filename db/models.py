from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Artista(Base):
    __tablename__ = "artistas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    usuario = Column(String(50), unique=True)
    correo = Column(String(100), unique=True)

class Disciplina(Base):
    __tablename__ = "disciplinas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True)

class ArtistaDisciplina(Base):
    __tablename__ = "artista_disciplinas"
    id_artista = Column(Integer, ForeignKey("artistas.id"), primary_key=True)
    id_disciplina = Column(Integer, ForeignKey("disciplinas.id"), primary_key=True)

class Publicacion(Base):
    __tablename__ = "publicaciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_artista = Column(Integer, ForeignKey("artistas.id"))
    titulo = Column(String(255))
    contenido = Column(String(1000))
    fecha_publicacion = Column(String(100)) 

class Reaccion(Base):
    __tablename__ = "reacciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id"))
    id_usuario = Column(Integer, ForeignKey("artistas.id"))
    tipo_reaccion = Column(String(20), nullable=False) 
    comentario = Column(String(1000))
    fecha_reaccion = Column(String(100))

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    descripcion = Column(String(1000))
    precio = Column(Integer)
    stock = Column(Integer)

class PublicacionTienda(Base):
    __tablename__ = "publicaciones_tienda"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_artista = Column(Integer, ForeignKey("artistas.id"))
    id_producto = Column(Integer, ForeignKey("productos.id"))
    nombre_producto = Column(String(255))
    descripcion = Column(String(1000))
    precio = Column(Integer)
    stock = Column(Integer)
    fecha_publicacion = Column(String(100))