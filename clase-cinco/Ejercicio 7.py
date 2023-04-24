#Ejercicio 7
def notaFinal():
    calificacion = int(input("Ingrese calificación del examen: "))#de 0 a 100
    proyectos = int(input("Ingrese número de proyectos completados: "))#de 0 en adelante
    
    #100, si la calificación del examen es superior a 90 o si el número de proyectos terminados es superior a 10.
    if calificacion > 90 and calificacion <= 100 or proyectos > 10:
        print("Nota final: ", 100)
    #90, si la calificación del examen es superior a 75 y si el número de proyectos completados es mínimo 5.
    elif calificacion > 75 and calificacion <= 90 or proyectos > 5 and proyectos <= 10:
        print("Nota final: ", 90)
    #75, si la calificación del examen es superior a 50 y si el número de proyectos completados es mínimo 2.
    elif calificacion > 50 and calificacion <= 75 or proyectos > 2 and proyectos <= 5:
        print("Nota final: ", 75)
notaFinal()