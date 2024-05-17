# Verificar se duas matrizes são simétricas (matriz simétrica -> matriz original = matriz transposta)

# VARIAVÉIS
matriz1 = []
matriz2 = []
matriz1_t = []


# LEITURA DAS MATRIZES
linhas = int(input("Quantas linhas para a matriz 01?: "))
colunas = int(input("Quantas colunas para a matriz 01??: "))

for x in range(linhas):
    matriz1.append([])
    
    for y in range(colunas):
        valor = int(input(f"Matriz 01 [{x}][{y}]: "))
        matriz1[x].append(valor)


linhas = int(input("\nQuantas linhas para a matriz 02?: "))
colunas = int(input("Quantas colunas para a matriz 02??: "))

for x in range(linhas):
    matriz2.append([])
    
    for y in range(colunas):
        valor = int(input(f"Matriz 02 [{x}][{y}]: "))
        matriz2[x].append(valor)


# CRIANDO A TRANSPOSTA DA MATRIZ 01
linhas = len(matriz1)
colunas = len(matriz1[0])

for x in range(colunas):
    matriz1_t.append([])
    
    for y in range(linhas):
        matriz1_t[x].append(matriz1[y][x])


# VERIFICANDO SE A TRANSPOSTA É IGUAL À MATRIZ 02
if (matriz1_t == matriz2):
    print("\nAs duas matrizes são simétricas")
    
else:
    print("\nAs duas matrizes não são simétricas")
    
# print(matriz1)
# print(matriz2)
# print(matriz1_t)
