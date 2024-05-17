matriz = []

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

for x in range(linhas):
    matriz.append([])
    
    for y in range(colunas):
        valor = int(input(f"Digite um valor para a coordenada [{x}][{y}]: "))
        matriz[x].append(valor)
        
for x in range(len(matriz)):
    for y in range(len(matriz)):
        print("|{: ^5}".format(matriz[x][y]), end="")
    
    print("|")
