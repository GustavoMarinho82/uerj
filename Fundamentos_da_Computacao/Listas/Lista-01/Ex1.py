# Lista 1 - Exercício 1

idades = []
sexos = []
salarios = []
contador = 1
media_salarial_M = media_salarial_F = maior_salario_jovem = 0

while (True):
    idade = int(input("Digite a idade do trabalhador n° {} (Digite uma idade negativa para finalizar a leitura de dados) \n".format(contador)))
    if (idade<0):
        break

    sexo = input("Digite a sexo do trabalhador n° {} (M ou F) \n".format(contador))
    salario = float(input("Digite o salário do trabalhador n° {} \n".format(contador)))

    idades.append(idade)
    sexos.append(sexo)
    salarios.append(salario)
    contador+=1


if (len(idades) != 0):

    for i in range(len(salarios)):
        if (sexos[i] == 'M'):
            media_salarial_M+= salarios[i]

        elif (sexos[i] == 'F'):
            media_salarial_F+= salarios[i]

        if (idades[i] < 30):
            maior_salario_jovem = salarios[i]

    if (sexos.count('M') != 0): 
        media_salarial_M /= sexos.count('M')

    if (sexos.count('F') != 0):
        media_salarial_F /= sexos.count('F')


    print("Média salarial dos homens: {} \nMédia salarial das mulheres: {}". format(media_salarial_M, media_salarial_F))

    if (maior_salario_jovem > 0 ):
        print("Maior salário entre os trabalhadores com menos de 30 anos:", maior_salario_jovem)

    else:
        print("Nehum trabalhador com menos de 30 anos registrado")