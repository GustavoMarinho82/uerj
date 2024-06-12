# Crie uma função que encontre os elementos em comum em duas listas, mantendo a ordem de aparição da primeira

def elementos_em_comum(lista1, lista2):
    elementos_comum = []
    
    for elemento in lista1:
        if (elemento in lista2) and (elemento not in elementos_comum):
            elementos_comum.append(elemento)
    
    return elementos_comum
    
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [7, 1, 3, 0, 4, 9]

print("Elementos em comum: ", elementos_em_comum(lista1, lista2))
