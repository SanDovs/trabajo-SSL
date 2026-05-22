from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from datetime import datetime
import os
 
def crearOrdenT(gestion):
    # Recibe gestion como parametro para desp ver si hay una orden con el mismo ID
    print("---CREANDO NUEVA ORDEN---")
 
    nuevaOrden = crearOT()
 
    try:
        id_m = int(input("ingrese el ID de la máquina: "))
    except ValueError:
        print("error, tipo de dato incorrecto")
        return None
 
    # Verificacion de ID duplicado:
    # Recorremos todas las ordenes existentes en la gestion
    # Si alguna ya tiene ese ID, avisamos y cancelamos la creacion
    for i in range(tamanio(gestion)):
        orden = recuperarOT(gestion, i)
        if verId(orden) == id_m:
            print(f"error: ya existe una orden con el ID {id_m}")
            return None
 
    # Si el for termino sin encontrar el ID, es unico y podemos continuar
    tecnico = input("ingrese el tecnico asignado: ")
    equipo = input("ingrese el nombre del equipo: ")
    sector = input("ingrese el sector: ")
 
    try:
        fecha = input("ingrese la fecha programada (dd/mm/yyyy): ")
        hora = input("ingrese la hora programada (hh:mm): ")
        fechaProg = datetime.strptime(fecha, "%d/%m/%Y").date()
        horaProg = datetime.strptime(hora, "%H:%M").time()
    except ValueError:
        print("error, vuelva a intentarlo")
        return None
 
    cargarOT(nuevaOrden, id_m, equipo, sector, tecnico, fechaProg, horaProg)
    return nuevaOrden