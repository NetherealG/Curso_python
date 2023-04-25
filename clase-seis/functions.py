def saludar (name):
    print (f'Hola {name}!!')


def saludar_dos(first_name, last_name):
    print (f'Hola {first_name}, {last_name}!!')


def mul_text(texto, multiplier= 2):
    print(texto * multiplier)

def varieltal (param1, param2, *others):
    print(param1)
    print(param2)
    print(others)  
def varieltal_dos (param1,  **others):
    print(param1)
    print(others) 


saludar('Alexa')
saludar('nicolas')

saludar_dos(last_name='soto', first_name='nico')
    
mul_text("V", 5)

mul_text("X")

print("\n-----------------\n")
varieltal("1A", "2B", 0, "XX", [0, 1])

print("\n-----------------\n")
varieltal_dos ("1A", id=0, name='nicolas')