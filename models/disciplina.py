from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Disciplina(Base):
    __tablename__ = "disciplinas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True)
    id_categoria = Column(Integer, ForeignKey("categorias_disciplinas.id"))
