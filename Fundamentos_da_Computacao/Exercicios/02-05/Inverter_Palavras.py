#Imprimir cada palavra que foi digitada na ordem inversa

palavras = ""
while (True):
    palavra = input("Digite uma palavra (Digite 'sair' para parar o programa): ")
    
    if (palavra.lower() == "sair"):
        break
    
    palavras += palavra[::-1] + "\n"

print(f"Palavras invertidas: \n{palavras}")
