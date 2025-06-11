from db import Base
from sqlalchemy import Column, Integer, ForeignKey

class ArtistaDisciplina(Base):
    __tablename__ = "artista_disciplinas"
    id_artista = Column(Integer, ForeignKey("artistas.id"), primary_key=True)
    id_disciplina = Column(Integer, ForeignKey("disciplinas.id"), primary_key=True)
