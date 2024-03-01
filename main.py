import numpy as np
import random

from variables import *
from FUNCIONES_2 import *

#print(tablero_1)

genera_barco(tablero_1.tablero_humano)
genera_barco(tablero_1.tablero_maquina)
disparar(tablero_1.tablero_maquina, tablero_1.tablero_humano_reflejo)

print(tablero_1)

#if __name__ == "__main__":
#    print('Máquina, te dejo que empieces primero, un poco de ventaja no te vendrá mal...')
#    juego_activo = True
#    while juego_activo == True:
#    #input para introducir las coords de disparo
#        disparar(tablero_1.tablero_maquina)
#        comprobar_victoria(tablero_1.tablero_maquina)
#
#        disparar_maquina(tablero_1.tablero_humano)
#        comprobar_victoria_maquina(tablero_1.tablero_humano)
