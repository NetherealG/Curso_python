#Ejercicio 5
def eliminar_exlamacion():
    cadena = input("Ingrese un texto: ")
    eliminar = cadena[:-1].replace("!", "")
    print(eliminar)
eliminar_exlamacion()