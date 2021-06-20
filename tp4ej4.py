#Comparación de números
#Escribir una función que reciba dos valores y retorne:

#Retornar -1 si el primero es menor que el segundo
#Retornar 0 si son iguales
#Retornar 1 si el primero es mayor que el segundo
def compara(numero, otro_numero):
    if (numero<otro_numero):
        return -1
    elif(numero==otro_numero):
        return 0
    else:
        return 1

def prueba():
    resultado= compara(2,1)
    print(resultado)
    
if __name__ == "__main__":
    prueba()    