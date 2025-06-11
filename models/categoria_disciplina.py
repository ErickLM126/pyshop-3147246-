from db import Base
from sqlalchemy import Column, Integer, String

class CategoriaDisciplina(Base):
    __tablename__ = "categorias_disciplinas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True)
