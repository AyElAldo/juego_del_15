import random
import heapq

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print("\t\t\t","_"* 19)
    for fila in tablero:
        print("\t\t\t|"," | ".join(map(str, fila)),"|")
        print("\t\t\t|","_"* 17,"|")

# Función para encontrar las coordenadas del espacio en blanco
def encontrar_espacio_en_blanco(tablero):
    for i in range(4):
        for j in range(4):
            if tablero[i][j] == "  ":
                return (i, j)

# Función para verificar si se ha ganado el juego
def juego_ganado(tablero):
    if tablero[0][0]=="1 " and tablero[0][1]=="2 " and tablero[0][2]=="3 " and tablero[0][3]=="4 " \
        and tablero[1][0]=="5 " and tablero[1][1]=="6 " and tablero[1][2]=="7 " and tablero[1][3]=="8 " \
        and tablero[2][0]=="9 " and tablero[2][1]=="10" and tablero[2][2]=="11" and tablero[2][3]=="12" \
        and tablero[3][0]=="13" and tablero[3][1]=="14" and tablero[3][2]=="15":
        imprimir_tablero(tablero)
        return True

# Función para calcular el costo total (f) en el algoritmo A*
def calcular_costo_total(tablero, movimientos_realizados):
    costo_heuristico = 0
    for i in range(4):
        for j in range(4):
            if tablero[i][j] != "  ":
                numero = int(tablero[i][j])
                
                objetivo_x, objetivo_y = (numero - 1) // 4, (numero - 1) % 4
                # Suma todas las distancias como heurística.
                costo_heuristico += abs(i - objetivo_x) + abs(j - objetivo_y)
    return len(movimientos_realizados) + costo_heuristico

# Implementa el algoritmo A*
def resolver_juego(tablero):
    # Define las direcciones de movimiento
    direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    movimientos = ["derecha", "abajo", "izquierda", "arriba"]
    
    # Utiliza una cola de prioridad para almacenar los estados a explorar
    cola_prioridad = [(calcular_costo_total(tablero, []), tablero, [])]

    while cola_prioridad:
        _, estado_actual, movimientos_realizados = heapq.heappop(cola_prioridad)
        imprimir_tablero(estado_actual)
        if juego_ganado(estado_actual):
            print("¡Felicidades! ¡Has ganado el juego del 15!")
            #imprimir_tablero(estado_actual)
            print("Movimientos realizados: ")
            for mov in movimientos_realizados:
                print(mov)
            return

        espacio_x, espacio_y = encontrar_espacio_en_blanco(estado_actual)

        for direccion, movimiento in zip(direcciones, movimientos):
            nueva_x, nueva_y = espacio_x + direccion[0], espacio_y + direccion[1]

            if 0 <= nueva_x < 4 and 0 <= nueva_y < 4:
                nuevo_tablero = [fila[:] for fila in estado_actual]
                nuevo_tablero[espacio_x][espacio_y], nuevo_tablero[nueva_x][nueva_y] = nuevo_tablero[nueva_x][nueva_y], nuevo_tablero[espacio_x][espacio_y]
                nuevo_movimientos = movimientos_realizados + [movimiento]
                heapq.heappush(cola_prioridad, (calcular_costo_total(nuevo_tablero, nuevo_movimientos), nuevo_tablero, nuevo_movimientos))
                
                
# Función para mezclar el tablero
def mezclar_tablero(tablero, movimientos):
    for _ in range(movimientos):
        espacio_x, espacio_y = encontrar_espacio_en_blanco(tablero)
        movimientos_posibles = []

        if espacio_x > 0:
            movimientos_posibles.append("arriba")
        if espacio_x < 3:
            movimientos_posibles.append("abajo")
        if espacio_y > 0:
            movimientos_posibles.append("izquierda")
        if espacio_y < 3:
            movimientos_posibles.append("derecha")

        movimiento = random.choice(movimientos_posibles)

        if movimiento == "arriba":
            tablero[espacio_x][espacio_y], tablero[espacio_x - 1][espacio_y] = tablero[espacio_x - 1][espacio_y], tablero[espacio_x][espacio_y]
        elif movimiento == "abajo":
            tablero[espacio_x][espacio_y], tablero[espacio_x + 1][espacio_y] = tablero[espacio_x + 1][espacio_y], tablero[espacio_x][espacio_y]
        elif movimiento == "izquierda":
            tablero[espacio_x][espacio_y], tablero[espacio_x][espacio_y - 1] = tablero[espacio_x][espacio_y - 1], tablero[espacio_x][espacio_y]
        elif movimiento == "derecha":
            tablero[espacio_x][espacio_y], tablero[espacio_x][espacio_y + 1] = tablero[espacio_x][espacio_y + 1], tablero[espacio_x][espacio_y]

# Inicializar el tablero
tablero = [["1 ", "2 ", "3 ", "4 "], ["5 ", "6 ", "7 ", "8 "], ["9 ", "10", "11", "12"], ["13", "14", "15", "  "]]

# Mezclar el tablero
mezclar_tablero(tablero, 50)
#imprimir_tablero(tablero)

# Resolver el juego utilizando A*
resolver_juego(tablero)
