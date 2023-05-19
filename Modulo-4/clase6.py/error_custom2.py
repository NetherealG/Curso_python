class NoPuedeEscribirDosException(Exception):
    def __init__(self, _value):
        self.value = _value
try:
    number = input("Introduce un numero: ")
    if (number == "2"): 
       raise  NoPuedeEscribirDosException("Introdujo un numero dos y este no es valido")
    else:
        print("Numero introducido correctamente")
except Exception as error:
    print(type(error))
    print(error.args)