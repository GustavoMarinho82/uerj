# Quantidade de alunos com mais de 13 anos e menores que a altura média

# [[idade1, altura1], [idade2, altura2], ...]
# Tive que botar o _ porque o progamiz não tava permitindo usar o .append()
alunos_ = []
altura = contador = altura_media = 0

for i in range(5):
    idade = int(input("Digite a idade do aluno n° {}\n".format(i+1)))
    altura = float(input("Digite a altura do aluno n° {}\n".format(i+1)))
    
    alunos_.append([idade, altura])
    altura_media += altura

altura_media /= len(alunos_)

for [i, h] in alunos_:
    if (i > 13) and (h < altura_media):
        contador+= 1
    
print("Vetor dos alunos: {}\n Altura média: {} \nN° de alunos com mais de 13 anos e altura inferior a média: {}".format(alunos_, altura_media, contador))
