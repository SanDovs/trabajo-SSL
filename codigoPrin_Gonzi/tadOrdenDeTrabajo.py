# IMPLEMENTACIÓN DEL TAD SIMPLE: OrdenDeTrabajo

#Operaciones de crear y cargar

def crearOT():
    # Crea una estructura vacía para una nueva orden de trabajo con valores iniciales.
    # Representación Interna:
    # [0]: ID Máquina
    # [1]: Equipo
    # [2]: Sector
    # [3]: Técnico
    # [4]: Fecha
    # [5]: Hora
    ot = [0, "", "", "", "", ""]
    return ot

def cargarOT(ot, id_m, equipo, sector, tec, fecha, hora):
    # Carga de forma masiva todos los atributos de una orden ya creada.
    ot[0] = id_m
    ot[1] = equipo
    ot[2] = sector
    ot[3] = tec
    ot[4] = fecha
    ot[5] = hora
    
def verOT(ot):
    return f"ID Máquina: {verId(ot)}\nEquipo: {verEquipo(ot)}\nSector: {verSector(ot)}\nTécnico: {verTecnico(ot)}\nFecha: {verFecha(ot)}\nHora: {verHora(ot)}"

#Operaciones de Selección

def verId(ot):
    # Retorna el identificador único de la máquina.
    return ot[0]

def verEquipo(ot):
    # Retorna el nombre del equipo a intervenir.
    return ot[1]

def verSector(ot):
    # Retorna el sector de la planta donde se encuentra la máquina.
    return ot[2]

def verTecnico(ot):
    # Retorna el nombre del técnico asignado a la tarea.
    return ot[3]

def verFecha(ot):
    # Retorna la fecha programada para el mantenimiento.
    return ot[4]

def verHora(ot):
    # Retorna la hora de inicio de la intervención.
    return ot[5]

#Operaciones de Modificación

def modiId(ot, nuevoId):
    # Modifica el ID de la máquina asignado a la orden.
    ot[0] = nuevoId

def modiEquipo(ot, nuevoEquipo):
    # Modifica el nombre del equipo de la orden.
    ot[1] = nuevoEquipo

def modiSector(ot, nuevoSector):
    # Modifica el sector de la planta asociado a la orden.
    ot[2] = nuevoSector

def modiTecnico(ot, nuevoTecnico):
    # Modifica el técnico asignado a la orden.
    ot[3] = nuevoTecnico

def modiFecha(ot, nuevaFecha):
    # Modifica la fecha programada de la orden.
    ot[4] = nuevaFecha

def modiHora(ot, nuevaHora):
    # Modifica la hora de inicio programada de la orden.
    ot[5] = nuevaHora
    
def modiCronograma(ot, nuevaFecha, nuevaHora):
    # Modifica tanto la fecha como la hora programada de la orden.
    ot[4] = nuevaFecha
    ot[5] = nuevaHora

#Operación de Asignación

def asignarOT(otDestino, otOrigen):
    # Copia todos los datos de la orden origen en la orden destino.
    # Se hace campo por campo para asegurar independencia en memoria.
    otDestino[0] = otOrigen[0]
    otDestino[1] = otOrigen[1]
    otDestino[2] = otOrigen[2]
    otDestino[3] = otOrigen[3]
    otDestino[4] = otOrigen[4]
    otDestino[5] = otOrigen[5]