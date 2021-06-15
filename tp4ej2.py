#Suma lenta
#Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa.
# Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

#La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.

def suma_lenta(numero, otro_numero):
    print("suma lenta de :",str(numero),"y",str(otro_numero))
    suma=numero  
    for i in range(abs(otro_numero)):  
        suma=suma+ int((abs(otro_numero)/otro_numero))
        if(otro_numero<0):
            print(str(suma+1),'+',str(int((abs(otro_numero)/otro_numero))),'=',str(suma))
        else:
            print(str(suma-1),'+',str(int((abs(otro_numero)/otro_numero))),'=',str(suma))
    return suma