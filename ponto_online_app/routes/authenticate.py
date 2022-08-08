from ponto_online_app import app
from ponto_online_app.models.database_model import User
from flask import request, redirect, session, flash

@app.route('/autenticar', methods=['POST',])
def authenticate():
    usuario = request.form['cpf_id']
    procurar = User.query.filter_by(username=usuario).first()
    check_password = request.form['password'] == procurar.password

    if procurar is None:
        flash('Usuário ou senha incorretos')
        return redirect('/login')

    else:
        if check_password == True:
            session['usuario_logado'] = request.form['cpf_id']
            flash('Usuário logado com sucesso.')
            return redirect('/')
        else:
            flash('Usuário ou senha incorretos')
            return redirect('/login')









#resposta = request.form['cpf_id']
    
    #if resposta in autenticacao:
        #senha = request.form['password']

        
        #if senha == autenticacao[resposta][1]['password']:
            #session['usuario_logado'] = request.form['cpf_id']
            #flash('Usuário logado com sucesso.')
            #return redirect('/')
        
        #else:
            #flash('Usuário não encontrado.')
            #return redirect('/login')
        
    #else:
        #return redirect('/login')
