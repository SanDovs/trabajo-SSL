from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from Fun_crearOrden import *
from Fun_modiCronograma import *
from Fun_eliminarOT import *


def MostrarOT(gestion):
    
    if estaVacia(gestion):
        print("No hay tareas en el sistema.")
        return False
    
    print("Tareas en el sistema:")
    
    for i in range(tamanio(gestion)):
        orden = recuperarOT(gestion, i)
        print(verOT(orden))
        
    return True
        
