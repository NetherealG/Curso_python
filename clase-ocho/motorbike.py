class Motorbike:
    is_new = True
    PowOn= False
    def __init__(self,_color , _matricula, _combustible_litros, _numeroruedas, _marca, _modelo,
                 _fecha_fabricacion, _velocidad_punta, _peso, _combustible_maximo):
        self.color= _color
        self.matricula= _matricula
        self.comb_lts= _combustible_litros
        self.numruedas= _numeroruedas
        self.marca= _marca
        self.model= _modelo
        self.Fabdate= _fecha_fabricacion
        self.velocityPeak= _velocidad_punta
        self.height= _peso
        self.combMax = _combustible_maximo
        
   # if self.variable == False == if not self.variable
   # if self.varible == True: == if self.variable      
    def arrancar(self):
        if not self.PowOn:
            print("La motocicleta está en marcha.")
            
        else:
            print("La motocicleta ya estaba en marcha.")
            
    
    def detener(self):
        if self.PowOn == False:
            print("La motocicleta ya estaba apagada.")
        else:
            print("La motocicleta ha sido apagada.")
    
    def consulta_price(self):
        print(f"el precio de la motocicleta {self.marca} {self.model} es de $ {self.price}.")
    
    def comprobar_deposito(self):
        print(f"--->REPORTE DE DEPÓSITO DE {self.marca} {self.model}<---")
        print(f"El depósito tiene {self.comb_lts} litros.")
        print(f"La capacidad máxima del tanque de combustible es de {self.combMax}.")
        print(f"Faltan {self.combMax - self.comb_lts} litros para llenar el depósito.")
        print(f"--->FIN DEL REPORTE<---\n")
        
    def repostar(self):
        while True:
            self.repostar_litros = float(input("Por favor, introduzca la cantidad de litros que desea repostar:\n"))
            
            if self.comb_lts + self.repostar_litros <= self.combMax:
                print("Repostaje exitoso.")
                print(f"Se han repostado {self.repostar_litros} litros.")
                self.comb_lts += self.repostar_litros 
                print(f"El depósito tiene {self.comb_lts} litros de combustible.")
                break
            else:
                print("No cabe tanto combustible. ¿Quieres encharcar el concesionario?")
    


Motorbike1 = Motorbike("negro","EFC-950",10, 2,"BMW", "BMW300Ex", "25/04/2023",290, 199, 18)
Motorbike2 = Motorbike(
    _marca = "Renegade",
    _modelo = "Renegade-Commando",
    _color = "negro",
    _numeroruedas = 2,
    _peso = 200,
    _matricula = "FX34K8",
    _combustible_litros = 0,
    _velocidad_punta = 320,
    _fecha_fabricacion = "25/04/2023",
    _combustible_maximo = 20   
)

Motorbike1.arrancar()
Motorbike1.detener()

Motorbike1.price = 3000000
Motorbike2.price = 4000000
print(f"el precio de la motocicleta {Motorbike1.marca} {Motorbike1.model} es de $ {Motorbike1.price}.")

Motorbike1.consulta_price()
Motorbike2.consulta_price()

Motorbike1.comprobar_deposito()
Motorbike2.comprobar_deposito()

Motorbike1.repostar()
Motorbike2.repostar()
Motorbike1.comprobar_deposito()
Motorbike2.comprobar_deposito()


