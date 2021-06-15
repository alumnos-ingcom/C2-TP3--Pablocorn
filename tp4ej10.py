##Palíndromo
#Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo.
# Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
def es_palindromo(texto):
    tex_a_list=list(texto)
    lista_inversa=list(texto)
    lista_inversa.reverse()
    i=0
    for i in range(len(tex_a_list)-1):
        if tex_a_list[i]!=lista_inversa[i]:
            print("no es palindromo")
            resultado=False
            break
        else:
            resultado=True
    return resultado