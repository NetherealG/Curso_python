import random

print("¡La pelea ha iniciado!")

vida_minima = 500
vida_maxima = 600

vida_jugador_a = random.randint(vida_minima, vida_maxima)
vida_jugador_b = random.randint(vida_minima, vida_maxima)

print("Infernape tiene", vida_jugador_a, "puntos de vida.")
print("Blaziken tiene", vida_jugador_b, "puntos de vida.")

# Variable para determinar qué jugador inicia atacando
jugador_actual = random.choice(["Infernape", "Blaziken"])

# Variables para almacenar la cantidad de vida actual de cada jugador
vida_actual_jugador_a = vida_jugador_a
vida_actual_jugador_b = vida_jugador_b

# Ciclo para realizar la pelea
while vida_actual_jugador_a > 0 and vida_actual_jugador_b > 0:
    # Determinar la cantidad de puntos de ataque del jugador actual
    puntos_ataque = random.randint(60, 120)
    
    # Determinar si el ataque es un golpe crítico o si falla
    if random.random() < 0.2:
        puntos_ataque *= 2
        print("¡Golpe crítico!")
    elif random.random() < 0.2:
        puntos_ataque = 0
        print("¡Ataque fallado!")

    # Determinar el jugador que va a defender
    if jugador_actual == "Infernape":
        jugador_defensor = "Blaziken"
        vida_actual_jugador_defensor = vida_actual_jugador_b
    else:
        jugador_defensor = "Infernape"
        vida_actual_jugador_defensor = vida_actual_jugador_a

    print("", jugador_actual, "ataca a ", jugador_defensor, "con", puntos_ataque, "puntos de ataque.")

    # Calcular la cantidad de vida restante después del ataque
    vida_actual_defensor = vida_actual_jugador_defensor - puntos_ataque
    if vida_actual_defensor < 0:
        vida_actual_defensor = 0

    # Actualizar la cantidad de vida actual del jugador defensor
    if jugador_defensor == "Infernape":
        vida_actual_jugador_a = vida_actual_defensor
    else:
        vida_actual_jugador_b = vida_actual_defensor

    print("Infernape tiene", vida_actual_jugador_a, "puntos de vida.")
    print("Blaziken tiene", vida_actual_jugador_b, "puntos de vida.")

    # Cambiar el jugador actual para el siguiente turno
    if jugador_actual == "Infernape":
        jugador_actual = "Blaziken"
    else:
        jugador_actual = "Infernape"

# Determinar al ganador
if vida_actual_jugador_a == 0:
    print("¡Blaziken ha ganado!")
else:
    print("¡Infernape ha ganado!")
