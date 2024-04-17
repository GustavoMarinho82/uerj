# Lista 1 - Exercício 10

soma_primeiros_20_pares = 0

for i in range(1, 21):
    soma_primeiros_20_pares += (i*2)

print(soma_primeiros_20_pares)

#OU

soma_primeiros_20_pares = 0

for i in range(2, 41, 2):
    soma_primeiros_20_pares += (i)

print(soma_primeiros_20_pares)

#OU

soma_primeiros_20_pares = ((2 + 40)*20)/2
print(soma_primeiros_20_pares)