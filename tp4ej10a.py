#10. Factores Primos
#Escribir una función que retorne una tuple con factores primos de un numero entero positivo.

def factores_primos(numero):
    i=1
    lista=[]
    while i<=numero:
        k=1
        j=0
        if numero%i==0:
            while k<=i:
                if i%k==0:
                    j=j+1
                k=k+1
        if j==2:
            lista.append(i)
        i=i+1
    return tuple(lista)