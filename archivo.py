from datetime import datetime

class Archivo: 
    def __init__(self, nombre: str, formato: str) -> None:
        self.__nombre = nombre
        self.__fecha = datetime.now().date()
        self.__formato = formato

    def __str__(self) -> str:
        return f"{self.__nombre}.{self.__formato}" 
    
    @property
    def fecha(self):
        return self.__fecha