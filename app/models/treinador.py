import sqlalchemy.orm as so
from app import db
from datetime import datetime
from typing import List


class Treinador(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome: so.Mapped[str] = so.mapped_column(db.String(100), nullable=False)
    idade: so.Mapped[int] = so.mapped_column(nullable=False)
    nacionalidade: so.Mapped[str] = so.mapped_column(db.String(50), nullable=False)
    anos_experiencia: so.Mapped[int] = so.mapped_column(default=0, nullable=False)
    created_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow)
    updated_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relacionamento com Time
    times: so.Mapped[List['Time']] = so.relationship("Time", back_populates="treinador")