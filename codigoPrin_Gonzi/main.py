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
from cargados import *


#usos del tad:

# tadOrdenDeTrabajo:
# crearOrdenT(): crea una nueva orden de trabajo
# verOT(): muestra la información de una orden
# verID(): obtiene el ID de una orden
# verEquipo(): obtiene el equipo asociado a una orden
# verTecnico(): obtiene el técnico asignado a una orden
# verFecha(): obtiene la fecha programada de una orden
# cambiarCronograma(): modifica el cronograma de una orden.

# tad_gestionOT:
# crearGestion(): crea una nueva gestión de órdenes
# agregarOT(): agrega una orden a la gestión
# recuperarOT(): recupera una orden de la gestión
# tamanio(): obtiene el tamaño de la gestión
# estaVacia(): verifica si la gestión está vacía.

# tadCola:
# crearCola(): crea una nueva cola
# encolar(): agrega un elemento a la cola
# desencolar(): elimina un elemento de la cola
# esVaciaCola(): verifica si la cola está vacía.


print("---INICIALIZACION DEL PROGRAMA")

#VARIABLES
continuar = 1
cola = crearCola()
gestion = crearGestion()
preCargarDatos(gestion) #datos precargados para la prueba

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
       
        orden = crearOrdenT(gestion)
        if orden is not None:
            agregarOT(gestion, orden)
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