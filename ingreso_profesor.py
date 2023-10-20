from profesor import Profesor
from curso import Curso
import os


def ingreso_profesor(profesores):
    email = input("Ingrese su e-mail: ")
    contra = input("Ingrese su contraseña: ")

    for profesor in profesores:
        if email == profesor.email:
            if profesor.validar_credenciales(email, contra):
                os.system("cls")
                sub_menu(profesor)
                break
            else:
                print("\nLa contraseña o el email ingresados son incorrectos")
                x = input("Presione ENTER para continuar")
        else:
            print("\nLa contraseña o el email ingresados son incorrectos")
            x = input("\nPresione ENTER para continuar")


def sub_menu(profesor):
    op = 0
    while op != 3:
        print("1- Dictar curso")
        print("2- Ver cursos")
        print("3- Volver al menu principal")
        op = int(input("\nIngrese una opcion: "))

        if op == 1:
            dictar_curso(profesor)
        elif op == 2:
            pass  # ver cursos
        elif op == 3:
            pass
        else:
            os.system("cls")
            print("Ingreso un valor incompatible, intentelo nuevamente\n")


def dictar_curso(profesor):
    nombre_curso = input("Ingrese el nombre del curso: ")
    nombre_curso = nombre_curso.title()
    curso = Curso(nombre_curso)

    cursos.append(curso)
    profesor.dictar_curso(curso) 
    print("El curso se registro correctamente!!")
    x = input("\nPresione ENTER para continuar")

def ver_cursos(profesor):
    for curso in profesor.mis_cursos():
        print(curso)
        print("---------------------------------------")


