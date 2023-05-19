class SumaNumbers:
    def encontrar_numbers(self, _numbers, _goal):
        numberslist = []
        element_see = {} #

        for i, number in enumerate(_numbers): #
            complement = _goal - number

            if complement in element_see:
                numberslist.append((element_see[complement], i))

            element_see[number] = i #

        if len(numberslist) == 0:
            raise ValueError("No se encontraron elementos que cumplan con la condición.")

        return numberslist

# Ingresar los números como una lista separada por comas
_numbers = input("Ingrese los números separados por comas: ").split(",")
_numbers = [int(num.strip()) for num in _numbers]

# Ingresar el objetivo
_goal = int(input("Ingrese el objetivo: "))

# Crear una instancia de la clase BuscadorPares
buscador = SumaNumbers()

# Encontrar pares cuya suma sea igual al objetivo
try:
    number_encontrados = buscador.encontrar_numbers(_numbers, _goal)
    # Imprimir los pares encontrados
    for numb in number_encontrados:
        print(f"numeros  encontrado: (índice  {numb[0]}) y  (índice  {numb[1]})") #
except ValueError as error:
    print(error)
