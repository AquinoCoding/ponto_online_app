from ponto_online_app import app, bcrypt
from flask import request, redirect, flash, url_for, session
from ponto_online_app.models.users_model import Users
from ponto_online_app.models.employees_model import Employees
from ponto_online_app.database.db_session import create_session


@app.route('/auth', methods=['POST'])
def authenticate():
    
    usuario = request.form['acess']
    password = request.form['password']

    with create_session() as session_db:
        find_acess = session_db.query(Users).filter(Users.cnpj_id == usuario).first()
        find_acess_employees = session_db.query(Employees).filter(Employees.cpf_id == usuario).first()

        if find_acess is None:
            if find_acess_employees is None:
                flash('Usuário não encontrado')
                return redirect(url_for('login'))

            elif bcrypt.check_password_hash(find_acess_employees.password, password) is False:
                flash('Senha incorreta')
                return redirect(url_for('login'))

            session['usuario_logado'] = usuario
            return redirect(url_for('index'))

        elif bcrypt.check_password_hash(find_acess.password, password) is False:
            flash('Senha incorreta')
            return redirect(url_for('login'))

        session['usuario_logado'] = usuario
        session.permanent = True
        return redirect(url_for('index'))
