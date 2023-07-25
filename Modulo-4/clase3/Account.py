class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    def __str__(self):
        return f"Titular: {self.titular}\nCantidad: {self.cantidad}"


class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
        
    def heredar_datos(self, cuenta):
        self.titular = cuenta.titular
        self.cantidad = cuenta.cantidad
        
    def mostrar_informacion(self):
        print("Información de Caja de Ahorro")
        print(self)
        

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes
        
    def obtener_interes(self):
        return (self.cantidad * self.interes) / 100
    
    def mostrar_informacion(self):
        print("Información de Plazo Fijo")
        print(self)
        print(f"Plazo: {self.plazo} días")
        print(f"Interés: {self.interes}%")
        print(f"Interés Total: {self.obtener_interes()}")
    
# Crear objetos de CajaAhorro y PlazoFijo
ca = CajaAhorro("Juan Perez", 5000)
pf = PlazoFijo("Pedro Gomez", 10000, 30, 5)

# Mostrar información de CajaAhorro
ca.mostrar_informacion()

# Mostrar información de PlazoFijo
pf.mostrar_informacion()
