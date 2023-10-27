from cod_generator import generar
from archivo import Archivo
from carrera import Carrera

class Curso:
    prox_cod = 0

    def __init__(self, nombre_curso: str, carrera: Carrera) -> None:
        self.__nombre = nombre_curso
        self.__clave = self.__generar_contraseña()
        self.__codigo = self.codigo()
        self.__archivos = []
        self.__carrera = carrera

    def __str__(self) -> str:
        return f"""Nombre: {self.__nombre} \nClave de matriculacion: {self.__clave}"""
    
    def nuevo_archivo(self, archivo: Archivo):
        self.__archivos.append(archivo)

    @classmethod
    def __generar_contraseña(cls):
        return generar()
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def clave(self):
        return self.__clave
    
    @classmethod
    def codigo(cls):
        cls.prox_cod += 1
        return cls.prox_cod