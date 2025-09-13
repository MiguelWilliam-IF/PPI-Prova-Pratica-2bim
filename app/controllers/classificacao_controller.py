from app import db
from app.controllers import JogoController
from app.controllers import TimeController
from app.models import Jogo
from sqlalchemy import select, or_, and_
from sqlalchemy.sql.functions import sum as sum_

class ClassificacaoController:
    def recuperar_informacoes_classificacao(): #NOME, QTD JOGOS DISPUTADOS, VITORIAS, EMPATES, DERROTAS, GOLS MARCADOS, GOLS SOFRIDOS, SALDO DE GOLS, PONTOS
        try:
            pontos_dict = ClassificacaoController.listar_dicionario_placar()

            dados = []

            for id in pontos_dict:
                jogos_stmt = select(Jogo).where(or_(Jogo.time_casa_id == id, Jogo.time_visitante_id == id))
                vitorias_stmt = select(Jogo).where(or_(and_(Jogo.time_casa_id == id, Jogo.gols_casa > Jogo.gols_visitante), and_(Jogo.time_visitante_id == id, Jogo.gols_visitante > Jogo.gols_casa)))
                empates_stmt = select(Jogo).where(and_(or_(Jogo.time_casa_id == id, Jogo.time_visitante_id == id), Jogo.gols_casa == Jogo.gols_visitante))
                derrotas_stmt = select(Jogo).where(or_(and_(Jogo.time_casa_id == id, Jogo.gols_casa < Jogo.gols_visitante), and_(Jogo.time_visitante_id == id, Jogo.gols_visitante < Jogo.gols_casa)))
                gols_feitos_casa_stmt = select(sum_(Jogo.gols_casa)).select_from(Jogo).where(Jogo.time_casa_id == id)
                gols_feitos_visitante_stmt = select(sum_(Jogo.gols_visitante)).select_from(Jogo).where(Jogo.time_visitante_id == id)
                gols_sofridos_casa_stmt = select(sum_(Jogo.gols_visitante)).select_from(Jogo).where(Jogo.time_casa_id == id)
                gols_sofridos_visitante_stmt = select(sum_(Jogo.gols_casa)).select_from(Jogo).where(Jogo.time_visitante_id == id)
                
                dados_time = {
                    'nome': TimeController.recuperar_time(id=id).nome,
                    'jogos-disputados': len(db.session.execute(jogos_stmt).all()),
                    'vitorias': len(db.session.execute(vitorias_stmt).all()),
                    'empates': len(db.session.execute(empates_stmt).all()),
                    'derrotas': len(db.session.execute(derrotas_stmt).all()),
                    'gols-marcados': sum([int(db.session.execute(gols_feitos_casa_stmt).first()[0] or 0), int(db.session.execute(gols_feitos_visitante_stmt).first()[0] or 0)]),
                    'gols-sofridos': sum([int(db.session.execute(gols_sofridos_casa_stmt).first()[0] or 0), int(db.session.execute(gols_sofridos_visitante_stmt).first()[0] or 0)]),
                    'gols-saldo': sum([int(db.session.execute(gols_feitos_casa_stmt).first()[0] or 0), int(db.session.execute(gols_feitos_visitante_stmt).first()[0] or 0)]) - sum([int(db.session.execute(gols_sofridos_casa_stmt).first()[0] or 0), int(db.session.execute(gols_sofridos_visitante_stmt).first()[0] or 0)]),
                    'pontos': pontos_dict[id]
                        }
                dados.append(dados_time)
                

            return dados
        
        except Exception as e:
            print(f"ERRO NA RECUPERAÇÃO DAS INFORMAÇÕES DE CLASSIFICAÇÃO: {e}")
            return False


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

        return dict(sorted(pontos.items(), key=lambda item: item[1], reverse=True))
