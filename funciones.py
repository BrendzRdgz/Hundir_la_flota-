'''
FUNCION PARA CREAR TABLERO por Fran 2/fafi

Si queremos generar un tablero de dimensiones diferentes a 10x10 debemos pasarle una tupla.
Ejemplo --> crear_tablero((12,12)). Tamaño maximo (26x26)

Debemos almacenar el tablero creado en una variable.
Ejemplo --> tablero_1 = crear_tablero()
'''
import tablero

def crear_tablero(x = None, y = None):

    dimensiones = (x+1, y+1)
    
    if dimensiones != (None, None):
        tablero = Tablero(dimensiones)
    else:
        tablero = Tablero()

    print(tablero)
    return tablero

