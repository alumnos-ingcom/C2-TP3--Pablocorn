################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from tp4ej10a import factores_primos
from tp4ej9 import es_primo
from tp4ej10 import es_palindromo
from tp4ej8 import ordenar_mayor_a_menor, ordenar_menor_a_mayor
from tp4ej6 import maximo, minimo
from tp4ej5 import signo
from tp4ej4 import compara
import tp4ej3  
from tp4ej2 import suma_lenta
import tp3ej1

def prueba():
    #valor=tp3ej1.ingreso_entero("ingrese numero entero")
    #print(valor)
    #tp4ej1.ingreso_entero_restringido("ingrese un numero entero")
    ##resultado_sumalenta=suma_lenta(4,5)
    ##print(resultado_sumalenta)

    ##probando conversion de Temperaturas
    #centi=32
    #faren=32
    #cent_a_faren=tp4ej3.convertir_a_fahrenheit(centi)
    #faren_a_centi=tp4ej3.convertir_a_centigrados(faren)
    #print(str(faren),"°F son: ",str(faren_a_centi),"°C")
    #print(str(centi),"°C son: ",str(cent_a_faren),"°F")

    ##probando comparacion de valores
    #resultado= compara(2,1)
    #print(resultado)

    ##probando que numero es menor a otro
#    print("el valor 3:")
#    signo(3)
#    print("-------")
#    print("el valor -2:")
#    signo(-2)
#    print("-------")
#    print("el valor 0:")
#    signo(0)

    ##Probando maximo y minimo de listas
    #lista=[63,66,433,72,43,62,8,1,29,42,41]
    #print(minimo(lista))
    #print(maximo(lista))

    ##7. Restas sucesivas
    #print(division_lenta(10,10))
    #print(division_lenta(12,4))
    #print(division_lenta(10,5))

    
    ##probando orden de tres valores y devolver una tupla
    #mayor_men=ordenar_mayor_a_menor(4,8,3)
    #menor_may=ordenar_menor_a_mayor(4,8,3)
    #print(menor_may)
    #print(mayor_men)

    #9- ver si un numero es primo 
   # for j in range(1,101):
        #prueba para los primeros 100 numeros
    #    print("el numero",j,"es primo?",es_primo(j)) 

    #10a - Factores primos
    print(factores_primos(10))


    #10- verificando si una palabra es un palindromo
    #caso falso
    #print(es_palindromo("banana"))
    #caso verdaderp
    #print(es_palindromo("anana"))


if __name__ == "__main__":
    prueba()