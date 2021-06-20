#Ordenar 3 valores
#Escribir una función que a partir de tres variables de tipo entero retorne una tupla
# con dichos valores ordenados de menor a mayor. Y Viceversa Interfaz

def ordenar_menor_a_mayor(uno, dos, tres):
    lista=[uno, dos, tres]
    lista.sort()
    tupla=tuple(lista)
    return tupla
    

def ordenar_mayor_a_menor(uno, dos, tres):

    lista=[uno, dos, tres]
    lista.sort(reverse=True)
    tupla=tuple(lista)
    return tupla

def prueba():
    mayor_men=ordenar_mayor_a_menor(4,8,3)
    menor_may=ordenar_menor_a_mayor(4,8,3)
    print(menor_may)
    print(mayor_men)
    
if __name__ == "__main__":
    prueba()