class IndexErrorException(Exception):
    def __init__(self, message="Index out of range"):
        self.message = message
        super().__init__(self.message)

# Ejemplo de uso
try:
    lista = [1, 2, 3]
    index = 4
    if index >= len(lista):
        raise IndexErrorException("Índice fuera de rango")
    else:
        elemento = lista[index]
        print("Elemento:", elemento)
except IndexErrorException as e:
    print("¡Error de índice personalizado:", e.message, "!")

#En este ejemplo, creamos una lista lista con 3 elementos y luego intentamos acceder 
# a un índice fuera de rango (index = 4). Si el índice es mayor o igual a la longitud
# de la lista, lanzamos la excepción IndexErrorException con un mensaje personalizado.
# De lo contrario, accedemos al elemento correspondiente y lo imprimimos. Si se captura la excepción
# IndexErrorException, imprimimos un mensaje de error personalizado con el mensaje proporcionado en la excepción.


class TypeErrorException(Exception):
    def __init__(self, message="Invalid type"):
        self.message = message
        super().__init__(self.message)

# Ejemplo de uso
try:
    numero = "10"
    if not isinstance(numero, int):
        raise TypeErrorException("Tipo de dato inválido")
    else:
        resultado = numero + 5
        print("Resultado:", resultado)
except TypeErrorException as e:
    print("¡Error de tipo personalizado:", e.message, "!")

#En este ejemplo, asignamos el valor de una cadena "10" a la variable numero.
#Luego, verificamos si el tipo de numero es un entero (int). Si no es un entero,
#lanzamos la excepción TypeErrorException con un mensaje personalizado. De lo contrario,
# realizamos una operación aritmética en numero y lo imprimimos. Si se captura la excepción TypeErrorException,
#imprimimos un mensaje de error personalizado con el mensaje proporcionado en la excepción.


class KeyErrorException(Exception):
    def __init__(self, message="Key not found"):
        self.message = message
        super().__init__(self.message)


try:
    diccionario = {"clave1": "valor1", "clave2": "valor2"}
    clave = "clave3"
    if clave not in diccionario:
        raise KeyErrorException("Clave no encontrada")
    else:
        valor = diccionario[clave]
        print("Valor:", valor)
except Exception as e:
    print("¡Error de clave personalizado:", e.message, "!")


#En este ejemplo, creamos un diccionario diccionario con dos claves y valores.
# Luego, verificamos si una determinada clave existe en el diccionario.
# Si la clave no está presente, lanzamos la excepción KeyErrorException con un mensaje personalizado.
# De lo contrario, accedemos al valor correspondiente y lo imprimimos. Si se captura la excepción KeyErrorException, 
# imprimimos un mensaje de error personalizado con el mensaje proporcionado en la excepción.