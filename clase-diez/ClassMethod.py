class Employer:
    Sueldo_base = 100.000
    
    def __init__(self, _name):
        self.__name = _name
        
    @property
    def name (self):
        return self.__name
    
    @name.setter
    def name(self, _name):
        self.__name = _name
        
