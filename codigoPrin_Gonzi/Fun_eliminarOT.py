from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *


def eliminandoOT(gestion):
    try:   
        id_maqElim = int(input("id de la maquina: "))
    except ValueError:
        print("valor ingresado incorrecto")
        return False
    ordenEncontrada = False
    
    for ot in range(tamanio(gestion)):
        orden = recuperarOT(gestion, ot)
        if verId(orden) == id_maqElim:
            ordenEncontrada = True
            print("orden encontrada:")
            print(verOT(orden))
            
            confirmacion = input("¿Desea eliminar esta orden? (s/n): ").lower()
            if confirmacion == 's':
                eliminarOT(gestion, orden)
                print("orden eliminada exitosamente")
                return True
            else:
                print("eliminación cancelada")
                return False  
            
    print("no se encontro una orden")
    return False