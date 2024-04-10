# Receber vetores e uni-los

vetor1 = [0]*3
vetor2 = [0]*3
vetor_unido = []

for i in range(len(vetor1)):
    vetor1[i] = int(input("Escreva um valor para Vetor1 na coordenada {}\n".format(i)))
    vetor2[i] = int(input("Escreva um valor para Vetor2 na coordenada {}\n".format(i)))
    
    vetor_unido.append(vetor1[i])

#for i in range(len(vetor1)):
#    vetor_unido.append(vetor1[i])
    
for i in range(len(vetor2)):
    vetor_unido.append(vetor2[i])
    
print("Vetor unido: ", vetor_unido)
