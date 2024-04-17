numero = int(input("Digite um número: "))
fatorial = 1

for i in range(numero, 0, -1):
    fatorial *= i

print(f"O fatorial do número é: {fatorial}")