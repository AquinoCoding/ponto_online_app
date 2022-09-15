from ponto_online_app import app
from flask import session, flash, redirect, url_for


@app.route('/logout')
def logout():

    if 'usuario_logado' in session:
        session.pop('usuario_logado')

    elif 'funcionario_logado' in session:
        session.pop('funcionario_logado')

    flash('Logout efetuado com sucesso.')
    return redirect(url_for('login'))
