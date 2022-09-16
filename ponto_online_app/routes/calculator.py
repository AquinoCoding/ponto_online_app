from ponto_online_app import app

from flask import render_template, redirect, request, url_for, flash

from ponto_online_app.services.time_calculator import calculator


@app.route('/calcular-tempo', methods=['GET', 'POST'])
def time_calculator():
    return render_template('time_calculator.html')


@app.route('/time-calculator', methods=['POST'])
def full_time():
    date = request.form['date']
    print(date)
    cpf = "admin"

    resultado = calculator(cpf, date)
    print(resultado, "<-----------", type(resultado))
    flash('teste')

    flash(resultado)

    return redirect(url_for('index'))
