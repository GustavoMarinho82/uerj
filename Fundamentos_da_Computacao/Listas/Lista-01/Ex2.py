# Lista 1 - Exercício 2

a1 = int(input("Digite o primeiro termo da PA \n"))
razao = int(input("Digite a razao da PA \n"))
n_final = int(input("Digite quantos termos dessa PA você deseja ver \n"))


for n in range(1, n_final+1, 1):
    an = a1 + (n-1)*razao
    print("a{} = {}".format((n), an))