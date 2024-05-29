from random import randint

TAMANHO_ID = 3

# funcionarios = {"ID": {"Nome": x, "Cargo": y}, ...}
funcionarios = {}


# FUNÇÕES
def adicionar_funcionario():
    id = ""
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o seu cargo: ")

    for _ in range(TAMANHO_ID):
        id += str(randint(0, 9))
    
    funcionarios[id] = {"Nome": nome, "Cargo": cargo}


def remover_funcionario():
    id = input("Digite o ID do funcionário: ")

    match (id in funcionarios.keys()):
        case True: funcionarios.pop(id)
        case False: print("ID do funcionário não encontrado")


def atualizar_funcionario():
    id = input("Digite o ID do funcionário: ")

    if (id in funcionarios.keys()):
        match input("Digite o novo nome (Deixe em branco para não alterar): "):
            case "": nome = funcionarios[id]["Nome"]
            case i: nome = i

        match input("Digite o novo cargo (Deixe em branco para não alterar): "):
            case "": cargo = funcionarios[id]["Cargo"]
            case i: cargo = i

        funcionarios[id] = {"Nome": nome, "Cargo": cargo}

    else:
        print("ID do funcionário não encontrado")

def buscar_funcionario():
    id = input("Digite o ID do funcionário: ")

    match (id in funcionarios.keys()):
        case True: texto = "Nome: {} \nCargo: {}".format(funcionarios[id]["Nome"], funcionarios[id]["Cargo"])
        case False: texto = "Funcionário não encontrado"

    print(texto)

# MAIN
while (True):
    print("\nO que você deseja fazer?")
    print(" (1) - Adicionar funcionario")
    print(" (2) - Remover funcioanrio")
    print(" (3) - Atualizar dados de um funcionario")
    print(" (4) - Ver todos os funcionários")
    print(" (5) - Buscar um funcionário em específico")

    match input("Digite o número correspondente à ação: "):
        case "1": adicionar_funcionario()
        case "2": remover_funcionario()
        case "3": atualizar_funcionario()
        case "4": print(funcionarios)
        case "5": buscar_funcionario()
        case _: print("Ação inválida!")