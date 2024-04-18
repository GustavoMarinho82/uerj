# Lista 1 - Exercício 13
# Sem armazenar as idades
idade_media = total_idades = idades_21_65 = 0

print("(Digite -1 para parar a leitura de dados)")

while (True):
    idade = int(input("Digite uma idade: "))
    if (idade >= 21) and (idade < 65): # >=21 porque é muito difícil uma pessoa ter exatamente 21 anos (sem dias/meses a mais), e quem tem 21 anos e 11 meses vai inserir só 21 anos
        idades_21_65 +=1

    elif (idade == -1):
        break

    idade_media += idade
    total_idades += 1


if (total_idades != 0):
    idade_media /= total_idades
    
    print("Idade média:", idade_media)
    print("Porcentagem de idades entre 21 e 65: {:0<5}%".format((idades_21_65 / total_idades)*100))