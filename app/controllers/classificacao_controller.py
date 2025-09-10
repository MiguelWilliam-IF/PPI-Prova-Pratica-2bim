from app import db
from app.models.jogo import Jogo
from app.controllers import JogoController
from app.controllers import TimeController

class ClassificacaoController:
    def listar_dicionario_placar():
        jogos = JogoController.listar_jogos()
        pontos = {time.id: 0 for time in TimeController.listar_times()}

        for jogo in jogos:
            if jogo.status != 'Finalizado': continue

            match jogo.resultado():
                case 'casa': #3 PONTOS PRA CASA
                    pontos[jogo.time_casa_id] += 3

                case 'visitante': #3 PONTOS PRO VISITANTE
                    pontos[jogo.time_visitante_id] += 3

                case 'empate': #1 PONTO PROS DOIS TIMES
                    pontos[jogo.time_casa_id] += 1
                    pontos[jogo.time_visitante_id] += 1

        return pontos