#10. Factores Primos
#Escribir una función que retorne una tuple con factores primos de un numero entero positivo.

def factores_primos(numero):
    factor_a_analizar=1
    lista_de_factores=[]
    while factor_a_analizar<=numero:
        divisor_de_primos=1
        contador_de_divisores_exactos=0
        if numero%factor_a_analizar==0:
            while divisor_de_primos<=factor_a_analizar:#verifico  que el factor sea un numero primo
                if factor_a_analizar%divisor_de_primos==0:
                    contador_de_divisores_exactos=contador_de_divisores_exactos+1
                divisor_de_primos=divisor_de_primos+1
        if contador_de_divisores_exactos==2:
            lista_de_factores.append(factor_a_analizar) #agrego los factores primos a la lista
        factor_a_analizar=factor_a_analizar+1
    return tuple(lista_de_factores) #convierto la lista en una tupla

def prueba():
    print(factores_primos(50))#probando sacar la tupla de factores primos de 50

if __name__=="__main__":
    prueba()
