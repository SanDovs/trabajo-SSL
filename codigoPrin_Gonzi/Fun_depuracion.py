from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *


def depurar(gestion):

    print("---DEPURANDO ORDENES---")

    if estaVacia(gestion):
        print("no hay ordenes")
        return False

    sector = input("ingrese el sector: ")

    eliminada = False

    # Usamos while recorriendo AL REVES (de la ultima a la primera).
    # Por que al reves? Porque si eliminamos un elemento, los indices
    # de lo que falta revisar (que estan ADELANTE, es decir en posiciones
    # menores) no se mueven. Si fueramos hacia adelante y eliminamos,
    # los indices se desplazan y nos saltariamos ordenes.
    #
    # Por que while y no for?
    # Con while tenemos control manual del indice.
    # Cuando eliminamos, i -= 1 porque la lista se achico en uno
    # y la posicion anterior ahora apunta a un elemento diferente.
    # Cuando no eliminamos, i -= 1 igualmente para seguir hacia atras.
    # En este caso ambas ramas hacen i -= 1, pero la separacion
    # deja el codigo claro y extensible.

    i = tamanio(gestion) - 1  # arrancamos desde el ultimo

    while i >= 0:
        orden = recuperarOT(gestion, i)

        if verSector(orden) == sector:
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