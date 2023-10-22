from profesor import Profesor
from curso import Curso
import os


def ingreso_profesor(profesores, cursos):
    os.system("cls")
    email = input("Ingrese su e-mail: ")
    contra = input("Ingrese su contraseña: ")

    bandera = False
    for profesor in profesores:
        if email == profesor.email:
            bandera = True
            break

    if not(bandera):
        print("\nEl usuario no se encuentra en el sistema")
        x = input("\nPresione ENTER para continuar")
    else:
        if profesor.validar_credenciales(email, contra):
                os.system("cls")
                sub_menu(profesor, cursos)
        else:
            print("\nLa contraseña o el email ingresados son incorrectos")
            x = input("\nPresione ENTER para continuar")


def sub_menu(profesor, cursos):
    op = 0
    while op != 3:
        os.system("cls")
        print("1- Dictar curso")
        print("2- Ver cursos")
        print("3- Volver al menu principal")
        op = int(input("\nIngrese una opcion: "))

        if op == 1:
            dictar_curso(profesor, cursos)
        elif op == 2:
            ver_cursos(profesor)
        elif op == 3:
            pass
        else:
            os.system("cls")
            print("\nIngreso un valor incompatible, intentelo nuevamente")
            x = input("\nPresione ENTER para continuar")


def dictar_curso(profesor, cursos):
    os.system("cls")
    nombre_curso = input("Ingrese el nombre del curso: ")
    nombre_curso = nombre_curso.title()
    curso = Curso(nombre_curso)

    cursos.append(curso)
    profesor.dictar_curso(curso) 
    print("El curso se registro correctamente!!")
    x = input("\nPresione ENTER para continuar")



def ver_cursos(profesor):
    
    os.system("cls")
    for curso in profesor.mis_cursos:
        print(curso)
        print("----------------------------------")

    x = input("\nPresione ENTER para continuar")


