# Escreva uma função que receba um dicionário e retorne um dicionario com as chaves trocadas pelos valores e vice-versa

def ler_dicionario():
    dicionario = {}
    tamanho = int(input(f"Quantos itens o dicionário vai ter?: "))
    
    for i in range(tamanho):
        chave = input(f"\nDigite uma chave para {(i+1)}º valor: ")
        valor = input(f"Digite um valor para a chave {chave}: ")
        
        dicionario[chave] = valor
        
    return dicionario


def inverter_dicionario(dicionario):
    d_invertido = {}

    for chave, valor in dicionario.items():
        d_invertido[valor] = chave

    return d_invertido


# PROGRAMA

dicionario = ler_dicionario()
d_invertido = inverter_dicionario(dicionario)

print("\nDicionário Original: ", dicionario)
print("Dicionário Invertido: ", d_invertido)
