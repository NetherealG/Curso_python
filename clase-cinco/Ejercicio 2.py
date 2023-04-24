#Ejercicio 2
def multiplicacion():
    start = 1
    end = 10

    x = start
    while x <= end:
        y = start
        while y <= end:
            print(x, "*", y, "=", x*y)
            y += 1
        x += 1
multiplicacion()        