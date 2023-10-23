import os
from usuario import *

def ingreso_estudiante(estudiantes,cursos):
    email= input("Ingrese su email ")
    contra = input("Ingrese su contraseña ")
    
    k=0
    for i in estudiantes:
        if email == i.email:
           i.validar_credenciales(email,contra) 
           if i.validar_credenciales(email,contra):        #esta función lo que hace es pedirle al usuario que ingrese un email y un password, luego toma ese email ingresado y lo 
               menu(i,cursos)                              #busca en los email guardados de los estudiantes (los objetos estudiantes) si lo encuentra llama al metodo validar_credenciales
           else:                                           #y si devuelve un True llama a la funcion menu pasandole de parametro la i (que es el estudiante que inicia sesion) y la lista de cursos 
               print("Contraseña incorrecta")              #si devuelve False se le indica que la contraseña es incorrecta y si k llega a ser mayor que la longitud de la lista estudiantes
               input("Presione cualquier tecla para continuar")# es porque el email ingresado no fué encontrado
        else:
            k = k+1
        if k >= len(estudiantes):
            print("No existe ningún alumno con ese correo, si quiere darse de alta, debe hacerlo en alumnado.")
            input("Presione cualquier tecla para continuar")
               
            
            
def menu(estudiante,cursos):
    
    op = 0
    while op != 3:
        os.system('cls')
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
            x = len(estudiante.mis_cursos)
            if x == 0:
                print("El alumno no está inscripto a ningún curso")
                input("Presione cualquier tecla para continuar")
            else:
                for curso in estudiante.mis_cursos:
                    print(curso.nombre)
                input("Presione cualquier tecla para continuar")
                
                """
                lo que hace esto es: la variable curso va tomando cada objeto de la lista que se encuentra en el atributo de la clase estudiante pero los objetos 
                que estan dentro de esa lista son de la clase "cursos" por lo cual muestro su nombre (el nombre de cada objeto dentro de la lista) 
                con el getter de la clase "cursos"
                """
    
        elif op == 3:
            break 
        else: 
            os.system("cls")
            print("Ingresó un valor incompatible, intentelo nuevamente\n")
                