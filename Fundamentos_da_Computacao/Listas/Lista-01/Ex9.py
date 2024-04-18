# Lista 1 - Exercício 9

qtd_respostas = 5
sims = naos = invalidas = 0

for i in range(qtd_respostas):
    resposta = input("Você é um consumidor e está satisfeito?: ")

    if (resposta.lower() == "sim") or (resposta.lower() == "s"):
        sims += 1
    
    elif (resposta.lower() == "não") or (resposta.lower() == "nao") or (resposta.lower() == "n"):
        naos += 1
    
    else:
        invalidas += 1
        print("Resposta inválida")


print("Respostas:")
print("Sim - {:0<5}%".format((sims/qtd_respostas*100)))
print("Não - {:0<5}%".format((naos/qtd_respostas*100)))
print("Inválidas - {:0<5}%".format((invalidas/qtd_respostas*100)))