# Bubble - ordem decrescente

vetor = [1, 5, 2, 4, 3]
print("Vetor original:", vetor)

for x in range(0, len(vetor)):
    for y in range(x+1, len(vetor)):
        if(vetor[y] > vetor[x]):
            valor_auxliar = vetor[x]
            vetor[x] = vetor[y]
            vetor[y] = valor_auxliar
            
            # print para mostar as mudanças do vetor durante o processo
            print(vetor)
