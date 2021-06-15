##Máximo / Mínimo
#Escribir una función que dada una lista de valores enteros, retorne el menor ellos.
# E implementar otra función que retorne el valor máximo del conjunto de valores.

def minimo(lista):
    menor=lista[0]
    for i in range(0,len(lista)):  
        if(lista[i]<menor):
            menor=lista[i]
    return menor
def maximo(lista):
    mayor=lista[0]
    for i in range(0,len(lista)):  
        if(lista[i]>mayor):
            mayor=lista[i]
    return mayor