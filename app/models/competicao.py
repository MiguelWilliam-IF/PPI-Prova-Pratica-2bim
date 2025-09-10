import sqlalchemy.orm as so
from app import db
from datetime import datetime, date
from typing import List, Optional


class Competicao(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome: so.Mapped[str] = so.mapped_column(db.String(100), nullable=False)
    temporada: so.Mapped[int] = so.mapped_column(nullable=False)
    data_inicio: so.Mapped[date] = so.mapped_column(db.Date, nullable=False)
    data_fim: so.Mapped[date] = so.mapped_column(db.Date, nullable=False)
    descricao: so.Mapped[Optional[str]] = so.mapped_column(db.Text)
    created_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow)
    updated_at: so.Mapped[datetime] = so.mapped_column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    jogos: so.Mapped[List['Jogo']] = so.relationship(back_populates='competicao')
    
    def status(self):
        hoje = datetime.now().date()
        if hoje < self.data_inicio:
            return 'Não Iniciada'
        elif hoje > self.data_fim:
            return 'Encerrada'
        else:
            return 'Ativa'