from ponto_online_app import app
from flask import render_template, request

@app.route('/ponto')
def point(user):
    return render_template("point.html")


@app.route('/validation_point', methods=['GET', 'POST'])
def validation_point():
    resultado = request.form['ponto']
    return resultado