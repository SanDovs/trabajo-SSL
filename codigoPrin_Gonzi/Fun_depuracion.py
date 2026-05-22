from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from cargados import *


def depurar(gestion):

    print("---DEPURANDO ORDENES---")

    if estaVacia(gestion):
        print("no hay ordenes")
        return False

    sector = input("ingrese el sector: ").lower()

    eliminada = False

    i = tamanio(gestion) - 1  # arrancamos desde el ultimo

    while i >= 0:
        orden = recuperarOT(gestion, i)

        if verSector(orden).lower() == sector:
            print(verOT(orden))
            elim = input("desea eliminar esta orden? (s/n): ").lower()

            if elim == "s":
                eliminarOT(gestion, orden)
                print(f"orden con id {verId(orden)} eliminada")
                print("---------------------------")
                eliminada = True
                # NO hacemos i -= 1 extra: al eliminar, la lista
                # se achico y el indice i ahora apunta al siguiente
                # elemento a revisar automaticamente.

            else:
                print("orden conservada, continuando...")

        # Avanzamos hacia atras en ambos casos
        i -= 1

    if eliminada:
        print("depuracion completa")
        return True
    else:
        print("no se encontraron ordenes para ese sector")
        return False