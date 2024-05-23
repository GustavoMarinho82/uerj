# Escreva uma função que receba duas palavras e retorne uma string dizendo se a primeira é prefixa da segunda

def eh_prefixo(p1, p2):
    if (p1.lower() == p2[0:len(p1)].lower()):
        return f"{p1} é prefixo de {p2}"
        
    else:
        return f"{p1} não é prefixo de {p2}"

# PROGRAMA

p1 = input("Digite uma palavra: ")
p2 = input("Digite outra palavra: ")

print(eh_prefixo(p1, p2))
