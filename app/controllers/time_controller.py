from app import db
from app.models.time import Time


class TimeController:
    def recuperar_time(id):
        return Time.query.get(id)


    def listar_times():
        return Time.query.all()


    def criar_time(form):
        try:
            time = Time()
            form.populate_obj(time)
            db.session.add(time)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False


    def atualizar_time(time, form):
        try:
            form.populate_obj(time)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False


    def remover_time(time):
        try:
            db.session.delete(time)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False