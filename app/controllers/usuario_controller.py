from app import db
import sqlalchemy as sa
from app.models import Usuario
from werkzeug.security import generate_password_hash


class UsuarioController:
    def salvar(form):
        try:
            usuario = Usuario()
            form.populate_obj(usuario)
            usuario.password_hash = generate_password_hash(form.password.data) # Gera a senha e atribui ao atributo do usuário
            
            db.session.add(usuario)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(e)
            return False
    
    
    def listar_usuarios():
        query = sa.select(Usuario)
        usuarios = db.session.scalars(query)
        return usuarios
    
    
    def buscar_por_username(username):
        query = sa.select(Usuario).where(Usuario.username == username)
        usuario = db.session.scalars(query).first()
        return usuario
    
    
    def atualizar_usuario(id, form):
        usuario = db.session.get(Usuario, id)
        if usuario:
            usuario.username = form.username
            db.session.commit()
            print('Usuário atualizado com sucesso!')
        else:
            print('Usuário não encontrado.')
            
            
    def remover_usuario(id):
        usuario = db.session.get(Usuario, id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            print('Usuário removido com sucesso!')
        else:
            print('Usuário não encontrado.')

    def checar_unicidade(campo, tipo):
        if tipo == 'username':
            if Usuario.query.filter_by(username=campo).first():
                return False
        if tipo == 'email':
            if Usuario.query.filter_by(email=campo).first():
                return False
        return True