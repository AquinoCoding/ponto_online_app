import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime

from .model_base import ModelBase
from ponto_online_app.models.users_model import Users


class Employees(ModelBase):
    __tablename__: str = 'employees'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    creat_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    name: str = sa.Column(sa.String(45), nullable=False)
    email: str = sa.Column(sa.String(45), unique=True, nullable=False)
    cpf_id: str = sa.Column(sa.String(45), unique=True, nullable=False)

    level: int = sa.Column(sa.Integer, nullable=False)
    password: str = sa.Column(sa.LargeBinary, nullable=False)

    id_user: int = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    user: Users = orm.relationship('Users', lazy='joined')

    def __repr__(self) -> str:
        return f'<Employees>'
