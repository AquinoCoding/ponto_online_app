__version__ = '0.1.0'

from flask import Flask
from flask_bcrypt import Bcrypt
from datetime import timedelta

from os import getenv

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.permanent_session_lifetime = timedelta(hours=3)

app.secret_key = '66e0c4a852d3b55ca598abf7792086b2'

from .all_routes import *
