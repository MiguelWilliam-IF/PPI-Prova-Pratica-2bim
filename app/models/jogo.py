import sqlalchemy.orm as so
from app import db
from datetime import datetime
from typing import Optional
import sqlalchemy as sa


class Jogo(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    data_hora: so.Mapped[datetime] = so.mapped_column(db.DateTime, nullable=False)
    
    time_casa_id: so.Mapped[Optional[int]] = so.mapped_column(sa.ForeignKey("time.id"), index=True, nullable=False)
    time_casa: so.Mapped[Optional['Time']] = so.relationship("Time", back_populates="jogos_casa", foreign_keys=[time_casa_id])
    time_visitante_id: so.Mapped[int] = so.mapped_column(db.Integer, db.ForeignKey('time.id'), nullable=False)
    time_visitante: so.Mapped[Optional['Time']] = so.relationship("Time", back_populates="jogos_visitante", foreign_keys=[time_visitante_id])

    competicao_id: so.Mapped[int] = so.mapped_column(db.Integer, db.ForeignKey('competicao.id'), nullable=False)
    competicao: so.Mapped['Competicao'] = so.relationship(back_populates='jogos')
    gols_casa: so.Mapped[Optional[int]] = so.mapped_column(db.Integer, nullable=True)
    gols_visitante: so.Mapped[Optional[int]] = so.mapped_column(db.Integer, nullable=True)
    status: so.Mapped[str] = so.mapped_column(db.String(20), nullable=False, default='Agendado')
    created_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow)
    updated_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def placar(self):
        if self.gols_casa is not None and self.gols_visitante is not None:
            return f"{self.gols_casa} x {self.gols_visitante}"
        return "-"
    
    def resultado(self):
        if self.gols_casa is None or self.gols_visitante is None:
            return None
        if self.gols_casa > self.gols_visitante:
            return 'casa'
        elif self.gols_visitante > self.gols_casa:
            return 'visitante'
        else:
            return 'empate'