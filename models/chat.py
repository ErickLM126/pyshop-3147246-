from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_emisor = Column(Integer, ForeignKey("artistas.id"))
    id_receptor = Column(Integer, ForeignKey("artistas.id"))
    mensaje = Column(String(1000))
    fecha_envio = Column(String(100))