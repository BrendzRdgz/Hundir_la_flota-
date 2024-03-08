# Battleship

Juego de hundir la flota desarrollado usando numpy. El objetivo del juego es hundir todos los barcos del enemigo, antes de que él consiga hundir los tuyos.

**¡El primer jugador en quedarse sin barcos pierde!**

## Instrucciones

* Hay dos jugadores: tú y la máquina

* El tablero es de 10x10. 

* Hay un total de 10 barcos

    * 1 portaaviones que ocupa 4 espacios
    * 2 acorazados que ocupan 3 espacios cada uno
    * 3 fragatas que ocupan 2 espacios cada una
    * 4 submarinos que ocupan 1 espacio cada uno
  
* Los barcos se colocan de manera aleatoria

* No puede haber dos barcos en la misma posición. 

* En cada turno, puedes disparar a una coordenada en la que no hayas disparado antes.
  1) Si das a uno de los barcos del contrincante, te vuelve a tocar
  2) Si fallas, y tu disparo cae al agua, le toca disparar a la máquina
  
## El tablero
El tablero está compuesto de 10 columnas (A-J), y 10 filas (1-10). Los barcos se colocan de forma aleatoria al iniciar la partida.
```
                    A B C D E F G H I J
                    -------------------
                 1 |O                  |
                 2 |          O O      |
                 3 |            O   O  |
                 4 |                O  |
                 5 |                   |
                 6 |                   |
                 7 |    O O O     O    |
                 8 |  O O O   O   O    |
                 9 |              O    |
                10 |  O O         O   O|
                    -------------------
```
Las "O" presentes en el tablero son los barcos.  

Cuando se dispara, si el impacto da en uno de los barcos del enemigo, este impacto se mostrará con una "X" en el tablero. En caso contrario, se mostrará un guion "-". 

En el siguiente caso, el jugador ha dado a uno de los barcos en la posición H8 del enemigo, pero al disparar a la posición D5 ha fallado.

```
                    A B C D E F G H I J
                    -------------------
                 1 |                   |
                 2 |                   |
                 3 |                   |
                 4 |                   |
                 5 |      -            |
                 6 |                   |
                 7 |                   |
                 8 |              X    |
                 9 |                   |
                10 |                   |
                    -------------------
```

Un tablero en una fase más adelantada del juego puede parecer así

```
                    A B C D E F G H I J
                    -------------------
                 1 |X   -     -       -|
                 2 |-         X       -|
                 3 |-           X   X -|
                 4 |-       -       X -|
                 5 |-   -     -     -  |
                 6 |- -     -   -  -  -|
                 7 |  -   X X         -|
                 8 |    X X -         -|
                 9 |        -         -|
                10 |        -          |
                    -------------------
```

## Recursos utilizados
* Lenguaje utilizado: Python 3.9.5
  * Librerías: 
    * numpy 
    * random
    * time
    * copy

## Contribuidores
Este proyecto ha sido elaborado por:
 <ol>
  <li> Fran Pujalte
  <li> Fran Pastor
  <li> Raúl Soler
  <li> Brenda Rodríguez
    
  </li>
</ol> 
