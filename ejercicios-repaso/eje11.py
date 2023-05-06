Name = input("Nombre del alumno: ")
Sexo = input("¿Qué sexo tiene?: ")

if Sexo == "Mujer" and Name[0].lower() < "m":
    print("Pertenece al grupo A.")
elif Sexo == "Mujer" and Name >= "m":
    print("Pertenece al grupo B.")
elif Sexo == "Hombre" and Name[0].lower() < "n":
    print("Pertenece al grupo A.")
else:
    print("Pertenece al grupo B.")



