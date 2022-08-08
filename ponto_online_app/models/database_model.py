from ponto_online_app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, username, name, password, email):
        self.username = username
        self.name = name
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username


db.create_all()
