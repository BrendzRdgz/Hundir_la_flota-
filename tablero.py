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
                
                print('| ', self.tablero_humano_reflejo[index_row][index_col], ' ', end = '')
                
            print('|', end = '')
        print('\n', '+-------'*len(self.tablero_humano_reflejo), '+', sep='')

        print('\nNUESTRO ESCENARIO')

        for index_row, row in enumerate(self.tablero_humano):
            print('\n', '+-------'*len(self.tablero_humano), '+', sep='')
            for index_col, col in enumerate(self.tablero_humano):
                
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
        

tablero_1 = Tablero()

tablero_1.tablero_humano[1][1] = ' - '
tablero_1.tablero_humano[2][3] = ' O '
tablero_1.tablero_humano[2][4] = ' X '
tablero_1.tablero_humano[5][7] = ' X '
print(tablero_1)
