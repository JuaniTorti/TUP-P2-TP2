from cod_generator import generar

class Curso:

    def __init__(self, nombre_curso: str) -> None:
        self.__nombre = nombre_curso
        self.__clave = self.__generar_contraseña()

    def __str__(self) -> str:
        return f"""Nombre: {self.__nombre} \nClave de matriculacion: {self.__clave}"""

    @classmethod
    def __generar_contraseña(cls):
        return generar()