import os
from usuario import *


def ingreso_estudiante(estudiantes,cursos):
    os.system("cls")
    email= input("Ingrese su email: ")
    contra = input("Ingrese su contraseña: ")
    
    k=0
    for i in estudiantes:
        if email == i.email:
           i.validar_credenciales(email,contra) 
           if i.validar_credenciales(email,contra):        #esta función lo que hace es pedirle al usuario que ingrese un email y un password, luego toma ese email ingresado y lo 
               menu(i,cursos)                              #busca en los email guardados de los estudiantes (los objetos estudiantes) si lo encuentra llama al metodo validar_credenciales
           else:  
               os.system("cls")                            #y si devuelve un True llama a la funcion menu pasandole de parametro la i (que es el estudiante que inicia sesion) y la lista de cursos 
               print("Contraseña o email incorrectos")              #si devuelve False se le indica que la contraseña es incorrecta y si k llega a ser mayor que la longitud de la lista estudiantes
               input("\nPresione cualquier tecla para continuar")# es porque el email ingresado no fué encontrado
        else:
            k = k+1
        if k >= len(estudiantes):
            os.system("cls")
            print("No existe ningún alumno con ese correo, si quiere darse de alta, debe hacerlo en alumnado.")
            input("\nPresione cualquier tecla para continuar")
               
            
            
def menu(estudiante,cursos):
    
    op = 0
    while op != 3:
        os.system('cls')
        print("---MENU ESTUDIANTE---")
        print("1 - Matricularse a un curso ") 
        print("2 - Ver cursos ") 
        print("3 - Desmatricularse de un curso ") 
        print("4 - Volver al menú principal ")
        op = int(input("\nIngrese una opcion: "))
        
        if op == 1:
            matricularse(estudiante,cursos)
        elif op == 2:
            ver_cursos(estudiante)
        elif op == 3:
            desmatricular(estudiante,cursos)
        elif op == 4:
            break
        else:
            os.system("cls")
            print("Ingreso un valor incompatible, intentelo nuevamente")
            x = input("\nPresione ENTER para continuar")

def matricularse(estudiante,cursos): #op1
        
    x = 1
    for curso in sorted(estudiante.carrera.cursos, key=lambda curso:curso.get_codigo):  #le muestro solo los cursos que pertenecen a la carrera a la cual pertenece el estudiante
            print(f"[{x}] - {curso.nombre}\n") 
            x += 1
            
    curso_a_inscribir = input("Ingrese el número del curso en el cual se quiere inscribir: ") #ingreso de opcion

    #valido que ingrese una opcion valida
    bandera = False
    while not(bandera): #queda en true y entra al bucle
        
        if curso_a_inscribir.isdigit() and int(curso_a_inscribir) <= x and int(curso_a_inscribir) > 0: #isdigit devuelve si es un numero
            bandera = True
        else: 
            print("\nIngresó una opcion invalida, intentelo nuevamente ")
            curso_a_inscribir = input("Ingrese el número del curso en el cual se quiere inscribir: ") #se pide el ingreso dev hasta que lo ingrese bien

    #validacion de si ya esta inscripto
    ya_anotado = False
    for curso in estudiante.mis_cursos:
        if curso == cursos[int(curso_a_inscribir)-1]: 
            ya_anotado = True
            print("Ya esta inscripto en este curso")
            input("\nPresione cualquier tecla para continuar ")
    
    #le pido la clave si es correcta se matricula sino no
    if not(ya_anotado):
        clave = input("Ingrese la clave de matriculacion: ")

        if clave == cursos[int(curso_a_inscribir)-1].clave:
            os.system("cls")
            estudiante.matricular_en_curso(estudiante.carrera.cursos[int(curso_a_inscribir)-1])#si no esta inscripto se pide la clave y se inscribe
            print("\nInscripción exitosa!!")                              
            input("\nPresione cualquier tecla para continuar ")
        else:
            os.system("cls")
            print("La clave es invalida")
            input("\nPresione cualquier tecla para continuar ")

def ver_cursos(estudiante): #op2
    x = len(estudiante.mis_cursos)
    if x == 0:
        print("El alumno no está inscripto a ningún curso")
        input("\nPresione cualquier tecla para continuar")
    else:
        os.system("cls")
        print("Se encuentra matriculado en:\n")
        for curso in estudiante.mis_cursos:
            print(curso.nombre)
        input("\nPresione cualquier tecla para continuar")
        
        """
        lo que hace esto es: la variable curso va tomando cada objeto de la lista que se encuentra en el atributo de la clase estudiante pero los objetos 
        que estan dentro de esa lista son de la clase "cursos" por lo cual muestro su nombre (el nombre de cada objeto dentro de la lista) 
        con el getter de la clase "cursos"
        """
                
def desmatricular(estudiante,curso): #op3 no testeada 
    os.system("cls")       
    x = 1
    for curso in estudiante.mis_cursos:  #le muestro solo los cursos que pertenecen a la carrera a la cual pertenece el estudiante
        print(f"[{x}] - {curso.nombre}\n")  #por ahora no me muestra ningun curso porque no hay cursos cargados
        x += 1
    
    curso_desmatricular = input("Ingrese el numero del curso del cual se quiere desmatricular")
    print(int(curso_desmatricular))
    
    
    #valido que ingrese una opcion valida
    bandera = False
    while not(bandera): #queda en true y entra al bucle
        
        #isdigit devuelve si es un numero
        if curso_desmatricular.isdigit() and int(curso_desmatricular) <= len(estudiante.carrera.cursos) and int(curso_desmatricular) > 0: 
            estudiante.desmatricular_curso(estudiante.mis_cursos[int(curso_desmatricular) -1]) 
            bandera = True
            input("Se desmatriculó con éxito!!!")
        else: 
            print("\nIngresó una opcion invalida, intentelo nuevamente ")
            curso_desmatricular = input("Ingrese el número del curso en el cual se quiere inscribir: ") #se pide el ingreso dev hasta que lo ingrese bien