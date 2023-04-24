#Ejercicio 3
def maximo_comun_divisor():
    '''Este ejercicio se basa en el algoritmo de Euclides'''
    a = int(input("Ingrese numero 1: "))
    b = int(input("Ingrese numero 2: "))
    c = 0
    while b != 0:
        c = b
        b = a % b
        a = c
    print("El máximo común divisor es: ", a)

maximo_comun_divisor()