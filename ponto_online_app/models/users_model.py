import sqlalchemy as sa

from datetime import datetime

from .model_base import ModelBase


class Users(ModelBase):
    __tablename__: str = 'users'
    
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    creat_date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    name: str = sa.Column(sa.String(45), nullable=False)
    email: str = sa.Column(sa.String(45), unique=True, nullable=False)
    cnpj_id: str = sa.Column(sa.String(45), unique=True, nullable=False)
    
    level: int = sa.Column(sa.Integer, nullable=False)
    password: str = sa.Column(sa.String(250), nullable=False)
    
    def __repr__(self) -> str:
        return f'<Users>'