from ponto_online_app import app
from flask import render_template

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')