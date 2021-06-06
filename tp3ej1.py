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
#
#def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
#    do:
#         esentero=ingreso_entero(mensaje)
#        si  esentero es un entero
#             resultado= verdadero
#        else
#            resultado=falso
#    while(resultado)

# def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    
    #si entero es menor a valor_maximo y menor a valor_minimo
      #  entonces
      #  return
    