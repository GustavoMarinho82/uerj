# Crie um função que retorne a soma dos elementos da diagonal secundária de uma matriz quadrada

def soma_diagonal_secundaria(matriz):
    soma = 0
    
    for x in range(len(matriz)):
        soma += matriz[x][len(matriz)-1 -x]
    
    return soma


matriz = [[1, 2, 3] ,[4, 5, 6], [7, 8, 9]]

print(soma_diagonal_secundaria(matriz))
