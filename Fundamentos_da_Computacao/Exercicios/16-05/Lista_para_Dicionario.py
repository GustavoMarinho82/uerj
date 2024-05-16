#Transformar uma lista em um dicionário

lista = []
dicionario = {}
tamanho = int(input("Digite o tamanho da lista: "))

for x in range(tamanho):
    valor = input(f"Digite o que a lista vai armazenar na posição [{x}]: ")
    lista.append(valor)
    
# Daria pra botar o conteúdo desse for dentro do for anterior, mas assim é mais visível
for x in range(tamanho):
    dicionario[x] = lista[x]

print(f"\nLista: {lista}")
print(f"Dicionario: {dicionario}")
