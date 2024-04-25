# Selection sort - ordem decrescente

vetor = [5, 3, 4, 1, 2]
print("Vetor original:", vetor)

for x in range(0, len(vetor)):
    index_menor = x
    
    for y in range(x+1, len(vetor)):
        if(vetor[y] > vetor[index_menor]):
            index_menor = y
    
    valor_auxliar = vetor[x]
    vetor[x] = vetor[index_menor]
    vetor[index_menor] = valor_auxliar
    
    # print para mostar as mudanças do vetor durante o processo
    print(vetor)
