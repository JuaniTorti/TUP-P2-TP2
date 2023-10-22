from app import cursos

#alumnos_ordenados = sorted(alumnos, key=lambda alumno: alumno.nombre)
def mostrar():
    for curso in sorted(cursos, key=lambda curso: curso.nombre):
        
        print(f"Materia: {curso.nombre}")
        
    """
    lo que hace este for es tomar cada curso que esta dentro de la lista y mostrarlos con el 
    getter de la clase "Curso" ya que los objetos que estan dentro de la lista son instancias de la clase "Curso"
    lo mismo con carrera
    """
