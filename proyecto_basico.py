
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def pedir_numero():
    numero = int(input("Escoge un numero: "))
    return numero

def imprimir_resultado(opcion):

    num1 = pedir_numero()
    num2 = pedir_numero()

    if opcion == 1:
        suma = sumar(num1, num2)
        print(f"La suma de {num1} + {num2} es: {suma}")
    elif opcion == 2:
        multiplicacion = multiplicar(num1, num2)
        print(f"La multiplicacion de {num1} * {num2} es: {multiplicacion}")
    elif opcion == 3:
        resta = restar(num1, num2)
        print(f"La resta de {num1} - {num2} es: {resta}")

mensaje_bienvenida = """
Escoge 1 para sumar
Escoge 2 para multiplicar
Escoge 3 para restar
"""

print(mensaje_bienvenida)
opcion = int(input("Escogo: "))

imprimir_resultado(opcion)