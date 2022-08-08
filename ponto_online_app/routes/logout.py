from ponto_online_app import app
from flask import session, flash, redirect

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso.')
    return redirect('/login')