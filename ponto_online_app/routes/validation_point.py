from ponto_online_app import app
from flask import render_template, redirect, url_for, flash, session, request

from datetime import date, datetime

from ponto_online_app.services.bd_insert import insert_point
from ponto_online_app.services.time import date_time

from ponto_online_app.database.db_session import create_session

from ponto_online_app.models.employees_model import Employees

from ponto_online_app.services.bd_read import read_all_point



@app.route('/ponto')
def point():
        
    obj = read_all_point('luiz')
    print(obj)

    """     if 'funcionario_logado' not in session:
            flash('Entrada não autorizada')
            return redirect(url_for('index'))
    """
    return render_template("point.html")


@app.route('/validation-point', methods=['POST'])
def validation_point():

    #employees = session['funcionario_logado']

    """     with create_session() as session_db:
            usuario1 = session_db.query(Employees).filter(Employees.cpf_id == employees).first()
            usuario = usuario1.cpf_id """
            

    print(str(date.today()))
    
    insert_point('admin', str(date.today()))

    flash(f'Ponto batido com sucesso. ({date_time()})')
    return redirect(url_for('index'))
