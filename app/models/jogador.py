import sqlalchemy.orm as so
from app import db
from datetime import datetime


class Jogador(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome: so.Mapped[str] = so.mapped_column(db.String(100), nullable=False)
    posicao: so.Mapped[str] = so.mapped_column(db.String(50), nullable=False)
    idade: so.Mapped[int] = so.mapped_column(nullable=False)
    numero_camisa: so.Mapped[int] = so.mapped_column(nullable=False)
    created_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow)
    updated_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relacionamento com Time    
    time_id: so.Mapped[int] = so.mapped_column(db.ForeignKey('time.id'), index=True, nullable=False)
    time: so.Mapped['Time'] = so.relationship(back_populates='jogadores')
