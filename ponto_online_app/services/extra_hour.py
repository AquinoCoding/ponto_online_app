from ponto_online_app.services.time_calculator import calculator_all
from ponto_online_app.services.bd_read import read_employees_session
from ponto_online_app.services.bd_update import update_extra_hour

from datetime import timedelta, datetime, time


def extra_hour() -> None:
    employees = read_employees_session()

    for employee in employees:

        name = employee['name']
        hours = employee['horas_por_semana']

        employees_hour = calculator_all(name)
        dia_semana = datetime.today().weekday()

        dia = int(hours[dia_semana])
        trasf_hour = timedelta(hours=dia)

        extra_hour = str(employees_hour - trasf_hour)

        update_extra_hour(name, extra_hour)