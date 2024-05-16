#Receber uma matriz e imprimir a transposta dela

matriz = []
linhas = int(input("Quantas linhas?: "))
colunas = int(input("Quantas colunas?: "))

for x in range(linhas):
    matriz.append([])
    
    for y in range(colunas):
        valor = int(input(f"Digite um valor para [{x}][{y}]: "))
        matriz[x].append(valor)
        
print("MATRIZ")
for x in range(linhas):
    for y in range(colunas):
        print("|{:^3}".format(matriz[x][y]), end="")
        
    print("|")
    
print("MATRIZ TRANSPOSTA")
for x in range(colunas):
    for y in range(linhas):
        print("|{:^3}".format(matriz[y][x]), end="")
        
    print("|")
