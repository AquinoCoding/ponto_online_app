from ponto_online_app import app, db
from flask import request, redirect
from ponto_online_app.models.database_model import User


@app.route("/cadastrar-novo-usuario", methods=["POST",])
def cadastroi():
    username = request.form['cpf_id']
    name = request.form['name']
    password = request.form['password']
    email = request.form['new_email']
    registration = User(username, name, password, email)
    db.session.add(registration)
    db.session.commit()

    return redirect('/')