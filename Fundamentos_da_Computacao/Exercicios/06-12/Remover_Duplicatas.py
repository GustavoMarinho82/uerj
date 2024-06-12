# Criar uma função para remover as dulpicatas de uma lista de inteiros, mantendo a ordem original

def remover_duplicatas(lista):
    nova_lista = []
    
    for elemento in lista:
        if (elemento not in nova_lista):
            nova_lista.append(elemento)

    return nova_lista
    
lista = [1, 3, 2, 1, 3, 4, 5, 6, 5, 2, 6, 8, 7, 1, 8, 7]

print(remover_duplicatas(lista))
