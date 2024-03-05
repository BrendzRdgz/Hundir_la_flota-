from variables import*
from funciones import*
import os

if __name__ == "__main__":

    genera_barco(tablero_1.tablero_humano)
    genera_barco_maquina(tablero_1.tablero_maquina)
    
    print('Lo primero de todo, ¿cómo están los máquinas?')
    print('Me llamo David Bisbal, campeón de Andalucía de hundir la flota, encantao de conocerle')
    print('Te dejo que empieces primero, un poco de ventaja no te vendrá mal...')

    while juego_activo:
        print(lista_de_barcos_maquina)
        juego_activo = disparar(tablero_1.tablero_maquina, tablero_1.tablero_humano_reflejo)
        juego_activo = disparar_maquina(tablero_1.tablero_humano, juego_activo)
        #os.system('clear')
