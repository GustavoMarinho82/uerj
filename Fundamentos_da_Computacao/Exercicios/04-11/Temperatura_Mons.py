# Menor, maior e média da lista de temperatura de Mons

temp_Mons = [-10, -8, 0, 1, 2, 5, -2, -4]
menor_temp = maior_temp = temp_Mons[0] # pode ser qualquer coordenada do vetor
temp_media = 0

for i in temp_Mons:
    if (menor_temp > i):
        menor_temp = i
        
    if (maior_temp < i):
        maior_temp = i
    
    temp_media+= i
    
temp_media = temp_media/len(temp_Mons)

print("Menor temperatura: {} \nMaior temperatura: {} \nTemperatura média: {}".format(menor_temp, maior_temp, temp_media))
