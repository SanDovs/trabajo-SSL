from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from Fun_crearOrden import *
from Fun_modiCronograma import *
from Fun_eliminarOT import *


def MostrarOT(gestion):
    if len(gestion) == 0:
        print("No hay tareas en el sistema.")
    else:
        print("Tareas en el sistema:")
        for tarea in gestion:
            pass
