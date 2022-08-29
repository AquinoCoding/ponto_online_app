from datetime import datetime


def date_time():
    time = datetime.now()
    formatacao = time.strftime('Dia:%d/%m/%Y Horas:%H:%M')

    return formatacao
