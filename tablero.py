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
'''

import numpy as np

class Tablero:

    def __init__(self, dimensiones = (11, 11)):

        self.dimensiones = dimensiones #seleccionamos las dimensiones de preferencia del jugador. Son 10x10 por defecto si no se indican

        self.tablero_humano = np.full(self.dimensiones, '  ') #generamos un array con las dimensiones del tablero especificadas y conformado por str de longitud 3

        self.tablero_humano_reflejo = np.full(self.dimensiones, '  ')

        self.tablero_maquina = np.full(self.dimensiones, '  ')

        self.tablero_maquina_reflejo = np.full(self.dimensiones, '  ')

        self.formato_letras_numeros()

    def __str__(self):
        
        print('\nESCENARIO ENEMIGO')
        for index_row, row in enumerate(self.tablero_humano_reflejo):
            if index_row == 1:
                print('\n', '+====='*len(self.tablero_humano_reflejo), '+', sep='')
            else:
                print('\n', '+-----'*len(self.tablero_humano_reflejo), '+', sep='')

            for index_col, col in enumerate(self.tablero_humano_reflejo):
                if index_col == 0:
                    print('|', self.tablero_humano_reflejo[index_row][index_col], '|', end = '')
                elif len(self.tablero_humano_reflejo[index_row][index_col]) == 1:
                    print('|', f' {self.tablero_humano_reflejo[index_row][index_col]}', ' ', end = '')
                else:
                    print('|', self.tablero_humano_reflejo[index_row][index_col], ' ', end = '')
                
            print('|', end = '')
        print('\n', '+-----'*len(self.tablero_humano_reflejo), '+', sep='')

        print('\nNUESTRO ESCENARIO')

        for index_row, row in enumerate(self.tablero_humano):
            if index_row == 1:
                print('\n', '+====='*len(self.tablero_humano), '+', sep='')
            else:
                print('\n', '+-----'*len(self.tablero_humano), '+', sep='')

            for index_col, col in enumerate(self.tablero_humano):
                
                if index_col == 0:
                    print('|', self.tablero_humano[index_row][index_col], '|', end = '')
                elif len(self.tablero_humano[index_row][index_col]) == 1:
                    print('|', f' {self.tablero_humano[index_row][index_col]}', ' ', end = '')
                else:
                    print('|', self.tablero_humano[index_row][index_col], ' ', end = '')
               
                
            print('|', end = '')
        print('\n', '+-----'*len(self.tablero_humano), '+', sep='')
        
        return ('\nSiguiente operacion?')
        

    def formato_letras_numeros(self):

        letras = [' ' + chr(x) for x in range(65, 64 + len(self.tablero_humano))]
        numeros = [x for x in range(1, len(self.tablero_humano))]
        tableros = [self.tablero_humano,
                    self.tablero_humano_reflejo,
                    self.tablero_maquina,
                    self.tablero_maquina_reflejo]

        for board in tableros:
            
            for index_row, row in enumerate(board[1:]):
                
                row[0] = f'{letras[index_row]}'

            board[0, 1:] = np.array(numeros)
