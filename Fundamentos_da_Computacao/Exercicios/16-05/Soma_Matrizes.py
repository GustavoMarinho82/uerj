#Receba duas matrizes e some as duas

matriz1 = []
matriz2 = []

linhas = int(input("Digite o número de linhas das matrizes: "))
colunas = int(input("Digite o número de colunas das matrizes: "))

for x in range(linhas):
    matriz1.append([])
    
    for y in range(colunas):
        valor = int(input(f"Matriz 01 [{x}][{y}]: "))
        
        matriz1[x].append(valor)
        
for x in range(linhas):
    matriz2.append([])
    
    for y in range(colunas):
        valor = int(input(f"Matriz 02 [{x}][{y}]: "))
        
        matriz2[x].append(valor)

print("\nSOMA DAS MATRIZES")

for x in range(linhas):
    for y in range(colunas):
        soma = matriz1[x][y] + matriz2[x][y]
        print("|{:^5}".format(soma), end="")
    
    print("|")
