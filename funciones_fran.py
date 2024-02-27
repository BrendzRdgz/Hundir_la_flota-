#1- para la función disparar, he supuesto que la conversión de letra a número se haría dentro de la función en sí, no sé cómo
#se haría así que lo dejo en pendiente, a falta de hablar con fran
#2- la comprobacion de los ifs para ver que haya hueco donde dejar el barco depende de la cantidad de espacios que haya,
#se queda pendiente también


def generar_barcos_aleatorios(tablero, longitud):
    import random
    filas, columnas = tablero.shape
    filas = filas - 1
    columnas = columnas - 1   #esto es solo para orientarme mejor con los indices
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
        #introducir inputs para el disparo (x y)
        if x > dimensiones or x < 0 or y > dimensiones or y < 0:
            print('Prueba a disparar dentro del tablero illo, que tienes el cañón desviao')
            continue
        elif tablero[x, y] == " O ":
            tablero[x, y] = " X "
            tablero_reflejo[x, y] = " X "
            print("¡Tocado!")
            continue
        else:
            tablero[x, y] = " - "
            tablero_reflejo[x, y] = " - "
            print("¡Agua!")
            break

def disparar_maquina(tablero):
    disparos = []
    aciertos = [] #estas listas tendrán que ir en otro lado al principio para no resetearse
    #se crea una lista disparos en la que se almacenan todos los disparos para que la máquina no se repita
    while True:
        #si queremos hacer que la máquina apunte a los tocados, habría que distinguir el icono de tocado con el de
        #tocado y hundido, coge un tocado, elige una orientacion random y dispara al lado
        if "X" in tablero:
            (x,y) = random.choice(aciertos)
            orientacion_elegida = random.choice(orientaciones)
            if orientacion_elegida == "N":
                if (x - 1, y) not in disparos:
                    disparos.append((x - 1, y))
                    if tablero[x - 1, y] == " O ":
                        tablero[x - 1, y] = " X "
                        aciertos.append((x - 1, y))
                        print("Tocado!")
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
                        print("Tocado!")
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
                        print("Tocado!")
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
                        print("Tocado!")
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
    if 'O' in all(tablero):
        continue
    else:
        print('Enhorabuena illo, eres un máquina, me has ganao bien ganao. Si quieres que nos echemos otra avisa!')
        break

def comprobar_victoria_maquina(tablero):
    if 'O' in all(tablero):
        continue
    else:
        print('Vaya manta estás hecho, vas a tener que prácticar mucho más si quieres ganarme la próxima vez')
        break

#hay que realizar una función juego, se correrá con los tableros ya creados y los barcos ya posicionados, solamente
#realizando la función de disparo y comprobación dentro de ella
        
def juego(self.tablero_jugador, self.tablero_jugador_reflejo, self.tablero_maquina, self.tablero_maquina_reflejo):
    #se colocan los barcos de la máquina
    for i in range(4):
        longitud = 1
        generar_barcos_aleatorios(self.tablero_maquina, longitud)
    for i in range(3):
        longitud = 2
        generar_barcos_aleatorios(self.tablero_maquina, longitud)
    for i in range(2):
        longitud = 3
        generar_barcos_aleatorios(self.tablero_maquina, longitud)
    generar_barcos_aleatorios(self.tablero_maquina, 4)

    print('Máquina, te dejo que empieces primero, un poco de ventaja no te vendrá mal...')
    while True:
    #input para introducir las coords de disparo
        disparar(self.tablero_maquina)
        comprobar_victoria(self.tablero_maquina)

        disparo_maquina(self.tablero_jugador)
        comprobar_victoria_maquina(self.tablero_jugador)