from ponto_online_app import app
from flask import request, redirect, render_template, flash, url_for, session

# services
from ponto_online_app.services.bd_insert import insert_session_users, insert_session_employees
from ponto_online_app.services.bd_read import read_user_single_session
from ponto_online_app.services.auth_data import auth_name, auth_cnpj, auth_email, auth_existence_user, \
    auth_existence_employees, auth_cpf


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/cadastrar-novo-usuario', methods=["POST"])
def cadastro_post():

    name = request.form['name']
    cnpj_id = request.form['cnpj_id']
    email = request.form['new_email']
    password = request.form['password']
    password2 = request.form['password2']
    level = 1

    if password != password2:
        flash('Preencha o campo de senhas corretamente.')
        return redirect(url_for('cadastro'))

    elif len(password) < 6:
        flash('A senha precisa ter no mínimo 6 caracteres.')
        return redirect(url_for('cadastro'))

    authe_name = auth_name(name)
    authe_cnpj = auth_cnpj(cnpj_id)
    authe_email = auth_email(email)
    authe_user = auth_existence_user(email, cnpj_id)

    if authe_name is not None or authe_cnpj is not None \
            or authe_email is not None or authe_user is not None:

        flash(authe_name or authe_cnpj or authe_email or authe_user)
        return redirect(url_for('cadastro'))

    insert_session_users(name, email, cnpj_id, level, password)
    return redirect(url_for('index'))


@app.route('/cadastrar-funcionario')
def novo_funcionario_get():

    if 'usuario_logado' not in session:
        flash('Entrada não autorizada.')
        return redirect(url_for('index'))

    return render_template("cadastro_employees.html")


@app.route('/cadastrar-novo-funcionario', methods=['POST'])
def novo_funcionario_post():

    name = request.form['name_employees']
    cpf_id = request.form['cpf_id_employees']
    email = request.form['new_email_employees']
    password = request.form['password_employees']
    password2 = request.form['password2_employees']
    id_user = read_user_single_session(session['usuario_logado'])["id"]
    level = 1

    if password != password2:
        flash('Preencha o campo de senhas corretamente.')
        return redirect(url_for('novo_funcionario_get'))

    elif len(password) < 6:
        flash('A senha precisa ter no mínimo 6 caracteres.')
        return redirect(url_for('novo_funcionario_get'))

    authe_name = auth_name(name)
    authe_cpf = auth_cpf(cpf_id)
    authe_email = auth_email(email)
    authe_employees = auth_existence_employees(email, cpf_id)

    if authe_name is not None or authe_cpf is not None or authe_email is not None \
            or authe_employees is not None:
        flash(authe_name or authe_cpf or authe_email or authe_employees)
        return redirect(url_for('novo_funcionario_get'))

    insert_session_employees(name, email, cpf_id, level, password, id_user)

    return redirect(url_for('index'))
