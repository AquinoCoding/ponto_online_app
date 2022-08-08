from ponto_online_app import app
from flask import render_template, redirect, session, flash


@app.route('/')
def index():
    if 'usuario_logado' in session or 'usuario_logado' == None:
        flash('Faça o login primeiro')
        return redirect('/login')

    return render_template('index.html', title='Ponto Online App')
