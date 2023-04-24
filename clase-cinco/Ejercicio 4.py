#Ejercicio 4
def calculo_trimestre():
    '''1-3, 4-6, 7-9, 10-12'''
    mes = int(input("Ingrese número del mes(1-12): "))
    
    if mes >= 1 and mes <= 3: #esta es la primer trimestre
        trimestre = 1
        
    elif mes >= 4 and mes <= 6: #este es el segundo trimestre
        trimestre = 2
        
    elif mes >= 7 and mes <= 9: #este es el tercer trimestre
        trimestre = 3
        
    elif mes >= 10 and mes <= 12:
    #este es el cuarto trimestre
        trimestre = 4
        
    else:
        print("Ingrese un número válido")
    
    if mes >= 1 and mes <= 12:
        print("el mes ", mes, "pertenece al trimestre: ", trimestre)
        
calculo_trimestre()  