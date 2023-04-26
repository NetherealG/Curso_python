# manufacturer(philidor)
# screen_size(float)
# num_cores()
# apps(list)
#status (false:off, true:on)


class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.apps =[]
        self.status= False
        self.num_cores = num_cores
        
    def power_on(self):
        self.power_on = True 
         
    def power_off(self):
        self.power_on = False
    
    def install_app(self,app):
        self.apps.append(app)
    def unistall_app(self, app):
        if app in self.apps:
            self.apps.remove(app)
            
mobile = MobilePhone ('philidor','6 pulgadas', '9')
print("Especificaciones tecnicas", mobile.manufacturer , mobile.screen_size, mobile.num_cores)    
        
        
  