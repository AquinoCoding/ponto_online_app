from ponto_online_app import app
from flask import request, redirect, flash, url_for, session
from ponto_online_app.models.users_model import Users

from ponto_online_app.database.db_session import create_session


@app.route('/auth', methods=['POST',])
def authenticate():
    
    usuario = request.form['acess']
    
    with create_session() as ession:
        find_acess = ession.query(Users).filter(Users.cpf_id == usuario).first()

        if find_acess is None:
            flash('CPF não encontrado')
            return redirect(url_for('login'))

        elif find_acess.password != request.form['password']:
            flash('Senha incorreta')
            return redirect(url_for('login'))

        session['usuario_logado'] = find_acess.name
        
        return redirect(url_for('index'))
