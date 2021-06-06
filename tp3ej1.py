"""Escribir una funcion que solicite el ingreso de un número entero y
vuelva a solicitarlo en caso de ingresar un valor incorrecto"""

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
     do:
         ingreso_entero(mensaje)
     while
    