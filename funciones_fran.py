
def coordenada_a_num(coord):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
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

#esta funcion te devuelve cualquier string introducida por una lista compuesta por dos numeros, para acceder
#a la coordenada en x se accede a disparo[0] y para y a disparo[1]

def comprobar_hundido(disparo, lista):
    for barco in lista:
        for coordenada in barco:
            if disparo in barco:
                barco.remove(disparo)

def generar_barcos_aleatorios(tablero, longitud):
    import random
    filas, columnas = tablero.shape
    filas = filas - 1
    columnas = columnas - 1   #esto es solo para orientarme mejor con los indices
    #habria que crear la lista de barcos pero para la maquina
    orientaciones = ["N", "S", "E", "Oe"]
    orientacion_elegida = random.choice(orientaciones)
    while True:
        if orientacion_elegida == "N":
            x = random.randint(longitud - 1, filas)
            y = random.randint(0, columnas)
            if all(tablero[x - posicion, y] == " " for posicion in range(longitud)):
                for posicion in range(longitud):
                    tablero[x - posicion,y] = "O"
                break
        elif orientacion_elegida == "S":
            x = random.randint(0, filas - longitud)
            y = random.randint(0, columnas)
            if all(tablero[x + posicion, y] == " " for posicion in range(longitud)):
                for posicion in range(longitud):
                    tablero[x + posicion,y] = "O"
                break
        elif orientacion_elegida == "E":
            x = random.randint(0, filas)
            y = random.randint(0, columnas - longitud)
            if all(tablero[x, y + posicion] == " " for posicion in range(longitud)):
                for posicion in range(longitud):
                    tablero[x,y + posicion] = "O"
                break
        elif orientacion_elegida == "Oe":
            x = random.randint(0, filas)
            y = random.randint(longitud, columnas)
            if all(tablero[x, y - posicion] == " " for posicion in range(longitud)):
                for posicion in range(longitud):
                    tablero[x, y - posicion] = "O"
                break


def disparar(tablero,tablero_reflejo):
    while True:
        coord = input('Introduce la coordenada donde quieras disparar (ejemplo: a1): ')
        coordenada_a_num(coord)
        x = disparo[0]
        y = disparo[1]
        if x > dimensiones or x < 0 or y > dimensiones or y < 0:
            print('Prueba a disparar dentro del tablero illo, que tienes el cañón desviao')
            continue
        elif tablero[x, y] == "O":
            tablero[x, y] = "X"
            tablero_reflejo[x, y] = "X"
            comprobar_hundido(disparo,lista_de_barcos_maquina)
            for barco in lista_de_barcos_maquina:
                if len(barco)!= 0:
                    print("¡Tocado!")
                else:
                    print("¡Tocado y hundido! Ahí va, me has dado bien dao...")
            continue
        else:
            tablero[x, y] = " - "
            tablero_reflejo[x, y] = " - "
            print("¡Agua!")
            break

#me falta ver como implementar los aciertos para que cuando un barco se destruya, sus coordenadas se destruyan en aciertos tmb
#tal vez crear una copia de la lista, y eliminar segun el indice????
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
            x = random.randint(0,9)
            y = random.randint(0,9)
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

#se tendría que realizar la comprobación siempre que haya un disparo, he hecho dos para realizar dos prints. El continue
#haría que saliera al bucle principal de nuevo, a volver a disparar
def comprobar_victoria(tablero):
    if 'O' not in all(tablero):
        print('Enhorabuena illo, eres un máquina, me has ganao bien ganao. Si quieres que nos echemos otra avisa!')
        juego_activo = True

def comprobar_victoria_maquina(tablero):
    if 'O' not in all(tablero):
        print('Vaya manta estás hecho, vas a tener que prácticar mucho más si quieres ganarme la próxima vez')
        juego_activo = True

#hay que realizar una función juego, se correrá con los tableros ya creados y los barcos ya posicionados, solamente
#realizando la función de disparo y comprobación dentro de ella
        
def juego(tablero_1.tablero_jugador, tablero_1.tablero_jugador_reflejo, tablero_1.tablero_maquina, tablero_1.tablero_maquina_reflejo):
    #se colocan los barcos de la máquina
    import numpy as np
    for i in range(4):
        longitud = 1
        generar_barcos_aleatorios(tablero_1.tablero_maquina, longitud)
        i = i + 1
    for i in range(3):
        longitud = 2
        generar_barcos_aleatorios(tablero_1.tablero_maquina, longitud)
        i = i + 1
    for i in range(2):
        longitud = 3
        generar_barcos_aleatorios(tablero_1.tablero_maquina, longitud)
        i = i + 1
    generar_barcos_aleatorios(tablero_1.tablero_maquina, 4)

    print('Máquina, te dejo que empieces primero, un poco de ventaja no te vendrá mal...')
    juego_activo = True
    while juego_activo == True:
    #input para introducir las coords de disparo
        disparar(tablero_1.tablero_maquina)
        comprobar_victoria(tablero_1.tablero_maquina)

        disparar_maquina(tablero_1.tablero_jugador)
        comprobar_victoria_maquina(tablero_1.tablero_jugador)



####################################
        
def genera_barco(tablero):
    num_filas = tablero.shape[0]
    num_columnas = tablero.shape[1]
    orientaciones = ["N","S","O","E"]
    
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
                lista_de_barcos.append(barco)
                coloca_barco(tablero, barco)
                barcos_generados += 1

    return barcos_generados    