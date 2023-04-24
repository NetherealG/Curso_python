#Ejercicio 1
def calificacion():
    n1 = float(input("Ingrese nota 1: "))
    n2 = float(input("Ingrese nota 2: "))
    n3 = float(input("Ingrese nota 3: "))
    
    x = promedio(n1, n2, n3)

    if x >= 0 or x <= 2:
        print("Calificación: D")
    elif x > 2 or x <= 5:
        print("Calificación: C")
    elif x > 5 or x <= 6:
        print("Calificación: B")
    elif x > 6 or x <= 7:
        print("Calificación: A")

def promedio(n1, n2, n3):
    x = (n1 + n2 + n3 )/3
    return x
calificacion()