def signo(numero):
    if numero>0:
        print("el numero es positivo")
        
    elif numero<0:
        print("el numero es negativo")
        
    else:
        print("el numero es cero")


def prueba():
    print("el valor 3:")
    signo(3)
    print("-------")
    print("el valor -2:")
    signo(-2)
    print("-------")
    print("el valor 0:")
    signo(0)
    
if __name__ == "__main__":
    prueba()