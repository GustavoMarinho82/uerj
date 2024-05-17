#Desafio 02

matriz = []
identidade = True #Diz se a matriz é uma matriz identidade

linhas = int(input("Quantas linhas?: "))
colunas = int(input("Quantas colunas?: "))

for x in range(linhas):
    matriz.append([])
    
    for y in range(colunas):
        valor = int(input(f"Digite um valor para [{x}][{y}]: "))
        matriz[x].append(valor)
        
        if ((x == y) and (valor != 1)) or ((x != y) and (valor !=0)):
            identidade = False

if (identidade):
    print("A matriz é uma matriz identidade")
    
else:
    print("A matriz não é uma matriz identidade")

