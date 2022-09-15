from ponto_online_app import app

from ponto_online_app.services.auth_data import auth_name, auth_cpf, auth_email, auth_existence_employees
from ponto_online_app.services.bd_insert import insert_session_employees

from flask import request, redirect, render_template, flash, url_for, session
from ponto_online_app.database.db_session import create_session
from ponto_online_app.models.users_model import Users


@app.route('/cadastrar_funcionario')
def novo_funcionario_get():

    if 'usuario_logado' not in session:
        flash('Entrada não autorizada.')
        return redirect(url_for('index'))

    return render_template("cadastro_employees.html")


@app.route('/cadastrar_novo_funcionario', methods=['POST'])
def novo_funcionario_post():

    name = request.form['name_employees']
    cpf_id = request.form['cpf_id_employees']
    email = request.form['new_email_employees']
    password = request.form['password_employees']
    password2 = request.form['password2_employees']
    employees1 = session['usuario_logado']
    level = 1

    if password != password2:
        flash('Preencha o campo de senhas corretamente.')
        return redirect(url_for('novo_funcionario_get'))

    elif len(password) < 6:
        flash('A senha precisa ter no mínimo 6 caracteres.')
        return redirect(url_for('novo_funcionario_get'))

    with create_session() as session_db:
        employees2 = session_db.query(Users).filter(Users.cnpj_id == employees1).first()
        employees = employees2.id

    authe_name = auth_name(name)
    authe_cpf = auth_cpf(cpf_id)
    authe_email = auth_email(email)
    authe_employees = auth_existence_employees(email, cpf_id)

    if authe_name is not None or authe_cpf is not None or authe_email is not None \
            or authe_employees is not None:
        flash(authe_name or authe_cpf or authe_email or authe_employees)
        return redirect(url_for('novo_funcionario_get'))

    insert_session_employees(name, email, cpf_id, level, password, employees)

    return redirect(url_for('index'))
