# Lista 1 - Exercício 7

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
soma = 0

if (a<=b):
    for i in range(a+1, b):
        if (i%4 == 0):
            soma += i

    print("Soma dos múltiplos de 4 entre A e B =", soma)

else:
    print("A>B, a soma não será realizada")