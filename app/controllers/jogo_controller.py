from app import db
from app.models.jogo import Jogo


class JogoController:
    def recuperar_jogo(id):
        return Jogo.query.get(id)


    def listar_jogos():
        return Jogo.query.all()


    def criar_jogo(form):
        try:
            jogo = Jogo()
            form.populate_obj(jogo)
            db.session.add(jogo)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False


    def atualizar_jogo(jogo, form):
        try:
            form.populate_obj(jogo)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False


    def remover_jogo(jogo):
        try:
            db.session.delete(jogo)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False