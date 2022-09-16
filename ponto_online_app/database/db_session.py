import sqlalchemy as sa

from sqlalchemy.orm import sessionmaker

from pathlib import Path
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

from ponto_online_app.models.model_base import ModelBase

__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    global __engine
    
    if __engine:
        return
    
    conn_str = 'postgresql://hzwtrwnbqzymjl:e9a295bd21d9fb38470a6effbd9171e3dd41b63c9aa75b72f45fd6d7af94555b@ec2-34-199-68-114.compute-1.amazonaws.com:5432/d9s9bd88052min'
    __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    global __engine
    
    if not __engine:
        create_engine(sqlite=True) 
        
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session_db: Session = __session()
    
    return session_db


def create_tables() -> None:
    global __engine 
    
    if not __engine:
        create_engine(sqlite=True)
        
    import ponto_online_app.models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
