from datetime import timedelta

from ponto_online_app.services.bd_read import read_all_point_email, read_all_date_point_email, read_point, read_point_month


def calculator_day(email: str, date: str):

    find_acess_time = read_point(email, date)

    horaSum = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)
    horas = []

    quantidade = len(find_acess_time)

    if quantidade <= 1:
        mensagem = 'Não há pontos suficientes para ser contabilizado o tempo de serviços.'
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


def calculator_all(email: str):


    find_acess_time = read_all_date_point_email(email)

    total_horas = []

    for date in find_acess_time:
        consulta_de_pontos = read_point(email, date)

        horaSum = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)
        horas_dia = []

        quantidade = len(consulta_de_pontos)

        if quantidade <= 1:
            quantidade = 0

        if (quantidade % 2) == 1:
            quantidade -= 1

        for i in range(1, quantidade, 2):

            calculo1 = consulta_de_pontos[i-1]
            calculo2 = consulta_de_pontos[i]
            
            horas_dia.append(calculo2 - calculo1)
            
            if i == (quantidade - 1):
                for indice in range(len(horas_dia)):
                    horaSum += horas_dia[indice]

        total_horas.append(horaSum)

    soma_horas_dias = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)

    for indice in range(len(total_horas)):
        soma_horas_dias += total_horas[indice]
                
    resultado = soma_horas_dias

    return resultado


def calculator_month(email: str, days):


    find_acess_time = read_point_month(email, days)

    total_horas = []

    for date in find_acess_time:
        consulta_de_pontos = read_point(email, date)

        horaSum = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)
        horas_dia = []

        quantidade = len(consulta_de_pontos)

        if quantidade <= 1:
            quantidade = 0

        if (quantidade % 2) == 1:
            quantidade -= 1

        for i in range(1, quantidade, 2):

            calculo1 = consulta_de_pontos[i-1]
            calculo2 = consulta_de_pontos[i]
            
            horas_dia.append(calculo2 - calculo1)
            
            if i == (quantidade - 1):
                for indice in range(len(horas_dia)):
                    horaSum += horas_dia[indice]

        total_horas.append(horaSum)

    soma_horas_dias = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)

    for indice in range(len(total_horas)):
        soma_horas_dias += total_horas[indice]
                
    resultado = soma_horas_dias

    return resultado
