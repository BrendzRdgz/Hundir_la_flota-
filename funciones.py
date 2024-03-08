from clases import*
from variables import*
import numpy as np
import random
import time
import copy

#Esta es la función para crear la variable tablero, compuesto según la clase definida, para el hundir la flota
def crear_tablero(x = None, y = None):
    dimensiones = (x, y)
    
    if dimensiones != (None, None):
        dimensiones = (x+1, y+1)
        tablero = Tablero(dimensiones)
    else:
        tablero = Tablero()

    return tablero

#Función para introducir a dónde quieres disparar y, a partir de ello, transformarlo en una tupla de coordenadas (x, y)
def elegir_coordenada():
    while True:
        coord = input('Introduce la coordenada donde quieras disparar (ejemplo: a1): ')
        disparo = [char for char in coord]

        if len(coord) == 3:
            if disparo[1] in abecedario or disparo[2] in abecedario:
                print('Introduce una coordenada válida porfa')
                continue
        elif len(coord) == 2:
            if disparo[1] in abecedario or disparo[0] not in abecedario:
                print('Introduce una coordenada válida porfa')
                continue
        else:
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
            disparo.pop(2)
        break
    return disparo

#Función para pintar los barcos creados en el tablero según las coordenadas establecidas en su función hermana genera_barco
def coloca_barco(tablero, barco):
    for pieza in barco:
        tablero[pieza] = "O"

#Función para generar las coordenadas aleatorias donde se posicionarán los barcos en el tablero del jugador, 
#y crear una lista de barcos de esas posiciones
def genera_barco(tablero):
    num_filas = tablero.shape[0]
    num_columnas = tablero.shape[1]
    
    barcos_generados = 0

    while barcos_generados < 10: # Generar 10 barcos en total
        if barcos_generados < 1:
            longitud = 4
        elif barcos_generados < 3:
            longitud = 3
        elif barcos_generados < 6:
            longitud = 2
        else:
            longitud = 1

        orientacion = np.random.choice(orientaciones)
        origen = (np.random.randint(1, num_filas), np.random.randint(1, num_columnas))

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

                if fila >= num_filas or fila < 1 or columna >= num_columnas or columna < 1:
                    break

                if tablero[fila, columna] == "O" or tablero[fila, columna] == "X":
                    break

                barco.append((fila, columna))

            if len(barco) == longitud:
                global lista_de_barcos
                lista_de_barcos.append(barco)
                global lista_de_barcos_copia
                lista_de_barcos_copia = copy.deepcopy(lista_de_barcos)
                coloca_barco(tablero, barco)
                barcos_generados += 1

#Función para generar las coordenadas aleatorias dónde se posicionarán los barcos en el tablero de la máquina, 
#y crear una lista de barcos de esas posiciones y una copia referencia
def genera_barco_maquina(tablero):
    num_filas = tablero.shape[0]
    num_columnas = tablero.shape[1]
    
    barcos_generados = 0

    while barcos_generados < 10: # Generar 10 barcos en total
        if barcos_generados < 1:
            longitud = 4
        elif barcos_generados < 3:
            longitud = 3
        elif barcos_generados < 6:
            longitud = 2
        else:
            longitud = 1

        orientacion = np.random.choice(orientaciones)
        origen = (np.random.randint(1, num_filas), np.random.randint(1, num_columnas))

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

                if fila >= num_filas or fila < 1 or columna >= num_columnas or columna < 1:
                    break

                if tablero[fila, columna] == "O" or tablero[fila, columna] == "X":
                    break

                barco.append((fila, columna))

            if len(barco) == longitud:
                global lista_de_barcos_maquina
                lista_de_barcos_maquina.append(barco)
                global lista_de_barcos_maquina_copia
                lista_de_barcos_maquina_copia = copy.deepcopy(lista_de_barcos_maquina)
                coloca_barco(tablero, barco)
                barcos_generados += 1

#Las 3 funciones siguientes componen el proceso de destrucción, eliminación de barcos y apuntado de la máquina.
#Comprobar_hundido se dedicará a iterar sobre la lista de barcos y eliminar la parte del barco donde hayas acertado
def comprobar_hundido(disparo, lista):
    disparo = tuple(disparo)
    for barco in lista:
        for i, parte_barco in enumerate(barco):
            if disparo == parte_barco:
                barco.pop(i)

#Eliminar_restos_maquina coge las dos listas de barcos del jugador y la lista de aciertos y, cuando haya habido un hundido confirmado,
#borrará la lista vacía de "barcos", la lista referencia de "copias" y, esas mismas coordenadas de la copia,
#las borrará de aciertos, para que la máquina no vuelva a apuntar al lado de esos aciertos
def eliminar_restos_maquina(barcos, copias, aciertos):
    for i, barco in enumerate(barcos):
        if len(barco) == 0:
            for acierto in aciertos:
                if acierto in copias[i]:
                    for elemento in copias[i]:
                        aciertos.remove(elemento)
                    barcos.pop(i)
                    copias.pop(i)
                    break
    return aciertos

#Eliminar_restos hace lo mismo que arriba pero solamente con la lista de barcos de la máquina
def eliminar_restos(barcos, copias):
    for i, barco in enumerate(barcos):
        if len(barco) == 0:
            barcos.pop(i)
            copias.pop(i)
            break

#Función disparar para el jugador, una de las dos funciones en bucle en el main
def disparar(tablero, tablero_reflejo):
    while True:
        print(tablero_1)
        juego_activo = comprobar_victoria(tablero)
        if juego_activo == False:
            break
        disparo = elegir_coordenada()
        if disparo in disparos:
            print('Illo, que ahí ya has tirao. Ahora te jodes, por tonto, un máquina no perdona...')
        disparos.append(disparo)
        x = disparo[0]
        y = disparo[1]
        if tablero[x, y] == "O":
            tablero[x, y] = "X"
            tablero_reflejo[x, y] = "X"
            comprobar_hundido(disparo,lista_de_barcos_maquina)
            for barco in lista_de_barcos_maquina:
                hundido = False
                if len(barco) == 0:
                    hundido = True
                    print("¡Tocado y hundido! Ahí va, me has dado bien dao...")
                    time.sleep(2)
                    eliminar_restos(lista_de_barcos_maquina, lista_de_barcos_maquina_copia)
                    print(tablero_1)
                    break
            if hundido == False:
                print('¡Tocado! Ha sido suerte, no te emociones...')
                time.sleep(2)    
                print(tablero_1)
                continue
        else:
            tablero[x, y] = "-"
            tablero_reflejo[x, y] = "-"
            print("¿Lo escuchas? Chof chof, ¡Agua!")
            time.sleep(2)
            print(tablero_1)
            break
    return juego_activo

#Función disparar_maquina, la otra función en bucle en el main, donde la máquina dará preferencia
#a apuntar a los lugares colindantes a sus aciertos y, si no los hay, disparará aleatoriamente
def disparar_maquina(tablero, juego_activo):
    #print(juego_activo)
    if juego_activo == True:
        print('¡Mi turno! ¡Prepárate! ¡Bulería, buleríaaaa!')
    while True:
        juego_activo_1 = comprobar_victoria_maquina(tablero)
        juego_activo_2 = comprobar_victoria(tablero_1.tablero_maquina)
        if juego_activo_1 == False or juego_activo_2 == False:
            juego_activo = False
            break
        time.sleep(1)

        if len(aciertos) != 0:
            acierto = random.choice(aciertos)
            (x,y) = acierto
            orientacion_elegida = random.choice(orientaciones)
            if orientacion_elegida == "N":
                if x == 1:
                    continue
                if (x - 1, y) not in disparos_maquina:
                    disparo = (x - 1, y)
                    disparos_maquina.append((x - 1, y))
                    if tablero[x - 1, y] == "O":
                        tablero[x - 1, y] = "X"
                        aciertos.append((x - 1, y))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            hundido = False
                            if len(barco)== 0:
                                print(tablero_1)
                                print("¡Tocado y hundido! ¡Uno menos!")
                                time.sleep(2)
                                hundido = True
                                eliminar_restos_maquina(lista_de_barcos, lista_de_barcos_copia, aciertos)
                                break
                        if hundido == False:
                            print(tablero_1)
                            print('¡Tocado! ¡Tomaaaa!')
                            time.sleep(2)
                            continue
                        continue
                    else:
                        tablero[x - 1, y] = "-"
                        print(tablero_1)
                        print("¿Otra vez he fallado? :(")
                        time.sleep(2)
                        break
                else:
                    continue
            if orientacion_elegida == "S":
                if x + 1 > dimensiones:
                    continue
                if (x + 1, y) not in disparos_maquina:
                    disparo = (x + 1, y)
                    disparos_maquina.append((x + 1, y))
                    if tablero[x + 1, y] == "O":
                        tablero[x + 1, y] = "X"
                        aciertos.append((x + 1, y))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            hundido = False
                            if len(barco)== 0:
                                print(tablero_1)
                                print("¡Tocado y hundido! ¡Uno menos!")
                                time.sleep(2)
                                hundido = True
                                eliminar_restos_maquina(lista_de_barcos, lista_de_barcos_copia, aciertos)
                                break
                        if hundido == False:
                            print(tablero_1)
                            print('¡Tocado! ¡Tomaaaa!')
                            time.sleep(2)
                            continue
                        continue
                    else:
                        tablero[x + 1, y] = "-"
                        print(tablero_1)
                        print("¿Otra vez he fallado? :(")
                        time.sleep(2)
                        break
                else:
                    continue
            if orientacion_elegida == "E":
                if y + 1 > dimensiones:
                    continue
                if (x, y + 1) not in disparos_maquina:
                    disparo = (x, y + 1)
                    disparos_maquina.append((x, y + 1))
                    if tablero[x, y + 1] == "O":
                        tablero[x, y + 1] = "X"
                        aciertos.append((x, y + 1))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            hundido = False
                            if len(barco)== 0:
                                print(tablero_1)
                                print("¡Tocado y hundido! ¡Uno menos!")
                                time.sleep(2)
                                hundido = True
                                eliminar_restos_maquina(lista_de_barcos, lista_de_barcos_copia, aciertos)
                                break
                        if hundido == False:
                            print(tablero_1)
                            print('¡Tocado! ¡Tomaaaa!')
                            time.sleep(2)
                            continue
                        continue
                    else:
                        tablero[x, y + 1] = "-"
                        print(tablero_1)
                        print("¿Otra vez he fallado? :(")
                        time.sleep(2)
                        break
                else:
                    continue
            if orientacion_elegida == "Oe":
                if y == 1:
                    continue
                if (x, y - 1) not in disparos_maquina:
                    disparo = (x, y - 1)
                    disparos_maquina.append((x, y - 1))
                    if tablero[x, y - 1] == "O":
                        tablero[x, y - 1] = "X"
                        aciertos.append((x, y - 1))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            hundido = False
                            if len(barco)== 0:
                                print(tablero_1)
                                print("¡Tocado y hundido! ¡Uno menos!")
                                time.sleep(2)
                                hundido = True
                                eliminar_restos_maquina(lista_de_barcos, lista_de_barcos_copia, aciertos)
                                continue
                        if hundido == False:
                            print(tablero_1)
                            print('¡Tocado! ¡Tomaaaa!')
                            time.sleep(2)
                            continue
                        continue
                    else:
                        tablero[x, y - 1] = "-"
                        print(tablero_1)
                        print("¿Otra vez he fallado? :(")
                        time.sleep(2)
                        break
                else:
                    continue
        else:
            x = np.random.randint(1,dimensiones+1)
            y = np.random.randint(1,dimensiones+1)
            if (x,y) in disparos_maquina:
                continue
            else:
                disparo = (x,y)
                disparos_maquina.append((x,y))
            if tablero[x, y] == "O":
                tablero[x, y] = "X"
                aciertos.append((x,y))
                comprobar_hundido(disparo,lista_de_barcos)
                for barco in lista_de_barcos:
                    hundido = False
                    if len(barco) == 0:
                        print(tablero_1)
                        print("¡Tocado y hundido! ¡Uno menos!")
                        time.sleep(2)
                        hundido = True
                        eliminar_restos_maquina(lista_de_barcos, lista_de_barcos_copia, aciertos)
                        break
                if hundido == False:
                    print(tablero_1)
                    print('¡Tocado! ¡Tomaaaa!')
                    time.sleep(2)
                    continue
                continue
            else:
                tablero[x, y] = "-"
                print(tablero_1)
                print("He fallado, mierda...")
                time.sleep(2)
                break
    return juego_activo

#Funciones para comprobar la victoria final del jugador o de la máquina
def comprobar_victoria(tablero_maquina):
    juego_activo = True
    if not any ("O" in fila for fila in tablero_maquina):
        print('Enhorabuena, illo ere" un máquina, me has ganao bien ganao. Si quieres que nos echemos otra avisa!')
        time.sleep(3)
        juego_activo = False
    return juego_activo    

def comprobar_victoria_maquina(tablero_humano):
    juego_activo = True
    if not any ("O" in fila for fila in tablero_humano):
        print('Vaya manta estás hecho, vas a tener que prácticar mucho más si quieres ganarme la próxima vez...')
        time.sleep(1)
        print('Es broma, ere" un máquina igual. ¡Un abrazo!')
        time.sleep(3)
        juego_activo = False
    return juego_activo