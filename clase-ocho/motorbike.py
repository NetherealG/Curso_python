class Motorbike:
    is_new = True
    def __init__(self,_color , _matricula, _combustible_litros, _numeroruedas, _marca, _modelo,
                 _fecha_fabricacion, _velocidad_punta, _peso):
        self.color= _color
        self.matricula= _matricula
        self.comb_lts= _combustible_litros
        self.numruedas= _numeroruedas
        self.marca= _marca
        self.model= _modelo
        self.Fabdate= _fecha_fabricacion
        self.velocityPeak= _velocidad_punta
        self.height= _peso
        self.PowOn = False
        
    def arrancar(self):
        if not self.PowOn:
            self.PowOn = True
            print("La motocicleta ha sido encendida.")
        else:
            print("La motocicleta ya estaba encendida.")
    
    def detener(self):
        if self.PowOn and self.velocityPeak == 0:
            self.PowOn = False
            print("La motocicleta ha sido apagada.")
        elif not self.PowOn:
            print("La motocicleta ya estaba apagada.")


    
        
    
        