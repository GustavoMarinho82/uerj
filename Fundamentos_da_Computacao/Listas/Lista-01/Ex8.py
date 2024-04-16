# Lista 1 - Exercício 8

Joao = Jose = Maria = Pedro = branco = nulo = 0

for i in range(1, 20001):
    voto = int(input(f"Digite o seu voto, eleitor n°{i}: "))

    match voto:
        case 0:
            branco += 1

        case 1:
            Joao += 1

        case 2:
            Jose += 1

        case 3:
            Maria += 1

        case 4:
            Pedro += 1

        case _:
            nulo += 1

print("Número de votos: \nJoão da Silva: {} \nJosé Ramalho: {} \nMaria Mattos: {} \nPedro Américo: {} \nBrancos: {} \nNulos: {}".format(Joao, Jose, Maria, Pedro, branco, nulo))