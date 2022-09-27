from ponto_online_app.database.db_session import create_session

from ponto_online_app.models.employees_model import Employees


def update_extra_hour(employee: str, extra_hour):
    with create_session as session:
        funcionario: Employees = session.query(Employees).filter(Employees.name == employee).one_or_none()

        if funcionario:
            funcionario.extra_hour = extra_hour

            session.commit()