# Faça uma função que calcule a média dos elementos das posições pares de uma lista

# Nessa função, a primeira posição da lista é 0
def media_posicoes_pares(lista):
    media = 0
    elementos_media = (len(lista) - (len(lista)%2))/2
    
    for i in range(len(lista)):
        if (i%2 == 0):
            media += lista[i] / elementos_media

    return media
    
lista = [1, 2, 3, 4, 5, 6]

print(media_posicoes_pares(lista))
