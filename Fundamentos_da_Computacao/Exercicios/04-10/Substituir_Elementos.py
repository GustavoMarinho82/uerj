# Substituir um elemento de um vetor

vetor1 = [0]*5

for i in range(len(vetor1)):
    vetor1[i] = int(input("Escreva um valor para Vetor1 na coordenada {}\n".format(i)))

substituido = int(input("Digite um valor que será substituído dos elementos do vetor\n"))
substituto = int(input("E agora, digite o valor que substituirá o outro\n"))

print("Vetor antes: ", vetor1)

for i in range(len(vetor1)):
    if (vetor1[i] == substituido):
        vetor1[i] = substituto

print("Vetor depois: ", vetor1)
