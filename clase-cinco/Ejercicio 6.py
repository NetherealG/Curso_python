#6. Se le asignado un tarea para programar un algoritmo para una lavadora, debe investigar cuanta agua se neceita para lavar prendas
#con las siguientes caracteriticas, algodon, nilon, poliester, debe investigar para una lavadora de xx kg cuantas prendas de cada una puede 
#lavar entendiendo, que solo se puede lavar ropa de un mismo tipo y asi poder calcular lo siguiente

#Por ejemplo, si la carga es 10, la cantidad de agua que requiere es 5 y la cantidad de ropa a lavar es 14, entonces necesitas 5 * 1.1 ^ 
#(14 - 10) cantidad de agua.

#Escribe una función para calcular cuánta agua se necesita si tienes una cantidad de ropa.
#La función aceptará 2 argumentos: - carga lavadora, cantidad ropa, tipo de prenda (agg al final)
#Se puede lavar un solo tipo de prenda al mismo tiempo.

def cantAgua(cap_lav, cant_ropa):
    while cant_ropa <= 0 or cap_lav <= 0:
        print("Capacidad de carga y cantidad de ropa deben ser mayores a 0Kg")
        cap_lav = float(input("Ingresar capacidad de carga de la lavadora en Kg: "))
        cant_ropa = float(input("Ingresar cantidad de ropa en Kg: "))

    rel_ropa_lav = cant_ropa / cap_lav
    while rel_ropa_lav > 0.8:
        print("Excede la cantidad de ropa recomendable para lavar en una carga, por favor, disminuir carga")
        cap_lav = float(input("Ingresar capacidad de carga de la lavadora en Kg: "))
        cant_ropa = float(input("Ingresar cantidad de ropa en Kg: "))

    tipo_ropa = input("Ingresar tipo de ropa a lavar: ")
    if tipo_ropa == "algodon":
        fact_agua = 1.1
    elif tipo_ropa == "nylon" or tipo_ropa == "poliester":
        fact_agua = 1.05
    else:
        print("Solo se puede lavar ropa de tipo algodón, nylon o poliester")
    
    cant_agua = cap_lav*fact_agua*cant_ropa
    return cant_agua  

carga_lav = float(input("Ingresar capacidad de carga de la lavadora en Kg: "))
kg_ropa = float(input("Ingresar cantidad de ropa en Kg: "))
agua_neces = cantAgua(carga_lav, kg_ropa)
print("La cantidad de agua necesaria para lavar es:", agua_neces, "L")