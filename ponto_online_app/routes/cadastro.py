from ponto_online_app import app, bcrypt
from flask import request, redirect, render_template, flash, url_for
from ponto_online_app.models.users_model import Users
from ponto_online_app.models.employees_model import Employees
from ponto_online_app.services.bd_insert import insert_session
from ponto_online_app.services.auth_data import AuthData
from sqlalchemy.exc import IntegrityError
from ponto_online_app.database.db_session import create_session


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/cadastrar-novo-usuario', methods=["POST",])
def cadastro_post():

    try:
        name = request.form['name']
        cnpj_id = request.form['cnpj_id']
        email = request.form['new_email']
        password = request.form['password']
        level = 1

        if password != request.form['password2']:
            flash('Preencha o campo de senhas corretamente.')
            return redirect(url_for('cadastro'))

        resposta1 = AuthData.auth_name(name)[0] is False
        resposta2 = AuthData.auth_cnpj(cnpj_id)[0] is False
        resposta3 = AuthData.auth_email(email)[0] is False
        resposta4 = AuthData.auth_password(password)[0] is False

        if resposta1 or resposta2 or resposta3 or resposta4:
            flash(AuthData.auth_name(name)[1] or AuthData.auth_cnpj(cnpj_id)[1] or
                  AuthData.auth_email(email)[1] or AuthData.auth_password(password)[1])
            return redirect(url_for('cadastro'))

        password = bcrypt.generate_password_hash(password)

        an: Users = Users(name=name, email=email, cnpj_id=cnpj_id, level=level,
                          password=password)
        insert_session(an)

        return redirect(url_for('index'))

    except IntegrityError:
        flash("CNPJ ou Email já estar cadastrado.")
        return redirect(url_for('cadastro'))


@app.route('/cadastrar_funcionario')
def novo_funcionario_get():
    return render_template("cadastro_employees.html")


@app.route('/cadastrar_novo_funcionario', methods=['POST',])
def novo_funcionario_post():
    try:
        name = request.form['name_employees']
        cpf_id = request.form['cpf_id_employees']
        email = request.form['new_email_employees']
        password = request.form['password_employees']
        employees1 = request.form['employees']
        level = 1

        with create_session() as session_db:
            employees2 = session_db.query(Users).filter(Users.cnpj_id == employees1).first()
            employees = employees2.id

        password = bcrypt.generate_password_hash(password)

        an: Employees = Employees(name=name, email=email, cpf_id=cpf_id, level=level,
                                  password=password, id_user=employees)
        insert_session(an)

        return redirect(url_for('index'))

    except IntegrityError:
        flash("CNPJ ou Email já estar cadastrado.")
        return redirect(url_for('cadastro'))
