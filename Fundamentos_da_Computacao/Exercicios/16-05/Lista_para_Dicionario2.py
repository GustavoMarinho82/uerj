#Receber uma lista de palavras e tranformá-la em um dicionario tipo {"palavra": quantas_vezes_aparece, ...}

lista_palavras = []
dicionario = {}
tamanho = int(input("Digite o tamanho da lista de palavras: "))

for x in range(tamanho):
    valor = input(f"Digite a palavra número {(x+1)}: ")
    lista_palavras.append(valor)
    
for palavra in lista_palavras:
    dicionario[palavra] = lista_palavras.count(palavra)

print(f"\nLista: {lista_palavras}")
print(f"Dicionario: {dicionario}")
