#Receba uma matriz e um numero, e multiplique a matriz pelo numero

matriz = []

linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))
multiplicador = int(input("Digite um número para multiplicar toda a matriz: "))

for x in range(linhas):
    matriz.append([])
    
    for y in range(colunas):
        valor = int(input(f"Valor de [{x}][{y}]: "))
        
        matriz[x].append(valor)

print("\nMATRIZ RESULTANTE")

for x in range(linhas):
    for y in range(colunas):
        multiplicacao = matriz[x][y] * multiplicador
        print("|{:^5}".format(multiplicacao), end="")
    
    print("|")
