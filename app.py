from curso import Curso
from estudiante import Estudiante
from profesor import Profesor
from precarga import precarga
import os

cursos = []
profesores = []
estudiantes = []
precarga()

op = 0
while op != 4:
    print("---MENU PRINCIPAL---")
    print("1- Ingresar como estudiante")
    print("2- Ingresar como profesor")
    print("3- Ver cursos")
    print("4- Salir")
    op = int(input("\nIngrese una opcion: "))

    if op == 1:
        #ingreso como estudiante
    elif op == 2:
        #ingreso como profe
    elif op == 3:
        # mostrar cursos
    elif op == 4:
        os.system("cls")
        print("Hasta pronto!!")
    else: 
        os.system("cls")
        print("Ingreso un valor incompatible, intentelo nuevamente\n")