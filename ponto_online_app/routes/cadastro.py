from ponto_online_app import app
from flask import request, redirect, render_template, flash, url_for
from ponto_online_app.models.users_model import Users
from ponto_online_app.services.bd_insert import insert_session
from ponto_online_app.services.auth_data import AuthData


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route("/cadastrar-novo-usuario", methods=["POST",])
def cadastro_post():

    name = request.form['name']
    cpf_id = request.form['cpf_id']
    email = request.form['new_email']
    password = request.form['password']
    level = 1

    if "" == request.form['password2'] or password != request.form['password2']:
        flash('Preencha o campo de senhas corretamente.')
        return redirect(url_for('cadastro'))

    resposta1 = AuthData.auth_name(name)[0] is False
    resposta2 = AuthData.auth_cpf(cpf_id)[0] is False
    resposta3 = AuthData.auth_email(email)[0] is False
    resposta4 = AuthData.auth_password(password)[0] is False

    if resposta1 or resposta2 or resposta3 or resposta4:
        flash(AuthData.auth_name(name)[1] or AuthData.auth_cpf(cpf_id)[1] or
              AuthData.auth_email(email)[1] or AuthData.auth_password(password)[1])
        return redirect(url_for('cadastro'))

    an: Users = Users(name=name, email=email, cpf_id=cpf_id, level=level, password=password)
    insert_session(an)

    return redirect(url_for('index'))
