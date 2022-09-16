import re

from ponto_online_app.database.db_session import create_session

from ponto_online_app.models.users_model import Users
from ponto_online_app.models.employees_model import Employees


def auth_name(name: str):
    regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)

    res = regex_name.search(name)

    if res:
        return None

    mensagem = "Nome inválido."
    return mensagem


def auth_cpf(cpf: str):
    authe_cpf = len(cpf)

    if authe_cpf < 11 or authe_cpf > 16:
        mensagem = "CPF inválido."
        return mensagem

    return None


def auth_cnpj(cnpj: str):
    authe_cnpj = len(cnpj)

    if authe_cnpj < 14 or authe_cnpj > 20:
        mensagem = "CNPJ inválido."
        return mensagem

    return None


def auth_email(email: str):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}([.]\w{2,3})?$'

    if re.search(regex, email):
        return None

    mensagem = "Email inválido."
    return mensagem


def auth_existence_user(email: str, cnpj: str):
    with create_session() as session_db:
        consult_email = session_db.query(Users).filter(Users.email == email).first()

        consult_cnpj = session_db.query(Users).filter(Users.cnpj_id == cnpj).first()

    if consult_email is not None:
        mensagem = 'Este email já estar cadastrado em nosso banco de dados.'
        return mensagem

    if consult_cnpj is not None:
        mensagem = 'Este CNPJ já estar cadastrado em nosso banco de dados.'
        return mensagem

    return None


def auth_existence_employees(email: str, cpf: str):
    with create_session() as session_db:
        consult_email = session_db.query(Employees).filter(Employees.email == email).first()

        consult_cpf = session_db.query(Employees).filter(Employees.cpf_id == cpf).first()

    if consult_email is not None:
        mensagem = 'Este email já estar cadastrado em nosso banco de dados.'
        return mensagem

    if consult_cpf is not None:
        mensagem = 'Este CPF já estar cadastrado em nosso banco de dados.'
        return mensagem

    return None
