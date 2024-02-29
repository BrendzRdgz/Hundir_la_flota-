import numpy as np
import random




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
            x = random.randint(0,dimensiones[0])
            y = random.randint(0,dimensiones[0])
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

