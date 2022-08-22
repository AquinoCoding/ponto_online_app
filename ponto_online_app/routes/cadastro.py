from ponto_online_app import app
from flask import request, redirect, render_template, flash, url_for
from ponto_online_app.models.users_model import Users
from ponto_online_app.services.bd_insert import insert_session


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
    
    if password != request.form['password2']:
        flash('Senhas não iguais')
        return redirect('/login')
    
    an: Users = Users(name=name, email=email, cpf_id=cpf_id, level=level, password=password)
    insert_session(an)

    return redirect(url_for('index'))