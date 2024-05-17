#Transformar uma lista em uma tupla

lista = []
tamanho = int(input("Digite o tamanho da lista: "))

for x in range(tamanho):
    valor = input(f"Digite o que a lista vai armazenar na posição [{x}]: ")
    lista.append(valor)
    
tupla = tuple(lista)

#print(f"\nLista: {lista} \nTupla: {tupla}")
print("\nLista: ", lista)
print("Tupla: ", tupla)
