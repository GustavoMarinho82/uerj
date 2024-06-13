# Crie uma funcção que inverta suas chaves com seus valores. Suponha que os valores do dicionário orioginal são únicos

def inverter_dicionario(dicionario):
    dicionario_invertido = {}
    
    for chave, valor in dicionario.items():
        dicionario_invertido[valor] = chave
        
    return dicionario_invertido
    

dicionario = {'a': 1, 'b': 2, 'c': 3}

print("Dicionário:", dicionario)
print("Dicionário invertido:", inverter_dicionario(dicionario))

