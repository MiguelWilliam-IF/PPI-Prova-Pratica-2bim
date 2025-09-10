from app import db
from app.models.jogador import Jogador


class JogadorController:
    def recuperar_jogador(id):
        return Jogador.query.get(id)


    def listar_jogadores():
        return Jogador.query.all()


    def criar_jogador(form):
        try:
            jogador = Jogador()
            form.populate_obj(jogador)
            db.session.add(jogador)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False


    def atualizar_jogador(jogador, form):
        try:
            form.populate_obj(jogador)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False


    def remover_jogador(jogador):
        try:
            db.session.delete(jogador)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False