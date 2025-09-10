from flask import Flask, render_template, redirect, url_for, flash
from app import app, db
from app.forms import TimeForm, JogadorForm, TreinadorForm, CompeticaoForm, JogoForm
from app.controllers import CompeticaoController, TreinadorController, TimeController, JogadorController, JogoController


@app.route('/')
def index():
    stats = {
        'times': len(TimeController.listar_times()),
        'jogadores': len(JogadorController.listar_jogadores()),
        'treinadores': len(TreinadorController.listar_treinadores()),
        'competicoes': len(CompeticaoController.listar_competicoes()),
        'jogos': len(JogoController.listar_jogos())
    }
    return render_template('index.html', stats=stats)


# Rotas para Times
@app.route('/times')
def times_index():
    times = TimeController.listar_times()
    return render_template('times/index.html', times=times)


@app.route('/times/create', methods=['GET', 'POST'])
def times_create():
    form = TimeForm()
    if form.validate_on_submit():
        resultado = TimeController.criar_time(form)
        if resultado:
            flash('Time cadastrado com sucesso!', 'success')
            return redirect(url_for('times_index'))
        else:
            flash('Erro ao cadastrar time.', 'danger')
    return render_template('times/create.html', form=form)


@app.route('/times/<int:id>/edit', methods=['GET', 'POST'])
def times_edit(id):
    time = TimeController.recuperar_time(id)
    form = TimeForm(obj=time)
    if form.validate_on_submit():
        resultado = TimeController.atualizar_time(time, form)
        if resultado:
            flash('Time atualizado com sucesso!', 'success')
            return redirect(url_for('times_index'))
        else:
            flash('Erro ao atualizar time.', 'danger')
    return render_template('times/edit.html', form=form, time=time)


@app.route('/times/<int:id>/delete', methods=['POST'])
def times_delete(id):
    time = TimeController.recuperar_time(id)
    resultado = TimeController.deletar_time(time)
    if resultado:
        flash('Time excluído com sucesso!', 'success')
    else:
        flash('Erro ao excluir time.', 'danger')
    return redirect(url_for('times_index'))


# Rotas para Jogadores
@app.route('/jogadores')
def jogadores_index():
    jogadores = JogadorController.listar_jogadores()
    return render_template('jogadores/index.html', jogadores=jogadores)


@app.route('/jogadores/create', methods=['GET', 'POST'])
def jogadores_create():
    form = JogadorForm()
    if form.validate_on_submit():
        resultado = JogadorController.criar_jogador(form)
        if resultado:
            flash('Jogador cadastrado com sucesso!', 'success')
            return redirect(url_for('jogadores_index'))
        else:
            flash('Erro ao cadastrar jogador.', 'danger')
    return render_template('jogadores/create.html', form=form)
        

@app.route('/jogadores/<int:id>/edit', methods=['GET', 'POST'])
def jogadores_edit(id):
    jogador = JogadorController.recuperar_jogador(id)
    form = JogadorForm(obj=jogador)
    if form.validate_on_submit():
        resultado = JogadorController.atualizar_jogador(jogador, form)
        if resultado:
            flash('Jogador atualizado com sucesso!', 'success')
            return redirect(url_for('jogadores_index'))
        else:
            flash('Erro ao atualizar jogador.', 'danger')
    return render_template('jogadores/edit.html', form=form, jogador=jogador)


@app.route('/jogadores/<int:id>/delete', methods=['POST'])
def jogadores_delete(id):
    jogador = JogadorController.recuperar_jogador(id)
    resultado = JogadorController.remover_jogador(jogador)
    if resultado:
        flash('Jogador excluído com sucesso!', 'success')
    else:
        flash('Erro ao excluir jogador.', 'danger')
    return redirect(url_for('jogadores_index'))


# Rotas para Treinadores
@app.route('/treinadores')
def treinadores_index():
    treinadores = TreinadorController.listar_treinadores()
    return render_template('treinadores/index.html', treinadores=treinadores)


@app.route('/treinadores/create', methods=['GET', 'POST'])
def treinadores_create():
    form = TreinadorForm()
    if form.validate_on_submit():
        resultado = TreinadorController.criar_treinador(form)
        if resultado:
            flash('Treinador cadastrado com sucesso!', 'success')
            return redirect(url_for('treinadores_index'))
        else:
            flash('Erro ao cadastrar treinador.', 'danger')
    return render_template('treinadores/create.html', form=form)


@app.route('/treinadores/<int:id>/edit', methods=['GET', 'POST'])
def treinadores_edit(id):
    treinador = TreinadorController.recuperar_treinador(id)
    form = TreinadorForm(obj=treinador)
    if form.validate_on_submit():
        resultado = TreinadorController.atualizar_treinador(treinador, form)
        if resultado:
            flash('Treinador atualizado com sucesso!', 'success')
            return redirect(url_for('treinadores_index'))
        else:
            flash('Erro ao atualizar treinador.', 'danger')
    return render_template('treinadores/edit.html', form=form, treinador=treinador)


@app.route('/treinadores/<int:id>/delete', methods=['POST'])
def treinadores_delete(id):
    treinador = TreinadorController.recuperar_treinador(id)
    resultado = TreinadorController.remover_treinador(treinador)
    if resultado:
        flash('Treinador excluído com sucesso!', 'success')
    else:
        flash('Erro ao excluir treinador.', 'danger')
    return redirect(url_for('treinadores_index'))


# Rotas para Competições
@app.route('/competicoes')
def competicoes_index():
    competicoes = CompeticaoController.listar_competicoes()
    return render_template('competicoes/index.html', competicoes=competicoes)

@app.route('/competicoes/create', methods=['GET', 'POST'])
def competicoes_create():
    form = CompeticaoForm()
    if form.validate_on_submit():
        resultado = CompeticaoController.criar_competicao(form)
        if resultado:
            flash('Competição cadastrada com sucesso!', 'success')
            return redirect(url_for('competicoes_index'))
        else:
            flash('Erro ao cadastrar competição.', 'danger')
    return render_template('competicoes/create.html', form=form)


@app.route('/competicoes/<int:id>/edit', methods=['GET', 'POST'])
def competicoes_edit(id):
    competicao = CompeticaoController.recuperar_competicao(id)
    form = CompeticaoForm(obj=competicao)
    if form.validate_on_submit():
        resultado = CompeticaoController.atualizar_competicao(competicao, form)
        if resultado:
            flash('Competição atualizada com sucesso!', 'success')
            return redirect(url_for('competicoes_index'))
        else:
            flash('Erro ao atualizar competição.', 'danger')
    return render_template('competicoes/edit.html', form=form, competicao=competicao)


@app.route('/competicoes/<int:id>/delete', methods=['POST'])
def competicoes_delete(id):
    competicao = CompeticaoController.recuperar_competicao(id)
    resultado = CompeticaoController.remover_competicao(competicao)
    if resultado:
        flash('Competição excluída com sucesso!', 'success')
    else:
        flash('Erro ao excluir competição.', 'danger')
    return redirect(url_for('competicoes_index'))


# Rotas para Jogos
@app.route('/jogos')
def jogos_index():
    jogos = JogoController.listar_jogos()
    return render_template('jogos/index.html', jogos=jogos)


@app.route('/jogos/create', methods=['GET', 'POST'])
def jogos_create():
    form = JogoForm()
    if form.validate_on_submit():
        resultado = JogoController.criar_jogo(form)
        if resultado:
            flash('Jogo cadastrado com sucesso!', 'success')
            return redirect(url_for('jogos_index'))
        else:
            flash('Erro ao cadastrar jogo.', 'danger')
    return render_template('jogos/create.html', form=form)


@app.route('/jogos/<int:id>/edit', methods=['GET', 'POST'])
def jogos_edit(id):
    jogo = JogoController.recuperar_jogo(id)
    form = JogoForm(obj=jogo)
    if form.validate_on_submit():
        resultado = JogoController.atualizar_jogo(jogo, form)
        if resultado:
            flash('Jogo atualizado com sucesso!', 'success')
            return redirect(url_for('jogos_index'))
        else:
            flash('Erro ao atualizar jogo.', 'danger')
    return render_template('jogos/edit.html', form=form, jogo=jogo)
        

@app.route('/jogos/<int:id>/delete', methods=['POST'])
def jogos_delete(id):
    jogo = JogoController.recuperar_jogo(id)
    resultado = JogoController.remover_jogo(jogo)
    if resultado:
        flash('Jogo excluído com sucesso!', 'success')
    else:
        flash('Erro ao excluir jogo.', 'danger')
    return redirect(url_for('jogos_index'))