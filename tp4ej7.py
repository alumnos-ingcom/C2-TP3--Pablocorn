##7. Restas sucesivas
#Escribir una función que mediante restas sucesivas, 
#obtenga el valor del cociente y resto de dos números enteros.

def division_lenta(dividendo, divisor):
    termino=True
    resultado_parcial=dividendo
    contador=0
    while termino:
        if(resultado_parcial>=divisor):
            resultado_parcial=resultado_parcial-divisor
            contador=contador+1
        else:
            termino=False
    return contador