# Ler dois vetores e unir-los em um vetor composto, intercalando os valores

vetor1 = []
vetor2 = []
vetor_composto = []

for i in range(10):
    input1 = int(input("Digite um valor para o Vetor1 na coordenada {}\n".format(i)))
    input2 = int(input("Digite um valor para o Vetor2 na coordenada {}\n".format(i)))
    
    vetor1.append(input1)
    vetor2.append(input2)
    vetor_composto.append(input1)
    vetor_composto.append(input2)

    
print("Vetor1: {} \nVetor2: {} \nVetor Composto: {}".format(vetor1, vetor2, vetor_composto))
