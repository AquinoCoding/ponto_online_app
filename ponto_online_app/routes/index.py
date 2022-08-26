from ponto_online_app import app

from flask import render_template, redirect, session, flash, url_for


@app.route('/')
def index():
    if 'usuario_logado' not in session:
        flash('Faça o login primeiro')
        return redirect(url_for('login'))

    return render_template('index.html', title='Ponto Online App')
