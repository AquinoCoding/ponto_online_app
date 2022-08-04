from ponto_online_app import app
from flask import request, redirect
from ponto_online_app.models.user_model import *

autenticacao = user()

@app.route('/autenticar', methods=['POST',])
def authenticate():
    resposta = request.form['cpf_id']
    
    if resposta in autenticacao:
        senha = request.form['password']
        
        print(resposta, senha)
        
        if senha == autenticacao[resposta][1]['password']:
            return redirect('/')
        
        else:
            return redirect('/login')
        
    else:
        return redirect('/login')