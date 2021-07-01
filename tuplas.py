
# lista => numeros = [1,2,3,4,5]
numeros = (1,2,3,4,5,1,2)

def cantidad_repeticion_numero(numero):
    cantidad = numeros.count(numero)

    if numero not in numeros:
        print("No existe el numero en la lista.")
        return

    if cantidad > 1:
        print(f"El numero '{numero}' se repitio {cantidad} veces.")
    else:
        print(f"El numero '{numero}' no se repite.")

numero = int(input("Escoge un numero entre el 1 y 5: "))

cantidad_repeticion_numero(numero)