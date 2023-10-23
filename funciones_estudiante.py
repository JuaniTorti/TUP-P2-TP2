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
        print("1- Matricularse a un curso ") 
        print("2- Ver cursos ") 
        print("3- Volver al menú principal ")
        op = int(input("\nIngrese una opcion: "))

        x = 1               
        if op == 1:         
            x = 1
            for curso in cursos:
                print(f"[{x}] - {curso.nombre}\n") #mostrar opciones
                x += 1
                    
            curso_a_inscribir = input("Ingrese el número del curso en el cual se quiere inscribir: ") #ingreso de opcion

            bandera = False
            while not(bandera): #queda en true y entra al bucle
                
                if curso_a_inscribir.isdigit() and int(curso_a_inscribir) <= x and int(curso_a_inscribir) > 0:
                    bandera = True
                else: 
                    print("\nIngresó una opcion invalida, intentelo nuevamente ")
                    curso_a_inscribir = input("Ingrese el número del curso en el cual se quiere inscribir: ") #se pide el ingreso dev hasta que lo ingrese bien

            ya_anotado = False
            for curso in estudiante.mis_cursos:
                if curso == cursos[int(curso_a_inscribir)-1]: #validacion de si ya esta inscripto
                    ya_anotado = True
                    print("Ya esta inscripto en este curso")
                
            if not(ya_anotado):
                clave = input("ingrese la clave de matriculacion: ")

                if clave == cursos[int(curso_a_inscribir)-1].clave:
                    os.system("cls")
                    estudiante.matricular_en_curso(cursos[int(curso_a_inscribir)-1])  #si no esta inscripto se pide la clave y se inscribe
                    print("Inscripción exitosa!!")                              
                    input("Presione cualquier tecla para continuar ")
                else:
                    os.system("cls")
                    print("la clave es invalida")
                    input("Presione cualquier tecla para continuar ")
    
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
                