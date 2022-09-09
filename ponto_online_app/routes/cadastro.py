from ponto_online_app import app, bcrypt
from flask import request, redirect, render_template, flash, url_for, session

# models
from ponto_online_app.models.employees_model import Employees

# services
from ponto_online_app.services.bd_insert import insert_session
from ponto_online_app.services.auth_data import AuthDataUsers, AuthDataEmployees

from sqlalchemy.exc import IntegrityError
from ponto_online_app.database.db_session import create_session


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

        auth = AuthDataUsers(name=name, cnpj_id, email, password, password2).auth_users
        
        for dado in dados:
            
            if len(cnpj_id) > 10:
                return 'CNPJ invalido'
            if len(name)
        

        if auth is True:

            insert_session(name, email, cnpj_id, level, password)

            return redirect(url_for('index'))

        flash(auth)
        return redirect(url_for('cadastro'))

    except IntegrityError:
        flash("CNPJ ou Email já estar cadastrado.")
        return redirect(url_for('cadastro'))


@app.route('/cadastrar_funcionario')
def novo_funcionario_get():
    return render_template("cadastro_employees.html")


@app.route('/cadastrar_novo_funcionario', methods=['POST'])
def novo_funcionario_post():
    try:
        name = request.form['name_employees']
        cpf_id = request.form['cpf_id_employees']
        email = request.form['new_email_employees']
        password = request.form['password_employees']
        password2 = request.form['password2_employees']
        employees1 = session['usuario_logado']
        level = 1

        auth = AuthDataEmployees(name, cpf_id, email, password, password2).auth_employees

        if auth is True:
            with create_session() as session_db:
                employees2 = session_db.query(Users).filter(Users.cnpj_id == employees1).first()
                employees = employees2.id

            password = bcrypt.generate_password_hash(password)

            an: Employees = Employees(name=name, email=email, cpf_id=cpf_id, level=level,
                                      password=password, id_user=employees)
            insert_session(an)

            return redirect(url_for('index'))

        flash(auth)
        return redirect(url_for('novo_funcionario_get'))

    except IntegrityError:
        flash("CPF ou Email já estar cadastrado.")
        return redirect(url_for('novo_funcionario_get'))
