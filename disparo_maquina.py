import numpy as np
import random

def dispara(tablero,coordenada):
    if tablero[coordenada]==' ':
        print("Disparo ha hecho agua!")
        tablero[coordenada]='-'
    elif tablero[coordenada]=='O':
        print("Tocado!")
        tablero[coordenada]='X'
    else: 
        pass


def terminator(random.randint(3, 9),2)

coordenadas = []
coordenadas.append(random.randint(0,tablero))
coordenadas.append(random.randint(0,tablero))
print(coordenadas)
print(type(tablero))
dispara(tablero,coordenadas)
