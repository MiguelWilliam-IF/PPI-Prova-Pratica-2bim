from app.models.treinador import Treinador
from app import db


class TreinadorController:
    def recuperar_treinador(id):
        return Treinador.query.get(id)
    
    
    def listar_treinadores():
        return Treinador.query.all()
    
    
    def criar_treinador(form):
        try:
            treinador = Treinador()
            form.populate_obj(treinador)
            db.session.add(treinador)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False


    def atualizar_treinador(treinador, form):
        try:
            form.populate_obj(treinador)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False


    def remover_treinador(treinador):
        try:
            db.session.delete(treinador)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False