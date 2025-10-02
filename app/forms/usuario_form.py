from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from app.controllers.usuario_controller import UsuarioController
from wtforms import ValidationError

class UsuarioForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message="Por favor, preencha o nome de usuário.")])
    email = EmailField('Email', validators=[DataRequired(message="Por favor, preencha o email."), Email(message="Email inválido")])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Salvar')

    def validate_username(self, username):
        if not UsuarioController.checar_unicidade(username.data.strip(), 'username'):
            raise ValidationError('Nome de usuário já cadastrado!')
        
    def validate_email(self, email):
        if not UsuarioController.checar_unicidade(email.data.strip().lower(), 'email'):
            raise ValidationError('Endereço de email já cadastrado!')