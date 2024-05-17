# Converter binário para decimal sem usar int(x, bin)

n_bin = input("Digite um número binário: ")
n_dec = 0
    
for x in range((len(n_bin)-1), -1, -1):
    if (n_bin[x] == "1"):
        n_dec += 2**(len(n_bin) - int(x) - 1) 

print("Em decimal:", n_dec)
