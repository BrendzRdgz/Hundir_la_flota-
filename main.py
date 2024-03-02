import numpy as np
#import random

from variables import*
from funciones import*

if __name__ == "__main__":

    lista_de_barcos = genera_barco(tablero_1.tablero_humano)    
    lista_de_barcos_maquina = genera_barco_maquina(tablero_1.tablero_maquina)
    print(lista_de_barcos_maquina)

    print('Máquina, lo primero de todo, ¿cómo estás?')
    print('Soy David Bisbal, campeón de Andalucía de hundir la flota, encantao')
    print('Te dejo que empieces primero, un poco de ventaja no te vendrá mal...')

    while juego_activo == True:
        disparar(tablero_1.tablero_maquina, tablero_1.tablero_humano_reflejo, barcos_hundidos)

        disparar_maquina(tablero_1.tablero_humano, barcos_hundidos_maquina)
