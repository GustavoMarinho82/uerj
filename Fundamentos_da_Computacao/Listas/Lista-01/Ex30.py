# Lista 1 - Exercício 30 EM PRODUÇÃO

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #até 100
potencia_fatores = []

n = int(input("Digite um número: "))
n_intermediario = n

for i in primos:
    if (n_intermediario != 1):

        if(n_intermediario//i != 0):
            potencia_fatores.append(n_intermediario//i)
            n_intermediario = n_intermediario%i

        else:
            potencia_fatores.append(0)

    else:
        break

print(f"Fatoração de {n}: ")

for i in range(len(potencia_fatores)):
    if (potencia_fatores[i] != 0):
        print(f"{primos[i]}^{potencia_fatores[i]}")

print(potencia_fatores)