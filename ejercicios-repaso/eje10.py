Edad_min = 16
Ing_tope = 1000

User_age = float(input("Edad usuario: "))
Ing_mens = float(input("Ingreso mensual: "))

if User_age < Edad_min:
    print("El usuario es demasiado joven para pagar impuestos.")
else:
    if Ing_mens >= Ing_tope:
        print("Debe pagar impuesto.")
    else:
        print("No debe pagar impuesto.")
