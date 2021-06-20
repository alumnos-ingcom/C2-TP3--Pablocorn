"""Escribir una funcion que solicite el ingreso de un número entero y
vuelva a solicitarlo en caso de ingresar un valor incorrecto"""
class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 
def ingreso_entero(mensaje):
    """Recibe un número y verifica que sea entero"""
    while True:
        entrada = input(mensaje + " #")    
        try:
            entero=int(entrada)
            print("es entero")
            return entero
        except ValueError as err:
            print("error ingrese numero nuevo")
            continue
        return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """Recibe un número y verifica que sea entero"""
    while cantidad_reintentos>=0:
        entrada = input(mensaje + " #")
        cantidad_reintentos=cantidad_reintentos-1
        try:
            entero=int(entrada)
            print("es entero")
            return entero
        except ValueError as err:
            print("error ingrese numero nuevo")
            continue
        return entero
def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    
    entero=ingreso_entero(mensaje);
    if(entero>=valor_minimo and entero<=valor_maximo):
        print("el valor es correcto")
    else:
        print("el valor es incorrecto")    

def prueba():
    #valor=ingreso_entero("ingrese numero entero")
    #print(valor)
    #valor=ingreso_entero_reintento("ingrese numero entero")   
    #print(valor)    
    ingreso_entero_restringido("ingrese numero entero")
if __name__ == "__main__":
    prueba()