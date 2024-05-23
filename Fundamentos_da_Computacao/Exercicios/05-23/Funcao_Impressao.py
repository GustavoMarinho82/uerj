# Escreva uma função que imprima (...) baseando-se em um número n informado

def impressao_estranha(n):
    for i in range(1, (n+1)):
        for _ in range(i):
            print(i, end=" ")
        
        print("")

# PROGRAMA

n = int(input("Digite um número: "))

impressao_estranha(n)
