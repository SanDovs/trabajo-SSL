
from Tad_Cola import *
from Tad_GestionOT import *
from Tad_OrdenDeTrabajo import *

print("---INICIALIZACION DEL PROGRAMA")

#VARIABLES
continuar = 1
lista_Ordenes = []

while continuar != 0:
    print("---menu---")
    print("1 - registrar nuevas ordenes")
    print("2 - modificar cronograma")
    print("3 - cancelar tareas")
    print("4 - mostrar todas las ordenes activas")
    print("5 - reprogramar tareas")
    print("6 - depurar")
    print("0 - finalizar")
    
    try:
        opc = int(input("opcion: "))
    except ValueError:
        print("valor ingresado incorrecto")
        continue
        
    if opc == 0:
        continuar = 0
        break
    
    elif opc == 1:
        pass
    
    elif opc == 2:
        pass
    
    elif opc == 3:
        pass
    
    elif opc == 4:
        pass
    
    elif opc == 5:
        pass
    
    elif opc == 6:
        pass
