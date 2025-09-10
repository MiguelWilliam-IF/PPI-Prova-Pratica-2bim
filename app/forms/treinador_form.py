from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class TreinadorForm(FlaskForm):
    nome = StringField('Nome do Treinador', validators=[
        DataRequired(message='Nome é obrigatório'),
        Length(min=2, max=100, message='Nome deve ter entre 2 e 100 caracteres')
    ])
    idade = IntegerField('Idade', validators=[
        DataRequired(message='Idade é obrigatória'),
        NumberRange(min=25, max=80, message='Idade deve estar entre 25 e 80 anos')
    ])
    nacionalidade = StringField('Nacionalidade', validators=[
        DataRequired(message='Nacionalidade é obrigatória'),
        Length(min=2, max=50, message='Nacionalidade deve ter entre 2 e 50 caracteres')
    ])
    anos_experiencia = IntegerField('Anos de Experiência', validators=[
        DataRequired(message='Anos de experiência são obrigatórios'),
        NumberRange(min=0, max=60, message='Experiência deve estar entre 0 e 60 anos')
    ])