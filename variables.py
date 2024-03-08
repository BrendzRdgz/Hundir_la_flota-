from clases import*

tablero_1 = Tablero()
juego_activo = True
abecedario = 'abcdefghijklmnopqrstuvwxyz-#$%&/ç|><'
orientaciones = ["N","S","Oe","E"]
lista_de_barcos = []
lista_de_barcos_maquina = []
disparos = []
disparos_maquina = []
aciertos = []
dimensiones = 10       #se puede ampliar hasta todo el alfabeto (tablero 26x26), el código está preparado para ello