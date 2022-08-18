__version__ = '0.1.0'

from flask import Flask
from ponto_online_app.database.db_session import create_tables

from os import getenv

app = Flask(__name__)
db = create_tables()

app.secret_key = '66e0c4a852d3b55ca598abf7792086b2'

from .all_routes import *
