class Transporte:
    pass

class BuzzeLightyear:
    pass
bozz1 = BuzzeLightyear()
bozz2 = BuzzeLightyear()

#instanciar la clase y crear un objeto
transporte1= Transporte()
transporte2= Transporte()

print(type(transporte1))
print(type(bozz1))

class Droid:
    def switch_on(self):
        print ("hola soy un droid, y estoy a tu orden")
        self.power_on = True 
    def switch_off(self):
        print("adios, enciendeme cuando me necesites")
        self.power_on = False
        
k8_arthur = Droid()
k8_tripio = Droid()
    
k8_arthur.switch_on()
print("power on arthur:", k8_arthur.power_on) 
k8_tripio.switch_off()
print("power on citripio:", k8_tripio.power_on) 
k8_arthur.switch_off()
print(k8_arthur.power_on)  


  
