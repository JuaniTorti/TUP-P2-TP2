from usuario import Usuario
from curso import Curso

class Estudiante(Usuario):

    def __init__(self, nombre: str, apellido: str, email: str, contra: str, legajo: int, anio_inscripcion: int) -> None:
        super().__init__(nombre, apellido, email, contra)
        self.__legajo = legajo
        self.__anio_inscripcion = anio_inscripcion
        self.__mis_cursos = []  # aca se almacenaran los cursos que cursa

    def __str__(self) -> str:
        return f"""{super().__str__()} \nLegajo: {self.__legajo} \nAño de inscripcion: {self.__anio_inscripcion} \nCursando: {self.__mis_cursos}"""

    def matricular_en_curso(self, curso: Curso):
        pass