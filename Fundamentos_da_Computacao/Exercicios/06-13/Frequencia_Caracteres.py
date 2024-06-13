# Crie uma função que receba uma string e retorne um dicionário com os caracteres da string como chaves e com a frequência em que eles aparecem como os valores

def frequencia_chars(texto):
    frequencia_caracteres = {}
    texto_casefolded = texto.casefold()
    
    for letra in texto_casefolded:
        if (letra not in frequencia_caracteres.keys()):
            frequencia_caracteres[letra] = texto_casefolded.count(letra)

    return frequencia_caracteres
    
texto = "Hello World!"

print(frequencia_chars(texto))
