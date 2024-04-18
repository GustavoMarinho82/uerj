# Lista 1 - Exercício 5
produtos = [] #Conteúdo -> [[descricao, preço, quantidade], [...], ...]
total_gasto = maior_preco = descricao_mais_caro = 0

for i in range(10):
    descricao = input(f"Digite a descrição do produto n° {i+1}: ")
    preco = float(input("Digite o preço unitário desse produto: "))
    qtd = int(input("Digite quantos desse produto foram comprados: "))

    produtos.append([descricao, preco, qtd])

    total_gasto += (preco*qtd)

    if (preco > maior_preco): #Considerando que não produto com preço <= 0
        maior_preco = preco
        descricao_mais_caro = descricao


print(f"Gasto total: R${total_gasto}")
print(f"Descrição do produto mais caro: {descricao_mais_caro}")