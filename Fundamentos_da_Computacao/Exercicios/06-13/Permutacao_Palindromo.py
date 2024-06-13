# Fazer uma função que determina se uma string é uma permutação de um palíndromo. Exemplo: "Saa" -> True (asa)

def frequencia_chars_texto(texto):
    frequencia_caracteres = {}
    texto_casefolded = texto.casefold()
    
    for letra in texto_casefolded:
        if (letra not in frequencia_caracteres.keys()):
            frequencia_caracteres[letra] = texto_casefolded.count(letra)

    return frequencia_caracteres
    
def permutacao_palindromo(palavra):
    frequencia_caracteres = frequencia_chars_texto(palavra)
    impar_de_vezes_ja_apareceu = False
    
    for valor in frequencia_caracteres.values():
        # Toda letra que aparecer na string tem que aparecer um número par de vezes, caso a string tenha um número par de caracteres
        if (valor%2 != 0):
            if (len(palavra)%2 == 0):
                return False
        
        # Se a string ter um número ímpar de caracteres, somente uma letra pode aparecer um número ímpar de vezes
            else:
                if (impar_de_vezes_ja_apareceu):
                    return False
                
                else:
                    impar_de_vezes_ja_apareceu = True

    return True


palavra1 = "Saa"
palavra2 = "Oaoa"
palavra3 = "Nao"

print("{} é uma permutação de um palíndromo: {}".format(palavra1, permutacao_palindromo(palavra1)))
print("{} é uma permutação de um palíndromo: {}".format(palavra2, permutacao_palindromo(palavra2)))
print("{} é uma permutação de um palíndromo: {}".format(palavra3, permutacao_palindromo(palavra3)))
