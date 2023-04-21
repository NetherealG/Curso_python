first_Name = "nicolas"
last_name = "soto"
print(first_Name + " " + last_name)

mensaje = (("hola"+" ")*3)
#mensaje = "hola " *3
print(mensaje)
msj2 = "nico"
print(msj2)
msj2 += "+"
print(msj2)
msj2 += "alexita"
print(msj2)
print(len(msj2))

cadena = "esto es una oracion por la madre rusia"
posicion = cadena.find("juanito")
print("juanito se encuentra en:",posicion )
posicion = cadena.find("rusia")
print("rusia se encuentra en:",posicion )
puntito ="ESTOY EN MAYUSCULA"
puntito_lower = puntito.lower()
print(puntito_lower)

print("===== list =====")

empty_list = []
print(empty_list)

fullfiled_list = [1, 3, 500, 1.4,[2, "a"], {"name": "nico"}, (1, 3, 5)]
print(fullfiled_list)

second_list = list ()
print (second_list)
print(list("concurso"))

range_one = range(50)
print(list(range_one))

numeros = [1, 4, 6]
print(numeros)
numeros.append(10)
print(numeros)

print(numeros[2])

lista5 = ["hola", "a", "todos"]
for y in range(len(lista5)):
    if lista5[y] == "hola":
        lista5[y] = "adios"
        
print(lista5)

