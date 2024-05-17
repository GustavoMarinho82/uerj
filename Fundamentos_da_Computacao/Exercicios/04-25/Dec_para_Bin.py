# Converter decimal para binario sem usar bin()

n_dec = int(input("Digite um número decimal: "))
n_bin = ""

while (n_dec != 0):
    n_bin += str(n_dec % 2)
    n_dec //= 2

n_bin = n_bin[::-1]

print("Em binário:", n_bin)
