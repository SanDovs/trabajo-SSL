
from Tad_Cola import *
from Tad_GestionOT import *
from Tad_OrdenDeTrabajo import *
import datetime
import os

print("---INICIALIZACION DEL PROGRAMA")

#VARIABLES
continuar = 1
lista_Ordenes = []
def NuevasOrdenes():
    gestion = crearGestion()
    cola = crearCola()
    orden = crearOT()
    print("=====CREACION DE NUEVA ORDEN=====")
    id_m = int(input("Ingrese el ID de la maquina: "))
    equipo = input("Ingrese el nombre del equipo: ")
    sector = input("Ingrese el secotr al que pertenece la orden: ")
    tec = input("Ingrese el nombre del técnico responsable: ")
    fecha = datetime.date(input("Ingrese la fecha programada: "))
    hora_ini = datetime.time("Ingrese la hora de inicio de la tarea: ")
    cargarOT(orden, id_m, equipo, sector, tec, fecha, hora_ini)
    agregarOT(gestion, orden)
    encolar(cola, orden) ### No estoy seguro de que sea de esta manera su aplicacion
    print(crearOT) ## Para revisar que se haya creado correctamente
    print(crearCola) ## Para revisar que se haya creado correctamente
    print(crearGestion) ## Para revisar que se haya creado correctamente

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
        NuevasOrdenes()
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


