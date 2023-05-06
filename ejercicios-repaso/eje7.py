Interes = 0.04

Monto_incial = float(input("Cual es tu monto inicial ?: "))

Saldo_año1 = (Monto_incial * Interes) + Monto_incial
Saldo_simply1 = round(Saldo_año1,2)
print("El interes anual sumado al año 1 es : ", Saldo_simply1)
Saldo_año2 = (Saldo_simply1 * Interes) + Saldo_simply1
Saldo_simply2 = round(Saldo_año2,2)
print("El interes anual sumado al año 2 es : ", Saldo_simply2)
Saldo_año3 = (Saldo_año2 * Interes) + Saldo_año2
Saldo_simply3 = round(Saldo_año3,2)
print("El interes anual sumado al año 3 es : ", Saldo_simply3)
