##7. Restas sucesivas
#Escribir una función que mediante restas sucesivas, 
#obtenga el valor del cociente y resto de dos números enteros.

def division_lenta(dividendo, divisor):
    termino=True
    resultado_parcial=dividendo
    cociente=0
    while termino:
        if(resultado_parcial>=divisor):
            resultado_parcial=resultado_parcial-divisor
            cociente=cociente+1
        else:
            termino=False
    resto=dividendo-(cociente*divisor)
    return (cociente,resto)

def prueba():
    print(division_lenta(10,10))
    print(division_lenta(12,4))
    print(division_lenta(10,5))
    
if __name__ == "__main__":
    prueba()