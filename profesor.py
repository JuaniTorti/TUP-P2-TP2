from usuario import Usuario
from curso import Curso


class Profesor(Usuario):

    def __init__(self, nombre: str, apellido: str, email: str, contra: str, titulo: str, anio_egreso: int) -> None:
        super().__init__(nombre, apellido, email, contra)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []  # aca se almacenaran los cursos que da

    def __str__(self) -> str:
        return f"""{super().__str__()} \nTitulo: {self.__titulo} \nAño de egreso: {self.__anio_egreso} \nCurso que dicta: {self.__mis_cursos}"""

    def dictar_curso(self, curso: Curso):
        self.__mis_cursos.append(curso)

    def mostrar_cursos(self):
        for curso in self.__mis_cursos:
            print(curso)
            print("------------------")