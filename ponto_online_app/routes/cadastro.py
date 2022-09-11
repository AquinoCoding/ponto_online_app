from ponto_online_app import app
from flask import request, redirect, render_template, flash, url_for

# services
from ponto_online_app.services.bd_insert import insert_session_users
from ponto_online_app.services.auth_data import auth_name, auth_cnpj, auth_email

from sqlalchemy.exc import IntegrityError


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/cadastrar-novo-usuario', methods=["POST"])
def cadastro_post():

    try:
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

        if authe_name[0] is False or authe_cnpj[0] is False or authe_email[0] is False:
            flash(authe_name[1] or authe_cnpj[1] or authe_email[1])
            return redirect(url_for('cadastro'))

        insert_session_users(name, email, cnpj_id, level, password)
        return redirect(url_for('index'))

    except IntegrityError:
        flash("CNPJ ou Email já estar cadastrado.")
        return redirect(url_for('cadastro'))
