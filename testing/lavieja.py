#Función para dibujar el tablero del juego
# Fuente tomada del chatgpt
def dibujar_tablero(tablero):
    print(tablero[0] + "|" + tablero[1] + "|" + tablero[2])
    print("-" * 5)
    print(tablero[3] + "|" + tablero[4] + "|" + tablero[5])
    print("-" * 5)
    print(tablero[6] + "|" + tablero[7] + "|" + tablero[8])

#Función para verificar si un jugador ha ganado
def verificar_ganador(tablero, jugador):
    if (
        (tablero[0] == jugador and tablero[1] == jugador and tablero[2] == jugador) or
        (tablero[3] == jugador and tablero[4] == jugador and tablero[5] == jugador) or
        (tablero[6] == jugador and tablero[7] == jugador and tablero[8] == jugador) or
        (tablero[0] == jugador and tablero[3] == jugador and tablero[6] == jugador) or
        (tablero[1] == jugador and tablero[4] == jugador and tablero[7] == jugador) or
        (tablero[2] == jugador and tablero[5] == jugador and tablero[8] == jugador) or
        (tablero[0] == jugador and tablero[4] == jugador and tablero[8] == jugador) or
        (tablero[2] == jugador and tablero[4] == jugador and tablero[6] == jugador)
    ):
        return True
    else:
        return False

#Función para jugar el juego
def jugar():
    tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    jugador = "X"

    while True:
        dibujar_tablero(tablero)
        movimiento = int(input("Es el turno del jugador " + jugador + ". Ingresa el número de la posición donde deseas jugar (1-9): "))
        if tablero[movimiento - 1] != " ":
            print("Posición ocupada. Intenta nuevamente.")
            continue
        tablero[movimiento - 1] = jugador

        if verificar_ganador(tablero, jugador):
            dibujar_tablero(tablero)
            print("¡El jugador " + jugador + " ha ganado!")
            break

        if " " not in tablero:
            dibujar_tablero(tablero)
            print("¡Empate!")
            break

        jugador = "O" if jugador == "X" else "X"

#Iniciar el juego
jugar()