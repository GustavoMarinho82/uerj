# Ler um vetor e separar os pares dos ímpares

vetor = []
vetor_pares = []
vetor_impares = []

for i in range(20):
    input_ = int(input("Digite um valor para a coordenada {}\n".format(i)))
    vetor.append(input_)
    
    if (input_%2 == 0):
        vetor_pares.append(input_)
    else:
        vetor_impares.append(input_)

print("Vetor: {} \nVetor de Pares: {} \nVetor de Ímpares: {}".format(vetor, vetor_pares, vetor_impares))
