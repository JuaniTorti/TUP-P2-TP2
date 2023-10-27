from precarga import precarga
import os
from ingreso_profesor import ingreso_profesor
from funciones_estudiante import *
from mostrar_cursos import *

cursos = []
profesores = []
estudiantes = []
carreras = []
precarga(cursos,profesores,estudiantes,carreras)

op = 0
while op != "4":
    os.system("cls")
    print("---MENU PRINCIPAL---")
    print("1- Ingresar como estudiante")
    print("2- Ingresar como profesor")
    print("3- Ver cursos")
    print("4- Salir")
    op = input("\nIngrese una opcion: ")

    if op == "1":
        ingreso_estudiante(estudiantes,cursos)#ingreso como estudiante
    elif op == "2":
        ingreso_profesor(profesores, cursos) #ingreso como profe
    elif op == "3":
        mostrar(cursos)
    elif op == "4":
        os.system("cls")
        print("Hasta pronto!!")
        break
    else: 
        os.system("cls")
        print("Ingreso un valor incompatible, intentelo nuevamente")
        x = input("\nPresione ENTER para continuar")