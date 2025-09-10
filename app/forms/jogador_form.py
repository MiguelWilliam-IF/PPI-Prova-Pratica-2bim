from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange
from app.controllers.time_controller import TimeController


class JogadorForm(FlaskForm):
    nome = StringField('Nome do Jogador', validators=[
        DataRequired(message='Nome é obrigatório'),
        Length(min=2, max=100, message='Nome deve ter entre 2 e 100 caracteres')
    ])
    posicao = SelectField('Posição', validators=[DataRequired(message='Posição é obrigatória')], choices=[
        'Selecione uma posição',
        'Goleiro',
        'Zagueiro',
        'Lateral Direito',
        'Lateral Esquerdo',
        'Volante',
        'Meio-campo',
        'Meia-atacante',
        'Ponta Direita',
        'Ponta Esquerda',
        'Atacante'
    ])
    idade = IntegerField('Idade', validators=[
        DataRequired(message='Idade é obrigatória'),
        NumberRange(min=16, max=50, message='Idade deve estar entre 16 e 50 anos')
    ])
    numero_camisa = IntegerField('Número da Camisa', validators=[
        DataRequired(message='Número da camisa é obrigatório'),
        NumberRange(min=1, max=99, message='Número deve estar entre 1 e 99')
    ])
    time_id = SelectField('Time', coerce=int, validators=[DataRequired(message='Time é obrigatório')])
    
    def __init__(self, *args, **kwargs):
        super(JogadorForm, self).__init__(*args, **kwargs)
        # busca todos os times do banco de dados
        times = TimeController.listar_times()

        # cria uma lista de tuplas (id, nome) para popular o campo select
        choices = [(0, 'Selecione um time')]
        
        for i in times:
            choices.append((i.id, i.nome))

        self.time_id.choices = choices