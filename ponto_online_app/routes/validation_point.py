from ponto_online_app import app
from flask import render_template, redirect, url_for, flash, session
from ponto_online_app.services.bd_insert import insert_point
from ponto_online_app.database.db_session import create_session
from ponto_online_app.models.employees_model import Employees
from ponto_online_app.services.time import date_time
from datetime import date, datetime


@app.route('/ponto')
def point():

    if 'funcionario_logado' not in session:
        flash('Entrada não autorizada')
        return redirect(url_for('index'))

    return render_template("point.html")


@app.route('/validation_point', methods=['POST'])
def validation_point():

    employees = session['funcionario_logado']

    with create_session() as session_db:
        usuario1 = session_db.query(Employees).filter(Employees.cpf_id == employees).first()
        usuario = usuario1.cpf_id

    date_day = str(date.today())
    time_day = datetime.now()
    time_formatacao = time_day.strftime('%H:%M:%S')

    insert_point(usuario, date_day, time_formatacao)

    hours = date_time()
    flash(f'Ponto batido com sucesso. ({hours})')
    return redirect(url_for('index'))
