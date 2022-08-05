from ponto_online_app import app
from flask import render_template, redirect, session, flash

@app.route('/cadastro')
def cadastro():
    if 'usuario_logado' not in session or 'usuario_logado' == None:
        flash('Faça o login primeiro')
        return redirect('/login')

    return render_template('cadastro.html')