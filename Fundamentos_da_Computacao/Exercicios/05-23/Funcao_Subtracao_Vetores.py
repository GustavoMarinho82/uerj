# Ler dois vetores de tamanho inderminado e exibir os valores existentes no primeiro que não estão no segundo

def ler_vetor(nome):
    vetor = []
    tamanho = int(input(f"Digite o tamanho do {nome}: "))

    for i in range(tamanho):
        valor = int(input(f"Digite um valor para a coordenada {i}: "))
        vetor.append(valor)
        
    return vetor
    
def subtracao_vetores(v1, v2):
    vetor_resultante = []
    
    for valor in v1:
        if (valor not in v2):
            vetor_resultante.append(valor)
        
    
    if (len(vetor_resultante) != 0):
        return vetor_resultante
    
    else:
        return "Nenhum"

# PROGRAMA

vetor1 = ler_vetor("Vetor 01")
vetor2 = ler_vetor("Vetor 02")

print("\nVetor 01:", vetor1)
print("Vetor 02:", vetor2)
print("Valores que estão no Vetor 01 e não no Vetor 02:", subtracao_vetores(vetor1, vetor2))
