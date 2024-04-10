# Receber um vetor e imprimir outro

vetor_entrada = [0]*5

for i in range(len(vetor_entrada)):
    vetor_entrada[i] = int(input("Escreva um valor para a coordenada {}\n".format(i)))
    
vetor_saida = vetor_entrada[::-1]
print("Vetor de saída: ", vetor_saida)
