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