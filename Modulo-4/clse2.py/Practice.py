avion = {
    "model" : "Airbus 470",
    "año_fab" : 2012,
    "peso_max": 54320.2,
    "asientos":{
        "num":230
    },
    "disp_fly" : True,
    "Time_fly" : [2.5 , 4,0 , 5.0, 1,5]
}   
print("cantidad asientos:", avion["asientos"]["num"])
avion["asientos"]["num"] = 100
print("cantidad asientos:", avion["asientos"]["num"], ", 130 asientos ya fueron ocupados")

print("Disponibilidad de vuelo:", avion["disp_fly"])
avion["disp_fly"] = False
print("Disponibilidad de vuelo:", avion["disp_fly"],", Nuestro servicio de vuelos se encuentra temporalmente suspendido")
print("tiempos de vuelo ?:", avion["Time_fly"])
avion["Time_fly"] = [2.0 , 3.0 , 4.0 , 1.0] 
print("tiempos de vuelo ?:", avion["Time_fly"], " , Los tiempos de vuelo fueron acortados debido a la nueva tecnología implementada recientemente")









