class Carrera: 
    def __init__(self, nombre: str, cant_anios: int) -> None:
        self.__nombre: nombre
        self.__cant_anios: cant_anios
        self.__cursos: []
        self.__estudiantes: []

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} \nCantidad de años: {self.__cant_anios}"
    
    def get_cantidad_materias(self):
        return len(self.__cursos)