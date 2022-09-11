import re


def auth_name(name):
    regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)

    res = regex_name.search(name)

    if res:
        return True, None

    mensagem = "Nome inválido."
    return False, mensagem


def auth_cpf(cpf):
    authe_cpf = len(cpf)

    if authe_cpf < 11 or authe_cpf > 16:
        mensagem = "CPF inválido."
        return False, mensagem

    return True, None


def auth_cnpj(cnpj):
    authe_cnpj = len(cnpj)

    if authe_cnpj < 14 or authe_cnpj > 20:
        mensagem = "CNPJ inválido."
        return False, mensagem

    return True, None


def auth_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}([.]\w{2,3})?$'
    resultado = True

    if re.search(regex, str(email)):
        return resultado, None

    resultado = False
    mensagem = "Email inválido."
    return resultado, mensagem
