from cod_generator import generar

class Usuario:
    
    def __init__(self, nombre: str, apellido: str, email: str, contra: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__contra = contra

    def __str__(self) -> str:
        print("Nombre: ", self.__nombre)
        print("Apellido: ", self.__apellido)
        print("Email: ", self.__email)
        print("Contraseña: ", self.__contra)

    def validar_credenciales(self, email: str, contra: str):
        pass



class Curso:

    def __init__(self, nombre_curso: str) -> None:
        self.__nombre = nombre_curso
        self.__clave = ""

    def __str__(self) -> str:
        print("Nombre: ", self.__nombre)
        print("Clave de matriculacion: ", self.__clave)

    def __generar_contraseña(self):
        self.__clave = generar()





class Estudiante(Usuario):
    
    def __init__(self, nombre: str, apellido: str, email: str, contra: str, legajo: int, anio_inscripcion: int) -> None:
        super().__init__(nombre, apellido, email, contra)
        self.__legajo = legajo
        self.__anio_inscripcion = anio_inscripcion
        self.__mis_cursos = [] # aca se almacenaran los cursos que cursa

    def __str__(self) -> str:
        print(super().__str__()) 
        print("Legajo: ", self.__legajo)
        print("Año de inscripcion: ", self.__anio_inscripcion)
        print("Cursando: ", self.__mis_cursos)

    def matricular_en_curso(self, curso: Curso):
        pass





class Profesor(Usuario):

    def __init__(self, nombre: str, apellido: str, email: str, contra: str, titulo: str, anio_egreso: int) -> None:
        super().__init__(nombre, apellido, email, contra)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = [] # aca se almacenaran los cursos que da

    def __str__(self) -> str:
        print(super().__str__())
        print("Titulo: ", self.__titulo)
        print("Año de egreso: ", self.__anio_egreso)
        print("Cursos que dicta: ", self.__mis_cursos)

    def dictar_curso(self, curso: Curso):
        pass




