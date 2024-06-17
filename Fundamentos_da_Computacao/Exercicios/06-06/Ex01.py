# Escreva uma função que recebe um vetor e um número inteiro e retorna um novo vetor, onde os números são rotacionados para a difeita N vezes. 
# A rotação para a direita significa que cada elemento é deslocado uma posição para a direita, e o último elemento volta para a primeira opção.

def rotacionar_direita(lista, vezes):
    nova_lista = [0, 0, 0, 0, 0]
    
    for i in range(len(lista)):
        coordenada = (i + vezes) if ((i + vezes) < len(lista)) else ((i + vezes)%len(lista))
        
        nova_lista[coordenada] = lista[i]

    return nova_lista
    

lista = [1, 2, 3, 4, 5]

print(rotacionar_direita(lista, 2))
# Esperado: [4, 5, 1, 2, 3]
