from ponto_online_app import app

from flask import render_template, redirect, request, url_for, flash, session

from ponto_online_app.services.time_calculator import calculator
from ponto_online_app.services.bd_read import read_all_point_email


@app.route('/calcular-tempo', methods=['GET', 'POST'])
def time_calculator():
    return render_template('time-calculator.html')


@app.route('/tabela-tempo', methods=['GET', 'POST'])
def tabela_tempo():

    employees = session['funcionario_logado']
    hora_extra = calculator(employees)
    
    return render_template('tabela-pontos.html',
                           itens=[str(item) for item in read_all_point_email(employees)], hora_extra=hora_extra)


@app.route('/time-calculator', methods=['POST'])
def full_time():
    date = request.form['date']
    print(date)
    email = session['funcionario_logado']

    resultado = calculator(email)
    print(resultado, "<-----------", type(resultado))

    flash(resultado)

    return redirect(url_for('index'))
