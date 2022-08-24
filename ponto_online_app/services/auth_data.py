from validate_docbr import CPF, CNPJ
import re


class AuthData:

    @staticmethod
    def auth_name(name):
        regex = '[a-z]'
        resultado = True

        if re.search(regex, str(name)):
            return resultado, None

        resultado = False
        mensagem_nome = "Nome inválido."
        return resultado, mensagem_nome

    @staticmethod
    def auth_cpf(cpf):
        registro = CPF()
        authe_cpf = registro.validate(str(cpf))

        if authe_cpf is True:
            return authe_cpf, None

        mensagem_cpf = "CPF inválido."
        return authe_cpf, mensagem_cpf

    @staticmethod
    def auth_cnpj(cnpj):
        registro = CNPJ()
        authe_cnpj = registro.validate(cnpj)

        if authe_cnpj is True:
            return authe_cnpj, None

        mensagem_cnpj = "CNPJ inválido."
        return authe_cnpj, mensagem_cnpj

    @staticmethod
    def auth_email(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}([.]\w{2,3})?$'
        resultado = True

        if re.search(regex, str(email)):
            return resultado, None

        resultado = False
        mensagem_email = "Email inválido."
        return resultado, mensagem_email

    @staticmethod
    def auth_password(password):
        resultado = True
        if len(password) >= 6:
            return resultado, None

        resultado = False
        mensagem_password = "A senha precisa ter no mínimo 6 caracteres."
        return resultado, mensagem_password
