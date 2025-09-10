from app import db
from app.models.jogo import Jogo
from app.controllers import JogoController

def listarClassificacao():
    print(JogoController.listar_jogos)