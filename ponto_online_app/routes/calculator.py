from ponto_online_app import app

from flask import render_template, redirect, request, url_for, flash, session

from ponto_online_app.services.time_calculator import calculator_all, calculator_day, calculator_month
from ponto_online_app.services.bd_read import read_all_point_email, read_employees_single_session
from ponto_online_app.services.time import ponto_formatado


@app.route('/calcular-tempo', methods=['GET', 'POST'])
def time_calculator():
    return render_template('time-calculator.html')


@app.route('/tabela-tempo', methods=['GET', 'POST'])
def tabela_tempo():

    employees = session['funcionario_logado']
    hora_extra = calculator_all(employees)
    
    return render_template('tabela-pontos.html',
                           itens=[ponto_formatado(item) for item in read_all_point_email(employees)], hora_extra=hora_extra)


@app.route('/time-calculator', methods=['POST'])
def full_time():
    date = request.form['date']
    email = session['funcionario_logado']

    resultado = calculator_day(email, date)
    print(resultado, "<-----------", type(resultado))

    flash(resultado)

    return redirect(url_for('index'))


@app.route('/consultar-horas', methods=['GET', 'POST'])
def consult_hours():

    consulta_hora_extra = read_employees_single_session(session['funcionario_logado'])['extra_hour']
    
    if 'hours_day' not in request.form:
        if 'hours_month' not in request.form:
            return render_template('consulta-horas.html', resultado_mes='--:--', resultado_dia='--:--', 
                                    resultado_hora_extra=consulta_hora_extra)

        return render_template('consulta-horas.html', resultado_dia='--:--', resultado_hora_extra=consulta_hora_extra)

    if 'hours_month' not in request.form:
            return render_template('consulta-horas.html', resultado_mes='--:--', resultado_hora_extra=consulta_hora_extra)

    consulta_dia = calculator_day(session['funcionario_logado'],request.form['hours_day'])
    consulta_mes = calculator_month(session['funcionario_logado'],request.form['hours_month'])


    return render_template('consulta-horas.html', resultado_mes=consulta_mes, resultado_dia=consulta_dia, 
                            resultado_hora_extra=consulta_hora_extra)
