from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange, Optional



class CompeticaoForm(FlaskForm):
    nome = StringField('Nome da Competição', validators=[
        DataRequired(message='Nome é obrigatório'),
        Length(min=2, max=100, message='Nome deve ter entre 2 e 100 caracteres')
    ])
    temporada = IntegerField('Temporada', validators=[
        DataRequired(message='Temporada é obrigatória'),
        NumberRange(min=1900, max=2100, message='Temporada deve ser válida')
    ])
    data_inicio = DateField('Data de Início', validators=[
        DataRequired(message='Data de início é obrigatória')
    ])
    data_fim = DateField('Data de Fim', validators=[
        DataRequired(message='Data de fim é obrigatória')
    ])
    descricao = TextAreaField('Descrição', validators=[Optional(), Length(max=500)])
    
    # validação customizada para garantir que data_fim seja após data_inicio
    def validate_data_fim(self, field):
        if field.data <= self.data_inicio.data:
            raise ValidationError('Data de fim deve ser posterior à data de início')
