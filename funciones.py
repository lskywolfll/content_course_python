
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

    
def imprimir_resultado(numero):
    
    verificar = es_par(numero)
    if verificar:
        print(f"El {numero} es par")
    else:
        print(f"El {numero} es impar")

numero = int(input("Escoge un numero para verificar si es par o impar: "))
imprimir_resultado(numero)