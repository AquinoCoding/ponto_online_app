from ponto_online_app import app, bcrypt
from flask import request, redirect, flash, url_for, session

from ponto_online_app.services.bd_read import read_user_single_session, read_employees_single_session


@app.route('/auth', methods=['POST'])
def authenticate():
    
    usuario = request.form['acess']
    password = request.form['password']

    find_acess_user = read_user_single_session(usuario)
    find_acess_employees = read_employees_single_session(usuario)

    if find_acess_user[0] is None:
        if find_acess_employees is None:
            flash('Usuário não encontrado')
            return redirect(url_for('login'))

        elif bcrypt.check_password_hash(find_acess_employees[1], password) is False:
            flash('Senha incorreta')
            return redirect(url_for('login'))

        session['funcionario_logado'] = usuario
        return redirect(url_for('index'))

    elif bcrypt.check_password_hash(find_acess_user[1], password) is False:
        flash('Senha incorreta')
        return redirect(url_for('login'))

    session['usuario_logado'] = usuario
    session.permanent = True
    return redirect(url_for('index'))
