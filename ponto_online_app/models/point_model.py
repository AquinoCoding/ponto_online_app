import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime, date

from .model_base import ModelBase


class Point(ModelBase):
    __tablename__: str = 'points'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    creat_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    cpf_user: str = sa.Column(sa.String(45), nullable=False)
    date: datetime = sa.Column(sa.String(20), nullable=False)
    time: datetime = sa.Column(sa.String(20), nullable=False)

    def __repr__(self) -> str:
        return f'<Point>'
