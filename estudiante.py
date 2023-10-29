from usuario import Usuario
from curso import Curso
from carrera import Carrera

class Estudiante(Usuario):

    def __init__(self, nombre: str, apellido: str, email: str, contra: str, legajo: int, anio_inscripcion: int, carrera: Carrera) -> None:
        super().__init__(nombre, apellido, email, contra)
        self.__legajo = legajo
        self.__anio_inscripcion = anio_inscripcion
        self.__mis_cursos = []  # aca se almacenaran los cursos que cursa
        self.__carrera = carrera

    def __str__(self) -> str:
        return f"""{super().__str__()} \nLegajo: {self.__legajo} \nAño de inscripcion: {self.__anio_inscripcion} \nCursando: {self.__mis_cursos}"""

    def matricular_en_curso(self, curso: Curso):
        self.__mis_cursos.append(curso)

    def desmatricular_curso(self, curso: Curso):
        self.__mis_cursos.remove(curso)
        
    @property
    def mis_cursos(self):
        return self.__mis_cursos
    
    @property
    def carrera(self):
        return self.__carrera