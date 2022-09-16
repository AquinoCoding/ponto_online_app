from datetime import timedelta

from ponto_online_app.services.bd_read import read_point


def calculator(cpf: str, date: str):

    find_acess_time = read_point(cpf, date)

    horaSum = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)
    horas = []

    quantidade = len(find_acess_time)

    if quantidade == 1:
        mensagem = 'Não há pontos suficientes para ser contabilizado o tempo trabalhado.'
        return mensagem

    if (quantidade % 2) == 1:
        quantidade -= 1

    for i in range(1, quantidade, 2):

        ind = i - 1
        calculo1 = find_acess_time[ind]
        calculo2 = find_acess_time[i]

        resultado = calculo2 - calculo1
        horas.append(resultado)

        horasLen = len(horas)

        if i == quantidade - 1:
            for indice in range(horasLen):
                horaSum += horas[indice]

    mensagem = f'Você tem {horaSum} horas trabalhadas'

    return mensagem

# insert_point("0", "2022-09-09", "14:30:00")
