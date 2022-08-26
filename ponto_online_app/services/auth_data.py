from validate_docbr import CPF, CNPJ
import re

# A class AuthDataUsers se encontra na linha 44


class AuthDataEmployees:
    def __init__(self, name, cpf, email, password, password2):
        self.__name = name
        self.__cpf = cpf
        self.__email = email
        self.__password = password
        self.__password2 = password2

    @property
    def auth_employees(self):
        resposta = auth_name(self.__name)[0] is False
        resposta1 = auth_cpf(self.__cpf)[0] is False
        resposta2 = auth_email(self.__email)[0] is False
        resposta3 = auth_password(self.__password, self.__password2)[0] is False
        mensagem = True

        if resposta or resposta1 or resposta2 or resposta3:
            mensagem = (auth_name(self.__name)[1] or auth_cpf(self.__cpf)[1] or
                        auth_email(self.__email)[1] or auth_password(self.__password, self.__password2)[1])

        return mensagem


class AuthDataUsers:
    def __init__(self, name, cnpj, email, password, password2):
        self.__name = name
        self.__cnpj = cnpj
        self.__email = email
        self.__password = password
        self.__password2 = password2

    @property
    def auth_users(self):
        resposta = auth_name(self.__name)[0] is False
        resposta1 = auth_cnpj(self.__cnpj)[0] is False
        resposta2 = auth_email(self.__email)[0] is False
        resposta3 = auth_password(self.__password, self.__password2)[0] is False
        mensagem = True

        if resposta or resposta1 or resposta2 or resposta3:
            mensagem = (auth_name(self.__name)[1] or auth_cnpj(self.__cnpj)[1] or
                        auth_email(self.__email)[1] or auth_password(self.__password, self.__password2)[1])

        return mensagem


def auth_name(name):
    regex_name = re.compile(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$', re.IGNORECASE)

    res = regex_name.search(name)

    if res:
        return True, None

    mensagem_nome = "Nome inválido."
    return False, mensagem_nome


def auth_cpf(cpf):
    registro = CPF()
    authe_cpf = registro.validate(str(cpf))

    if authe_cpf is True:
        return authe_cpf, None

    mensagem_cpf = "CPF inválido."
    return authe_cpf, mensagem_cpf


def auth_cnpj(cnpj):
    registro = CNPJ()
    authe_cnpj = registro.validate(str(cnpj))

    if authe_cnpj is True:
        return authe_cnpj, None

    mensagem_cnpj = "CNPJ inválido."
    return authe_cnpj, mensagem_cnpj


def auth_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}([.]\w{2,3})?$'
    resultado = True

    if re.search(regex, str(email)):
        return resultado, None

    resultado = False
    mensagem_email = "Email inválido."
    return resultado, mensagem_email


def auth_password(password, password2):
    resultado = False

    if password != password2:
        mensagem_password = 'Preencha o campo de senhas corretamente.'
        return resultado, mensagem_password

    if len(password) >= 6:
        resultado = True
        return resultado, None

    mensagem_password = "A senha precisa ter no mínimo 6 caracteres."
    return resultado, mensagem_password





