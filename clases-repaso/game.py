import random

print("¡La pelea ha iniciado!")

vida_minima = 5000
vida_maxima = 15000
ataque_minimo = 100
ataque_maximo = 5000
probabilidad_fallo = 0.5
probabilidad_critico = 0.1
danio_critico = 20000

jugador_a_vida = random.randint(vida_minima, vida_maxima)
jugador_b_vida = random.randint(vida_minima, vida_maxima)
jugador_a_ataque = random.randint(ataque_minimo, ataque_maximo)
jugador_b_ataque = random.randint(ataque_minimo, ataque_maximo)

if random.random() < 0.5:
    atacante = 'A'
else:
    atacante = 'B'

while jugador_a_vida > 0 and jugador_b_vida > 0:
    if atacante == 'A':
        # probabilidad de fallar o hacer un golpe crítico
        probabilidad = random.random()
        if probabilidad <= probabilidad_fallo:
            print("Jugador A falló su ataque")
        elif probabilidad <= probabilidad_fallo + probabilidad_critico:
            jugador_b_vida -= jugador_a_ataque * danio_critico
            print("¡Jugador A hizo un golpe crítico! Jugador B perdió %d puntos de vida" % (jugador_a_ataque * danio_critico))
        else:
            jugador_b_vida -= jugador_a_ataque
            print("Jugador A atacó a Jugador B, Jugador B perdió %d puntos de vida" % jugador_a_ataque)
    else:
        probabilidad = random.random()
        if probabilidad <= probabilidad_fallo:
            print("Jugador B falló su ataque")
        elif probabilidad <= probabilidad_fallo + probabilidad_critico:
            jugador_a_vida -= jugador_b_ataque * danio_critico
            print("¡Jugador B hizo un golpe crítico! Jugador A perdió %d puntos de vida" % (jugador_b_ataque * danio_critico))
        else:
            jugador_a_vida -= jugador_b_ataque
            print("Jugador B atacó a Jugador A, Jugador A perdió %d puntos de vida" % jugador_b_ataque)

    if atacante == 'A':
        atacante = 'B'
    else:
        atacante = 'A'

if jugador_a_vida <= 0:
    print("Jugador B ganó")
else:
    print("Jugador A ganó")
