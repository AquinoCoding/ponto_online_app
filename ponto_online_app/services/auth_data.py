from validate_docbr import CPF, CNPJ
import re


class AuthData:

    @staticmethod
    def auth_cpf(cpf):
        registro = CPF()
        authe_cpf = registro.validate(str(cpf))

        if authe_cpf is True:
            return authe_cpf
        return authe_cpf

    @staticmethod
    def auth_cnpj(cnpj):
        registro = CNPJ()
        authe_cnpj = registro.validate(cnpj)

        if authe_cnpj is True:
            return authe_cnpj

        return authe_cnpj

    @staticmethod
    def auth_email(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}([.]\w{2,3})?$'
        resultado = True

        if re.search(regex, str(email)):
            return resultado

        resultado = False
        return resultado
