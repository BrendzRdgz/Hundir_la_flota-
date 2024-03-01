from tablero import*
from variables import*

import numpy as np
import random

def crear_tablero(x = None, y = None):

    dimensiones = (x, y)
    
    if dimensiones != (None, None):
        dimensiones = (x+1, y+1)
        tablero = Tablero(dimensiones)
    else:
        tablero = Tablero()

    print(tablero)
    return tablero

def coordenada_a_num(coord):
    while True:
        disparo = [char for char in coord]
        if disparo[1] in abecedario or (disparo[2] in abecedario & len(coord) > 3) or len(coord) < 2 or len(coord) > 3 or disparo[0] not in abecedario:
            print('Introduce una coordenada válida porfa')
            continue
        diccionario_letras = {letra: indice + 1 for indice, letra in enumerate(abecedario)}
        for letra,numero in diccionario_letras.items():
            if disparo[0] == letra:
                disparo[0] = numero
        if len(disparo) == 2:
            disparo[1] = int(disparo[1])
        if len(disparo) == 3:
            disparo[1] = int(str(disparo[1]) + str(disparo[2]))
        break

def comprobar_hundido(disparo, lista):
    for barco in lista:
        for coordenada in barco:
            if disparo in barco:
                barco.remove(disparo)

def disparar(tablero,tablero_reflejo):
    while True:
        coord = input('Introduce la coordenada donde quieras disparar (ejemplo: a1): ')
        coordenada_a_num(coord)
        x = disparo[0]
        y = disparo[1]
        #if x > dimensiones or x < 0 or y > dimensiones or y < 0:
            #print('Prueba a disparar dentro del tablero illo, que tienes el cañón desviao')
            #continue
        if tablero[x, y] == "O":
            tablero[x, y] = "X"
            tablero_reflejo[x, y] = "X"
            print("¡Tocado!")
            comprobar_hundido(disparo,lista_de_barcos_maquina)
        else:
            tablero[x, y] = " - "
            tablero_reflejo[x, y] = " - "
            print("¡Agua!")
            break

        '''
        esto antes de else
            for barco in lista_de_barcos_maquina:
                if len(barco)!= 0:
                    print("¡Tocado!")
                else:
                    print("¡Tocado y hundido! Ahí va, me has dado bien dao...")
            continue
        '''

def disparar_maquina(tablero):
    disparos = []
    aciertos = [] #estas listas tendrán que ir en variables/constantes para no resetearse
    #se crea una lista disparos en la que se almacenan todos los disparos para que la máquina no se repita
    while True:
        #si queremos hacer que la máquina apunte a los tocados, habría que distinguir el icono de tocado con el de
        #tocado y hundido, coge un tocado, elige una orientacion random y dispara al lado
        if "X" in tablero:
            (x,y) = np.random.choice(aciertos)
            orientacion_elegida = np.random.choice(orientaciones)
            if orientacion_elegida == "N":
                if (x - 1, y) not in disparos:
                    disparos.append((x - 1, y))
                    if tablero[x - 1, y] == " O ":
                        tablero[x - 1, y] = " X "
                        aciertos.append((x - 1, y))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            if len(barco)!= 0:
                                print("¡Tocado!")
                            else:
                                print("¡Tocado y hundido! Ahí va, me has dado bien dao...")
                        continue
                    else:
                        tablero[x - 1, y] = " - "
                        print("Agua!")
                        break
                else:
                    continue
            if orientacion_elegida == "S":
                if (x + 1, y) not in disparos:
                    disparos.append((x - 1, y))
                    if tablero[x + 1, y] == "O":
                        tablero[x + 1, y] = "X"
                        aciertos.append((x + 1, y))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            if len(barco)!= 0:
                                print("¡Tocado!")
                            else:
                                print("¡Tocado y hundido! Ahí va, me has dado bien dao...")
                        continue                        
                    else:
                        tablero[x + 1, y] = "-"
                        print("Agua!")
                        break
                else:
                    continue
            if orientacion_elegida == "E":
                if (x, y + 1) not in disparos:
                    disparos.append((x, y + 1))
                    if tablero[x, y + 1] == "O":
                        tablero[x, y + 1] = "X"
                        aciertos.append((x, y + 1))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            if len(barco)!= 0:
                                print("¡Tocado!")
                            else:
                                print("¡Tocado y hundido! Ahí va, me has dado bien dao...")
                        continue
                    else:
                        tablero[x, y + 1] = "-"
                        print("Agua!")
                        break
                else:
                    continue
            if orientacion_elegida == "Oe":
                if (x, y - 1) not in disparos:
                    disparos.append((x, y + 1))
                    if tablero[x, y - 1] == "O":
                        tablero[x, y - 1] = "X"
                        aciertos.append((x, y + 1))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            if len(barco)!= 0:
                                print("¡Tocado!")
                            else:
                                print("¡Tocado y hundido! Ahí va, me has dado bien dao...")
                        continue
                    else:
                        tablero[x, y - 1] = "-"
                        print("Agua!")
                        break
                else:
                    continue
        else:
            x = np.random.randint(0,9)
            y = np.random.randint(0,9)
            if (x,y) in disparos:
                continue
            else:
                disparos.append(x,y)
            if tablero[x, y] == " O ":
                tablero[x, y] = " X "
                aciertos.append((x, y))
                print("Tocado!")
                continue
            else:
                tablero[x, y] = " - "
                tablero[x, y] = " - "
                print("Agua!")
                break

def comprobar_victoria(tablero):
    if 'O' not in all(tablero):
        print('Enhorabuena illo, eres un máquina, me has ganao bien ganao. Si quieres que nos echemos otra avisa!')
        juego_activo = True

def comprobar_victoria_maquina(tablero):
    if 'O' not in all(tablero):
        print('Vaya manta estás hecho, vas a tener que prácticar mucho más si quieres ganarme la próxima vez')
        juego_activo = True

def coloca_barco(tablero, barco):
    for pieza in barco:
        tablero[pieza] = "O"

def genera_barco(tablero):
    num_filas = tablero.shape[0]
    num_columnas = tablero.shape[1]
    dimensiones = num_filas
    
    barcos_generados = 0
    lista_de_barcos = []

    while barcos_generados < 10: # Generar 10 barcos en total
        if barcos_generados < 1:  # Generar barco de 4 posiciones
            longitud = 4
        elif barcos_generados < 3:  # Generar barcos de 3 posiciones
            longitud = 3
        elif barcos_generados < 6:  # Generar barcos de 2 posiciones
            longitud = 2
        else:  # Generar barcos de 1 posición
            longitud = 1

        orientacion = np.random.choice(orientaciones)
        origen = (np.random.randint(0, num_filas - 1), np.random.randint(0, num_columnas - 1))

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
                lista_de_barcos.append(barco)
                coloca_barco(tablero, barco)
                barcos_generados += 1

    return barcos_generados


