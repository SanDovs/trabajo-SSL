from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *


def depurar(gestion):
    
    print("---DEPURANDO ORDENES---")
    
    if estaVacia(gestion):
        print("no hay ordenes")
        return False
    
    sector = input("ingrese el sector: ").lower()
    
    eliminada = False
    
    for i in range(tamanio(gestion) -1, -1, -1):
        
        orden = recuperarOT(gestion, i)
        
        if verSector(orden) == sector:
            
            print(verOT(orden))
            elim = input("desea eliminar esta orden? (s/n): ").lower()
            
            if elim == "s":
                eliminarOT(gestion, orden)
                print(f"orden con id {verId(orden)} eliminada")
                print("---------------------------")
                eliminada = True
                
            else:
                print("cancelado...")
                return False
            
    if eliminada:
        print("depuracion completa")
        return True
    
    else:
        print("no se encontraron ordenes para determinado secto")
        return False
        