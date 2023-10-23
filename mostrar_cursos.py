import os

def mostrar(cursos):
    os.system('cls')
    for curso in sorted(cursos, key=lambda curso: curso.nombre):
        print(f"Materia: {curso.nombre}\nClave: {curso.clave}")
        print("---------------------------------")
    input("Presione cualquier tecla para continuar")       
   
    """
    lo que hace este for es tomar cada curso que esta dentro de la lista y mostrarlos con el 
    getter de la clase "Curso" ya que los objetos que estan dentro de la lista son instancias de la clase "Curso"
    lo mismo con clave
    """
