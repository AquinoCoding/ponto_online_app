from ponto_online_app import app
from flask import request, redirect, session, flash

from ponto_online_app.models.users_model import Users

from ponto_online_app.database.db_session import create_session

@app.route('/auth', methods=['POST',])
def authenticate():
    
    usuario = request.form['acess']
    
    with create_session() as session:
        find_acess = session.query(Users).filter(Users.cpf_id == usuario).first()
        print(find_acess)
        if find_acess != None:
            flash('CPF não encontrado')
            return redirect('/login')
        
        elif find_acess.password != request.form['password']:
            flash('Senha incorreta')
            return redirect('/login')
        
        return redirect('/index')
