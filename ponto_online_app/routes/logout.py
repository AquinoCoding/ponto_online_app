from ponto_online_app import app
from flask import session, flash, redirect, url_for


@app.route('/logout')
def logout():
    session.pop('usuario_logado')
    flash('Logout efetuado com sucesso.')
    return redirect(url_for('login'))
