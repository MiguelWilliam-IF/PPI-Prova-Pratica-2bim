import sqlalchemy.orm as so
import sqlalchemy as sa
from app import db
from datetime import datetime
from typing import List, Optional
import app.models as models


class Time(db.Model):    
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome: so.Mapped[str] = so.mapped_column(db.String(100), nullable=False, unique=True)
    cidade: so.Mapped[str] = so.mapped_column(db.String(100), nullable=False)
    ano_fundacao: so.Mapped[int] = so.mapped_column(nullable=False)
    created_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow)
    updated_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    jogadores: so.Mapped[List['Jogador']] = so.relationship(back_populates='time')
    treinador_id: so.Mapped[Optional[int]] = so.mapped_column(sa.ForeignKey("treinador.id"), index=True, nullable=True)
    treinador: so.Mapped[Optional['Treinador']] = so.relationship("Treinador", back_populates="times", foreign_keys=[treinador_id])

    jogos_casa: so.Mapped[List['Jogo']] = so.relationship('Jogo', foreign_keys='Jogo.time_casa_id', back_populates='time_casa')
    jogos_visitante: so.Mapped[List['Jogo']] = so.relationship('Jogo', foreign_keys='Jogo.time_visitante_id', back_populates='time_visitante')