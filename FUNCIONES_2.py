def crear_tablero(x = None, y = None):

    dimensiones = (x, y)
    
    if dimensiones != (None, None):
        dimensiones = (x+1, y+1)
        tablero = Tablero(dimensiones)
    else:
        tablero = Tablero()

    print(tablero)
    return tablero
