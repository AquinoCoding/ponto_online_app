__version__ = '0.1.0'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



app.secret_key = '66e0c4a852d3b55ca598abf7792086b2'

from .all_routes import *
from ponto_online_app.models import database_model
