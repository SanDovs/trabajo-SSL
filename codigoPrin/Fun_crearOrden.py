from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from datetime import datetime

def crearOrdenT():
    #creando una orden nueva
    nuevaOrden = crearOT()
    #ingresando datos
    try:
        id_m = int(input("ingrese el ID de la máquina: "))
    except ValueError:
        print("error, tipo de dato incorrecto")
        return None
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
    
    