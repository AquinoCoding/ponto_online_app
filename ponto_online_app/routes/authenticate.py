from ponto_online_app import app
from flask import request, redirect, session, flash
from ponto_online_app.models.user_model import *

autenticacao = user()

@app.route('/autenticar', methods=['POST',])
def authenticate():
    resposta = request.form['cpf_id']
    
    if resposta in autenticacao:
        senha = request.form['password']

        
        if senha == autenticacao[resposta][1]['password']:
            session['usuario_logado'] = request.form['cpf_id']
            flash('Usuário logado com sucesso.')
            return redirect('/')
        
        else:
            flash('Usuário não encontrado.')
            return redirect('/login')
        
    else:
        return redirect('/login')
