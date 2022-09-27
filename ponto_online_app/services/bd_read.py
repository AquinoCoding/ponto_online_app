from ponto_online_app.database.db_session import create_session

# Models
from ponto_online_app.models.point_model import Point
from ponto_online_app.models.users_model import Users
from ponto_online_app.models.employees_model import Employees


def read_users_session():

    with create_session() as session_db:
        users = session_db.query(Users)
        return [{"id": an.id, "data_criacao": an.creat_date,
                 "name": an.name, "email": an.email,
                 "cnpj_id": an.cnpj_id, "level": an.level}
                for an in users]


def read_user_single_session(email: str):

    with create_session() as session_db:
        user = session_db.query(Users).filter(Users.email == email).first()

    if user is None:
        return user
        
    return {"id": user.id, "user": user, "password": user.password}


def read_employees_session():

    with create_session() as session_db:
        employees = session_db.query(Employees)
        return [{"id": an.id, "data_criacao": an.creat_date, "name": an.name, 
                 "email": an.email, "cpf_id": an.cpf_id, "horas_por_semana": an.hours_per_week,
                 "extra_hour": an.extra_hour,"level": an.level}
                for an in employees]


def read_employees_single_session(email: str):

    with create_session() as session_db:
        employees = session_db.query(Employees).filter(Employees.email == email).first()

    if employees is None:
        return employees

    return {"id": employees.id, "data_criacao": employees.creat_date, "employees": employees.name,
            "email": employees.email, "cpf_id": employees.cpf_id, "horas_por_semana": employees.hours_per_week,
            "extra_hour": employees.extra_hour, "level": employees.level, "password": employees.password}


def read_point(email: str, date: str):

    with create_session() as session_db:
        find_acess = session_db.query(Point).filter(Point.email_user == email).filter(Point.date == date).all()

    find_acess_time = [consulta.time for consulta in find_acess]

    return find_acess_time


def read_all_point_email(email: str):

    with create_session() as session_db:
        pontos_batidos = session_db.query(Point).filter(Point.email_user == email)

    find_acess_time = [an.time for an in pontos_batidos]

    return find_acess_time


def read_all_date_point_email(email: str):

    with create_session() as session_db:
        funcionario = session_db.query(Point).filter(Point.email_user == email)

        datas_dos_pontos = list(set([an.date for an in funcionario]))

    return datas_dos_pontos


def read_point_month(email: str, month: str):
    
    with create_session() as session_db:
        pontos_do_mes = session_db.query(Point).filter(Point.email_user == email).filter(Point.date.ilike(month +'%'))

        date = list(set([an.date for an in pontos_do_mes]))

    return date
