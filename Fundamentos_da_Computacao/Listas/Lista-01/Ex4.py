# Lista 1 - Exercício 4

nomes = []
precos = []
contador = 1

while (True):
    nome = input("Digite o nome do produto n° {} (Digite XXX para finalizar o algoritmo) \n".format(contador))
    if (nome == 'XXX'):
        break

    preco = float(input("Digite o preço do produto n° {} (Não digite preços repetidos) \n".format(contador)))
    if (preco in precos):
        print("Um produto de mesmo preço já foi registrado!")
        continue

    nomes.append(nome)
    precos.append(preco)
    contador += 1
    
if (contador > 1):
    print("Nome do produto mais caro:", nomes[precos.index(max(precos))])