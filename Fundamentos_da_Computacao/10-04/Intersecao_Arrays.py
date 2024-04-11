# Imprimir a interseção de dois vetores

vetor1 = [0]*3
vetor2 = [0]*3
vetor_intersecao = []

for i in range(len(vetor1)):
    vetor1[i] = int(input("Escreva um valor para Vetor1 na coordenada {}\n".format(i)))
    vetor2[i] = int(input("Escreva um valor para Vetor2 na coordenada {}\n".format(i)))
    
for x in vetor1:
    if (x in vetor2) and not (x in vetor_intersecao):
        vetor_intersecao.append(x)

print("Vetor1: {} \nVetor2: {} \nInterceção dos vetores: {}".format(vetor1, vetor2, vetor_intersecao))
