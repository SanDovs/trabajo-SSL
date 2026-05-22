from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from cargados import *


def eliminandoOT(gestion):

    if estaVacia(gestion):
        print("no hay ordenes en el sistema")
        return False

    try:
        id_maqElim = int(input("id de la maquina: "))
    except ValueError:
        print("valor ingresado incorrecto")
        return False

    ordenEncontrada = False

    # Usamos while en lugar de for para recorrer la gestion.
    # Esto nos da control manual del indice: si eliminamos,
    # NO avanzamos porque la lista ya se achico sola.
    # Si no eliminamos, avanzamos con i += 1.
    i = 0
    while i < tamanio(gestion):
        orden = recuperarOT(gestion, i)

        if verId(orden) == id_maqElim:
            ordenEncontrada = True
            print("orden encontrada:")
            print(verOT(orden))

            # Pedir el motivo de eliminacion (segun consigna)
            print("Motivo de cancelacion:")
            print("  1 - Falta de repuestos")
            print("  2 - Cambio de prioridad")
            motivo = input("ingrese el motivo (1/2): ")

            if motivo == "1":
                motivo_texto = "falta de repuestos"
            elif motivo == "2":
                motivo_texto = "cambio de prioridad"
            else:
                print("motivo invalido, cancelacion abortada")
                return False

            confirmacion = input(f"confirma eliminar esta orden por {motivo_texto}? (s/n): ")
            if confirmacion.lower() == "s":
                eliminarOT(gestion, orden)
                print(f"orden eliminada exitosamente — motivo: {motivo_texto}")
                return True
            else:
                print("eliminacion cancelada")
                return False

        else:
            # Solo avanzamos si NO eliminamos
            i += 1

    if not ordenEncontrada:
        print("no se encontro una orden con ese ID")
        return False