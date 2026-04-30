#librerias, modulos
import os
from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from Fun_crearOrden import *
from Fun_modiCronograma import *
from Fun_eliminarOT import *
from Fun_mostrarOT import *
from Fun_reproFecha import *
from Fun_depuracion import *
from Fun_colaIntervencion import *



print("---INICIALIZACION DEL PROGRAMA")

#VARIABLES
continuar = 1
cola = crearCola()
gestion = crearGestion()

while continuar != 0:
    print("---menu---")
    print("1 - registrar nuevas ordenes")
    print("2 - modificar cronograma")
    print("3 - finalizar/cancelar tareas")
    print("4 - ordenes activas")
    print("5 - reprogramar tareas")
    print("6 - depurar")
    print("0 - finalizar")
    
    try:
        opc = int(input("opcion: "))
    except ValueError:
        print("valor ingresado incorrecto")
        continue
    
    os.system("cls")
    
    #--------------------------------------------------------#
        
        
    if opc == 0:
        print("finalizando...")
        continuar = 0
        break
    
    
    #--------------------------------------------------------#
    
    
    elif opc == 1:
        #crea una orden nueva 
        orden = crearOrdenT()
        if orden is not None:
            agregarOT(gestion, orden)
            encolar(cola, orden)
            print("orden creada exitosamente")
            print(verOT(orden))
        else:
            print("no se pudo crear la orden")
        
        
    #--------------------------------------------------------#
    
    
    elif opc == 2:
        
        print("---MODIFICANDO CRONOGRAMA---")
        cambiarCronograma(gestion)
    
    
    #--------------------------------------------------------#
    
    
    elif opc == 3:
        
        print("---FINALIZANDO/CANCELANDO TAREAS---")
        eliminar = eliminandoOT(gestion)
        if eliminar:
            print("proceso completo")
            
        else:
            print("proceso no realizado")
            
    
    #--------------------------------------------------------#
    
    
    elif opc == 4:
        
        print("---TAREAS ACTIVAS---")
        MostrarOT(gestion)    
    
    #--------------------------------------------------------#
    
    
    elif opc == 5:
        
        print("---REPROGRAMANDO ORDENES POR FECHA---")
        reprogramarPorFecha(gestion)
    
    
    #--------------------------------------------------------#
    
    
    elif opc == 6:
        
        print("---seleccion una opcion---")
        print("A - baja por sector")
        print("B - cola de intervencion")
        print("C - salir")
        
        option = input("opcion: ").upper()
        
        if option == "C":
            print("saliendo...")
            continue
        
        elif option == "A": 
            depurar(gestion)
        
        elif option == "B":
            colaIntervencion(gestion)
            
            
    #--------------------------------------------------------#
    else:
        print("opcion inexistente, vueva a intentarlo")
        continue