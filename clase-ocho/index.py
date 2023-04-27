
class animal:
    def __init__(self, name , type):
        self.name= name
        self.type= type

gato = animal ( "Angora" , "Persa")
print (gato.type)

gato.type= ("Grandanes")
print (gato.type)

print ("\n ******************** \n ")
class Droid:
    def __init__(self, name):
        self.hidden_name = name
        
    @property
    def name(self) -> str:
        return self.hidden_name
    
    @name.setter
    def name(self, name: str) -> None:
        self.hidden_name = name
              

android = Droid ("arthur")

print(android.name)
android.name ="C3PO"
print(android.name)

android.hidden_name = "Rojo"
print(android.hidden_name)
print(android.name)

print ("\n ******************** \n ")

class CalculatedValue:
    def __init__(self, _name, _height):
        self.name = _name
        self.height = _height
        
    @property
    def get_calculate_value(self) -> float:
        return 0.35 * self.height
    
valuex = CalculatedValue("ratio", 10)

print (f'El {valuex.name} es: {valuex.get_calculate_value}')

print ("\n ******************** \n ")

class Guns:
    can_shoot= True
    def __init__(self, _name):
        self.name = _name
        
gun_one = Guns("ak47")
gun_two =  Guns("m4a1")
gun_three = Guns("famas")

print(f'{gun_one.name} puede disparar en rafaga?:{gun_one.can_shoot}')
print(f'{gun_two.name} puede disparar en rafaga?:{gun_two.can_shoot}')
print(f'{gun_three.name} puede disparar en rafaga?:{gun_three.can_shoot}')

print ("\n ******************** \n ")

gun_one.can_shoot = True

print(f'{gun_one.name} puede disparar en rafaga?:{gun_one.can_shoot}')
print(f'{gun_two.name} puede disparar en rafaga?:{gun_two.can_shoot}')
print(f'{gun_three.name} puede disparar en rafaga?:{gun_three.can_shoot}')

print ("\n ******************** \n ")

Guns.can_shoot = False
print(f'{gun_one.name} puede disparar en rafaga?:{gun_one.can_shoot}')
print(f'{gun_two.name} puede disparar en rafaga?:{gun_two.can_shoot}')
print(f'{gun_three.name} puede disparar en rafaga?:{gun_three.can_shoot}')


