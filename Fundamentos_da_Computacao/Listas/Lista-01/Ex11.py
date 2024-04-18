# Lista 1 - Exercício 11
n = int(input("N primeiros números ímpares positivos. N: "))

if (n>=0):
    for i in range(1, (n*2), 2):
        print(i)

else:
    print("N não pode ser negativo")