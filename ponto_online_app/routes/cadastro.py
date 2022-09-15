from ponto_online_app import app
from flask import request, redirect, render_template, flash, url_for

# services
from ponto_online_app.services.bd_insert import insert_session_users
from ponto_online_app.services.auth_data import auth_name, auth_cnpj, auth_email, auth_existence_user


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
