import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime

from .model_base import ModelBase
from ponto_online_app.models.employees_model import Employees


class Point(ModelBase):
    __tablename__: str = 'points'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    creat_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    id_employees: int = sa.Column(sa.Integer, sa.ForeignKey('employees.id'))
    user: Employees = orm.relationship('Employees', lazy='joined')

    def __repr__(self) -> str:
        return f'<Point>'
