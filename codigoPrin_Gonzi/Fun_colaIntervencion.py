from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from datetime import datetime


def colaIntervencion(gestion):
    print("---COLA DE INTERVENCION---")
    
    # Verificamos que haya órdenes cargadas
    if estaVacia(gestion):
        print("no hay ordenes en el sistema")
        return False
    
    # Pedimos la fecha al usuario
    try:
        fecha_input = input("ingrese la fecha del dia (dd/mm/yyyy): ")
        fechaBuscada = datetime.strptime(fecha_input, "%d/%m/%Y").date()
    except ValueError:
        print("formato de fecha incorrecto")
        return False
    
    # Creamos una cola NUEVA y VACÍA solo para el reporte de ese día
    # Es distinta a la cola general del main: esta es temporal y solo
    # guarda [equipo, tecnico], no la orden completa
    colaDelDia = crearCola()
    
    # Recorremos todas las órdenes de la gestión
    for i in range(tamanio(gestion)):
        orden = recuperarOT(gestion, i)
        
        # Si la fecha coincide, armamos el resumen y lo encolamos
        if verFecha(orden) == fechaBuscada:
            resumen = [verEquipo(orden), verTecnico(orden)]
            encolar(colaDelDia, resumen)
    
    # Si no encontramos ninguna orden para ese día, avisamos y salimos
    if esVaciaCola(colaDelDia):
        print(f"no hay ordenes programadas para el {fechaBuscada}")
        return False
    
    # Imprimimos la cola respetando el TAD:
    # Usamos desencolar() para sacar de a uno desde el frente,
    # que es la única forma "correcta" de recorrer una cola.
    print(f"\nordenes del dia {fechaBuscada}:")
    print("=" * 30)
    
    turno = 1
    while not esVaciaCola(colaDelDia):
        item = desencolar(colaDelDia)
        print(f"Turno {turno}:")
        print(f"  Equipo  : {item[0]}")
        print(f"  Tecnico : {item[1]}")
        print("-" * 30)
        turno += 1
    
    return True