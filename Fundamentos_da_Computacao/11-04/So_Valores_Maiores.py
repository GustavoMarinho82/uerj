# Vetor que só permite inserir um valor maior que o anterior

vetor = []
i = 0

print("Sempre digite um valor maior que o anterior")

while (i<5):
    valor = int(input("Digite um valor para a coordenada {}\n".format(i)))
    
    if (i == 0) or (valor > vetor[i-1]):
        vetor.append(valor)
        i+=1
    else:
        print("Valor menor ou igual ao anterior digitado!")
        
print("Vetor: ", vetor)
