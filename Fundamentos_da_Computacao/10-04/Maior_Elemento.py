# Maior elemento de um vetor de inteiros

vetor1 = [0]*5

for i in range(len(vetor1)):
    vetor1[i] = int(input("Escreva um valor para a coordenada {}\n".format(i)))
    
maior_valor = vetor1[0]

for i in range(len(vetor1)):
    if (vetor1[i] > maior_valor):
        maior_valor = vetor1[i]

print("Vetor: {} \nO maior valor é: {}".format(vetor1, maior_valor))
