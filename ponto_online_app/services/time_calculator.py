from datetime import timedelta

from ponto_online_app.services.bd_read import read_all_point_email


def calculator(email: str):

    find_acess_time = read_all_point_email(email)

    horaSum = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)
    horas = []

    quantidade = len(find_acess_time)

    if quantidade <= 1:
        mensagem = 'Não há pontos suficientes para ser contabilizado o tempo trabalhado.'
        return mensagem

    if (quantidade % 2) == 1:
        quantidade -= 1

    for i in range(1, quantidade, 2):

        calculo1 = find_acess_time[i-1]
        calculo2 = find_acess_time[i]
        
        horas.append(calculo2 - calculo1)
        
        if i == (quantidade - 1):
            for indice in range(len(horas)):
                horaSum += horas[indice]
                
    resultado = str(horaSum)

    return resultado

# insert_point("0", "2022-09-09", "14:30:00")
