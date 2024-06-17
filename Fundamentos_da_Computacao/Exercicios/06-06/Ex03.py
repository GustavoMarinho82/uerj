# Escreva uma função que recebe uma string e retorna uma versão comprimida, na qual cada sequência de caracteres repetidos é substituída pelo caractere seguido pelo nº de repetições.
# String="aaabcccccaaa"
# saída="a3b1c5a3"

def comprimir_string(palavra):
    saida = ""
    letra_anterior = palavra[0]
    contagem = 0
    
    for i in range(len(palavra)):
        #Última iteração do for
        if (i == (len(palavra) - 1)):
            if (palavra[i] == letra_anterior):
                saida += (letra_anterior + str(contagem + 1))
                
            else:
                saida += (letra_anterior + str(contagem))
                saida += (palavra[i] + "1")
                
        elif (palavra[i] == letra_anterior):
            contagem += 1
            
        else:
            saida += (letra_anterior + str(contagem))
            contagem = 1
            letra_anterior = palavra[i]
            
    return saida 
            
            
print("aaabcccccaaa ->", comprimir_string("aaabcccccaaa"))
print("cbbba ->", comprimir_string("cbbba"))