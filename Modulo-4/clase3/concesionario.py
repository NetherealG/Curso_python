class Vehiculos:
    def __init__(self, _color, _ruedas, _tipo_freno):
        self.color = _color
        self.ruedas = _ruedas
        self.tipo_freno = _tipo_freno
    
    def frenar(self):
        print ("este vehiculo está frenando")

class VehiculosMotorizados:
    def __init__(self, _tipo_motor, _tipo_encendido):
        self.tipo_motor = _tipo_motor
        self.tipo_encendido = _tipo_encendido


class Auto(Vehiculos, VehiculosMotorizados):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_motor, _tipo_encendido):
        Vehiculos.__init__(_color, _ruedas, _tipo_freno)
        VehiculosMotorizados.__init__(self, _tipo_motor, _tipo_encendido)

    
    def abrir_puerta(self,_puerta):
        print (f'abriendo puerta {_puerta}')
    
class Moto(Vehiculos, VehiculosMotorizados):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_motor, _tipo_encendido, _tipo_cadena):
        super().__init__(_color, _ruedas, _tipo_freno)
        VehiculosMotorizados.__init__(self, _tipo_motor, _tipo_encendido)
        self.tipo_cadena = _tipo_cadena
    
    
class Bicicleta(Vehiculos):
    def __init__(self, _color, _ruedas, _tipo_freno, _tipo_manubrio):
        super().__init__(_color, _ruedas, _tipo_freno)
        self.tipo_manubrio = _tipo_manubrio
    
    def pedalear(self, sentido):
        print("La bicicleta está siendo pedaleada hacia {sentido}")
