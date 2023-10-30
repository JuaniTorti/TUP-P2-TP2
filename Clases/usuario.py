from abc import ABC, abstractmethod


class Usuario(ABC):

    def __init__(self, nombre: str, apellido: str, email: str, contra: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contra = contra

    def __str__(self) -> str:
        return f"""\nNombre: {self.__nombre} \nApellido: {self.__apellido} \nEmail: {self.__email} \nContraseña: {self.__contra}"""

    def validar_credenciales(self, email: str, contra: str):
        if email == self.__email and contra == self.__contra:
            return True
        else:
            return False

    @property
    def email(self):
        return self.__email