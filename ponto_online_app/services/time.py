from datetime import datetime


def date_time():
    time = datetime.now()
    formatacao = time.strftime('Dia:%d/%m/%Y Horas:%H:%M')

    return formatacao


def ponto_formatado(time) -> str:
    formatacao: str = time.strftime('Dia:%d/%m/%Y Horas:%H:%M')

    return formatacao
