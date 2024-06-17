""" 
Escreva uma função que recebe uma matriz de inteiros e retorna uma lista contendo os elementos que formam a fronteira da matriz. 
A fronteira é composta pelos elementos da primeira e última linhas, bem como primeira e última coluna, excluindo os elementos já considerados das linhas.
 Obs1: Coloque a matriz direto no código 
 Obs2: Não pergunte as dimensões ao usuário 
"""

def fronteira_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    fronteira = []
    
    fronteira += [matriz[0][coluna] for coluna in range(colunas) if (matriz[0][coluna] not in fronteira)]
    fronteira += [matriz[linha][0] for linha in range(linhas) if (matriz[linha][0] not in fronteira)]
    
    fronteira += [matriz[(linhas - 1)][coluna] for coluna in range(colunas) if (matriz[(linhas - 1)][coluna] not in fronteira)]
    fronteira += [matriz[linha][(colunas - 1)] for linha in range(linhas) if (matriz[linha][(colunas - 1)] not in fronteira)]
    
    return sorted(fronteira) # sorted() -> ordena numericamente

    """ OU
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    fronteira = set()
    
    for x in range(linhas):
        for y in range(colunas):
            if (x in [0, (linhas - 1)]) or (y in [0, (colunas - 1)]):
                fronteira.add(matriz[x][y])
                
    return sorted(list(fronteira))
    """

matriz = [[1, 2, 3, 4], [5, 6, 7, 1], [9, 10, 11, 12], [13, 14, 15, 2]]
    
print(fronteira_matriz(matriz))