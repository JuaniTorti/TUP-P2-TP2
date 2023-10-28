from profesor import Profesor
from curso import Curso
import os


def ingreso_profesor(profesores, cursos, carreras):
    os.system("cls")
    email = input("Ingrese su email: ")
    contra = input("Ingrese su contraseña: ")

    bandera = False
    for profesor in profesores:
        if email == profesor.email: 
            bandera = True
            break

    if not(bandera):
        if email.lower() == "admin":
            alta_profe(profesores)
        else:
            print("\nEl usuario no se encuentra en el sistema")
            input("\nPresione ENTER para continuar")
    else:
        if profesor.validar_credenciales(email, contra):
                os.system("cls")
                sub_menu(profesor, cursos, carreras)
        else:
            print("\nLa contraseña o el email ingresados son incorrectos")
            input("\nPresione ENTER para continuar")


def alta_profe(profesores):
    os.system("cls")
    print("---Alta profesor---\n")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    email = input("ingrese su email: ")
    contra = input("Ingrese su contraseña: ")
    titulo = input("Ingrese su titulo adquirido: ")
    anio = input("Ingrese en que año egreso: ")
    while not(anio.isdigit()) or (int(anio) > 2023 or int(anio) < 1988): #se valida que ingrese un numero y que el año sea valido
        print("\nIngreso un año invalido, intentelo nuevamente")
        anio = input("Ingrese en que año egreso: ")
    anio = int(anio)

    profesor = Profesor(nombre, apellido, email, contra, titulo, anio)
    profesores.append(profesor)
    os.system("cls")
    print("La carga fue exitosa!!")
    input("\nPresione ENTER para continuar")


def sub_menu(profesor, cursos, carreras):
    op = 0
    while op != '3':
        os.system("cls")
        print("---MENU PROFESOR---")
        print("1- Dictar curso")
        print("2- Ver cursos")
        print("3- Volver al menu principal")
        op = input("\nIngrese una opcion: ")

        if op == '1':
            dictar_curso(profesor, cursos, carreras)
        elif op == '2':
            ver_cursos(profesor)
        elif op == '3':
            pass
        else:
            os.system("cls")
            print("\nIngreso un valor incompatible, intentelo nuevamente")
            input("\nPresione ENTER para continuar")


def dictar_curso(profesor, cursos, carreras):
    os.system("cls")
    x = 1
    for carrera in carreras:
        print(f"{x}- {carrera.nombre}") #le muestro las carreras para que pueda seleccionar donde quiere agregar una materia
        x += 1

    op_carrera = input("\nIngrese la opcion de la carrera en la que desea dictar un curso: ")
    while not(op_carrera.isdigit()) or (int(op_carrera) > x or int(op_carrera) <= 0):
        print("\nIngreso una opcion invalida, intentelo nuevamente")
        op_carrera = input("\nIngrese la opcion de la carrera en la que desea dictar un curso: ") #valido la seleccion
    
    carrera_selec = carreras[op_carrera - 1] #me guardo la carrera para asignarle a la materia

    os.system("cls")
    nombre_curso = input("Ingrese el nombre del curso: ") #carga de datos
    nombre_curso = nombre_curso.title()                    
    curso = Curso(nombre_curso, carrera_selec)

    cursos.append(curso) #agrego a la lista cursos
    profesor.dictar_curso(curso) #agrego a la lista mis_cursos del profesor
    carrera_selec.add_curso(curso) #agrego el curso a la carrera
    print("El curso se registro correctamente!!")
    input("\nPresione ENTER para continuar")



def ver_cursos(profesor):
    os.system("cls")
    cant_cursos = len(profesor.mis_cursos)
    
    if cant_cursos > 0:
        for curso in profesor.mis_cursos:
            print(curso)
            print("----------------------------------")
    else:
        print("No se encuentra dictando ningun curso")
    
    input("\nPresione ENTER para continuar")


