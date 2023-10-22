import os
from usuario import *

def ingreso_estudiante(estudiantes,cursos):
    email= input("Ingrese su email ")
    contra = input("Ingrese su contraseña ")
    
    k=0
    for i in estudiantes:
        if email == i.email:
           i.validar_credenciales(email,contra) 
           if i.validar_credenciales(email,contra):
               menu(i,cursos)
           else:
               print("Ingresó los datos incorrectamente")
        else:
            k = k+1
        if k >= len(estudiantes):
            print("No existe ningún alumno con ese correo, si quiere darse de alta, debe hacerlo en alumnado.")
               
            
            
def menu(estudiante,cursos):
    os.system('cls')
    op = 0
    while op != 3:
        print("---MENU ESTUDIANTE---")
        print("1- Matricularse a un curso ") #listo
        print("2- Ver cursos ") #listo
        print("3- Volver al menú principal ")
        op = int(input("\nIngrese una opcion: "))

        cantidad_cursos = 1 # cuanta todas los cursos que hay en total
        if op == 1:
            for i in cursos:
                print(f"[{cantidad_cursos}] {i.nombre}\n")
                cantidad_cursos = cantidad_cursos+1
                
            curso_a_inscribir = int(input("Ingrese el número del curso en el cual se quiere inscribir "))
            
            while curso_a_inscribir <= cantidad_cursos and curso_a_inscribir > 0:
                
                if curso_a_inscribir <= cantidad_cursos and curso_a_inscribir > 0:
                    
                    estudiante.matricular_en_curso(cursos[curso_a_inscribir-1]) #cursos es la lista cursos que esta en app.py 
                    print("Inscripción exitosa!!")                              #y le paso el indice que seleccionó el usuario menos 1
                    input("Presione cualquier tecla para continuar ")
                    
                    os.system('cls')
                    break
                
                elif curso_a_inscribir > cantidad_cursos or curso_a_inscribir <= 0:
                    os.system('cls')                            
                    print("Ingresó un curso erroneo ")
                    
                
        
        elif op == 2:
            for curso in estudiante.mis_cursos:
                print(curso.nombre) 
                
                """
                lo que hace esto es: la curso va tomando cada objeto de la lista que se encuentra en el atributo de la clase estudiante pero los objetos 
                que estan dentro de esa lista son de la clase "cursos" por lo cual muestro su nombre (el nombre de cada objeto dentro de la lista) 
                con el getter de la clase "cursos"
                """
    
        elif op == 3:
            break #debe volver al menu principal
        else: 
            os.system("cls")
            print("Ingresó un valor incompatible, intentelo nuevamente\n")
                