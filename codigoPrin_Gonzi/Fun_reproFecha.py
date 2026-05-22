from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from Fun_crearOrden import *
from datetime import datetime

def reprogramarPorFecha(gestion):

    if estaVacia(gestion):
        print("No hay ordenes cargadas")
        return False

    try:
        fecha_vieja = input("Ingrese la fecha a reprogramar (dd/mm/yyyy): ")
        fecha_nueva = input("Ingrese la nueva fecha (dd/mm/yyyy): ")

        fechaVieja = datetime.strptime(fecha_vieja, "%d/%m/%Y").date()
        fechaNueva = datetime.strptime(fecha_nueva, "%d/%m/%Y").date()

    except ValueError:
        print("Formato de fecha incorrecto")
        return False

    contador = 0

    for i in range(tamanio(gestion)):
        orden = recuperarOT(gestion, i)

        if verFecha(orden) == fechaVieja:

            # Mostramos la orden ANTES de modificarla
            print("orden a reprogramar:")
            print(verOT(orden))
            print("---------------------------")

            hora_actual = verHora(orden)
            modiCronograma(orden, fechaNueva, hora_actual)
            contador += 1

            # Mostramos la orden DESPUES del cambio
            print("orden reprogramada:")
            print(verOT(orden))
            print("===========================")

    if contador > 0:
        print(f"Se reprogramaron {contador} ordenes correctamente")
        return True
    else:
        print("No se encontraron ordenes con esa fecha")
        return False