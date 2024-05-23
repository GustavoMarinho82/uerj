# Escreva uma função que busque um valor específico em uma matriz

def ler_matriz():
    matriz = []
    
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))
    
    for x in range(linhas):
        matriz.append([])
        
        for y in range(colunas):
            valor = int(input(f"Digite um valor para a coordenada [{x}][{y}]: "))
            matriz[x].append(valor)
            
    return matriz
    
def buscar_numa_matriz(valor, matriz):
    coordenadas = []
    
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if (valor == matriz[x][y]):
                coordenadas.append(f"[{x}][{y}]")
    
    return coordenadas

# PROGRAMA

matriz = ler_matriz()

valor = int(input("Digite um valor que será procurado na matriz: "))

print("O valor aparece nas coordenadas: ")

for coordenada in buscar_numa_matriz(valor, matriz):
    print(coordenada)
