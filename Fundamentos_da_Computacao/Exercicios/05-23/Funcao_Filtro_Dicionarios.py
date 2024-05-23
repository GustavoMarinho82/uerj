# Escreva uma função que receba dois dicionários e que filtre e mantenha apenas os valores >=2

def ler_dicionario(nome):
    dicionario = {}
    tamanho = int(input(f"\nQuantos itens o {nome} vai ter?: "))
    
    for i in range(tamanho):
        chave = input(f"\nDigite uma chave para {(i+1)}º valor: ")
        valor = int(input(f"Digite um valor para a chave {chave}: "))
        
        dicionario[chave] = valor
        
    return dicionario


def filtro(d, d_filtrado):
    for chave, valor in d.items():
        if (valor >= 2):
            d_filtrado[chave] = valor


def filtrar_dicionarios(d1, d2):
    d_filtrado = {}
    
    filtro(d1, d_filtrado)
    filtro(d2, d_filtrado)
    
    return d_filtrado

  
# PROGRAMA

d1 = ler_dicionario("Dicionário 01")
d2 = ler_dicionario("Dicionário 02")
d_filtrado = filtrar_dicionarios(d1, d2)

print("\nDicionário 01: ", d1)
print("Dicionário 02: ", d2)
print("Dicionário Filtrado: ", d_filtrado)
