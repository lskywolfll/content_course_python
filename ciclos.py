
numeros = [1,2,3,4,5,6,7,8,9,10]
cantidad_numeros = len(numeros)

def imprimir_numero(numero):
    print(f"Numero: {numero}")

# 1er
# for numero in numeros:
#     imprimir_numero(numero)

# for posicion in range(0,cantidad_numeros + 1, 2):
#     imprimir_numero(posicion)

# 2er

contador = 0
while contador < cantidad_numeros:
    numero = numeros[contador]

    if numero % 2 == 0:
        imprimir_numero(numero)
        
    contador += 1