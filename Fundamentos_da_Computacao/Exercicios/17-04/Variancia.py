# Feito originalmente no papel

subgrupos = [[0, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 100]]
qtd_idades = 10
idades = [0]*qtd_idades
qtd_idades_por_subgrupo = [0]*8
variancia = media = 0


for i in range(len(idades)):
    idades[i] = int(input(f"Digite a idade da pessoa n {i+1}: "))
    media += idades[i]

media /= qtd_idades


for j in range(len(idades)):
    for k in range(len(subgrupos)):
        if (subgrupos[k][0] <= idades[j]) and (idades[j] < subgrupos[k][1]):
            qtd_idades_por_subgrupo[k]  += 1


for xi in idades:
    variancia += (xi - media)**2

variancia = ((variancia / (qtd_idades-1)) ** (1/2))


for l in range(len(subgrupos)):
    print("N° de pessoas no subgrupo {} ({}<=idade<{}): {}".format((l+1), subgrupos[l][0], subgrupos[l][1], qtd_idades_por_subgrupo[l]))

print(f"Média de idades: {media} \nVariância: {variancia}")