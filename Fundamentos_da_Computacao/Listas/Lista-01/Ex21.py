# Lista 1 - Exercício 21

print("Somatório de i=1 até n de (1/i)")
n = int(input("Digite um numero para n: "))
somatorio = 0

for i in range(1, n+1):
    somatorio+= (1/i)

print("Resultado:", somatorio)