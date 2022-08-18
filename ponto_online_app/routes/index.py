from ponto_online_app import app

from flask import render_template, redirect, session, flash

@app.route('/')
def index():

    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        flash('Faça o login primeiro')
        return redirect('/login')

    return render_template('index.html', title='Ponto Online App')
