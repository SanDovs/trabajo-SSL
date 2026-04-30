from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from datetime import datetime
import os

def colaIntervencion(gestion, cola):
    print("---COLA DE INTERVENCION---")
    
    if estaVacia(gestion):
        print("no hay ordenes en el sistema")
        return False
    
    #ME FALTA TERMINAR, TODAVIA NO PENSE EN LA LOGICA