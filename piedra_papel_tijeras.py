nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

salir = False

while not salir:
    jugador1 = input("¡Hola " + nombre1 + "! ¿Qué eliges? ¿piedra, papel o tijeras?: ").lower().strip()
    jugador2 = input("¡Hola " + nombre2 + "! ¿Qué eliges? ¿piedra, papel o tijeras?: ").lower().strip()

    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

    if jugador1 == jugador2:
        print("¡Es un empate!")
    elif condicion1 or condicion2 or condicion3:
        print("¡" + nombre1 + " has ganado!")
    else:
        print("¡" + nombre2 + " has ganado!")
    
    quierosalir = input("¿Desea salir? si/no: ").lower().strip()
    if quierosalir == "si":
        salir = True
