from db import Base
from sqlalchemy import Column, Integer, String, Enum
from models.enums import TipoDocumento

class Artista(Base):
    __tablename__ = "artistas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    numero_contacto = Column(String(12))
    usuario = Column(String(50), unique=True)
    correo = Column(String(100), unique=True)
    documento = Column (String (20))
    tipo_documento = Column(Enum(TipoDocumento))
