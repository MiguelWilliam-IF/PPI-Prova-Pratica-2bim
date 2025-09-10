from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from app.controllers.treinador_controller import TreinadorController
from app.models import Treinador
from datetime import datetime


class TimeForm(FlaskForm):
    nome = StringField('Nome do Time', validators=[
        DataRequired(message='Nome é obrigatório'),
        Length(min=2, max=100, message='Nome deve ter entre 2 e 100 caracteres')
    ])
    cidade = StringField('Cidade', validators=[
        DataRequired(message='Cidade é obrigatória'),
        Length(min=2, max=100, message='Cidade deve ter entre 2 e 100 caracteres')
    ])
    ano_fundacao = IntegerField('Ano de Fundação', validators=[
        DataRequired(message='Ano de fundação é obrigatório'),
        NumberRange(min=1850, max=datetime.now().year, message='Ano deve ser válido')
    ])
    # o atributo coerce é utilizado para converter o valor selecionado em um inteiro
    treinador_id = SelectField('Treinador', coerce=int, validators=[Optional()])
    
    def __init__(self, *args, **kwargs):
        super(TimeForm, self).__init__(*args, **kwargs)
        # busca todos os treinadores do banco de dados
        treinadores = TreinadorController.listar_treinadores()
        
        # cria uma lista de tuplas (id, nome) para popular o campo select
        choices = [(0, 'Selecione um treinador')]
        
        for i in treinadores:
            choices.append((i.id, i.nome))
        
        self.treinador_id.choices = choices