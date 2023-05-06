magos = []
cientificos = []
otros = []
nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

# Separar los nombres en tres grupos
for nombre in nombres:
    if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
        magos.append(nombre)
    elif nombre in ['Newton', 'Hawking', 'Einstein']:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

# Función para modificar los nombres de los magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]

# Función para imprimir los nombres de una lista
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

# Imprimir la lista original de nombres
print("Lista completa de nombres:")
imprimir_nombres(nombres)
print()

# Modificar los nombres de los magos
hacer_grandioso(magos)

# Imprimir los nombres de los magos grandiosos, los científicos y los restantes
print("Magos grandiosos:")
imprimir_nombres(magos)
print()

print("Científicos:")
imprimir_nombres(cientificos)
print()

print("Otros:")
imprimir_nombres(otros)
