jugador1 = input("Jugador1, elige piedra, papel o tijera")
jugador2 = input("Jugador2, elige piedra, papel o tijera")


if jugador1 == jugador2:
    print("¡Es un empate!")
elif (jugador1 == "piedra" and jugador2 == "tijera") or \
     (jugador1 == "papel"  and jugador2 == "piedra") or \
     (jugador1 == "tijera" and jugador2 == "papel"):
    print("¡Jugador 1 gana!")
else:
    print("¡Jugador 2 gana!")
