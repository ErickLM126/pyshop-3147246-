from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table

class CategoriaDisciplina(Base):
    __tablename__ = "categorias_disciplinas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True)

class Disciplina(Base):
    __tablename__ = "disciplinas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True)
    id_categoria = Column(Integer, ForeignKey("categorias_disciplinas.id"))

class Artista(Base):
    __tablename__ = "artistas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    numero_contacto = Column(String(12))
    usuario = Column(String(50), unique=True)
    correo = Column(String(100), unique=True)

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
    id_disciplina = Column(Integer, ForeignKey("disciplinas.id"))

class Reaccion(Base):
    __tablename__ = "reacciones"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id"))
    id_usuario = Column(Integer, ForeignKey("artistas.id"))
    tipo_reaccion = Column(String(20))
    comentario = Column(String(1000))
    fecha_reaccion = Column(String(100))

class CategoriaProducto(Base):
    __tablename__ = "categorias_productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True)

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255))
    descripcion = Column(String(1000))
    precio = Column(Integer)
    stock = Column(Integer)
    id_categoria = Column(Integer, ForeignKey("categorias_productos.id"))

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

class Imagen(Base):
    __tablename__ = "imagenes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(500), nullable=False)
    id_publicacion = Column(Integer, ForeignKey("publicaciones.id"), nullable=True)
    id_publicacion_tienda = Column(Integer, ForeignKey("publicaciones_tienda.id"))

class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_emisor = Column(Integer, ForeignKey("artistas.id"))
    id_receptor = Column(Integer, ForeignKey("artistas.id"))
    mensaje = Column(String(1000))
    fecha_envio = Column(String(100))
