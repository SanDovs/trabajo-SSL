from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from Fun_crearOrden import *
from Fun_modiCronograma import *




print("---INICIALIZACION DEL PROGRAMA")

#VARIABLES
continuar = 1
cola = crearCola()
gestion = crearGestion()

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
    
    #--------------------------------------------------------#
        
        
    if opc == 0:
        print("finalizando...")
        continuar = 0
        break
    
    
    #--------------------------------------------------------#
    
    
    elif opc == 1:
        #crea una orden nueva
        print("---CREANDO NUEVA ORDEN---")  
        orden = crearOrdenT()
        cola.append(orden)
        if orden is not None:
            agregarOT(gestion, orden)
            print("orden creada exitosamente")
            print(verOT(orden))
        else:
            print("no se pudo crear la orden")
        
        
    #--------------------------------------------------------#
    
    
    elif opc == 2:
        
        print("---MODIFICANDO CRONOGRAMA---")
        nuevoCronograma = cambiarCronograma(gestion)
    
    
    #--------------------------------------------------------#
    
    
    elif opc == 3:
        print("---ELIMINANDO TAREAS---")
        pass
    
    
    #--------------------------------------------------------#
    
    
    elif opc == 4:
        print("---TAREAS ACTIVAS---")
        tamanioCola(cola)
        pass
    
    
    #--------------------------------------------------------#
    
    
    elif opc == 5:
        pass
    
    
    #--------------------------------------------------------#
    
    
    elif opc == 6:
        pass
    
    
    #--------------------------------------------------------#