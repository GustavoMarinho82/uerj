# Escreva uma função recursiva que calcula a soma dos n primeiros números naturais

def soma_primeiros_naturais(quantos):
    if (quantos <= 0):
        return 0
    
    elif (quantos == 1):
        return 1
    
    else:
        return quantos + soma_primeiros_naturais(quantos - 1)


print(soma_primeiros_naturais(1))
print(soma_primeiros_naturais(2))
print(soma_primeiros_naturais(3))
print(soma_primeiros_naturais(4))
print(soma_primeiros_naturais(5))