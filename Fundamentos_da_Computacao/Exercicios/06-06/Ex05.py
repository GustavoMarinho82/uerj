# Escreva uma função que recebe uma lista de palavras e um número inteiro, e retorne um dicionário no qual 
# os primeiros números são caracteres de cada palavra e os valores são as listas de palavras que começam com aquele prefixo.

def dicionario_prefixos(palavras, tamanho_prefixo):
    dic_prefixos = {}
    prefixos = [palavra[0:tamanho_prefixo] for palavra in palavras]
    
    """ OU
    prefixos = []
    for palavra in palavras:
        prefixos.append(palavra[0:tamanho_prefixo])
    """
    
    # sets não aceitam valores repetidos, eliminando esses valores
    for prefixo in set(prefixos):
        dic_prefixos[prefixo] = prefixos.count(prefixo)
        
    return dic_prefixos


palavras = ["abacate", "abacaxi", "cenoura", "senhor", "abelha", "centavo"]

print(dicionario_prefixos(palavras, 1))
print(dicionario_prefixos(palavras, 2))
print(dicionario_prefixos(palavras, 3))
print(dicionario_prefixos(palavras, 4))
print(dicionario_prefixos(palavras, 5))