from ponto_online_app import app
from flask import render_template

from ponto_online_app.models.login_model import *

@app.route('/login')
def login():
    
    auth = authenticate()
    if auth == True:
        pass
        #ponto passou 
    else:
        return render_template('login.html', title='Ponto Online App Login')
