#Números primos
#Escribir una función que indique con True si un numero indicado es Primo.

def es_primo(numero):
    contador=0
    for i in range(1, numero+1):
        if numero % i == 0:
            contador += 1
    
    if contador == 2:
        return True
    else:
        return False

def prueba():
    for j in range(1,101):
        #prueba para los primeros 100 numeros
        print("el numero",j,"es primo?",es_primo(j)) 

    
if __name__ == "__main__":
    prueba()