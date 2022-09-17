from ponto_online_app.database.db_session import create_session

# Models
from ponto_online_app.models.point_model import Point
from ponto_online_app.models.users_model import Users
from ponto_online_app.models.employees_model import Employees


def read_user_session(email: str):

    with create_session() as session_db:
        users = session_db.query(Users).filter(Users.email == email)
        return [users]


def read_user_single_session(email: str):

    with create_session() as session_db:
        user = session_db.query(Users).filter(Users.email == email).first()
        password_user = user.password
        
        return user, password_user


def read_employees_session(email: str):

    with create_session() as session_db:
        employees = session_db.query(Employees).filter(Employees.email == email)
        return [employees]


def read_employees_single_session(email: str):

    with create_session() as session_db:
        employees = session_db.query(Employees).filter(Employees.email == email).first()

        password_employees = employees.password

        return employees, password_employees

# find_acess_employees = session_db.query(Employees).filter(Employees.cpf_id == usuario).first()


def read_point(cpf: str, date: str):

    with create_session() as session_db:
        find_acess = session_db.query(Point).filter(Point.cpf_user == cpf).filter(Point.date == date).all()

    find_acess_time = [consulta.time for consulta in find_acess]

    return find_acess_time
