from ponto_online_app import app
from flask import render_template, redirect, url_for, flash, session
from ponto_online_app.models.point_model import Point
from ponto_online_app.services.bd_insert import insert_session
from ponto_online_app.database.db_session import create_session
from ponto_online_app.models.employees_model import Employees
from ponto_online_app.services.time import date_time


@app.route('/ponto')
def point():
    return render_template("point.html")


@app.route('/validation_point', methods=['POST'])
def validation_point():

    employees = session['usuario_logado']

    with create_session() as session_db:
        usuario1 = session_db.query(Employees).filter(Employees.cpf_id == employees).first()
        usuario = usuario1.id

    an: Point = Point(id_employees=usuario)
    insert_session(an)

    time = date_time()
    flash(f'Ponto batido com sucesso. ({time})')
    return redirect(url_for('index'))
