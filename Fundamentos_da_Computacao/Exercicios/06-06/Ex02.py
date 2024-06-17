# Escreva uma função que recebe dois vetores de mesmo comprimento e retorna True se os vetores forem ortogonais e False caso contrário. 2 vetores são ortogonais se seu produto escalar é 0.

def sao_ortogonais(vetor1, vetor2):
    if (len(vetor1) != len(vetor2)):
        return False
    
    else:
        produto_escalar = 0
        
        for i in range(len(vetor1)):
            produto_escalar += (vetor1[i] * vetor2[i])
            
        return True if (produto_escalar == 0) else False
    

vetor1 = [0, 2, 3]
vetor2 = [1, -6, 4]
vetor3 = [1, 1, 1]
vetor4 = [0, 0]

print("Vetores 01 e 02 são ortogonais:", sao_ortogonais(vetor1, vetor2))
print("Vetores 02 e 03 são ortogonais:", sao_ortogonais(vetor2, vetor3))
print("Vetores 03 e 04 são ortogonais:", sao_ortogonais(vetor3, vetor4))