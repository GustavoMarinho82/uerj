# Escreva uma função que procure por um valor num dicionario e retorne a chave correspondente ao valor

def ler_dicionario():
    dicionario = {}
    tamanho = int(input(f"Quantos itens o dicionário vai ter?: "))
    
    for i in range(tamanho):
        chave = input(f"\nDigite uma chave para {(i+1)}º valor: ")
        valor = input(f"Digite um valor para a chave {chave}: ")
        
        dicionario[chave] = valor
        
    return dicionario


def encontrar_valor(dicionario, termo):
    chaves = []
    
    for chave, valor in dicionario.items():
        if (valor == termo):
            chaves.append(chave)
    
    return chaves


# PROGRAMA

dicionario = ler_dicionario()

termo = input("\nDigite um termo que será procurado no dicionário: ")
chaves = encontrar_valor(dicionario, termo)


print("\nDicionário: ", dicionario)
print("Chaves que levam ao termo: ")

for chave in chaves:
    print(chave)
