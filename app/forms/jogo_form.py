from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, DateTimeLocalField, ValidationError
from wtforms.validators import DataRequired, NumberRange, Optional
from app.controllers.competicao_controller import CompeticaoController
from app.controllers.time_controller import TimeController
from app.models import Time, Competicao


class JogoForm(FlaskForm):
    data_hora = DateTimeLocalField('Data e Hora', validators=[
        DataRequired(message='Data e hora são obrigatórias')
    ])
    time_casa_id = SelectField('Time da Casa', coerce=int, validators=[
        DataRequired(message='Time da casa é obrigatório')
    ])
    time_visitante_id = SelectField('Time Visitante', coerce=int, validators=[
        DataRequired(message='Time visitante é obrigatório')
    ])
    competicao_id = SelectField('Competição', coerce=int, validators=[
        DataRequired(message='Competição é obrigatória')
    ])
    gols_casa = IntegerField('Gols Time Casa', validators=[
        Optional(), NumberRange(min=0, max=20, message='Gols devem estar entre 0 e 20')
    ])
    gols_visitante = IntegerField('Gols Time Visitante', validators=[
        Optional(), NumberRange(min=0, max=20, message='Gols devem estar entre 0 e 20')
    ])
    status = SelectField('Status', validators=[DataRequired()], choices=[
        'Agendado', 'Em Andamento', 'Finalizado', 'Cancelado'
    ])
    
    def __init__(self, *args, **kwargs):
        super(JogoForm, self).__init__(*args, **kwargs)
        # busca todos os times do banco de dados
        times = TimeController.listar_times()
        competicoes = CompeticaoController.listar_competicoes()

        # cria uma lista de tuplas (id, nome) para popular o campo select
        choices = [(0, 'Selecione o time da casa')]
        for i in times:
            choices.append((i.id, i.nome))
        self.time_casa_id.choices = choices

        # cria uma lista de tuplas (id, nome) para popular o campo select
        choices = [(0, 'Selecione o time visitante')]
        for i in times:
            choices.append((i.id, i.nome))
        self.time_visitante_id.choices = choices
        
        # cria uma lista de tuplas (id, nome) para popular o campo select
        choices = [(0, 'Selecione a competição')]
        for i in competicoes:
            choices.append((i.id, f"{i.nome} {i.temporada}"))
        self.competicao_id.choices = choices

    # valida se a seleção de times é consistente
    def validate_time_visitante_id(self, field):
        if field.data == self.time_casa_id.data:
            raise ValidationError('Time visitante deve ser diferente do time da casa')