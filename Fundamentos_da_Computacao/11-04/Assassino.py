# Ver se é ou não o assassino

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia dinheiro para a vítima?", "Já trabalhou com a vítima?"]
pontuacao = 0

for pergunta in perguntas:
    resposta = input(pergunta + "\n")
    
    if (resposta.lower() == "sim") or (resposta.lower() == "s"):
        pontuacao += 1
        
if (pontuacao < 2):
    print("Relatório: Não é suspeito")
elif (pontuacao < 5):
    print("Relatório: É suspeito")
else:
    print("Relatório: É o assassino")
