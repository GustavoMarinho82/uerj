# Receber um numero inderterminado de valores e ...

# VARIAVÉIS
valores = []
valores_ordenado = []
valores_ordenado_d = [] #d = decrescente
acima_media = []
qtd_valores = soma = 0


while (True):
    valor = int(input("Digite um valor númerico: (Digite -1 para parar a leitura): "))
    
    if (valor == -1):
        break
    
    valores.append(valor)
    qtd_valores += 1

for valor in valores:
    valores_ordenado.append(valor)
    valores_ordenado_d.append(valor)


# ORDENAMENTO
for x in range(len(valores_ordenado)):
    index_menor = x
    
    for y in range(x+1, len(valores_ordenado)):
        if (valores_ordenado[y] < valores_ordenado[index_menor]):
            index_menor = y
            
    v_auxiliar = valores_ordenado[x]
    valores_ordenado[x] = valores_ordenado[index_menor]
    valores_ordenado[index_menor] = v_auxiliar


# ORDENAMENTO DECRESCENTE
for x in range(len(valores_ordenado_d)):
    index_maior = x
    
    for y in range(x+1, len(valores_ordenado_d)):
        if (valores_ordenado_d[y] > valores_ordenado_d[index_maior]):
            index_maior = y
            
    v_auxiliar = valores_ordenado_d[x]
    valores_ordenado_d[x] = valores_ordenado_d[index_maior]
    valores_ordenado_d[index_maior] = v_auxiliar


# SOMA E MÉDIA
for valor in valores:
    soma += valor
    
media = (soma / qtd_valores)


# VALORES ACIMA DA MÉDIA
for valor in valores_ordenado:
    if (valor > media):
        acima_media.append(valor)


# PRINT's
print("Qtd de valores lidos: ", qtd_valores) #ou len(valores)
print("Em ordem: ", valores_ordenado) #ou valores_o = valores.sort()
print("Em ordem inversa: ", valores_ordenado_d) 
print("Soma dos valores: ", soma) #ou sum(valores)
print("Média dos valores: ", media) #ou (sum(valores)/len(valores))
print("Valores acima da média: ", acima_media)
