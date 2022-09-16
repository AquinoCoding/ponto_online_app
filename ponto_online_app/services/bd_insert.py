from ponto_online_app import bcrypt

from ponto_online_app.database.db_session import create_session

from ponto_online_app.models.point_model import Point
from ponto_online_app.models.users_model import Users
from ponto_online_app.models.employees_model import Employees


def insert_session_users(name: str, email: str, cnpj_id: str, level: int, password: str):
    
    password = bcrypt.generate_password_hash(password)

    an: Users = Users(name=name, email=email, cnpj_id=cnpj_id, level=level,
                      password=password)

    with create_session() as session:
        session.add(an)
        session.commit()


def insert_session_employees(name, email, cpf_id, level, password, employees):
    password = bcrypt.generate_password_hash(password)

    an: Employees = Employees(name=name, email=email, cpf_id=cpf_id, level=level,
                              password=password, id_user=employees)

    with create_session() as session:
        session.add(an)
        session.commit()


def insert_point(cpf_user: str, date: str):

    points: Point = Point(cpf_user=cpf_user, date=date)

    with create_session() as session:
        session.add(points)
        session.commit()
