import numpy as np
import random
#from funciones import crear_tablero
#from tablero import Tablero


"""
Para este juego los barcos se colocan de manera aleatoria.
Ahora bien, puedes empezar colocando los barcos en unas posiciones fijas, que no cambien con cada partida,
y después implementarlo aleatoriamente, ya que es más complejo. Los barcos son:

  -  4 barcos de 1 posición de eslora
  -  3 barcos de 2 posiciones de eslora
  -  2 barcos de 3 posiciones de eslora
  -  1 barco de 4 posiciones de eslora
"""



def coloca_barco(tablero, barco):
    for pieza in barco:
        tablero[pieza] = "O"


def genera_barco(tablero):
    num_filas = tablero.shape[0]
    num_columnas = tablero.shape[1]
    orientaciones = ["N","S","O","E"]
    
    barcos_generados = 0
    
    while barcos_generados < 10: # Generar 10 barcos en total
        if barcos_generados < 1:  # Generar barco de 4 posiciones
            longitud = 4
        elif barcos_generados < 3:  # Generar barcos de 3 posiciones
            longitud = 3
        elif barcos_generados < 6:  # Generar barcos de 2 posiciones
            longitud = 2
        else:  # Generar barcos de 1 posición
            longitud = 1

        orientacion = random.choice(orientaciones)
        origen = (random.randint(0, num_filas - 1), random.randint(0, num_columnas - 1))

        fila = origen[0]
        columna = origen[1]
        barco = []
        if tablero[origen] != "O" and tablero[origen] != "X":
            barco.append(origen)
            for _ in range(longitud - 1):
                if orientacion == "N":
                    fila -= 1
                elif orientacion == "S":
                    fila += 1
                elif orientacion == "E":
                    columna += 1
                else:
                    columna -= 1

                if fila >= num_filas or fila < 0 or columna >= num_columnas or columna < 0:
                    break

                if tablero[fila, columna] == "O" or tablero[fila, columna] == "X":
                    break

                barco.append((fila, columna))

            if len(barco) == longitud:
                coloca_barco(tablero, barco)
                barcos_generados += 1

    return barcos_generados        
                

tamano_tablero = (10, 10)
tablero = np.full(tamano_tablero, " ", dtype=str)

print("Tablero inicial:")
for fila in tablero:
    print("['{}']".format("' '".join(fila)))

print("\nGenerando barcos específicos de forma aleatoria:")
genera_barco(tablero)

print("\nTablero después de colocar los barcos:")
for fila in tablero:
    print("['{}']".format("' '".join(fila)))
