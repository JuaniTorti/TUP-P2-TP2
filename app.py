from precarga import precarga
import os
from ingreso_profesor import ingreso_profesor
from funciones_estudiante import *

cursos = []
profesores = []
estudiantes = []
precarga(cursos,profesores,estudiantes)

op = 0
while op != 4:
    os.system("cls")
    print("---MENU PRINCIPAL---")
    print("1- Ingresar como estudiante")
    print("2- Ingresar como profesor")
    print("3- Ver cursos")
    print("4- Salir")
    op = int(input("\nIngrese una opcion: "))

    if op == 1:
        ingreso_estudiante(estudiantes,cursos)#ingreso como estudiante
    elif op == 2:
        ingreso_profesor(profesores, cursos) #ingreso como profe
    elif op == 3:
        pass# mostrar cursos
    elif op == 4:
        os.system("cls")
        print("Hasta pronto!!")
        break
    else: 
        print("Ingreso un valor incompatible, intentelo nuevamente\n")
        x = input("\nPresione ENTER para continuar")