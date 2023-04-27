# manufacturer(philidor)
# screen_size(float)
# num_cores()
# apps(list)
#status (false:off, true:on)


class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.apps = []
        self.status = False
        self.num_cores = num_cores
        
    def power_on(self):
        self.status = True 
         
    def power_off(self):
        self.status = False
    
    def install_app(self, app):
        self.apps.append(app)
        print("Installing", app, "was successful")
       
    def uninstall_app(self, app):
        if app in self.apps:
            self.apps.remove(app)
            print("The app was uninstalled successfully")

mobile = MobilePhone('philidor', '6.5 pulgadas', '9 núcleos')
print("Especificaciones tecnicas:", mobile.manufacturer, mobile.screen_size, mobile.num_cores)

mobile.install_app("Facebook")
mobile.install_app("Instagram")
print(mobile.apps)

mobile.uninstall_app("Facebook")
print(mobile.apps)

  