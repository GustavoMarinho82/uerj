#Desafio 01

personagens = [] #[[nome, forca, destreza, magia, media], ...]

linhas = int(input("Quantos personagens serão registrados?: "))

for x in range(linhas):
    nome = input(f"Nome do personagem {x+1}: ")
    forca = int(input(f"Força do personagem {x+1}: "))
    destreza = int(input(f"Destreza do personagem {x+1}: "))
    magia = int(input(f"Magia do personagem {x+1}: "))
    media = (forca + destreza + magia)/3
    
    personagens.append([nome, forca, destreza, magia, media])
    
print("|{:<10}|{:<10}|{:<10}|{:<10}|{:<10}|".format("Nome", "Força", "Destreza", "Magia", "Média"))

for personagem in personagens:
    print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(personagem[0], personagem[1], personagem[2], personagem[3], personagem[4]))
