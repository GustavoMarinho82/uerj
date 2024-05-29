# estudantes = {"Nome": {"Idade": x, "Notas": y}, ...}
estudantes = {}

# FUNÇÕES
def adicionar_estudante():
    nome = input("Digite o nome do estudante: ")
    idade = int(input("Digite a sua idade: "))
    notas = []

    for i in range(4):
        nota = float(input(f"Digite a nota do {i+1}° Bimestre: "))
        notas.append(nota)
    
    estudantes[nome] = {"Idade": idade, "Notas": notas}


def remover_estudante():
    nome = input("Digite o nome do estudante: ")

    match (nome in estudantes.keys()):
        case True: estudantes.pop(nome)
        case False: print("Estudante não encontrado")


def atualizar_estudante():
    nome = input("Digite o nome do estudante: ")

    if (nome in estudantes.keys()):
        match input("Digite a nova idade (Deixe em branco para não alterar): "):
            case "": idade = estudantes[nome]["Idade"]
            case i: idade = int(i)

        notas = []

        for i in range(4):
            match input(f"Digite a nota do {i+1}° Bimestre (Deixe em branco para não alterar): "):
                case "": notas.append(estudantes[nome]["Notas"][i])
                case nota: notas.append(float(nota))

        estudantes[nome] = {"Idade": idade, "Notas": notas}

    else:
        print("Estudante não encontrado")


# MAIN
while (True):
    print("\nO que você deseja fazer?")
    print(" (1) - Adicionar estudante")
    print(" (2) - Remover estudante")
    print(" (3) - Atualizar dados de um estudante")
    print(" (4) - Ver estudantes")

    match input("Digite o número correspondente à ação: "):
        case "1": adicionar_estudante()
        case "2": remover_estudante()
        case "3": atualizar_estudante()
        case "4": print(estudantes)
        case _: print("Ação inválida!")