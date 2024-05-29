# vendas = {"Produto": N°_de_Vendas, ...}
vendas = {}


# FUNÇÕES
def adicionar_vendas():
    produto = input("Digite o nome do produto: ")
    qtd_vendas = int(input("Digite a qtd de vendas: "))

    match (produto in vendas.keys()):
        case True: vendas[produto] += qtd_vendas
        case False: vendas[produto] = qtd_vendas


def remover_produto():
    produto = input("Digite o nome do produto: ")

    match (produto in vendas.keys()):
        case True: vendas.pop(produto)
        case False: print("Produto não encontrado")


def atualizar_vendas():
    produto = input("Digite o nome do produto: ")
    
    if (produto in vendas.keys()):
        qtd_vendas = int(input("Digite a qtd de vendas: "))
        vendas[produto] = qtd_vendas
    
    else: 
        print("Produto não encontrado")

def obter_total_vendas():
    total_vendas = 0

    for qtd_vendas in vendas.values():
        total_vendas += qtd_vendas

    return total_vendas

# MAIN
while (True):
    print("\nO que você deseja fazer?")
    print(" (1) - Adicionar vendas")
    print(" (2) - Remover produto")
    print(" (3) - Atualizar n° de vendas de um produto")
    print(" (4) - Ver vendas por produto")
    print(" (5) - Ver vendas totais")

    match input("Digite o número correspondente à ação: "):
        case "1": adicionar_vendas()
        case "2": remover_produto()
        case "3": atualizar_vendas()
        case "4": print(vendas)
        case "5": print("Total de vendas:", obter_total_vendas())
        case _: print("Ação inválida!")