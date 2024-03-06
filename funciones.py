from clases import*
from variables import*
import numpy as np
import random
import time
import copy

def crear_tablero(x = None, y = None):
    global dimensiones
    dimensiones = (x, y)
    
    if dimensiones != (None, None):
        dimensiones = (x+1, y+1)
        tablero = Tablero(dimensiones)
    else:
        tablero = Tablero()

    #print(tablero)
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
                global lista_de_barcos_maquina
                lista_de_barcos_maquina.append(barco)
                global lista_de_barcos_maquina_copia
                lista_de_barcos_maquina_copia = copy.deepcopy(lista_de_barcos_maquina)
                coloca_barco(tablero, barco)
                barcos_generados += 1

def comprobar_hundido(disparo, lista):
    disparo = tuple(disparo)
    for barco in lista:
        for i, parte_barco in enumerate(barco):
            if disparo == parte_barco:
                barco.pop(i)

def eliminar_restos_maquina(barcos, copias, aciertos):
    #print(barcos)
    #print(copias)
    for i, barco in enumerate(barcos):
        if len(barco) == 0:
            for acierto in aciertos:
                if acierto in copias[i]:
                    #print(acierto)
                    #print(copias[i])
                    for elemento in copias[i]:
                        #print(elemento)
                        #print(aciertos)
                        aciertos.remove(elemento)
                        #print(aciertos)
                    barcos.pop(i)
                    copias.pop(i)
                    break
    return aciertos

def eliminar_restos(barcos, copias):
    for i, barco in enumerate(barcos):
        if len(barco) == 0:
            barcos.pop(i)
            copias.pop(i)
            break

def disparar(tablero, tablero_reflejo):
    while True:
        print(tablero_1)
        juego_activo = comprobar_victoria(tablero)
        if juego_activo == False:
            break
        disparo = elegir_coordenada()
        if disparo in disparos:
            print('Illo, que ahí ya has tirao. Illo ahora te jodes, por tonto, un campeón no perdona...')
        disparos.append(disparo)
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
                hundido = False
                if len(barco) == 0:
                    hundido = True
                    print("¡Tocado y hundido! Ahí va, me has dado bien dao...")
                    eliminar_restos(lista_de_barcos_maquina, lista_de_barcos_maquina_copia)
                    print(tablero_1)
                    break
            if hundido == False:
                print('¡Tocado!')     
                print(tablero_1)
                continue
        else:
            tablero[x, y] = "-"
            tablero_reflejo[x, y] = "-"
            print("¡Agua!")
            print(tablero_1)
            break
    return juego_activo

def disparar_maquina(tablero, juego_activo):
    #print(juego_activo)
    if juego_activo == True:
        print('¡Mi turno! ¡Prepárate! ¡Bulería, buleríaaaa!')
    while True:
        juego_activo_1 = comprobar_victoria(tablero)
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
                                hundido = True
                                eliminar_restos_maquina(lista_de_barcos, lista_de_barcos_copia, aciertos)
                                break
                        if hundido == False:
                            print(tablero_1)
                            print('¡Tocado! ¡Tomaaaa!')
                            continue
                        continue
                    else:
                        tablero[x - 1, y] = "-"
                        print(tablero_1)
                        print("¿Otra vez he fallado? :(")
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
                                hundido = True
                                eliminar_restos_maquina(lista_de_barcos, lista_de_barcos_copia, aciertos)
                                break
                        if hundido == False:
                            print(tablero_1)
                            print('¡Tocado! ¡Tomaaaa!')
                            continue
                        continue
                    else:
                        tablero[x + 1, y] = "-"
                        print(tablero_1)
                        print("¿Otra vez he fallado? :(")
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
                                hundido = True
                                eliminar_restos_maquina(lista_de_barcos, lista_de_barcos_copia, aciertos)
                                break
                        if hundido == False:
                            print(tablero_1)
                            print('¡Tocado! ¡Tomaaaa!')
                            continue
                        continue
                    else:
                        tablero[x, y + 1] = "-"
                        print(tablero_1)
                        print("¿Otra vez he fallado? :(")
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
                                hundido = True
                                eliminar_restos_maquina(lista_de_barcos, lista_de_barcos_copia, aciertos)
                                continue
                        if hundido == False:
                            print(tablero_1)
                            print('¡Tocado! ¡Tomaaaa!')
                            continue
                        continue
                    else:
                        tablero[x, y - 1] = "-"
                        print(tablero_1)
                        print("¿Otra vez he fallado? :(")
                        break
                else:
                    continue
        else:
            x = np.random.randint(1,11)
            y = np.random.randint(1,11)
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
                        hundido = True
                        eliminar_restos_maquina(lista_de_barcos, lista_de_barcos_copia, aciertos)
                        break
                if hundido == False:
                    print(tablero_1)
                    print('¡Tocado! ¡Tomaaaa!')
                    continue
                continue
            else:
                tablero[x, y] = "-"
                print(tablero_1)
                print("He fallado, mierda...")
                break
    #print(tablero_1)
    return juego_activo

def comprobar_victoria(tablero_maquina):
    juego_activo = True
    if not any ("O" in fila for fila in tablero_maquina):
        print('Enhorabuena illo, eres un máquina, me has ganao bien ganao. Si quieres que nos echemos otra avisa!')
        juego_activo = False
    return juego_activo    

def comprobar_victoria_maquina(tablero_humano):
    juego_activo = True
    if not any ("O" in fila for fila in tablero_humano):
        print('Vaya manta estás hecho, vas a tener que prácticar mucho más si quieres ganarme la próxima vez')
        print('Es broma, eres un máquina igual ;)')
        juego_activo = False
    return juego_activo