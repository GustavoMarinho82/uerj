#Receber dois dicionarios e unir-los (onde tem chaves iguais deve-se unir os valores tambem)

# VARIÁVEIS
dicionario1 = {}
dicionario2 = {}
dicionarios_unidos = {}

tamanhoD1 = int(input("Digite o tamanho do dicionário 01: "))
tamanhoD2 = int(input("Digite o tamanho do dicionário 02: "))


# FOR's DE LEITURA DOS DICIONÁRIOS
for x in range(tamanhoD1):
    chave = input("\nDigite uma chave para o dicionário 01: ")
    valor = int(input(f"Digite um valor númerico para a chave {chave}: "))
    
    dicionario1[chave] = valor
    
for x in range(tamanhoD2):
    chave = input("\nDigite uma chave para o dicionário 02: ")
    valor = int(input(f"Digite um valor númerico para a chave {chave}: "))
    
    dicionario2[chave] = valor


#CONCATENAÇÃO DOS DICIONÁRIOS
chaves = list(dicionario1.keys()) + list(dicionario2.keys())

for chave in chaves:   
    if (chave in dicionario1.keys()) and (chave in dicionario2.keys()):
        dicionarios_unidos[chave] = (dicionario1[chave] + dicionario2[chave])
        
    elif (chave in dicionario1.keys()):
        dicionarios_unidos[chave] = dicionario1[chave]
        
    else:
        dicionarios_unidos[chave] = dicionario2[chave]

# OUTRA FORMA DE FAZER A CONCATENAÇÃO
#for chave in dicionario1.keys():   
#    if (chave in dicionario2.keys()):
#        dicionarios_unidos[chave] = (dicionario1[chave] + dicionario2[chave])
#    else:
#        dicionarios_unidos[chave] = dicionario1[chave]
#
#for chave in dicionario2.keys():
#    if (chave not in dicionario1.keys()):
#        dicionarios_unidos[chave] = dicionario2[chave]

# PRINT's
print(f"\nDicionário 01: {dicionario1}") 
print(f"Dicionário 02: {dicionario2}")
print(f"União: {dicionarios_unidos} ")
