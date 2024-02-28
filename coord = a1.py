abecedario = 'abcdefghijklmnopqrstuvwxyz'
while True:
    coord = input('Introduce la coordenada donde quieras disparar (ejemplo: a1): ')
    letras = [char for char in coord]
    if letras [1] in abecedario or len(coord) != 2 or letras[0] not in abecedario:
        print('Introduce una coordenada válida porfa')
        continue
    diccionario_letras = {letra: indice + 1 for indice, letra in enumerate(abecedario)}
    for letra,numero in diccionario_letras.items():
        if letras[0] == letra:
            letras[0] = numero
    letras[1] = int(letras[1])
    break
print(letras)