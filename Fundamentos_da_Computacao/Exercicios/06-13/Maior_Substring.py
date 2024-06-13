# Faça uma função que encontre a substring mais longa em uma string. Exemplo de substring em uma string: string: "abcabcabcc" -> substring: "abc"

def maior_substring(palavra):
    maior = " "
    
    for x in range(len(palavra)):
        for y in range(x, len(palavra)):
            if (len(maior) < len(palavra[x:y])) and (palavra.count(palavra[x:y]) >= palavra.count(maior)):
                maior = palavra[x:y]

    return maior

palavra = "abc_palavra_abc_abc_palavra_abc"

print(maior_substring(palavra))
