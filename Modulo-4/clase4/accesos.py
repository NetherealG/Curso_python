class Empleado:
    sueldo = 0
    
    def __init__(self, _name) -> None:
        self.name = _name

persona = Empleado("Juan Perez")
print(persona.name)



class EmpleadoProtected:
    sueldo = 0
    
    def __init__(self, _name) -> None:
        self.__name = _name
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, _name):
        self.__name = _name
    
persona2 = EmpleadoProtected("Nico")
print(persona2.name)

persona2.name ="alexa"
print(persona2.name)