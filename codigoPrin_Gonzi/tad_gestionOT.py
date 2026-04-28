# IMPLEMENTACIÓN DEL TAD COMPUESTO: TadGestionOT

def crearGestion():
    # Crea una estructura vacía para almacenar el conjunto de las órdenes de trabajo.
    # Representación Interna: Una lista de Python que contendrá objetos OT.
    return []

def agregarOT(gestion, ot):
    # Agrega una orden de trabajo completa a la gestión actual.
    gestion.append(ot)

def eliminarOT(gestion, ot):
    # Elimina una orden de trabajo específica de la gestión.
    # Usamos remove para quitar el objeto exacto de la lista.
    if ot in gestion:
        gestion.remove(ot)

def tamanio(gestion):
    # Retorna la cantidad total de órdenes de trabajo almacenadas en la gestión.
    return len(gestion)

def recuperarOT(gestion, i):
    # Retorna la orden de trabajo que se encuentra en la posición i-ésima.
    # Pre-condición: 0 <= i < len(gestion)
    return gestion[i]

def reemplazarOT(gestion, i, nuevaOt):
    # Sustituye la orden de trabajo de la posición i-ésima por una nueva orden.
    gestion[i] = nuevaOt

def estaVacia(gestion):
    # Retorna True o False dependiendo de si la gestión tiene órdenes cargadas o no.
    return len(gestion) == 0