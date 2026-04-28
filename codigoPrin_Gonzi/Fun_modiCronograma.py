from tadOrdenDeTrabajo import *
from tad_gestionOT import *
from tadCola import *
from Fun_crearOrden import *

def cambiarCronograma(gestion):
    
    if estaVacia(gestion):
        print("no se encontraron ordenes")
        return False
    
    try:
        id_maq = int(input("ingrese el ID de la máquina para modificar su cronograma: "))
    except ValueError:
        print("valor ingresado incorrecto")
        return False
    
    ordenEncontrada = False
    
    for ord in range(tamanio(gestion)):
        orden = recuperarOT(gestion, ord)
        
        if verId(orden) == id_maq:
            ordenEncontrada = True
            print("orden encontrada:")
            print(verOT(orden))
            
            
            try:
                fecha = input("ingrese la nueva fecha programada (dd/mm/yyyy): ")
                hora = input("ingrese la nueva hora programada (hh:mm): ")
                nuevaFecha = datetime.strptime(fecha, "%d/%m/%Y").date()
                nuevaHora = datetime.strptime(hora, "%H:%M").time()
            except ValueError:
                print("datos ingresados incorrectos")
                return False
            
            modiCronograma(orden, nuevaFecha, nuevaHora)
            print("cronograma modificado exitosamente")
            print(verOT(orden))
            return True
        
        else:
            print("no se encontro la orden")
            return False