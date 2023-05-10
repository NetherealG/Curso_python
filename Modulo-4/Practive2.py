list_carb = {
    "Menu1": "Porotos granados",
    "Menu2": "Salpicón",
    "Menu3": "Cereal con leche",
    "Menu4": "Arroz con verduras",
    "Menu5": "Lentejas"
}

list_prot = {
    "Menu1": "Pescado a la plancha",
    "Menu2": "Huevos cocidos",
    "Menu3": "Asado carnicero",
    "Menu4": "Ensalada de almendras con pollo"
}

list_fib = {
    "Menu1": "Mix de verduras",
    "Menu2": "Alcachofa con limoncito",
    "Menu3": "Lechuga rellena xd"
}

User_Weight = float(input("Ingrese su peso: "))

if 60 <= User_Weight <= 70:
    print("Recomiendo esta dieta alta en carbohidratos:")
    for key, value in list_carb.items():
        print(f"{key}: {value}")
elif 70 < User_Weight <= 80:
    print("Recomiendo esta dieta alta en proteínas:" )
    for key, value in list_prot.items():
        print(f"{key}: {value}")
elif User_Weight > 80:
    print("Recomiendo esta dieta alta en fibras:")
    for key, value in list_fib.items():
        print(f"{key}: {value}")
