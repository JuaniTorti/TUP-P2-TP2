from curso import Curso
from estudiante import Estudiante
from profesor import Profesor

def precarga(cursos,profesores,estudiantes):

    #precarga estudiantes
    estudiante = Estudiante("Juan", "Torti", "nachi.tortjuani@gmail.com", "sapito123", 53286, 2010)
    estudiantes.append(estudiante)
    estudiante = Estudiante("Maria", "Gomez", "Mari_gomez@hotmail.com", "//vllc", 45963, 1997)
    estudiantes.append(estudiante)

    #precarga profesores
    profesor = Profesor("Carlos", "Rossi", "car.ross@gmail.com", "lunes13","Licenciado en matematica", 1961)
    profesores.append(profesor)
    profesor = Profesor("Vanina", "Nich", "vaninanich@gmail.com", "oplus00","Analista en sistemas", 1986)
    profesores.append(profesor)

    #precarga cursos
    curso = Curso("Matematica I")
    cursos.append(curso)
    curso = Curso("Ingles I")
    cursos.append(curso)
    curso = Curso("Programacion I")
    cursos.append(curso)
    curso = Curso("Metodologia de la investigaion")
    cursos.append(curso)