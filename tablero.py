'''
INSTRUCCIONES

1.- El tablero esta diseñado para generar un array y mostrar un tablero hasta una dimension maxima(cuadrada, con igual cantidad de filas y columnas)
    de 26x26 (cantidad de letras en el alfabeto). 

2.- Al instanciar un objeto Tablero, la dimension por defecto es de 10x10. En caso de generar un tablero de mayores dimensiones debemos pasar las
    dimensiones como una tupla. Ejemplo: tablero_1 = Tablero((16, 16)).

3.- La instancia de tablero genera automaticamente 4 tableros con sus representaciones. Para referirnos a ellas debenos referenciarlas tal que asi
    (tomando como ejemplo de ahora en adelante que llamamos a la instancia "tablero_1"):

    a.- tablero_1.tablero_humano
    b.- tablero_1.tablero_humano_reflejo
    c.- tablero_1.tablero_maquina
    d.- tablero_1.tablero_maquina_reflejo

4.- Para colocar los barcos del jugador humano deberemos colocarlos en el tablero del humano --> tablero_1.tablero_humano

5.- Para colocar los barcos del jugador maquina deberemos colocarlos en el tablero de la maquina --> tablero_1.tablero_maquina

6.- En caso de que el jugador humano realice un disparo:

    a.- Para reflejar el disparo en el tablero del jugador maquina deberemos referenciar la celda/escalar/casilla en tablero_1.tablero_maquina.
    b.- Para reflejar el disparo en el tablero reflejo que observa el jugador humano debemos referenciar la celda/escalar/casilla en tablero_1.tablero_humano_reflejo.

7.- En caso de que el jugador maquina realice un disparo:

    a.- Para reflejar el disparo en el tablero del jugador humano deberemos referenciar la celda/escalar/casilla en tablero_1.tablero_humano.
    b.- Para reflejar el disparo en el tablero reflejo que observa el jugador maquina debemos referenciar la celda/escalar/casilla en tablero_1.tablero_maquina_reflejo.

8.- Para imprimir el tablero en su condicion actual solo debemos imprimir la instancia.
    Ejemplo: "print(tablero_1)", esto mostrara los tableros que observa el jugador humano(su tablero y el reflejo del tablero de la maquina).

9.- IMPORTANTE:
    Las filas de la 1 a la 9 estan compuestas por 3 espacios/caracteres.
    De la fila 10 en adelante estan compuestas por 4 espacios/caracteres.
    
    Para no romper la estructura de la cuadricula, cuando reflejamos un disparo acertado, un disparo errado o un barco(por ejemplo 'X', '-' u 'O') es importante
    mantener esta estructura. Por ejemplo:

    Si realizamos un disparo a la casilla B-4(en el array indices [3][1]) y acertamos lo reflejaremos como ' X '. Con tres espacios/caracteres.
    Si realizamos un disparo a la casilla C-10(en el array indices [9][2]) y acertamos lo reflejaremos como '  X ' o ' X  '. Con cuatro espacios/caracteres.
    Lo mismo para la hubicacion de barcos o disparos errados.
'''

import numpy as np

class Tablero:

    def __init__(self, dimensiones = (10, 10)):

        self.dimensiones = dimensiones #seleccionamos las dimensiones de preferencia del jugador. Son 10x10 por defecto si no se indican

        self.tablero_humano = np.full(dimensiones, '    ') #generamos un array con las dimensiones del tablero especificadas y conformado por str de longitud 3

        self.tablero_humano_reflejo = np.full(dimensiones, '    ')

        self.tablero_maquina = np.full(dimensiones, '    ')

        self.tablero_maquina_reflejo = np.full(dimensiones, '    ')

        self.formato_letras_numeros()

    def __str__(self):


        print('\nESCENARIO ENEMIGO')
        for index_row, row in enumerate(self.tablero_humano_reflejo):
            print('\n', '+-------'*len(self.tablero_humano_reflejo), '+', sep='')
            for index_col, col in enumerate(self.tablero_humano_reflejo):

                if index_row > 8:
                    print('|', self.tablero_humano_reflejo[index_row][index_col], ' ', end = '')
                else:
                    print('| ', self.tablero_humano_reflejo[index_row][index_col], ' ', end = '')
                
            print('|', end = '')
        print('\n', '+-------'*len(self.tablero_humano_reflejo), '+', sep='')

        print('\nNUESTRO ESCENARIO')

        for index_row, row in enumerate(self.tablero_humano):
            print('\n', '+-------'*len(self.tablero_humano), '+', sep='')
            for index_col, col in enumerate(self.tablero_humano):

                if index_row > 8:
                    print('|', self.tablero_humano[index_row][index_col], ' ', end = '')
                else:
                    print('| ', self.tablero_humano[index_row][index_col], ' ', end = '')
                
            print('|', end = '')
        print('\n', '+-------'*len(self.tablero_humano), '+', sep='')
        
        return ('\nSiguiente operacion?')

    def formato_letras_numeros(self):

        letras = [chr(x) for x in range(65, 91)]
        numeros = [x for x in range(1, len(self.tablero_humano)+1)]

        for index_col, col in enumerate(self.tablero_humano[0]):
            for index_row, row in enumerate(self.tablero_humano):

                self.tablero_humano[index_row][index_col] = f'{letras[index_col]}-{numeros[index_row]}'
                self.tablero_humano_reflejo[index_row][index_col] = f'{letras[index_col]}-{numeros[index_row]}'

                #las dos siguientes lineas de codigo las comento porque referencian los tableros con que juega la maquina, como estos no se
                #muestran en pantalla no veo necesidad de ponerlos en formato 'A-1'. No obstante, ahi estan por si
                
                #self.tablero_maquina[index_col][index_row] = f'{letras[index_col]}-{numeros[index_row]}'
                #self.tablero_maquina_reflejo[index_col][index_row] = f'{letras[index_col]}-{numeros[index_row]}'
        
