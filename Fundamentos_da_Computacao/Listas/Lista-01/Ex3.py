# Lista 1 - Exercício 3
contador = par = impar = media_pares = 0
while (True):
    numero = int(input("Digite um numero inteiro (Digite 0 para finalizar o algoritmo)\n"))
    if (numero == 0):
        break

    if (numero%2 == 0):
        par += 1
        media_pares += numero

    else:
        impar += 1

    contador += 1

media_pares /= contador

print("Qtd de pares: {} \nQtd de ímpares: {} \nMédia dos pares: {}".format(par, impar, media_pares))