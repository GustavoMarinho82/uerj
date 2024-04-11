# Ler um vetor de reais e imprimir seus valores ao contrário

vetor = []

for i in range(10):
    input_ = float(input("Digite um valor para a coordenada {}\n".format(i)))
    vetor.append(input_)
    
for i in vetor[::-1]:
    print(i)
