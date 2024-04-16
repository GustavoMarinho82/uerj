# Lista 1 - Exercício 6

a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
soma = 0

if (a<=b):
    for i in range(a+1, b):
        soma += i

    print("Soma entre A e B =", soma)

else:
    print("A>B, a soma não será realizada")