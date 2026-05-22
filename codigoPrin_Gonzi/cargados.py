from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from datetime import date, time

def preCargarDatos(gestion):
    # Carga 20 ordenes de trabajo predefinidas en la gestion al inicio del programa.
    # Se usa crearOT() y cargarOT() del TAD OrdenDeTrabajo para respetar la abstraccion.
    # Se usa agregarOT() del TAD GestionOT para agregar cada orden a la estructura.
    # Los datos cubren distintos sectores, tecnicos y fechas para permitir
    # probar todas las funciones del sistema (depurar, colaIntervencion, reproFecha, etc.)

    datos = [
        # (ID, Equipo, Sector, Tecnico, Fecha, Hora)
        (101, "Compresor de aire",     "Fundicion",   "Brandan Gonzalo",    date(2025, 6, 15), time(8,  0)),
        (102, "Horno de fundicion",    "Fundicion",   "Lisandro Rojas",   date(2025, 6, 15), time(9,  0)),
        (103, "Cinta transportadora",  "Fundicion",   "Santiago Dovidio",   date(2025, 6, 16), time(7, 30)),
        (201, "Torno CNC",             "Embalaje",    "Ana Lopez",     date(2025, 6, 15), time(10, 0)),
        (202, "Selladora automatica",  "Embalaje",    "Pedro Diaz",    date(2025, 6, 17), time(8,  0)),
        (203, "Flejadora",             "Embalaje",    "Laura Vega",    date(2025, 6, 17), time(9, 30)),
        (301, "Bomba hidraulica",      "Pintura",     "Brandan Gonzalo",date(2025, 6, 15), time(11, 0)),
        (302, "Compresor de pintura",  "Pintura",     "Sofia Torres",  date(2025, 6, 18), time(8,  0)),
        (303, "Cabina de secado",      "Pintura",     "Diego Morales", date(2025, 6, 18), time(10, 0)),
        (401, "Prensa hidraulica",     "Mecanizado",  "Roberto Silva", date(2025, 6, 16), time(8,  0)),
        (402, "Fresadora CNC",         "Mecanizado",  "Lisandro Rojas", date(2025, 6, 16), time(9,  0)),
        (403, "Rectificadora",         "Mecanizado",  "Francisco Martinez", date(2025, 6, 19), time(7,  0)),
        (404, "Centro de mecanizado",  "Mecanizado",  "Juan Perez",    date(2025, 6, 19), time(8, 30)),
        (501, "Caldera principal",     "Calderas",    "Francisco Martinez",   date(2025, 6, 17), time(6,  0)),
        (502, "Intercambiador calor",  "Calderas",    "Maria Gomez",   date(2025, 6, 17), time(7,  0)),
        (503, "Valvula de seguridad",  "Calderas",    "Ana Lopez",     date(2025, 6, 20), time(8,  0)),
        (601, "Robot de soldadura",    "Ensamble",    "Pedro Diaz",    date(2025, 6, 18), time(9,  0)),
        (602, "Banda de ensamble",     "Ensamble",    "Laura Vega",    date(2025, 6, 20), time(10, 0)),
        (603, "Armario electrico",     "Ensamble",    "Luis Fernandez",date(2025, 6, 20), time(11, 0)),
        (701, "Generador electrico",   "Electricidad","Sofia Torres",  date(2025, 6, 21), time(7,  0)),
    ]

    for id_m, equipo, sector, tecnico, fecha, hora in datos:
        # Para cada fila de datos:
        # 1. Creamos una ficha vacia con crearOT()
        # 2. La llenamos con cargarOT()
        # 3. La agregamos a la gestion con agregarOT()
        ot = crearOT()
        cargarOT(ot, id_m, equipo, sector, tecnico, fecha, hora)
        agregarOT(gestion, ot)