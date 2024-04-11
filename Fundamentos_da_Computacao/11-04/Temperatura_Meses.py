# Calcule a média anual da temperatura e diga quais meses apresentaram temperaturas acima da média

ano = {"Janeiro": 0, "Fevereiro": 0, "Março": 0, "Abril": 0, "Maio": 0, "Junho": 0, "Julho": 0, "Agosto": 0, "Outubro": 0, "Setembro": 0, "Novembro": 0, "Dezembro": 0}

temp_media = 0

for mes in ano.keys():
    temp = float(input("Digite a temperatura do mês de {}\n".format(mes)))
    
    temp_media += temp
    ano[mes] = temp
    
temp_media /= 12

print("Temperatura média: {} \nMeses em que as temperaturas ficaram acima da média: ".format(temp_media))

for mes in ano:
    if (ano.get(mes) > temp_media):
        print(mes)
