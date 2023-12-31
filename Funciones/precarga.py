from Clases.estudiante import Estudiante
from Clases.profesor import Profesor
from Clases.carrera import Carrera

def precarga(profesores,estudiantes,carreras):

    #precarga carrera
    carrera = Carrera("Ingenieria en sistemas", 5)
    carreras.append(carrera)

    #precarga estudiantes
    estudiante = Estudiante("Juan", "Torti", "nachi.tortjuani@gmail.com", "sapito123", 53286, 2010, carrera) 
    estudiantes.append(estudiante)
    estudiante = Estudiante("Maria", "Gomez", "Mari_gomez@hotmail.com", "//vllc", 45963, 1997, carrera)
    estudiantes.append(estudiante)

    #precarga profesores
    profesor = Profesor("Carlos", "Rossi", "car.ross@gmail.com", "4574","Licenciado en matematica", 1961)
    profesores.append(profesor)
    profesor = Profesor("Vanina", "Nich", "vaninanich@gmail.com", "oplus00","Analista en sistemas", 1986)
    profesores.append(profesor)