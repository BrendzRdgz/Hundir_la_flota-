from tablero import*
import variables

import numpy as np
import random

juego_activo = True
abecedario = 'abcdefghijklmnopqrstuvwxyz-'
orientaciones = ["N","S","O","E"]
lista_de_barcos = []
lista_de_barcos_maquina = []
disparos = []
aciertos = []
barcos_hundidos = 0
barcos_hundidos_maquina = 0
dimensiones = 10 #a falta de adaptar la variable dimensiones en el codigo

def crear_tablero(x = None, y = None):

    dimensiones = (x, y)
    
    if dimensiones != (None, None):
        dimensiones = (x+1, y+1)
        tablero = Tablero(dimensiones)
    else:
        tablero = Tablero()

    print(tablero)
    return tablero

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

def coloca_barco(tablero, barco):
    for pieza in barco:
        tablero[pieza] = "O"

def genera_barco(tablero):
    num_filas = tablero.shape[0]
    num_columnas = tablero.shape[1]
    
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

                if fila >= num_filas or fila < 0 or columna >= num_columnas or columna < 0:
                    break

                if tablero[fila, columna] == "O" or tablero[fila, columna] == "X":
                    break

                barco.append((fila, columna))

            if len(barco) == longitud:
                lista_de_barcos.append(barco)
                coloca_barco(tablero, barco)
                barcos_generados += 1
    return lista_de_barcos

def genera_barco_maquina(tablero):
    num_filas = tablero.shape[0]
    num_columnas = tablero.shape[1]
    
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
                lista_de_barcos_maquina.append(barco)
                coloca_barco(tablero, barco)
                barcos_generados += 1
    return lista_de_barcos_maquina

def comprobar_hundido(disparo, lista):
    disparo = tuple(disparo)
    for barco in lista:
        for parte_barco in barco:
            if disparo == parte_barco:
                barco.remove(parte_barco)

def eliminar_restos(barcos):
    for barco in barcos:
        if len(barco) == 0:
            barcos.remove(barco)


def disparar(tablero,tablero_reflejo,barcos_hundidos):
    while True:
        comprobar_victoria(barcos_hundidos)
        disparo = elegir_coordenada()
        x = disparo[0]
        y = disparo[1]
        if x > dimensiones or y > dimensiones:
            print('Prueba a disparar dentro del tablero illo, que tienes el cañón desviao...')
            continue
        if tablero[x, y] == "O":
            tablero[x, y] = "X"
            tablero_reflejo[x, y] = "X"
            comprobar_hundido(disparo,lista_de_barcos_maquina)
            for barco in lista_de_barcos_maquina:
                print(barco)
                hundido = False
                if len(barco) == 0:
                    hundido = True
                    print("¡Tocado y hundido! Ahí va, me has dado bien dao...")
                    barcos_hundidos += 1
                    eliminar_restos(lista_de_barcos_maquina)
                    #_reflejo)
                    break
            if hundido == False:
                print('¡Tocado!')     
                #print(tablero_reflejo)
                continue
        else:
            tablero[x, y] = " - "
            tablero_reflejo[x, y] = " - "
            print("¡Agua!")
            #print(tablero_reflejo)
            break


def disparar_maquina(tablero, barcos_hundidos_maquina):
    print('¡Mi turno! ¡Prepárate!')
    while True:
        comprobar_victoria_maquina(barcos_hundidos_maquina)
        #si queremos hacer que la máquina apunte a los tocados, habría que distinguir el icono de tocado con el de
        #tocado y hundido, coge un tocado, elige una orientacion random y dispara al lado
        if "X" in tablero:
            acierto = random.choice(aciertos)
            (x,y) = acierto
            orientacion_elegida = random.choice(orientaciones)
            if orientacion_elegida == "N":
                if (x - 1, y) not in disparos:
                    disparo = (x - 1, y)
                    disparos.append((x - 1, y))
                    if tablero[x - 1, y] == "O":
                        tablero[x - 1, y] = "X"
                        aciertos.append((x - 1, y))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            if len(barco)== 0:
                                print("¡Tocado y hundido! ¡Uno menos!")
                                barcos_hundidos_maquina += 1
                                eliminar_restos(lista_de_barcos)
                                #print(tablero)
                                continue
                        print('¡Tocado! ¡Tomaaaa!')
                        #print(tablero)
                        continue
                    else:
                        tablero[x - 1, y] = "-"
                        print("¿Otra vez he fallado? :(")
                        #print(tablero)
                        break
                else:
                    continue
            if orientacion_elegida == "S":
                if (x + 1, y) not in disparos:
                    disparo = (x + 1, y)
                    disparos.append((x + 1, y))
                    if tablero[x + 1, y] == "O":
                        tablero[x + 1, y] = "X"
                        aciertos.append((x + 1, y))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            if len(barco)== 0:
                                print("¡Tocado y hundido! ¡Uno menos!")
                                barcos_hundidos_maquina += 1
                                eliminar_restos(lista_de_barcos)
                                #print(tablero)
                                continue
                        print('¡Tocado! ¡Tomaaaa!')
                        #print(tablero)
                        continue
                    else:
                        tablero[x + 1, y] = "-"
                        print("¿Otra vez he fallado? :(")
                        #print(tablero)
                        break
                else:
                    continue
            if orientacion_elegida == "E":
                if (x, y + 1) not in disparos:
                    disparo = (x, y + 1)
                    disparos.append((x, y + 1))
                    if tablero[x, y + 1] == "O":
                        tablero[x, y + 1] = "X"
                        aciertos.append((x, y + 1))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            if len(barco)== 0:
                                print("¡Tocado y hundido! ¡Uno menos!")
                                barcos_hundidos_maquina += 1
                                eliminar_restos(lista_de_barcos)
                                #print(tablero)
                                continue
                        print('¡Tocado! ¡Tomaaaa!')
                        #print(tablero)
                        continue
                    else:
                        tablero[x, y + 1] = "-"
                        print("¿Otra vez he fallado? :(")
                        #print(tablero)
                        break
                else:
                    continue
            if orientacion_elegida == "Oe":
                if (x, y - 1) not in disparos:
                    disparo = (x, y - 1)
                    disparos.append((x, y - 1))
                    if tablero[x, y - 1] == "O":
                        tablero[x, y - 1] = "X"
                        aciertos.append((x, y + 1))
                        comprobar_hundido(disparo,lista_de_barcos)
                        for barco in lista_de_barcos:
                            if len(barco)== 0:
                                print("¡Tocado y hundido! ¡Uno menos!")
                                barcos_hundidos_maquina += 1
                                eliminar_restos(lista_de_barcos)
                                #print(tablero)
                                continue
                        print('¡Tocado! ¡Tomaaaa!')
                        #print(tablero)
                        continue
                    else:
                        tablero[x, y - 1] = "-"
                        print("¿Otra vez he fallado? :(")
                        #print(tablero)
                        break
                else:
                    continue
        else:
            x = np.random.randint(1,10)
            y = np.random.randint(1,10)
            if (x,y) in disparos:
                continue
            else:
                disparo = (x,y)
                disparos.append((x,y))
            if tablero[x, y] == "O":
                tablero[x, y] = "X"
                aciertos.append((x,y))
                comprobar_hundido(disparo,lista_de_barcos)
                for barco in lista_de_barcos:
                    if len(barco)== 0:
                        print("¡Tocado y hundido! ¡Uno menos!")
                        barcos_hundidos_maquina += 1
                        eliminar_restos(lista_de_barcos)
                        #print(tablero)
                        continue
                print("¡Tocado! ¡Bien!")
                #print(tablero)
                continue
            else:
                tablero[x, y] = "-"
                tablero[x, y] = "-"
                print("He fallado, mierda...")
                #print(tablero)
                break

def comprobar_victoria(barcos_hundidos):
        if barcos_hundidos == 10:
            print('Enhorabuena illo, eres un máquina, me has ganao bien ganao. Si quieres que nos echemos otra avisa!')
            #juego_activo = False

def comprobar_victoria_maquina(barcos_hundidos_maquina):
        if barcos_hundidos_maquina == 10:
            print('Vaya manta estás hecho, vas a tener que prácticar mucho más si quieres ganarme la próxima vez')
            print('Es broma, eres un máquina igual ;)')
            #juego_activo = False
