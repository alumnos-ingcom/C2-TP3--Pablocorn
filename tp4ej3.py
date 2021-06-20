#3. Conversión de temperaturas
#Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
#Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit
#como un número real, utilice esta formula para calcular los grados centígrados y 
#retorne el resultado obtenido. Y viceversa.

#formula para pasar de Centigrados a Fahrenheit 
# ºF = (ºC · 1,8) + 32
#formula para pasar de Fahrenheit a Centigrados   
#ºC = (ºF -32) / 1,8
def convertir_a_fahrenheit(centigrados):
    fah=(centigrados*1.8)+32
    return fah
def convertir_a_centigrados(fahrenheit):
    centi=(fahrenheit-32)/1.8
    return centi

def prueba():
    centi=32
    faren=32
    cent_a_faren=convertir_a_fahrenheit(centi)
    faren_a_centi=convertir_a_centigrados(faren)
    print(str(faren),"°F son: ",str(faren_a_centi),"°C")
    print(str(centi),"°C son: ",str(cent_a_faren),"°F")

if __name__ == "__main__":
    prueba()