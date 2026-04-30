# IMPLEMENTACIÓN DEL TAD: TadCola

def crearCola():
    # Crea una estructura vacía para almacenar elementos bajo la lógica de una cola.
    # Representación Interna: Una lista donde el índice 0 es el frente.
    return []

def encolar(cola, elemento):
    # Agrega un elemento al final de la cola (operación de modificación).
    cola.append(elemento)

def desencolar(cola):
    # Elimina y retorna el elemento que se encuentra al frente de la cola (el primero).
    # Usamos pop(0) para sacar el primer elemento y desplazar el resto.
    if not esVaciaCola(cola):
        return cola.pop(0)
    else:
        return None

def verFrente(cola):
    # Retorna el elemento que está al frente de la cola sin eliminarlo.
    if not esVaciaCola(cola):
        return cola[0]
    else:
        return None

def tamanioCola(cola):
    # Retorna la cantidad de elementos que se encuentran actualmente en la cola.
    return len(cola)

def esVaciaCola(cola):
    # Retorna True o False dependiendo de si la cola tiene elementos o está vacía.
    return len(cola) == 0