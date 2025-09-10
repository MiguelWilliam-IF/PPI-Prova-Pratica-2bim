from app.models.competicao import Competicao
from app import db


class CompeticaoController:
    def listar_competicoes():
        competicoes = Competicao.query.all()
        return competicoes
    
    
    def recuperar_competicao(id):
        competicao = Competicao.query.get(id)
        return competicao
    
    
    def criar_competicao(form):
        try:
            competicao = Competicao()
            form.populate_obj(competicao)
            db.session.add(competicao)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False
        
        
    def atualizar_competicao(competicao, form):
        try:
            form.populate_obj(competicao)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False
        
        
    def remover_competicao(competicao):
        try:
            db.session.delete(competicao)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False